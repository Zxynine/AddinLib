# Error wrapper. Prints a message in the debug console. Can show a message box (optional)
#
# Typically used instead of try/except in the base of event handlers and run()/stop().
# This allows for less clutter as most cases will always need to be handled the same

import traceback, getpass
import re, sys
# Avoid Fusion namespace pollution
from . import utils, AppObjects
from functools import wraps




""" # Only keep the AddIns/Scripts part of the path
	C:/Users/ZXYNI/AppData/Roaming/Autodesk/Autodesk Fusion 360/API/AddIns/CommandManager\AddinUtil\ErrorUtilities.py
	>>> caller = re.sub(r'.*API[/\\]', '', self.callerPath)
	AddIns\CommandManager\AddinUtil\ErrorUtilities.py
	
	# Shorten file paths, to compact the message
	>>> traceString = ''.join(traceback.format_exception(exctype, value, traceb))

	# Attempt to scrub the user's username from the traceback, if any remains """

def GetTraceString(exctype, value, traceb):
	traceString = '\u200b'.join(traceback.format_exception(exctype, value, traceb))
	traceString = re.sub(r'"[^"]+/(?:API/AddIns|Api/Python)', '"', traceString)
	return traceString.replace(getpass.getuser(),'<user>').replace('\\','\\\u200b').replace('/','/\u200b')
	
def GetMessage(PreMessage,ErrorValue, callerPath, FusionVersion, TraceString):
	# Only keep the AddIns/Scripts part of the path
	caller = re.sub(r'.*API[/\\]','',callerPath)
	return (f'{PreMessage} error: {ErrorValue}\n\n' +
			'Copy this message by taking a screenshot. ' +
			'Describe what you did to get this error or record a video.\n\n' +
			f'{"-"*50}\n\n'+
			f'Fusion 360 v. {FusionVersion}\n' +
			f'{caller} failed: \n\n' + TraceString)




class ErrorCatcher():
	'''	Showing a messagebox is disabled in debugging, by default,
		to avoid the case where Fusion is stopped and the debugger
		fails to reattach on Restart.
		---

		## __init__

		msgbox_in_debug: Show an error message box also when debugging.
		msg_prefix: Prefix error message with this text. E.g. with
					add-in name and version.

		#### Usage:
		to always have the same options-
		
		Globally, set:
			error_catcher_ = ErrorCatcher()

		In function use:
			with error_catcher_:
				code that can throw
	'''
	def __init__(self, msgbox_in_debug=False, msg_prefix=''):
		self.msgbox_in_debug = msgbox_in_debug
		self.msg_prefix = msg_prefix

	def __call__(self, func, blockFuncSelf=False):
		@wraps(func)
		def wrapper(func_self=None,*args,**kwds):
			if not blockFuncSelf and func_self: args = [func_self, *args]
			with self: func(*args, **kwds)
		return wrapper

	def __enter__(self): self.caller_file = utils.get_caller_path()
	def __exit__(self, exctype, value, traceb):
		if not traceb: return
		app ,ui = AppObjects.GetAppUI()
		tb_str = GetTraceString(exctype, value, traceb)
		message = GetMessage(self.msg_prefix, value, self.caller_file, app.version, tb_str)
		print(message)

		in_debugger = hasattr(sys, 'gettrace') and sys.gettrace()
		if ui and (not in_debugger or self.msgbox_in_debug):
			print("Also showed in message box.")
			ui.messageBox(message)
		else: print("Not shown in message box.")
		return True # Exception handled


# def _error_catcher_wrapper(class_self_Ref, func):
# 	def catcher(func_self, args):
# 		with class_self_Ref.error_catcher: func(args)
# 	return catcher