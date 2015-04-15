#!/bin/bash
python filter_noncoord.py /lfs/madmax7/0/ramasshe/xdata/output/dropoff_time_bucket/results_sort.txt /lfs/madmax7/0/ramasshe/xdata/output/dropoff_time_bucket/results_filter.txt
python filter_noncoord.py /lfs/madmax7/0/ramasshe/xdata/output/dropoff_bucket/results_sort.txt /lfs/madmax7/0/ramasshe/xdata/output/dropoff_bucket/results_filter.txt
python filter_noncoord.py /lfs/madmax7/0/ramasshe/xdata/output/pickup_time_bucket/results_sort.txt /lfs/madmax7/0/ramasshe/xdata/output/pickup_time_bucket/results_filter.txt
python filter_noncoord.py /lfs/madmax7/0/ramasshe/xdata/output/pickup_bucket/results_sort.txt /lfs/madmax7/0/ramasshe/xdata/output/pickup_bucket/results_filter.txt
