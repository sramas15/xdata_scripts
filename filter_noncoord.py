import sys

def filter_noncoord(inFNm, outFNm):
    with open(inFNm, "r") as inF:
        with open(outFNm, "w") as outF:
            for line in inF:
                vals = line.strip().split(",")
                if vals[1] != "-1" and vals[1] != "-2":
                    outF.write(line)

if __name__ == "__main__":
    filter_noncoord(sys.argv[1], sys.argv[2])
