import numpy as np
import matplotlib.pyplot as plt
import sys

def plotFile(inFNm):
    xs = []
    ys = []
    count = 0
    with open(inFNm, "r") as fIn:
        for line in fIn:
            xs.append(count)
            count += 1
            val = int(line.strip().split(" ")[0])
            ys.append(val)
    x_arr = np.array(xs)
    y_arr = np.array(ys)
    plt.scatter(x_arr, y_arr)
    plt.show()

if __name__ == "__main__":
    plotFile(sys.argv[1])
