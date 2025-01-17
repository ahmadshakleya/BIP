import sys
import math

from lib.controller import Controller, pretty_time
from lib.realtime.realtime import WallClock
from lib.tracer import Tracer, format_trace_as_python_code
from lib.yakindu_helpers import YakinduTimerServiceAdapter, trace_output_events
from lib.yakindu.rx import Observer
from srcgen.statechart import Statechart # generated code

import atexit

MOVES = [
    # x       y
    (0.0    , 2.0), # pickup
    (1000.0 , 3.0), # drop

    (0.0    , 2.0), # pickup
    (1000.0 , 4.0), # drop

    # etc.
]

# Intended to respond to 'ready' output events
class FakeScheduler(Observer):
    def __init__(self, controller, sc, move_status_callback):
        self.controller = controller
        self.sc = sc
        self.next_move_idx = 0
        self.move_status_callback = move_status_callback
        self.terminate = False

    def done(self):
        return self.next_move_idx == len(MOVES)

    def termination_condition(self):
        return self.terminate

    # called when receiving 'ready' output event
    def next(self, value=None):
        if not self.done():
            x,y = MOVES[self.next_move_idx]
            self.controller.add_input_relative(self.sc, 'scheduler.set_target_x', value=x)
            self.controller.add_input_relative(self.sc, 'scheduler.set_target_y', value=y)
            self.controller.add_input_relative(self.sc, 'scheduler.make_move')
            self.move_status_callback(f"making move {self.next_move_idx}")
            self.next_move_idx += 1
        else:
            self.move_status_callback("done (made all hardcoded moves)")
            self.terminate = True

def setup_fake_scheduler(controller, sc, move_status_callback=print):
    sched = FakeScheduler(controller, sc, move_status_callback)
    sc.scheduler.ready_observable.subscribe(sched)
    return sched


# Intended to respond to 'move' and 'hoist' output events
class FakeInertia(Observer):
    def __init__(self, controller, sc, dir, initial_pos, crane_status_callback):
        self.controller = controller
        self.sc = sc
        self.dir = dir
        self.current_pos = initial_pos
        self.crane_status_callback = crane_status_callback

    # respond to 'move' or 'hoist' event:
    def next(self, value=None):
        dist = abs(self.current_pos - value)
        fake_time_to_move = int(math.sqrt(dist)/10 * 1000000000) # nanoseconds
        msg = f"moving {self.dir} from {self.current_pos} to {value} which will take {pretty_time(fake_time_to_move)}"
        self.crane_status_callback(msg) # display message (in terminal or GUI)

        # we already add the 'done_moving'-event to the Controller's event queue, but with a timestamp in the future:
        self.controller.add_input_relative(self.sc, 'crane_control.done_moving', time_offset=fake_time_to_move) # s to ns
        self.current_pos = value

class FakeStopper(Observer):
    def __init__(self, controller, sc, crane_status_callback):
        self.controller = controller
        self.sc = sc
        self.crane_status_callback = crane_status_callback

    def next(self, value=None):
        msg = f"stopping all movement..."
        self.crane_status_callback(msg)
        self.controller.add_input_relative(self.sc, 'crane_control.done_moving', time_offset=500000000) # 500 ms

def setup_fake_crane_control(controller, sc, crane_status_callback):
    sc.crane_control.move_observable.subscribe(FakeInertia(controller, sc, "horizontally", 0.0, crane_status_callback))
    sc.crane_control.hoist_observable.subscribe(FakeInertia(controller, sc, "vertically", 100.0, crane_status_callback))
    sc.crane_control.stop_all_movement_observable.subscribe(FakeStopper(controller, sc, crane_status_callback))



def setup_wall_clock():
    # read time scale from command line
    try:
        time_scale = float(sys.argv[1])
    except:
        time_scale = 1.0
    print(f"TIME SCALE is {time_scale}")
    wall_clock = WallClock(time_scale)
    return wall_clock


# Setup controller, statechart, and event handlers
def setup(print_trace_at_the_end=True):
    controller = Controller()
    sc = Statechart()
    sc.timer_service = YakinduTimerServiceAdapter(controller)

    # Record input and output events
    tracer = Tracer()
    controller.input_tracers.append(tracer.record_input_event)
    trace_output_events(controller, sc, iface="scheduler", callback=tracer.record_output_event)
    trace_output_events(controller, sc, iface="crane_control", callback=tracer.record_output_event)

    if print_trace_at_the_end:
        def print_trace():
            print("End of simulation. Full I/O trace:")
            print("{")
            print('    "input_events": ', end='')
            print(format_trace_as_python_code(tracer.input_events, indent=4))
            print('    "output_events": ', end='')
            print(format_trace_as_python_code(tracer.output_events, indent=4))
            print("}")
        atexit.register(print_trace)

    return (
        controller, sc,
        tracer,
        # sched.done, # termination condition: stop when all moves were made
    )
