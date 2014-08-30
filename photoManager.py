#!/usr/bin/python
# -*-coding:Utf-8 -*

from photo import *

class PhotoManager:
	
	def __init__(self, name, directory):
		self.name = name
		self.directory = directory
		self.provide = photoProvider.PhotoProvider()
	

if __name__ == "__main__":
	
	p = photoProvider.PhotoProvider()
	p.provideListOfPhoto(".")

