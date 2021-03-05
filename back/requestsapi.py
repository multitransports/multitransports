def requestnexttram(cursor, station, ville):
    """The function search on the table 'infoarret'
    Then it returns the next passes the line and the direction.

    cursor : It acts like a position indicator and will be mostly use to
    retrieve data.
    
    station : is the station to select for see the next tramway in 
    this station

    ville : Is the city for search station 
    in this city
    """
    res=[]
    cursor.execute("""
    SELECT * FROM infoarret
    WHERE Station = ?
    AND Ville = ?
    """, (station ,ville,))
    for row in cursor.fetchall():
        res.append((dict(row)))
    return res
# logging.info("next_tram: Affichage de la demande de l'utilisateur(argument next) ")

def request_city_station(cursor,ville):
    """This function search  from table 'infoarret'
    return all station in the country selected.

    cursor : It acts like a position indicator and will
    be mostly use to retrieve data.

    ville : Is the city for search all station 
    in this city
    """


    res = []
    cursor.execute("""SELECT DISTINCT Station
    From infoarret WHERE Ville = ?""",
    (ville,))
    for row in cursor.fetchall():
        res.append((dict(row)))

    return res


def request_line_station(cursor, ville ,ligne):
    """
    The function search on the table 'infoarret'
    Then it returns all station with number of line.

    cursor : It acts like a position indicator and will be mostly use to
    retrieve data.
    
    line : is the line to select for see all stations in this line

    ville : Is the city for search station 
    in this city"""

    res = []
    cursor.execute("""SELECT DISTINCT Station
    FROM infoarret WHERE Ville = ?
    AND Ligne = ?""", (ville,ligne,))

    for row in cursor.fetchall():
        res.append((dict(row)))
    return res


def request_next_to_direction(cursor,ville, station, ligne, direction):
    """ This function search on the table 'infoarret'
    the database for recuperate the line in the column
    (Station , line and direction) and return the request

    cursor : It acts like a position indicator and will be mostly use to
    retrieve data.

    line : is the line to select for see all stations in this line

    ville : Is the city for search station 
    in this city

    station : is the station to select for see the next tramway in 
    this station

    direction : Is the direction select for see the next tramway in
    this direction

    """
    res = []
    cursor.execute("""
    SELECT * FROM infoarret
    WHERE Station = ?
    AND Ligne = ?
    AND Direction = ?
    AND Ville = ?""",
    (station, ligne, direction, ville))
    for row in cursor.fetchall():
        res.append((dict(row)))
    return res


def request_station_like(cursor,station,ville):
    """This function search on the table 'infoarret'
    then it return, the station start with the search
    in the city choice.

    ville : Is the city for search station 
    in this city

    station : is the station to select for see the next tramway in 
    this station
    """
    
    res=[]
    rows = cursor.execute("""
    SELECT * FROM infoarret
    WHERE Station like ?
    AND Ville = ?
    """, ('%'+station+'%' , ville))
    for row in cursor.fetchall():
        res.append((dict(row)))
    return res