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
import adsk.core, adsk.fusion
from. import AppObjects,utils


# class ReferenceBase:
# 	def __init__(self,cmdDef:adsk.core.CommandDefinition=None, cmdCtrl: Union[adsk.core.CommandControl,adsk.core.DropDownControl]=None):
# 		self.definition = cmdDef
# 		self.control = cmdCtrl
# 		if exists(cmdCtrl): self.id = cmdCtrl.id
# 		elif exists(cmdDef): self.id = cmdDef.id
# 		else: self.id = None
# 	def deleteMe(self):	utils.ifDelete(self.control); self.definition=self.control=None

# class CommandRef(ReferenceBase):
# 	def __init__(self,parentControls:adsk.core.ToolbarControls,newId,newName,newIcon='./resources/noicon',newToolTip=''):
# 		getDelete(ui_.commandDefinitions, newId)
# 		cmdDef = ui_.commandDefinitions.addButtonDefinition(newId, newName, newToolTip, newIcon)
# 		super().__init__(cmdDef, parentControls.addCommand(checkIcon(cmdDef)))

# class DropdownRef(ReferenceBase):
# 	def __init__(self,parentControls:adsk.core.ToolbarControls,newId,newName,newIcon='./resources/noicon',newToolTip=''):
# 		getDelete(parentControls, newId)
# 		cmdCtrl:adsk.core.DropDownControl = parentControls.addDropDown(newName, newIcon, newId)
# 		self.dropdownControls = cmdCtrl.controls
# 		super().__init__(None, cmdCtrl)
	
# class ToggleRef(ReferenceBase):
# 	def __init__(self,parentControls:adsk.core.ToolbarControls,newId,newName,startValue,newToolTip=''):
# 		getDelete(ui_.commandDefinitions, newId)
# 		cmdDef = ui_.commandDefinitions.addCheckBoxDefinition(newId, newName, newToolTip, startValue)
# 		self.controlDefinition:adsk.core.CheckBoxControlDefinition = cmdDef.controlDefinition
# 		super().__init__(cmdDef, parentControls.addCommand(cmdDef))
# 	@property
# 	def value(self):return self.controlDefinition.isChecked


# class UiObject:
# 	def __init__(self, id:str,name:str):
# 		self.id = id
# 		self.name = name

# class Workspace:
# 	def __init__(self,workspace:adsk.core.Workspace):
# 		self.referance = workspace
# 		self.id = workspace.id
# 		self.name = workspace.name
		
# class Toolbars:
# 	def __init__(self):
# 		pass
# class Tab:
# 	def __init__(self):
# 		pass
# class Panel:
# 	def __init__(self):
# 		pass
# class Control:
# 	def __init__(self):
# 		pass


def TryGet(collection):
	for I in range(len(collection)):
		try: yield collection.item(I)
		except:pass

def GetUi():
	app,ui = AppObjects.GetAppUI()

	UiToolbars = list(TryGet(ui.toolbars))
	UiWorkspaces = list(TryGet(ui.workspaces))
	UiTabs : list[adsk.core.ToolbarTab]=[]
	UiPanels : list[adsk.core.ToolbarPanel]=[]
	UiControls : list[adsk.core.ToolbarControl]=[]

	UiWorkspaces = [workspace for workspace in UiWorkspaces if utils.CheckWorkspace(workspace)]

	
	for workspace in UiWorkspaces:
		tabs = list(TryGet(workspace.toolbarTabs))
		UiTabs.append(tabs)
		for tab in tabs:
			panels = list(TryGet(tab.toolbarPanels))
			UiPanels.append(panels)
			controlIds = ''
			for panel in panels:
				controls = list(TryGet(panel.controls))
				UiControls.append(controls)
				
				controlIds += str((panel.name,[control.id for control in controls]))+'\t\n'
			ui.messageBox(controlIds)

