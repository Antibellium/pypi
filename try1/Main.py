from array import array
#from Greedy import greedy
from GuessAndCheck import guessAndCheck
from LoadMap import loadMap

print("Welcome to Arianna's Shortest Path program. \nWorking through Guess-and-Check.")

cityCount = 8
print("Our city count is", cityCount)
path = [0 for i in range(cityCount)]

cityMap = loadMap(cityCount)
guessAndCheck(path, cityMap)
#greedy(path, cityMap)