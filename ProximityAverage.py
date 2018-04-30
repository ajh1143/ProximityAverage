import sys
import numpy as np

#Program that takes input of N integers on a single line, separated by single spaces.
#The program should then print the number from the list that is closest to the average of the N integers in the list.
#If there is more than one solution, output the one that occurs first in the input list.

class ProximityAverage(object):

    # Input N values, ex: 1 2 3 4 5
    def inputValue(self):
        N = input()
        return N

    # Split our N on space, to an array named digits
    def stripSplit(self, N):
        # Strip and Split N into digits
        digits = N.strip().split(" ")
        return digits

    # Create a list mapping digits to ints, named castDigits
    def digitMapper(self, digs):
        # Map digits to ints as list
        castDigits = list(map(int, digs))
        return castDigits

    def findMean(self, mappedDigits):
        # Calculate Mean of list, NumPy for ease
        meanVal = np.mean(mappedDigits)
        return meanVal

    def findMinAbsDif(self, mappedDigits, meanValue):
        # Find smallest abs dif for each element in list compared to mean
        smallestDif = np.abs(mappedDigits - meanValue).argmin()
        return smallestDif


    def finalAnswer(self, mappedDigits, smallestDifference):
        # Access index position of smallestDif in castDigits list of values
        print(mappedDigits[smallestDifference])


if __name__ == "__main__":
    a = ProximityAverage()
    num = a.inputValue()
    digits = a.stripSplit(num)
    mapperResult = a.digitMapper(digits)
    mean = a.findMean(mapperResult)
    smallest = a.findMinAbsDif(mapperResult, mean)
    a.finalAnswer(mapperResult, smallest)
