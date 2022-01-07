# Event managing.
# 
# Allows catching events with functions instead of classes.
# Tracks registered events and allows clean-up with one function call.
# All event callbacks are also wrapped in an error.ErrorCatcher().
#
# This file is part of a modified version of thomasa88lib, a library of useful 
# Fusion 360 add-in/script functions.
#
# Copyright (c) 2021 ZXYNINE
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import adsk.core, adsk.fusion, adsk.cam
import sys, time
import threading
# Avoid Fusion namespace pollution
from . import error, utils

# Try to resolve base class automatically

HANDLER_MAP = {}
def getHandler(event:str)-> 'adsk.core.EventHandler':
	base_class = HANDLER_MAP.get(event, None)
	if base_class is not None: return base_class
	return HANDLER_MAP.setdefault(event, buildHandler(event))

"""`AUTO_HANDLER_CLASS` results in:
1: Adding 'Handler' to the end of the classType and Splitting at '::'
2: Getting the module using the first segment
3: recursivly rebuilds the object reference from the parts"""
def buildHandler(event:str)-> 'adsk.core.EventHandler':
	handler_class_parts = f'{event}Handler'.split('::')
	base_class = sys.modules[handler_class_parts.pop(0)]
	for cls in handler_class_parts: base_class = getattr(base_class, cls)
	return base_class

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Data Containers
class LinkedHandler:
	def __init__(self, event: adsk.core.CommandEvent, handler:type,manager:'EventsManager'=None,callback:'function'=None):
		self.event = event
		self.handler = handler
		self.callback = callback
		self.manager = manager
		if not event.add(handler): raise Exception(f'Failed to add the "{callback.__name__}" handler ')
	def remove(self):
		with utils.Ignore(): self.event.remove(self.handler)



AUTO_HANDLER_CLASS = None
class EventsManager:
	def __init__(self, error_catcher=None):
		#Declared in init to allow multiple commands to use a single lib
		self.handlers: 'list[LinkedHandler]' = []
		self.custom_event_names = []
		self.CustomEvents = utils.CustomEvents

		self.next_delay_id = 0
		self.delayed_funcs = {}
		self.delayed_event = None
		self.delayed_event_id = f'{utils.get_caller_path()}_delay_event'
		self.error_catcher = error_catcher or error.ErrorCatcher()
	
	#Assigning
	#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	def add_handler(self, event:adsk.core.CommandEvent, callback, base_class=AUTO_HANDLER_CLASS):
		if base_class == AUTO_HANDLER_CLASS: base_class = getHandler(event.classType())

		handler_name = f'{base_class.__name__}_{callback.__name__}'
		handler_class = type(handler_name, (base_class,), {"notify": self.error_catcher(callback,True)})
		handler_class.__init__ = lambda self: super(handler_class, self).__init__()
		handler = handler_class()

		handler_info = LinkedHandler(event, handler, callback)
		self.handlers.append(handler_info)# Avoid garbage collection
		return handler_info
	
	def register_event(self, name):
		# Clears and then starts the event (makes sure there is not an old event registered due to a bad stop)
		event = self.CustomEvents.Create(name)
		if event: self.custom_event_names.append(name)
		return event

	#Searching
	#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

	def find_handler_by_event(self, findevent:adsk.core.Event):
		eventName = findevent.name
		for linkedHandler in self.handlers:
			if eventName == linkedHandler.event.name: 
				return linkedHandler

	def find_handler_by_func(self, func:'function'):
		for linkedHandler in self.handlers:
			if linkedHandler.callback == func: 
				return linkedHandler

	#Timing
	#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	def delay(self, func, secs=0):
		'''Puts a function at the end of the event queue, and optionally delays it. '''
		if self.delayed_event is None:# Register the event. Will be removed when user runs clean_up()
			self.delayed_event = self.register_event(self.delayed_event_id)
			self.add_handler(self.delayed_event, callback=self._delayed_event_handler)
		delay_id = self.next_delay_id
		self.next_delay_id += 1

		self.delayed_funcs[delay_id] = func
		def fireEvent():self.CustomEvents.Fire(self.delayed_event_id, str(delay_id))

		if secs <= 0: return fireEvent()
		thread = DelayThread(target=fireEvent, delayTime=secs,autoStart=True)

	def _delayed_event_handler(self, args: adsk.core.CustomEventArgs):
		delay_id = int(args.additionalInfo)
		func = self.delayed_funcs.pop(delay_id, None)
		if func: func()


	#Removing
	#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	#Removes one or many
	def remove_handler(self, handler_info: LinkedHandler):
		handler_info.remove();self.handlers.remove(handler_info)
	def remove_handlers(self, *handler_infos: 'list[LinkedHandler]'):
		map(self.remove_handler, handler_infos)

	#Removes ALL
	def remove_all_handlers(self):
		map(LinkedHandler.remove, self.handlers)
		self.handlers.clear()

	#Removed first that has event
	def remove_handler_by_event(self, event: adsk.core.CommandEvent):
		handler = self.find_handler_by_event(event)
		self.remove_handler((handler, event))

	def unregister_all_events(self):
		self.CustomEvents.RemoveAll(self.custom_event_names)
		self.custom_event_names.clear()

	def clean_up(self, oldControl = None):
		self.remove_all_handlers()
		self.unregister_all_events()








class DelayThread(threading.Thread):
	def __init__(self, target, delayTime=0, autoStart=False):
		def waiter(): time.sleep(delayTime); target()

		super().__init__(target=waiter, daemon=True)
		if autoStart: self.start()












#This should be a manager that lets you assign funcs to specific input changed events.
class InputEvents:
	registeredInputs = []
	@classmethod
	def InputChangedHandler(cls, args:adsk.core.InputChangedEventArgs):
		pass

	def __init__(self) -> None:
		pass
