def calculate_traffic_distance_miles(row):
    """Calculates the distance in miles between two coordinate pairs using geopy.

    Args:
        row: A row in the GeoDataFrame.

    Returns:
        The distance in miles.
    """

    # Extract latitude and longitude for the two points
    lat1, lon1 = row['LATITUDE_x'], row['LONGITUDE_x']
    lat2, lon2 = row['LATITUDE_y'], row['LONGITUDE_y']

    # Create coordinate tuples
    coord1 = (lat1, lon1)
    coord2 = (lat2, lon2)

    # Calculate distance in miles using geodesic distance
    #distance_miles = geodesic(coord1, coord2).miles 
    distance_miles = (((lat1 - lat2)**2 + (lon1 - lon2)**2)**.5) * 58.129816

    return distance_miles
