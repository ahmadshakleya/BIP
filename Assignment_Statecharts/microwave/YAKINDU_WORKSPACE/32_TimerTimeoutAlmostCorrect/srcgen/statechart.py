"""Implementation of statechart statechart.
Generated by itemis CREATE code generator.
"""

import queue
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from yakindu.rx import Observable

class Statechart:
	"""Implementation of the state machine Statechart.
	"""

	class State:
		""" State Enum
		"""
		(
			main_region_door_closed,
			main_region_door_closed_r1magnetron_on,
			main_region_door_closed_r1magnetron_off,
			main_region_door_open,
			null_state
		) = range(5)
	
	
	def __init__(self):
		""" Declares all necessary variables including list of states, histories etc. 
		"""
		
		self.start_pressed = None
		self.stop_pressed = None
		self.increase_time_pressed = None
		self.door_opened = None
		self.door_closed = None
		self.turn_magnetron_on = None
		self.turn_magnetron_on_observable = Observable()
		self.turn_magnetron_off = None
		self.turn_magnetron_off_observable = Observable()
		self.set_displayed_time = None
		self.set_displayed_time_value = None
		self.set_displayed_time_observable = Observable()
		self.ring_bell = None
		self.ring_bell_observable = Observable()
		
		self.in_event_queue = queue.Queue()
		self.__remaining_time = None
		
		# enumeration of all states:
		self.__State = Statechart.State
		self.__state_conf_vector_changed = None
		self.__state_vector = [None] * 1
		for __state_index in range(1):
			self.__state_vector[__state_index] = self.State.null_state
		
		# for timed statechart:
		self.timer_service = None
		self.__time_events = [None] * 1
		
		# initializations:
		#Default init sequence for statechart Statechart
		self.__remaining_time = 0
		self.__is_executing = False
	
	def is_active(self):
		"""Checks if the state machine is active.
		"""
		return self.__state_vector[0] is not self.__State.null_state
	
	def is_final(self):
		"""Checks if the statemachine is final.
		Always returns 'false' since this state machine can never become final.
		"""
		return False
			
	def is_state_active(self, state):
		"""Checks if the state is currently active.
		"""
		s = state
		if s == self.__State.main_region_door_closed:
			return (self.__state_vector[0] >= self.__State.main_region_door_closed)\
				and (self.__state_vector[0] <= self.__State.main_region_door_closed_r1magnetron_off)
		if s == self.__State.main_region_door_closed_r1magnetron_on:
			return self.__state_vector[0] == self.__State.main_region_door_closed_r1magnetron_on
		if s == self.__State.main_region_door_closed_r1magnetron_off:
			return self.__state_vector[0] == self.__State.main_region_door_closed_r1magnetron_off
		if s == self.__State.main_region_door_open:
			return self.__state_vector[0] == self.__State.main_region_door_open
		return False
		
	def time_elapsed(self, event_id):
		"""Add time events to in event queue
		"""
		if event_id in range(1):
			self.in_event_queue.put(lambda: self.raise_time_event(event_id))
			self.run_cycle()
	
	def raise_time_event(self, event_id):
		"""Raise timed events using the event_id.
		"""
		self.__time_events[event_id] = True
	
	def __execute_queued_event(self, func):
		func()
	
	def __get_next_event(self):
		if not self.in_event_queue.empty():
			return self.in_event_queue.get()
		return None
	
	
	def raise_start_pressed(self):
		"""Raise method for event start_pressed.
		"""
		self.in_event_queue.put(self.__raise_start_pressed_call)
		self.run_cycle()
	
	def __raise_start_pressed_call(self):
		"""Raise callback for event start_pressed.
		"""
		self.start_pressed = True
	
	def raise_stop_pressed(self):
		"""Raise method for event stop_pressed.
		"""
		self.in_event_queue.put(self.__raise_stop_pressed_call)
		self.run_cycle()
	
	def __raise_stop_pressed_call(self):
		"""Raise callback for event stop_pressed.
		"""
		self.stop_pressed = True
	
	def raise_increase_time_pressed(self):
		"""Raise method for event increase_time_pressed.
		"""
		self.in_event_queue.put(self.__raise_increase_time_pressed_call)
		self.run_cycle()
	
	def __raise_increase_time_pressed_call(self):
		"""Raise callback for event increase_time_pressed.
		"""
		self.increase_time_pressed = True
	
	def raise_door_opened(self):
		"""Raise method for event door_opened.
		"""
		self.in_event_queue.put(self.__raise_door_opened_call)
		self.run_cycle()
	
	def __raise_door_opened_call(self):
		"""Raise callback for event door_opened.
		"""
		self.door_opened = True
	
	def raise_door_closed(self):
		"""Raise method for event door_closed.
		"""
		self.in_event_queue.put(self.__raise_door_closed_call)
		self.run_cycle()
	
	def __raise_door_closed_call(self):
		"""Raise callback for event door_closed.
		"""
		self.door_closed = True
	
	def __entry_action_main_region_door_closed_r1_magnetron_on(self):
		"""Entry action for state 'MagnetronOn'..
		"""
		#Entry action for state 'MagnetronOn'.
		self.timer_service.set_timer(self, 0, (1 * 1000), False)
		self.turn_magnetron_on_observable.next()
		
	def __exit_action_main_region_door_closed_r1_magnetron_on(self):
		"""Exit action for state 'MagnetronOn'..
		"""
		#Exit action for state 'MagnetronOn'.
		self.timer_service.unset_timer(self, 0)
		self.turn_magnetron_off_observable.next()
		
	def __enter_sequence_main_region_door_closed_default(self):
		"""'default' enter sequence for state doorClosed.
		"""
		#'default' enter sequence for state doorClosed
		self.__enter_sequence_main_region_door_closed_r1_default()
		
	def __enter_sequence_main_region_door_closed_r1_magnetron_on_default(self):
		"""'default' enter sequence for state MagnetronOn.
		"""
		#'default' enter sequence for state MagnetronOn
		self.__entry_action_main_region_door_closed_r1_magnetron_on()
		self.__state_vector[0] = self.State.main_region_door_closed_r1magnetron_on
		self.__state_conf_vector_changed = True
		
	def __enter_sequence_main_region_door_closed_r1_magnetron_off_default(self):
		"""'default' enter sequence for state MagnetronOff.
		"""
		#'default' enter sequence for state MagnetronOff
		self.__state_vector[0] = self.State.main_region_door_closed_r1magnetron_off
		self.__state_conf_vector_changed = True
		
	def __enter_sequence_main_region_door_open_default(self):
		"""'default' enter sequence for state DoorOpen.
		"""
		#'default' enter sequence for state DoorOpen
		self.__state_vector[0] = self.State.main_region_door_open
		self.__state_conf_vector_changed = True
		
	def __enter_sequence_main_region_default(self):
		"""'default' enter sequence for region main region.
		"""
		#'default' enter sequence for region main region
		self.__react_main_region__entry_default()
		
	def __enter_sequence_main_region_door_closed_r1_default(self):
		"""'default' enter sequence for region r1.
		"""
		#'default' enter sequence for region r1
		self.__react_main_region_door_closed_r1__entry_default()
		
	def __exit_sequence_main_region_door_closed(self):
		"""Default exit sequence for state doorClosed.
		"""
		#Default exit sequence for state doorClosed
		self.__exit_sequence_main_region_door_closed_r1()
		self.__state_vector[0] = self.State.null_state
		
	def __exit_sequence_main_region_door_closed_r1_magnetron_on(self):
		"""Default exit sequence for state MagnetronOn.
		"""
		#Default exit sequence for state MagnetronOn
		self.__state_vector[0] = self.State.main_region_door_closed
		self.__exit_action_main_region_door_closed_r1_magnetron_on()
		
	def __exit_sequence_main_region_door_closed_r1_magnetron_off(self):
		"""Default exit sequence for state MagnetronOff.
		"""
		#Default exit sequence for state MagnetronOff
		self.__state_vector[0] = self.State.main_region_door_closed
		
	def __exit_sequence_main_region_door_open(self):
		"""Default exit sequence for state DoorOpen.
		"""
		#Default exit sequence for state DoorOpen
		self.__state_vector[0] = self.State.null_state
		
	def __exit_sequence_main_region(self):
		"""Default exit sequence for region main region.
		"""
		#Default exit sequence for region main region
		state = self.__state_vector[0]
		if state == self.State.main_region_door_closed:
			self.__exit_sequence_main_region_door_closed()
		elif state == self.State.main_region_door_closed_r1magnetron_on:
			self.__exit_sequence_main_region_door_closed_r1_magnetron_on()
		elif state == self.State.main_region_door_closed_r1magnetron_off:
			self.__exit_sequence_main_region_door_closed_r1_magnetron_off()
		elif state == self.State.main_region_door_open:
			self.__exit_sequence_main_region_door_open()
		
	def __exit_sequence_main_region_door_closed_r1(self):
		"""Default exit sequence for region r1.
		"""
		#Default exit sequence for region r1
		state = self.__state_vector[0]
		if state == self.State.main_region_door_closed_r1magnetron_on:
			self.__exit_sequence_main_region_door_closed_r1_magnetron_on()
		elif state == self.State.main_region_door_closed_r1magnetron_off:
			self.__exit_sequence_main_region_door_closed_r1_magnetron_off()
		
	def __react_main_region_door_closed_r1__choice_0(self):
		"""The reactions of state null..
		"""
		#The reactions of state null.
		if self.__remaining_time == 0:
			self.ring_bell_observable.next()
			self.__enter_sequence_main_region_door_closed_r1_magnetron_off_default()
		else:
			self.__enter_sequence_main_region_door_closed_r1_magnetron_on_default()
		
	def __react_main_region_door_closed_r1__entry_default(self):
		"""Default react sequence for initial entry .
		"""
		#Default react sequence for initial entry 
		self.__enter_sequence_main_region_door_closed_r1_magnetron_off_default()
		
	def __react_main_region__entry_default(self):
		"""Default react sequence for initial entry .
		"""
		#Default react sequence for initial entry 
		self.__enter_sequence_main_region_door_closed_default()
		
	def __react(self, transitioned_before):
		"""Implementation of __react function.
		"""
		#State machine reactions.
		return transitioned_before
	
	
	def __main_region_door_closed_react(self, transitioned_before):
		"""Implementation of __main_region_door_closed_react function.
		"""
		#The reactions of state doorClosed.
		transitioned_after = self.__react(transitioned_before)
		if transitioned_after < 0:
			if self.door_opened:
				self.__exit_sequence_main_region_door_closed()
				self.__enter_sequence_main_region_door_open_default()
				transitioned_after = 0
		return transitioned_after
	
	
	def __main_region_door_closed_r1_magnetron_on_react(self, transitioned_before):
		"""Implementation of __main_region_door_closed_r1_magnetron_on_react function.
		"""
		#The reactions of state MagnetronOn.
		transitioned_after = self.__main_region_door_closed_react(transitioned_before)
		if transitioned_after < 0:
			if self.stop_pressed:
				self.__exit_sequence_main_region_door_closed_r1_magnetron_on()
				self.__enter_sequence_main_region_door_closed_r1_magnetron_off_default()
				transitioned_after = 0
			elif self.__time_events[0]:
				self.__exit_sequence_main_region_door_closed_r1_magnetron_on()
				self.__remaining_time = self.__remaining_time - 1
				self.set_displayed_time_observable.next(self.__remaining_time)
				self.__time_events[0] = False
				self.__react_main_region_door_closed_r1__choice_0()
				transitioned_after = 0
		return transitioned_after
	
	
	def __main_region_door_closed_r1_magnetron_off_react(self, transitioned_before):
		"""Implementation of __main_region_door_closed_r1_magnetron_off_react function.
		"""
		#The reactions of state MagnetronOff.
		transitioned_after = self.__main_region_door_closed_react(transitioned_before)
		if transitioned_after < 0:
			if self.start_pressed:
				self.__exit_sequence_main_region_door_closed_r1_magnetron_off()
				self.__enter_sequence_main_region_door_closed_r1_magnetron_on_default()
				transitioned_after = 0
			elif self.increase_time_pressed:
				self.__exit_sequence_main_region_door_closed_r1_magnetron_off()
				self.__remaining_time = self.__remaining_time + 1
				self.set_displayed_time_observable.next(self.__remaining_time)
				self.__enter_sequence_main_region_door_closed_r1_magnetron_off_default()
				transitioned_after = 0
		return transitioned_after
	
	
	def __main_region_door_open_react(self, transitioned_before):
		"""Implementation of __main_region_door_open_react function.
		"""
		#The reactions of state DoorOpen.
		transitioned_after = self.__react(transitioned_before)
		if transitioned_after < 0:
			if self.door_closed:
				self.__exit_sequence_main_region_door_open()
				self.__enter_sequence_main_region_door_closed_default()
				transitioned_after = 0
		return transitioned_after
	
	
	def __clear_in_events(self):
		"""Implementation of __clear_in_events function.
		"""
		self.start_pressed = False
		self.stop_pressed = False
		self.increase_time_pressed = False
		self.door_opened = False
		self.door_closed = False
		self.__time_events[0] = False
	
	
	def __micro_step(self):
		"""Implementation of __micro_step function.
		"""
		state = self.__state_vector[0]
		if state == self.State.main_region_door_closed_r1magnetron_on:
			self.__main_region_door_closed_r1_magnetron_on_react(-1)
		elif state == self.State.main_region_door_closed_r1magnetron_off:
			self.__main_region_door_closed_r1_magnetron_off_react(-1)
		elif state == self.State.main_region_door_open:
			self.__main_region_door_open_react(-1)
	
	
	def run_cycle(self):
		"""Implementation of run_cycle function.
		"""
		#Performs a 'run to completion' step.
		if self.timer_service is None:
			raise ValueError('Timer service must be set.')
		
		if self.__is_executing:
			return
		self.__is_executing = True
		next_event = self.__get_next_event()
		if next_event is not None:
			self.__execute_queued_event(next_event)
		condition_0 = True
		while condition_0:
			self.__micro_step()
			self.__clear_in_events()
			condition_0 = False
			next_event = self.__get_next_event()
			if next_event is not None:
				self.__execute_queued_event(next_event)
				condition_0 = True
		self.__is_executing = False
	
	
	def enter(self):
		"""Implementation of enter function.
		"""
		#Activates the state machine.
		if self.timer_service is None:
			raise ValueError('Timer service must be set.')
		
		if self.__is_executing:
			return
		self.__is_executing = True
		#Default enter sequence for statechart Statechart
		self.__enter_sequence_main_region_default()
		self.__is_executing = False
	
	
	def exit(self):
		"""Implementation of exit function.
		"""
		#Deactivates the state machine.
		if self.__is_executing:
			return
		self.__is_executing = True
		#Default exit sequence for statechart Statechart
		self.__exit_sequence_main_region()
		self.__state_vector[0] = self.State.null_state
		self.__is_executing = False
	
	
	def trigger_without_event(self):
		"""Implementation of triggerWithoutEvent function.
		"""
		self.run_cycle()
	