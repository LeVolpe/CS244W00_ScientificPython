import numpy as np

def read_data(filename):

    a = np.genfromtxt(filename, delimiter=",", dtype=None)


    return a

def main():
    print(read_data('iris.csv'))

main()