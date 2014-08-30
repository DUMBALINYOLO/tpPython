#!/usr/bin/python
# -*-coding:Utf-8 -*

class Photo:
	
	def __init__(self, author, device, size):
		self.author = author
		self.device = device
		self.size = size

if __name__ == "__main__":
	
	pA = Photo("JPascal", "D7000", 20)
	print "Photo prise par {} avec {} [{} M]".format(pA.author, pA.device, pA.size)

