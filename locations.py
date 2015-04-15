
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
PICKUP_TIME = 4
DROPOFF_TIME = 5

TIME_FORMAT = "%Y-%m-%d %H:%M:%S"
OUTPUT_TIME_FORMAT = "%Y-%m-%d"

BUCKET_DIST = 50 # in miles

class Direction:
    north = 1
    south = 2
    east = 3
    west = 4

def GetLongLat(bucket_x, bucket_y, coord2=(CENTER_LONG, CENTER_LAT)):
    middle_bucket = BUCKET_DIST * BUCKETS_PER_MILE
    # Get direction from the center point
    dist_x = bucket_x/float(BUCKETS_PER_MILE)
    dist_y = bucket_y/float(BUCKETS_PER_MILE)
    direction = [0, 0]
    if dist_x > BUCKET_DIST:
        dist_x -= BUCKET_DIST
        direction[0] = Direction.east
    else:
        dist_x = BUCKET_DIST - dist_x
        direction[0] = Direction.west
    if dist_y > BUCKET_DIST:
        dist_y -= BUCKET_DIST
        direction[1] = Direction.north
    else:
        dist_y = BUCKET_DIST - dist_y
        direction[1] = Direction.south
    # Get longitude
    (lon2, lat2) = coord2
    lat2 *= math.pi / 180
    lon2 *= math.pi / 180
    c = dist_x/RADIUS_EARTH
    b = math.tan(c/2)
    a = pow(b, 2)/(1 + pow(b,2))
    deltaLon =  2 * math.asin(math.sqrt(a / (pow(math.cos(lat2), 2))))
    if direction[0] == Direction.east:
        lon1 = lon2 + deltaLon
        lon1 /= (math.pi * 1/180)
    else:
        lon1 = lon2 - deltaLon
        lon1 /= (math.pi * 1/180)
    # Calculate latitude
    c = dist_y/RADIUS_EARTH
    b = math.tan(c/2)
    a = pow(b, 2)/(1 + pow(b,2))
    deltaLat =  2 * math.sqrt(a)
    if direction[1] == Direction.north:
        lat1 = lat2 + deltaLat
        lat1 /= (math.pi * 1/180)
    else:
        lat1 = lat2 - deltaLat
        lat1 /= (math.pi * 1/180)
    return (lon1, lat1)

def PrintLatLong(inFNm, outFNm):
    with open(outFNm, "w") as fOut:
        with open(inFNm, "r") as fIn:
            for line in fIn:
                coords = line.strip().split(",")
                bucket_lon = float(coords[0])
                bucket_lat = float(coords[1])
                (lon, lat) = GetLongLat(bucket_lon, bucket_lat)
                fOut.write("%f,%f\n" % (lon, lat))

if __name__ == "__main__":
    PrintLatLong(sys.argv[1], sys.argv[2])
