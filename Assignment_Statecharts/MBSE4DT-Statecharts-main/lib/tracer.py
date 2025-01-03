from lib.controller import pretty_time

# Records input/output events
class Tracer:
    def __init__(self, verbose=True):
        self.verbose = verbose
        self.input_events = []
        self.output_events = []

    def record_input_event(self, simtime, event_name, value):
        if self.verbose:
            print(f"time = {pretty_time(simtime)}, input event: {event_name}, value = {value}")
        self.input_events.append( (simtime, event_name, value) )

    def record_output_event(self, simtime, event_name, value):
        if self.verbose:
            print(f"time = {pretty_time(simtime)}, output event: {event_name}, value = {value}")
        self.output_events.append( (simtime, event_name, value))


def format_trace_as_python_code(trace, indent=0):
    txt = "[\n"
    for (timestamp, event_name, value) in trace:
        txt += (" "*indent)+"    (%i, \"%s\", %s),\n" % (timestamp, event_name, value)
    txt += (" "*indent)+"],"
    return txt

# almost same as Python, but with arrays instead of tuples
def format_trace_as_json(trace, indent=0):
    txt = "[\n"
    for (timestamp, event_name, value) in trace:
        txt += (" "*indent)+"    [%i, \"%s\", %s],\n" % (timestamp, event_name, value)
    txt += (" "*indent)+"],"
    return txt
