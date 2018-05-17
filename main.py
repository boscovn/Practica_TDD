import sys
import practica

if __name__ == "__main__":
    file = open(sys.argv[1], 'r')
    print (practica.wordStats(file.read()))
