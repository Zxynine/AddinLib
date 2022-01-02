# import adsk.core, adsk.fusion, adsk.cam
import os,json
import platform as osInfo
import subprocess
import tempfile



# def StringInstantiator(count): return ['']*count
# (USER_DIR, DESKTOP_DIR, TEMP_DIR, APPDATA_DIR, LOCAL_APPDATA_DIR, 
# USERDATA_DIR, USERDATA_DIR, PYTHON_DIR, 
# AUTODESK_DIR, AUTODESK_LOCAL_DIR, API_PYTHON_DIR, 
# FUSION_DIR, FUSION_CPP_DIR, FUSION_PYTHON_DIR, FUSION_RES_DIR, 
# PLUGINS_DIR, SCRIPTS_DIR, ADDINS_DIR,NEUTRON_OPTIONS) = StringInstantiator(19)





def getOS() -> str:
	osMap = dict( 	Windows='Windows',	win32='Windows',
					Darwin='Darwin',	Linux='Linux')
	osName = osMap.get(osInfo.system(), None)
	if osName is not None: return osName
	raise OSError(2, "Operating System Not Supported", f"{osInfo.system()}")
_osType = getOS()
iswindows = (_osType == 'Windows')


def PathExists(path, *args): return path is not '' and os.path.exists(os.path.join(path, *args))

def GetPath(fileDir, fileName):
	if not os.path.exists(fileDir): os.makedirs(fileDir)
	return os.path.join(fileDir, fileName)











USER_DIR=DESKTOP_DIR=TEMP_DIR=APPDATA_DIR=''
AUTODESK_DIR=PLUGINS_DIR=SCRIPTS_DIR=ADDINS_DIR=''
NEUTRON_OPTIONS=USER_OPTIONS_DIR=''




from xml.etree import ElementTree as XML
def XMLRead(dir,file): return XML.parse(os.path.join(dir,file))
def XMLRoot(dir,file): return XMLRead(dir,file).getroot()
def XMLHasChild(parent: XML.Element, XMLPath:str): return XMLPath == '' or parent.find(XMLPath) is not None

def getUserID(neutronPath=None):
	XMLROOT = XMLRoot(neutronPath or NEUTRON_OPTIONS,'NMachineSpecificOptions.xml')
	return XMLROOT.find('./NetworkOptionGroup/LastUserOptionId').attrib['Value']

def getUserHotkeys(userOptionsPath=None)->'list[dict]':#command_argument
	XMLROOT = XMLRoot(userOptionsPath or USER_OPTIONS_DIR,'NGlobalOptions.xml')
	return json.loads(XMLROOT.find('./HotKeyGroup/HotKeyJSONString').attrib['Value'])['hotkeys']




