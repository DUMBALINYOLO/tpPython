#!/usr/bin/python
# -*-coding:Utf-8 -*

class Album:
	
	def __init__(self, name):
		self.name = name
		self.photos = []

	def addPhoto(self,photo):
		self.photos.append(photo)

class Photo:
	
	def __init__(self, author, device, size, unit):
		self.author = author
		self.device = device
		self.size = size
		self.unitSize = unit

class UnitSize:
	
	def __init__(self, name, shortName):
		self.name = name
		self.shortName = shortName

if __name__ == "__main__":
	
	pA = Photo("JPascal", "D7000", 20, UnitSize("Megaoctet", "Mo"))
	print "Photo prise par {} avec {} [{} {}]".format(pA.author, pA.device, pA.size, pA.unitSize.shortName)

	albumVacances = Album("Vacances")
	print "Il y a {} photos dans l'album".format(len(albumVacances.photos))
	
	albumVacances.addPhoto(pA)
	print "Il y a {} photos dans l'album".format(len(albumVacances.photos))

