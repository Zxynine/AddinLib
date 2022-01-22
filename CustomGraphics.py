
from __future__ import annotations
import adsk.core, adsk.fusion
from adsk.core import Color as Colour
from enum import Enum


from. import AppObjects,utils




class VisualEffects(Enum):
	BasicMonoChrome = adsk.fusion.CustomGraphicsSolidColorEffect.create
	Overlayed = adsk.fusion.CustomGraphicsShowThroughColorEffect.create
	FusionApperence = adsk.fusion.CustomGraphicsAppearanceColorEffect.create
	VertexShading = adsk.fusion.CustomGraphicsVertexColorEffect.create
	ShadedMaterial = adsk.fusion.CustomGraphicsBasicMaterialColorEffect.create



class LineStyles(Enum):
	Solid = adsk.fusion.LineStylePatterns.continuousLineStylePattern
	DashDotted = adsk.fusion.LineStylePatterns.centerLineStylePattern
	Dashed = adsk.fusion.LineStylePatterns.dashedLineStylePattern
	Dotted = adsk.fusion.LineStylePatterns.dotLineStylePattern
	DashDoubleDotted = adsk.fusion.LineStylePatterns.phantomLineStylePattern
	Ribbed = adsk.fusion.LineStylePatterns.tracksLineStylePattern
	ZigZagged = adsk.fusion.LineStylePatterns.zigzagLineStylePattern




def getMaterialLibNames(libFilter):
	materialLibs = AppObjects.GetApp().materialLibraries
	libNames = []
	for materialLib in materialLibs:
		if (not libFilter) or libFilter(materialLib): libNames.append(materialLib.name)
	return libNames   
	

def hasAppearances(lib:adsk.core.MaterialLibrary): return (lib and lib.appearances.count > 0)
def getAppearance(libName, appearanceName):
		if not appearanceName or appearanceName == 'None': return
		appearance = AppObjects.GetDesign().appearances.itemByName(appearanceName)
		if appearance: return appearance
		matLib = AppObjects.GetApp().materialLibraries.itemByName(libName)      
		if matLib: appearance = matLib.appearances.itemByName(appearanceName)
		return appearance            


appearancesMap = {}
def getAppearancesFromLib(libName, filterExp:str):
		global appearancesMap
		appearanceList = None
		if libName in appearancesMap: appearanceList = appearancesMap[libName]
		else:
			materialLib = AppObjects.GetApp().materialLibraries.itemByName(libName)
			appearances = utils.Items(materialLib.appearances)
			appearanceList = [apperance.name for apperance in appearances]
			appearancesMap[libName] = appearanceList

		if filterExp and len(filterExp) > 0:
			filteredList = []
			for appearanceName in appearanceList:
				if appearanceName.lower().find(filterExp.lower()) >= 0: filteredList.append(appearanceName)
			return filteredList
		else: return appearanceList
			









TransparentRed = Colour.create(255,0,0,50)
RemovalRed = adsk.fusion.CustomGraphicsShowThroughColorEffect.create(TransparentRed,0.25)




def ClearCustomGraphics(root:adsk.fusion.Component,returnNew=False):
	if root.customGraphicsGroups.count > 0:
		[group.deleteMe() for group in root.customGraphicsGroups]
		AppObjects.GetApp().activeViewport.refresh()
	if returnNew:return root.customGraphicsGroups.add()


def CustomGraphicMeshFromBRep(graphics:adsk.fusion.CustomGraphicsGroup, object:adsk.fusion.BRepBody):
	objectGroup = graphics.addGroup()
	allMeshes:list[adsk.fusion.TriangleMesh] = object.meshManager.displayMeshes
	for mesh in allMeshes:
		meshCoords = adsk.fusion.CustomGraphicsCoordinates.create(mesh.nodeCoordinatesAsDouble)
		graphicObj = objectGroup.addMesh(meshCoords,mesh.nodeIndices, [],[])
		graphicObj.color = RemovalRed
	return objectGroup





class CustomGraphics:
	def __init__(self, root: adsk.fusion.Component=None):
		if root is None: root = AppObjects.GetRoot()
		self.graphics = ClearCustomGraphics(root,True)
		self.root = root
	def clear(self):return self.graphics.deleteMe()



def DrawLine(curve):
	pass


# def DrawGraphics():
# 	des = adsk.fusion.Design.cast(app_.activeProduct)
# 	root = des.rootComponent
# 	# Check to see if a custom graphics groups already exists and delete it.
# 	graphics = ClearCustomGraphics(root,True)

# 	allFaces:'list[adsk.fusion.BRepFace]' = [face_selection_input.selection(face).entity for face in range(face_selection_input.selectionCount)]

# 	interSections:'list[adsk.core.InfiniteLine3D]' = []
# 	for i in range(-1,len(allFaces)-1):
# 		PlanarGeom : adsk.core.Plane= allFaces[i].geometry
# 		interSections.append(PlanarGeom.intersectWithPlane(allFaces[i+1].geometry))

# 	tryLines = []
# 	for line in interSections:
# 		start = line.origin
# 		end = start.asVector()
# 		direction = line.direction
# 		direction.scaleBy(30)
# 		end.add(direction)
# 		end = end.asPoint()

# 		tryLines.append(adsk.core.Line3D.create(line.origin,end))
# 		graphics.addCurve(tryLines[-1])
