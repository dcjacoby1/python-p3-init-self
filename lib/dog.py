#!/usr/bin/env python3

#init is called when an object is added to class
#different then a def, bc def isn't performed on initialization of object
#if no init is defined, python will automatically init behind the scences that does nothing
class Dog:
    def __init__(self, name, breed = 'Mutt'):
        self.name = name
        self.breed = breed