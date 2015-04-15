import sys
import os

def create_script(directory, outFNm):
  with open(outFNm, "w") as outF:
    outF.write("#!/bin/bash\n")
    for fin in os.listdir(directory):
      if directory[-1] == "/":
        full_path = "%s%s" % (directory, fin)
      else:
        full_path = "%s/%s" % (directory, fin)
      outF.write("python bucket_week.py %s %s\n" % (full_path, fin))

if __name__ == '__main__':
  create_script('/dfs/scratch0/dataset/xdata/SummerCamp2015/nyc_taxi_trip', 'bucket_week.sh')
