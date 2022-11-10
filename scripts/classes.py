#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 09:15:24 2022

@author: danielagaio
"""

class sample:
    
    def __init__(self,number_of_bins):
        self.number_of_bins=number_of_bins
        
    def bins(self):
        print(f"I'am a sample and I have {self.number_of_bins}")
        
    def info2(self):
        print("something else")
        
        
    def contigs(self):
        pass
        
        
    def parsing(self):
        pass
    
        
class positive_control(sample):
    
    def __init__(self,number_of_replicates):
        super().__init___(number_of_replicates)
        self.number_of_replicates=number_of_replicates
        
    def info(self):
        print(f"I'am a positive control and I have {self.number_of_replicates} replicates.")
        
    def info2(self):
        print("something else")
        
        
class pig(sample):
    
    def __init__(self,number_of_bins,.....):
        super().__init___(number_of_bins)
        self.....=....
        
    def info(self):
        print(f"I'am a positive control and I have {self.number_of_replicates} replicates.")
        
    def info2(self):
        print("something else")
    
    
    
    
#class sow(sample):
    
class Animal:
    def __init__(self, weight):
        self.weight = weight
    
    def info(self):
        print(f"I'am an abstract animal which weights {self.weight} kg.")
    
    def noise(self):
        print("I'am abstract, I don't make noises")
        
    
class Cat(Animal):
    def __init__(self,weight,name,age,color):
        super().__init__(weight)
        self.name = name
        self.age = age
        self.color = color
        
    def __str__(self):
        print( f"{self.name} is {self.age} years old")
    
    def description(self):
        return f"{self.name} is {self.age} years old"
        
    def noise(self):
        print("Meouw")
        
 
class Dog(Animal):
    species = "Canis familiaris"
    def __init__(self,weight,breed):
        super().__init__(weight)
        self.breed = breed
    
    # Instance method
    def info(self):
        print(f"I'am a (self.breed) cat that weights {self.weight} kg.")
    
    # Instance method
    def noise(self):
        print("Woof")
    
    
a = Dog(25,"dalmatian")
print(a.weight)
print(a.breed)
print(a.species)
print(a.noise())

a = Cat(5, "Garfield", 19, "orange")
print(a.description())
print(a.noise())

    
    
    