import os
import sys
from datetime import datetime
FILE_DIR = "/lfs/madmax7/0/ramasshe/xdata/output/time_buckets"
OUT_DIR = "/lfs/madmax7/0/ramasshe/xdata/output"
PICKUP_DATETIME = 5
DROPOFF_DATETIME = 6
PICKUP_LONG = 10
PICKUP_LAT = 11
DROPOFF_LONG = 12
DROPOFF_LAT = 13
TIME_FORMAT = "%Y-%m-%d %H:%M:%S"

def createOutput(inFNm, outFNm):
    out_path = "%s/%s" % (OUT_DIR, outFNm)
    with open(out_path, "w") as outF:
        full_path = "%s/%s" % (FILE_DIR, inFNm)
        with open(full_path, "r") as inF:
            for line in inF:
                line = line.strip()
                vals = line.split(",")
                out_line = "%s,%s,%s,%s,%s,%s\n" % (vals[PICKUP_LONG], vals[PICKUP_LAT], vals[DROPOFF_LONG], vals[DROPOFF_LAT], vals[PICKUP_DATETIME], vals[DROPOFF_DATETIME])
                outF.write(out_line)

if __name__ == '__main__':
  createOutput(sys.argv[1], sys.argv[2])
