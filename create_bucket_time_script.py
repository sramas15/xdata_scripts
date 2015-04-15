with open("loc_time_bucket.sh", "w") as f:
  f.write("#!/bin/bash\n")
  for i in range(10):
    f.write("python loc_time_bucket.py /lfs/madmax7/0/ramasshe/xdata/output/condense/ny-nyc-0%d.txt /lfs/madmax7/0/ramasshe/xdata/output/loc_time_bucket/ny-nyc-0%d.txt\n" % (i, i))
  for i in range(10, 53):
    f.write("python loc_time_bucket.py /lfs/madmax7/0/ramasshe/xdata/output/condense/ny-nyc-%d.txt /lfs/madmax7/0/ramasshe/xdata/output/loc_time_bucket/ny-nyc-%d.txt\n" % (i, i))
