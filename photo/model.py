#!/usr/bin/python
# -*-coding:Utf-8 -*

from unit import *

class Album:
	
	def __init__(self, name):
		self.name = name
		self.photos = []

	def addPhoto(self,photo):
		self.photos.append(photo)

	def printAllPhoto(self):
		print self
		for photo in self.photos:
			print "\t- {}".format(photo)

	def __str__(self):
		nbPhotos = len(self.photos)
		return "Il y a {} photo{} dans l'album \"{}\"".format(nbPhotos, "s" if nbPhotos > 0 else "", self.name )

class Photo:
	
	def __init__(self, author, device, size):
		self.author = author
		self.device = device
		self.size = size

	def __str__(self):
		return "Photo de {} avec un {} pour une taille de {}".format(self.author, self.device, self.size)


if __name__ == "__main__":
	
	unitMo = UnitSize("MegaOctet", "Mo")
	
	pA = Photo("JPascal", "D7000", Size(20,unitMo))
	
	print pA

	albumVacances = Album("Vacances")
	print albumVacances
	
	albumVacances.addPhoto(pA)

	albumVacances.printAllPhoto()
