#!/usr/bin/python
# -*-coding:Utf-8 -*

import os

class PhotoProvider:

	def provideListOfPhoto(self, rootDirectory):
		res = {}
		files = os.listdir(rootDirectory)
		for f in files:
			print f
		return res
		

if __name__ == "__main__":
	
	p = PhotoProvider()
	p.provideListOfPhoto(".")

