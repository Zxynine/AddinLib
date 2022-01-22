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

import adsk.core, adsk.fusion, adsk.cam
from . import utils,geometry

Name = str
IconPath = str
BeforeIndex = int

def __Wrapper__Init__(self, WrapObj):
	self.__dict__ = WrapObj.__dict__

class CommandInputs(adsk.core.CommandInputs):
	""" A wrapper around a CommandInputs instance which provides extra utility functions"""
	__init__ = __Wrapper__Init__
	#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	def addCheckboxInput(self, id, name, initialValue=False):
		return super().addBoolValueInput(id, name, True,'', initialValue)
	def addButtonInput(self, id, name, resourceFolder=''):
		return super().addBoolValueInput(id, name, False, resourceFolder, False)
	#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	def addCheckBoxDropDownInput(self, id, name, *DropdownItems:'tuple[Name,bool]'):
		return self.addDropDownCommandInput(id, name, adsk.core.DropDownStyles.CheckBoxDropDownStyle, *DropdownItems)
	def addLabeledIconDropDownInput(self, id, name, *DropdownItems:'tuple[Name,IconPath]'):
		return self.addDropDownCommandInput(id, name, adsk.core.DropDownStyles.LabeledIconDropDownStyle, *[(name,False,path) for (name,path) in DropdownItems])
	def addRadioButtonDropDownInput(self, id, name, *DropdownItems:'Name'):
		return self.addDropDownCommandInput(id, name, adsk.core.DropDownStyles.LabeledIconDropDownStyle, *DropdownItems)
	def addTextDropDownInput(self, id, name, *DropdownItems:'Name'):
		return self.addDropDownCommandInput(id, name, adsk.core.DropDownStyles.TextListDropDownStyle, *DropdownItems)

	def addDropDownCommandInput(self, id:str, name:str, dropDownStyle:adsk.core.DropDownStyles, *DropdownItems:'tuple[Name,bool,IconPath,BeforeIndex]'):
		input = super().addDropDownCommandInput(id, name, dropDownStyle)
		def addDropdownItem(name,selected=False,path='',beforeIndex=-1):input.listItems.add(name,selected,path,beforeIndex)
		for dropdownItem in DropdownItems: addDropdownItem(*dropdownItem) if utils.isIterable(dropdownItem) else addDropdownItem(dropdownItem)
		if len(DropdownItems) > 0 and dropDownStyle != adsk.core.DropDownStyles.CheckBoxDropDownStyle:  input.listItems.item(0).isSelected = True
		return input
	#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	def addVisualDividerInput(self, id, name='', isExpanded = False):
		input = super().addGroupCommandInput(id, name)
		input.isEnabledCheckBoxDisplayed = False
		input.isExpanded = isExpanded
		input.isEnabled = name!=''
		return input
	#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	def addDisplayTextInput(self, id:str, formattedText:str, alignment=-1, maxDisplayRows=-1):
		if maxDisplayRows == -1: maxDisplayRows= formattedText.count('<br>')+len(formattedText.splitlines())
		return TextBoxCommandInput(super().addTextBoxCommandInput(id, '', formattedText, maxDisplayRows, True), alignment)
	#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~






	def addMoveCommandInput(self, id,name): return MoveCommandInput(self, id,name)














#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class TextBoxCommandInput(adsk.core.TextBoxCommandInput):
	_AlignmentMap_ = {-1:'left',0:'center',1:'right'}
	def __init__(self,WrapObj:adsk.core.TextBoxCommandInput, alignment):
		self.__dict__ = WrapObj.__dict__
		self.parent = WrapObj
		self._baseText_ = WrapObj.formattedText
		self.alignment = alignment
		self.parent.isFullWidth = True
	
	@property
	def formattedText(self): return self._baseText_
	@formattedText.setter
	def formattedText(self, setVal):
		self._baseText_ = setVal
		self.parent.formattedText = f'<div align="{self.alignment}">{setVal}</div>'

	@property
	def alignment(self): return self._AlignmentMap_[self._alignment_]
	@alignment.setter
	def alignment(self, setVal):
		self._alignment_ = setVal
		self.formattedText = self._baseText_

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class MoveCommandInput(adsk.core.CommandInput):
	commandInputs=id=name = None
	def __init__(self, inputs:CommandInputs,id:str,name:str):
		self.commandInputs = inputs
		self.command = inputs.command
		self.id,self.name = id,name
		self.origin = geometry.points.Zero



		self.groupInput = inputs.addGroupCommandInput(id,name)
		self.children = CommandInputs(self.groupInput.children)

		self.selectionInput = self.children.addSelectionInput(f'{id}_Selection','Selection','')
		self.selectionInput.setSelectionLimits(1,1)

		self.originInput = self.children.addButtonInput(f'{id}_ChangeOrigin','Set Pivot', '././resources/repeat')
		
		self.XDistanceInput= self.children.addDistanceValueCommandInput(f'{id}_XDistance', 'X Distance',adsk.core.ValueInput.createByString('0.0mm'))
		self.YDistanceInput= self.children.addDistanceValueCommandInput(f'{id}_YDistance', 'Y Distance',adsk.core.ValueInput.createByString('0.0mm'))
		self.ZDistanceInput= self.children.addDistanceValueCommandInput(f'{id}_ZDistance', 'Z Distance',adsk.core.ValueInput.createByString('0.0mm'))
		self.XDistanceInput.setManipulator(self.origin,geometry.vectors.X)
		self.YDistanceInput.setManipulator(self.origin,geometry.vectors.Y)
		self.ZDistanceInput.setManipulator(self.origin,geometry.vectors.Z)
		
		self.BasisVectors = geometry.vectors.XYZ()
		self.DeltaPoint:adsk.core.Point3D = geometry.points.Zero