class GetDisplayLayouts:
	def FileName(userOptionsPath): return os.path.join(userOptionsPath or USER_OPTIONS_DIR, 'NULastDisplayedLayout.xml')
	def _GetTree(userOptionsPath): return XML.parse(GetDisplayLayouts.FileName(userOptionsPath))
	def _ToDictList(elements:'list[XML.Element]'): return [element.attrib for element in elements]
	def _SetArgs(element:XML.Element,**kwargs): [element.set(*kwarg) for kwarg in kwargs.items()]

	def _GetPalettes(tree:XML.ElementTree, filter:str): 
		XMLROOT = tree.getroot()
		ALLPALETTES = XMLROOT.findall('.//Area[@Contents="Palette"]')
		return [element for element in ALLPALETTES if XMLHasChild(element, filter)]
		
	def WritingGetPalettes(userOptionsPath, filter:str):
		TREE = XML.parse(GetDisplayLayouts.FileName(userOptionsPath))
		PALETTES = GetDisplayLayouts._GetPalettes(TREE, filter)
		return TREE,PALETTES

	def _PaletteByName(PALETTES:'list[XML.Element]', CommandId:str):
		PaletteMap = {palette.get('Name').lower():palette for palette in PALETTES}
		return PaletteMap.get(f'QTCommandDialogContentPanel{CommandId}'.lower(), None)

	def _GetCreate(parent:XML.Element, childName, XMLFilter:str=''):
		child = parent.find(childName+XMLFilter)
		if child is None: child = XML.SubElement(parent,childName)
		return child



	@classmethod
	def all(cls, userOptionsPath=None):
		PALETTES = cls._GetPalettes(cls._GetTree(userOptionsPath))
		return cls._ToDictList(PALETTES)

	@classmethod
	def resized(cls, userOptionsPath=None):
		PALETTES = cls._GetPalettes(cls._GetTree(userOptionsPath), 'State')
		return cls._ToDictList(PALETTES)

	@classmethod
	def commands(cls, userOptionsPath=None):
		PALETTES = cls._GetPalettes(cls._GetTree(userOptionsPath), 'Parameters[@Proxy]')
		return cls._ToDictList(PALETTES)





	@classmethod
	def setInitialSize(cls, CommandId:str, width, height, userOptionsPath=None):
		TREE,PALETTES = cls.WritingGetPalettes(userOptionsPath, 'Parameters[@Proxy]')
		CommandPalette = cls._PaletteByName(PALETTES, CommandId)
		if CommandPalette is None: return False

		StateElement = cls._GetCreate(CommandPalette, 'State','[@StateType="Initial"]')
		cls._SetArgs(StateElement, Size=f'{width},{height}', StateType='Initial')

		TREE.write(cls.FileName(userOptionsPath))
		return True

	@classmethod
	def setMinimumSize(cls, CommandId:str, width, height, userOptionsPath=None):
		TREE,PALETTES = cls.WritingGetPalettes(userOptionsPath, 'Parameters[@Proxy]')
		CommandPalette = cls._PaletteByName(PALETTES, CommandId)
		if CommandPalette is None: return False

		cls._SetArgs(CommandPalette, MinimumSize=f'{width},{height}')

		TREE.write(cls.FileName(userOptionsPath))
		return True



def join(*args): 
	newPath = os.path.join(*args)
	if PathExists(newPath):return newPath

USER_DIR=			os.path.expanduser('~')
DESKTOP_DIR=		join(USER_DIR,'Desktop')
APPDATA_DIR=		join(os.getenv('APPDATA'))	if iswindows else	join(USER_DIR,'Library','Application Support')
TEMP_DIR=			os.getenv('TMP') 			if iswindows else 	"/tmp" if _osType== "Darwin" else tempfile.gettempdir()

AUTODESK_DIR=		join(APPDATA_DIR,'Autodesk')
PLUGINS_DIR=		join(AUTODESK_DIR,'ApplicationPlugins')
SCRIPTS_DIR= 		join(AUTODESK_DIR,'Autodesk Fusion 360','API','Scripts')
ADDINS_DIR= 		join(AUTODESK_DIR,'Autodesk Fusion 360','API','AddIns')

NEUTRON_OPTIONS=	join(AUTODESK_DIR,'Neutron Platform','Options')
USER_OPTIONS_DIR=	join(NEUTRON_OPTIONS,getUserID(NEUTRON_OPTIONS))






def OpenFile(path):
	if iswindows: os.startfile(path)
	else: subprocess.check_call(["open", "--", path])





if __name__ == '__main__':
	print(	USER_DIR,DESKTOP_DIR,APPDATA_DIR,TEMP_DIR, '\n',
			AUTODESK_DIR,PLUGINS_DIR,SCRIPTS_DIR,ADDINS_DIR,'\n',
			NEUTRON_OPTIONS,USER_OPTIONS_DIR,'\n', sep='\n')
	# print(len(getCommandLayouts(USER_OPTIONS_DIR)))
	# print(len(GetDisplayLayouts.resized()))
	# print(len(GetDisplayLayouts.commands()))
	# GetDisplayLayouts.setInitialSize("thomasa88_keyboardShortcutsSimpleList",600, 650)
	# GetDisplayLayouts.setMinimumSize("thomasa88_keyboardShortcutsSimpleList",450, 500)
