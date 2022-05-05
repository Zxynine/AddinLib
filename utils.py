# Utility functions.
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
from __future__ import annotations
import adsk.core, adsk.fusion, adsk.cam

import inspect
import os, json
import importlib
from typing import Generic, Iterable, Type, TypeVar,Callable
# from tkinter import Tk

from . import AppObjects




def toIdentifier(toId: str, toUnder:set={'-',' '}): return ''.join(['_'*(c in toUnder) or c*(c.isidentifier()) for c in toId])
def toHtml(string:str): return string.replace('&','&amp').replace("'",'&apos').replace('"','&quot').replace('<','&lt').replace('>','&gt;')


basestring = (str, bytes, bytearray)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def isIterable(item): return (isinstance(item, Iterable) and not isinstance(item, basestring))


def exists(obj):return obj is not None
def ifDelete(obj:adsk.core.CommandControl): return obj.deleteMe() if exists(obj) and obj.isValid else False
def getDelete(collection:adsk.core.CommandDefinitions,objId): ifDelete(collection.itemById(objId))
def deleteAll(*objs): return all(map(ifDelete,objs))
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class ContextManager:
	"""A generic context manager that functions as a decorator too"""
	def __init__(self): pass
	def __call__(self): return self
	def __enter__(self): return self
	def __exit__(self,ExType,ExVal,ExTrace):
		return False


def listAppend(list:list,appendObj):
	"""Syntatic sugar. This appends the obj to the list and returns it."""
	if appendObj: list.append(appendObj); return appendObj



def short_class(obj:adsk.core.Base):
	'''Returns shortened name of Object class'''
	return obj.classType().split('::')[-1]


def get_caller_path():
	'''Gets the filename of the file calling the function
	that called this function. That is, is nested in "two steps". '''
	return os.path.abspath(inspect.stack(0)[2][1])

def get_file_path():
	'''Gets the filename of the function that called this function.'''
	return os.path.abspath(inspect.stack(0)[1][1])

def get_file_dir():
	'''Gets the directory containing the file which function called this function.'''
	return os.path.dirname(os.path.abspath(inspect.stack(0)[1][1]))

# Allows for re-import of multiple modules
def ReImport_List(*args): map(importlib.reload, args)

def clear_ui_items(*items):
	"""Attempts to call 'deleteMe()' on every item provided. Returns True if all deletions are a success"""
	return deleteAll(items)


def is_parametric_mode():
	# Checking workspace type in DocumentActivated handler fails since Fusion 360 v2.0.10032
	# UserInterface.ActiveWorkspace throws when it is called from DocumentActivatedHandler
	# during Fusion 360 start-up(?). Checking for app_.isStartupComplete does not help.
	try:
		app_, ui_ = AppObjects.GetAppUI()
		if ui_.activeWorkspace.id == 'FusionSolidEnvironment':
			design = adsk.fusion.Design.cast(app_.activeProduct)
			return bool(design and design.designType == adsk.fusion.DesignTypes.ParametricDesignType)
	except: return False



def CheckWorkspace(obj:adsk.core.Workspace):
	#Tying to get its panels can throw an error
	try: return obj.toolbarPanels and (obj.productType != '')
	except: return False


def GetCommandIcon(commandId:str): return AppObjects.GetUi().commandDefinitions.itemById(commandId).resourceFolder



class CustomEvents:
	def Create(CustomEventID:str):
		app = AppObjects.GetApp()
		app.unregisterCustomEvent(CustomEventID)
		return app.registerCustomEvent(CustomEventID)
		
	def Fire(CustomEventID:str, additionalInfo='', toJsonStr=False):
		return AppObjects.GetApp().fireCustomEvent(CustomEventID, 
			additionalInfo if not toJsonStr else json.dumps(additionalInfo))

	def Remove(CustomEventID:str):
		return AppObjects.GetApp().unregisterCustomEvent(CustomEventID)

	def RemoveAll(CustomEventIDs:'list[str]'):
		return all(map(CustomEvents.Remove, CustomEventIDs))



def TextCommands()->adsk.core.TextCommandPalette:return AppObjects.GetUi().palettes.itemById('TextCommands')

