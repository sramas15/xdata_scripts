import sys

NUM_DAYS = 368
BUCKETS_PER_DAY = 6

def findHigherThanAvg(inFNm, inFNm2, outFNm, num_time_buckets=NUM_DAYS*BUCKETS_PER_DAY):
    with open(outFNm, "w") as fOut:
        placeToFreq = {}
        with open(inFNm, "r") as fIn:
            for line in fIn:
                vals = line.strip().split(" ")
                freq = int(vals[0])
                coords = vals[1].split(",")
                placeToFreq[tuple(coords)] = freq
        with open(inFNm2, "r") as fIn:
            for line in fIn:
                vals = line.strip().split(" ")
                coords = vals[1].split(",")
                coords = (coords[0], coords[1])
                freq = float(vals[0])
                percent = freq/placeToFreq[coords]
                for i in range(1, len(vals)):
                    fOut.write("%s," % vals[i])
                fOut.write("%f,%d\n" % (percent, freq))

if __name__ == "__main__":
    findHigherThanAvg(sys.argv[1], sys.argv[2], sys.argv[3])
