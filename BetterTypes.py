






#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Descriptors
def Raise(ErrorType=Exception,*args): raise ErrorType(*args)

class ClassProperty(property):
	
	fget = lambda *args:Raise(AttributeError,"unreadable attribute")

	def __init__(self, fget=None, doc=None):
		if fget: self.fget = fget
		self.__doc__ = doc if doc else fget.__doc__

	def __get__(self, inst, cls=None):
		return self.fget(cls or type(inst))



class TestClass:
	testVal = 5
	@ClassProperty
	def testGet(cls):return cls.testVal


print(TestClass.testVal)
print(TestClass.testGet)
TestClass.testGet = 54


from typing import Callable,TypeVar,Generic
Return = TypeVar('Return')
class Action(Generic[Return]):
	def __init__(self, actionFunc:Callable[...,Return], *args,**kwds):
		self.computeFunc,self.args,self.kwds = actionFunc,args,kwds
	def compute(self):return self.computeFunc(*self.args,**self.kwds)
	def __call__(self):return self.compute()
