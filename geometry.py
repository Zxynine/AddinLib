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


FusionBRepEntity = (
	adsk.fusion.BRepBody,
	adsk.fusion.BRepLump,
	adsk.fusion.BRepShell,
	adsk.fusion.BRepFace,
	adsk.fusion.BRepLoop,
	adsk.fusion.BRepCoEdge,
	adsk.fusion.BRepEdge,
	adsk.fusion.BRepVertex,
)

HighlightableObjects = (
	adsk.fusion.BRepEdge, 
	adsk.fusion.BRepFace, 
	adsk.core.Curve3D, 
	adsk.fusion.BRepBody, 
	adsk.fusion.Occurrence, 
	adsk.core.Point3D,
	adsk.fusion.Path,
	adsk.fusion.PathEntity,
)


finiteGometry = (adsk.fusion.BRepEdge, adsk.fusion.SketchLine)
infiniteGeometry = (adsk.fusion.ConstructionAxis,)


class lines:
	def getEndpoints(line):
		if isinstance(line, adsk.fusion.BRepEdge):
			start,end = line.startVertex.geometry, line.endVertex.geometry
		elif isinstance(line, adsk.fusion.SketchLine):
			start,end = line.startSketchPoint.geometry, line.endSketchPoint.geometry
		elif isinstance(line, adsk.fusion.ConstructionAxis):
			start = line.geometry.origin
			end = start.copy(); end.translateBy(line.geometry.direction)
		return start,end

	def getDirection(line):
		if isinstance(line, (*finiteGometry, *infiniteGeometry)):
			start,end = lines.getEndpoints(line)
			return start.vectorTo(end)
		else: raise TypeError('Incorrect line Type.')

	def fromPointVector(origin:adsk.core.Point3D,direction: adsk.core.Vector3D):
		endPoint = origin.copy()
		endPoint.translateBy(direction)
		return adsk.core.Line3D.create(origin,endPoint)

class vectors:
	def new(x:float=0,y: float=0,z: float=0)->adsk.core.Vector3D:
		return adsk.core.Vector3D.create(x,y,z)

	X,Y,Z=new(1,0,0),new(0,1,0),new(0,0,1)
	@classmethod
	def XYZ(cls):
		return cls.X.copy(),cls.Y.copy(),cls.Z.copy()


	def project(fromVec:adsk.core.Vector3D,toVec:adsk.core.Vector3D, normalised=False):
		projection = toVec.copy()
		projection.scaleBy(fromVec.dotProduct(toVec) / fromVec.length**2)
		if normalised: projection.normalize()
		return projection 

	def normalOf(unNormVec:adsk.core.Vector3D,scale=1):
		newVec = unNormVec.copy()
		newVec.normalize()
		newVec.scaleBy(scale)
		return newVec
	
	def scaledBy(baseVec:adsk.core.Vector3D,scale=1):
		vecCopy = baseVec.copy()
		vecCopy.scaleBy(scale)
		return vecCopy

	def reverse(baseVec:adsk.core.Vector3D):
		baseVec.scaleBy(-1)
		return baseVec
	
	def subtract(minuhend:adsk.core.Vector3D, subtrahend:adsk.core.Vector3D):
		invSub = vectors.reverse(subtrahend)
		minuhend.add(invSub)
		return minuhend

	def squared(baseVec:adsk.core.Vector3D):
		return vectors.applyFunction(baseVec.copy(),lambda a:a*a)

	def sum(*addends: adsk.core.Vector3D):
		summation = vectors.new()
		for vec in addends:summation.add(vec)
		return summation

	def applyFunction(baseVec:adsk.core.Vector3D, func:'function'):
		baseVec.x=func(baseVec.x)
		baseVec.y=func(baseVec.y)
		baseVec.z=func(baseVec.z)
		return baseVec




class points:
	Zero:adsk.core.Point3D = adsk.core.Point3D.create(0,0,0)
	def copy(point:adsk.core.Point3D, offset:adsk.core.Vector3D=Zero):
		ptCopy = point.copy()
		ptCopy.translateBy(offset)
		return ptCopy

	def subtract(minuhend:adsk.core.Point3D, subtrahend:adsk.core.Vector3D):
		invSub = vectors.reverse(subtrahend)
		minuhend.translateBy(invSub)
		return minuhend


class translate:
	def __new__(cls,transform:adsk.core.Matrix3D=None,x:float=0.0,y:float=0.0,z:float=0.0, inMM=True) -> adsk.core.Matrix3D:
		if transform is None: transform = adsk.core.Matrix3D.create()
		if inMM: x,y,z = x/10,y/10,z/10
		translation = vectors.new(x,y,z)
		transform.translation = translation
		return transform
	create = __new__



class Matrix:
	def translation(translation:adsk.core.Vector3D, transform:adsk.core.Matrix3D=None):
		if transform is None: transform = adsk.core.Matrix3D.create()
		transform.translation = translation
		return transform

	def rotation(oldDirection:adsk.core.Vector3D, newDirection:adsk.core.Vector3D):
		oldDirection = vectors.normalOf(oldDirection)
		newDirection = vectors.normalOf(newDirection)
		R:adsk.core.Matrix3D = adsk.core.Matrix3D.create()
		R.setToRotateTo(oldDirection,newDirection)
		return R

	def apply(matrix:adsk.core.Matrix3D,*vectors:adsk.core.Vector3D):
		for vector in vectors: vector.transformBy(matrix)

	# #https://www.theochem.ru.nl/~pwormer/Knowino/knowino.org/wiki/Rotation_matrix.html#Vector_rotation
	# def rotation(oldDirection:adsk.core.Vector3D, newDirection:adsk.core.Vector3D):
	# 	oldDirection = vectors.normalOf(oldDirection)
	# 	newDirection = vectors.normalOf(newDirection)

	# 	U=oldDirection.crossProduct(newDirection)
	# 	# S=vectors.normalOf(U).length	#Sin of angle
	# 	C=oldDirection.dotProduct(newDirection)	#Cos of angle

	# 	H=((1-C)/(1-(C**2)))

	# 	CHD = vectors.applyFunction(U.copy(), lambda a:(H*(a**2))+C)
	# 	HUX,HUY,HUZ = (H*U.y*U.z),(H*U.x*U.z),(H*U.x*U.y)

	# 	R:adsk.core.Matrix3D = adsk.core.Matrix3D.create()
	# 	R.setWithArray((
	# 		CHD.x,		HUZ-U.z,	HUY+U.y,	0,
	# 		HUZ+U.z,	CHD.y,		HUX-U.x,	0,
	# 		HUY-U.y, 	HUX+U.x,	CHD.z,		0,
	# 		0,			0,			0,			1))
	# 	return R