def AppLog(*printString:str): return AppObjects.GetApp().log('\n'.join(map(str,printString)))
def UiLog(*printString:str): return AppObjects.GetUi().messageBox('\n'.join(map(str,printString)))
def DebugLog(*printString:str):print(*printString)

def FullLog(*printString:str): 
	AppLog(*printString)
	UiLog(*printString)
	DebugLog(*printString)



def executeCommand(cmdName):  AppObjects.GetUi().commandDefinitions.itemById(cmdName).execute()

class Scripts:
	"""Wrapper for adsk autoTerminate/terminate used in scripts"""
	def DontTerminate(): return adsk.autoTerminate(False)
	def Terminate(): return adsk.terminate()
def doEvents(): return adsk.doEvents()


class camera:
	def get(): return AppObjects.GetApp().activeViewport.camera
	
	def viewDirection(camera_copy:adsk.core.Camera=None):
		camera_copy = camera_copy or camera.get()
		return camera_copy.eye.vectorTo(camera_copy.target)

	def updateCamera(camera_copy:adsk.core.Camera, smoothTransition=True):
		camera_copy.isSmoothTransition = smoothTransition
		AppObjects.GetApp().activeViewport.camera = camera_copy
		doEvents()



class Ignore:
	def __init__(self, *types): self.types=types
	def __enter__(self):return self
	def __exit__(self,ExType,ExVal,ExTrace): 
		return self.types or ExType in self.types




# # From https://stackoverflow.com/a/25476462/106019
# def copy_to_clipboard(string, displayMessage = False):
# 	r = Tk(); r.withdraw()
# 	r.clipboard_clear(); r.clipboard_append(string)
# 	r.update(); r.destroy() 
# 	# now it stays on the clipboard after the window is closed
# 	if displayMessage: AppObjects.GetUi().messageBox('Copied to clipboard')



	
def MessagePromptCast(messageText, messageBoxTitle, buttonType=adsk.core.MessageBoxButtonTypes.YesNoCancelButtonType, iconType=adsk.core.MessageBoxIconTypes.QuestionIconType):
	dialogResult = AppObjects.GetUi().messageBox(messageText, messageBoxTitle, buttonType, iconType) 
	return {adsk.core.DialogResults.DialogYes:True,adsk.core.DialogResults.DialogNo:False}.get(dialogResult, None)




class Collections:
	def single(item:any):
		collection:adsk.core.ObjectCollection = adsk.core.ObjectCollection.create()
		collection.add(item)
		return collection

	def fromIterable(iterable:list):
		return Collections.extend(adsk.core.ObjectCollection.create(), iterable)

	def join(*iterables:list):
		collection:adsk.core.ObjectCollection = adsk.core.ObjectCollection.create()
		[Collections.extend(collection,iterable) for iterable in iterables]
		return collection

	def extend(collection:adsk.core.ObjectCollection, iterable:list):
		for item in iterable: collection.add(item)
		return collection
	
class Iter:
	"""This is a more powerful version of the `range` function. It will function the same as range unless
	given an iterable object, which it will then function as `range(len(iterable))`. It also supports an iterable
	with a specific start index (pos or neg) or end index (only neg) which functions like list access. See examples:
	```
		iterable = 'abcdef' #6 long

		Iter(iterable)    -> [0,1,2,3,4,5]
		Iter(2,iterable)  -> [2,3,4,5]
		Iter(-2,iterable) -> [-2,-1,0,1,2,3,4,5]
		Iter(iterable,-2) -> [0,1,2,3]
	```"""
	def __new__(cls,Start:any=0,Stop:any=0,Step=1):
		I,II,III = [I if type(I) is int else len(I) for I in (Start,Stop,Step)]
		return range(*(I*(II>0),((abs(I))*(II<=0))+II),III)
		
FuncReturn = TypeVar('FuncReturn')
class Items:
	"""Function to use on iterating through fusion collections. They typically do not return a type hinted object
	when using bracket access, this works around that by using an index and the collections `.item()` fucntion."""
	def __new__(cls,testobj): return [testobj.item(i) for i in Iter(testobj)]
	def custom(func:Callable[...,FuncReturn],size:int)->list[FuncReturn]:return [func(i) for i in range(size)]