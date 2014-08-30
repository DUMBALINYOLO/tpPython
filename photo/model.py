#!/usr/bin/python
# -*-coding:Utf-8 -*

class Album:
	
	def __init__(self, name):
		self.name = name
		self.photos = []

	def addPhoto(self,photo):
		self.photos.append(photo)

	def __str__(self):
		nbPhotos = len(self.photos)
		return "Il y a {} photo{} dans l'album \"{}\"".format(nbPhotos, "s" if nbPhotos > 0 else "", self.name )

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

	print pA

	albumVacances = Album("Vacances")
	print albumVacances
	
	albumVacances.addPhoto(pA)

	print albumVacances
