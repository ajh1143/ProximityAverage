import sys
import numpy as np

class ProximityAverage(object):

"""
Program that takes input of N integers on a single line, separated by single spaces. 
The program should then print the number from the list that is closest to the average of the N integers in the list. 
If there is more than one solution, output the one that occurs first in the input list.
"""

    def inputValue(self):
        #Input N values
        N = input()
        if N.isnumeric():
            return N
        else:
            raise ValueError("Please Enter a Valid Integer")
            inputValue()
                    
    def stripSplit(self, N):
        #Strip and Split N into digits
        digits = N.strip().split(" ")
        return digits
        
    def digitMapper(self, digs):
        #Map digits to ints as list
        castDigits = list(map(int, digits))
        return castDigits
        
    def findMean(self, mappedDigits):
        #Calculate Mean of list, NumPy for ease
        meanVal = np.mean(mappedDigits)
    
    def findMinAbsDif(self, meanValue)
        #Find smallest abs dif for each element in list compared to mean
        smallestDif = np.abs(castDigits-meanVal).argmin()
        return smallestDif
    
    def finalAnswer(self, mappedDigits, smallestDifference):
        #Access index position of smallestDif in castDigits list of values
        print(mappedDigits[smallestDifference])
        
if __name__ == "__main__":
    a = ProximityAverage()
    num = a.inputValue()
    digits = a.stripSplit(num)
    mapperResult = a.digitMapper(digits)
    mean = a.findMean(mapperResult)
    smallest = a.findMinAbsDif(mean)
    a.finalAnswer(mapperResult, smallest)
