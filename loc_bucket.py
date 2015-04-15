import math
import sys

CENTER_LONG = -73.9954898
CENTER_LAT = 40.7214947
RADIUS_EARTH = 3959 # in miles
OUT_BOUNDS = -1
NO_COORDS = -2
BUCKETS_PER_MILE = 20
PICKUP_LONG = 0
PICKUP_LAT = 1
DROPOFF_LONG = 2
DROPOFF_LAT = 3

BUCKET_DIST = 50 # in miles

class Direction:
    north = 1
    south = 2
    east = 3
    west = 4

def dist(lat1, lon1, lat2, lon2):
  lat1 *= math.pi / 180
  lat2 *= math.pi / 180
  lon1 *= math.pi / 180
  lon2 *= math.pi / 180
  dlon = lon2 - lon1 
  dlat = lat2 - lat1 
  a = pow(math.sin(dlat/2), 2) + math.cos(lat1) * math.cos(lat2) * pow(math.sin(dlon/2), 2) 
  c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a)) 
  d = RADIUS_EARTH * c
  return d


# Change in longitude
def GetDX(coord1, coord2=(CENTER_LONG, CENTER_LAT)):
    """Coordinates should be tuples consisting of floats, of the form (longitude, latitude)."""
    (lon1, lat1) = coord1
    (lon2, lat2) = coord2
    # Keep latitude fixed to get horizontal distance distance
    distance = dist(lat1, lon1, lat1, lon2)
    if lon1 > lon2:
        direction = Direction.east
    else:
        direction = Direction.west
    return (distance, direction)

def GetDY(coord1, coord2=(CENTER_LONG, CENTER_LAT)):
    """Coordinates should be tuples consisting of floats, of the form (longitude, latitude)."""
    (lon1, lat1) = coord1
    (lon2, lat2) = coord2
    # Keep latitude fixed to get horizontal distance distance
    distance = dist(lat1, lon1, lat2, lon1)
    if lat1 > lat2:
        direction = Direction.north
    else:
        direction = Direction.south
    return (distance, direction)

def GetBucket(coord1, coord2=(CENTER_LONG, CENTER_LAT)):
    (xdist, xdir) = GetDX(coord1, coord2)
    (ydist, ydir) = GetDY(coord1, coord2)
    bucketx = buckety = 0
    if xdist >= BUCKET_DIST or ydist >= BUCKET_DIST:
        bucketx = buckety = OUT_BOUNDS
        if (coord1[0] == 0 and coord1[1] == 0):
            bucketx = buckety = NO_COORDS
    else:
        if xdir == Direction.east:
            tempx = BUCKET_DIST + xdist
        else:
            tempx = BUCKET_DIST - xdist
        if ydir == Direction.north:
            tempy = BUCKET_DIST + ydist
        else:
            tempy = BUCKET_DIST - ydist
        bucketx = int(tempx*BUCKETS_PER_MILE)
        buckety = int(tempy*BUCKETS_PER_MILE)
    return (bucketx, buckety)

def BucketByLocation(inFNm, outFNm, location_type="dropoff"):
    if location_type not in ["pickup", "dropoff"]:
        raise Exception("Not a proper location to bucket")
    with open(outFNm, "w") as outF:
        with open(inFNm, "r") as inF:
            longInd = PICKUP_LONG
            latInd = PICKUP_LAT
            if location_type == "dropoff":
                longInd = DROPOFF_LONG
                latInd = DROPOFF_LAT
            for line in inF:
                vals = line.split(",")
                if vals[longInd] == "\N":
                    vals[longInd] = "0.0"
                if vals[latInd] == "\N":
                    vals[latInd] = "0.0"
                longitude = float(vals[longInd])
                latitude = float(vals[latInd])
                bucket = GetBucket((longitude, latitude))
                outF.write("%d,%d\n" % bucket)

if __name__ == "__main__":
    BucketByLocation(sys.argv[1], sys.argv[2])
