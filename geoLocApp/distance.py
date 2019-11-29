from math import radians, cos, sin, asin, sqrt

def distance(lat1: float, lat2: float, lon1: float,lon2: float) -> float:
    
    assert isinstance(lat1,(float,int)),f"TypeError:{lat1} is not type of float or int."
    assert isinstance(lat2,(float,int)),f"TypeError:{lat2} is not type of float or int."
    assert isinstance(lon2,(float,int)),f"TypeError:{lon2} is not type of float or int."
    assert isinstance(lon1,(float,int)),f"TypeError:{lon1} is not type of float or int."
    
    #Convertion from degree to radians
    lat1 = radians(lat1)
    lat2 = radians(lat2)
    lon1 = radians(lon1)
    lon2 = radians(lon2)

    #Heversine formula
    dlon = lon2-lon1
    dlat = lat2-lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * asin(sqrt(a))

    #Radius of earth in kilometers.
    EARTH_RADIUS = 6371
    
    #Calculate the result
    return c * EARTH_RADIUS * 1000

    
    