import math 
def Calculate_Distance_Nodes(lat01,lat02,long01,long02):
    R=6378.137 #km
    lat01=float(lat01)
    lat02=float(lat02)
    long01=float(long01)
    long02=float(long02)
    dLat=(lat02-lat01)*(math.pi/180)
    dLong=(long02-long01)*(math.pi/180)
    Lat01torad=lat01*math.pi/180
    Lat02torad=lat02*math.pi/180
    Value_a=math.sin(dLat/2)*math.sin(dLat/2)+math.cos(Lat01torad)*math.cos(Lat02torad)*math.sin(dLong/2)*math.sin(dLong/2)
    Value_b=2*math.atan(math.sqrt(Value_a)/math.sqrt(1-Value_a))
    Distance=R*Value_b

    return Distance
def Calculate_Distance_Way(latlong): #takes 2 nodes same time and calulate all ways
    Distance_ways = 0

    for i in range(1, len(latlong)):
        a = latlong[i - 1]
        b = latlong[i]

        lat1 = a['lat']
        lat2 = b['lat']
        long1 = a['long']
        long2 = b['long']

        Distance2nodes = Calculate_Distance_Nodes(lat1, lat2, long1, long2)
        Distance_ways += Distance2nodes

    return Distance_ways