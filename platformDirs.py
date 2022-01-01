# import adsk.core, adsk.fusion, adsk.cam
import os,json
import platform as osInfo
import subprocess
import tempfile


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




from xml.etree import ElementTree as XMLTree
def getUserID(neutronPath):
	optionsFile = os.path.join(neutronPath,'NMachineSpecificOptions.xml')
	return XMLTree.parse(optionsFile).getroot().find('./NetworkOptionGroup/LastUserOptionId').attrib['Value']

def getUserHotkeys(userOptionsPath)->'list[dict["commands":list,"hotkey_sequence":"A+B+C", "isDefault":bool]]':#command_argument
	optionsFile = os.path.join(userOptionsPath,'NGlobalOptions.xml')
	return json.loads(XMLTree.parse(optionsFile).getroot().find('./HotKeyGroup/HotKeyJSONString').attrib['Value'])['hotkeys']


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
# getUserHotkeys(USER_OPTIONS_DIR)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
