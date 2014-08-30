#!/usr/bin/python
# -*-coding:Utf-8 -*

class UnitSize:
	
	def __init__(self, name, symbole):
		self.name = name
		self.symbole = symbole

class Size:
	
	def __init__(self, value, unitSize):
		self.value = value
		self.unitSize = unitSize

	def __str__(self):
		return "{0:d} {1:s}".format(self.value,self.unitSize.symbole)

if __name__ == "__main__":
	
	unitMo = UnitSize("MegaOctet", "Mo")
	s = Size(42, unitMo)
	
	print s

