from datetime import datetime
import sys

TEMP_DIR = "/lfs/madmax7/0/ramasshe/xdata/temp"
TIME_FORMAT = "%Y-%m-%d %H:%M:%S"
PICKUP_DATETIME = 5

def processFile(filename, fileWODir):
    with open(filename, "r") as f:
        for line in f:
            vals = line.split(",")
            try:
                dt = datetime.strptime(vals[PICKUP_DATETIME], TIME_FORMAT)
                week_num = dt.isocalendar()[1] - 1 # subtract 1 to make 0-index
                if (week_num == 0 and dt.month == 12) or dt.year == 2014:
                    week_num += 52
                temp_file = "%s/%s-%d" % (TEMP_DIR, fileWODir, week_num)
                with open(temp_file, "a") as out:
                    out.write(line)
            except ValueError:
                print "error"

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print 'Usage: %s <InputFile> <ID>' % (sys.argv[0])
        sys.exit(1)
    filename = sys.argv[1]
    file_id = sys.argv[2]
    processFile(filename, file_id)
