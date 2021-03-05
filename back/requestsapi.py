def requestnexttram(cursor, station, ville):
    """The function configure the argument 'next'
    this function request the
    database for recuperate line in the column stop_name,delay_sec and
    route_short_name.
    Then it returns the next passes in min,sec, the line and the direction.
    cursor : It acts like a position indicator and will be mostly use to
    retrieve data.
    database : Search in the SQlite database.
    """
    res=[]
    #rows = 
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
    res = []
    cursor.execute("""SELECT DISTINCT Station
    From infoarret WHERE Ville = ?""",
    (ville,))
    for row in cursor.fetchall():
        res.append((dict(row)))

    return res


def request_line_station(cursor, ville ,ligne):
    res = []
    cursor.execute("""SELECT DISTINCT Station
    FROM infoarret WHERE Ville = ?
    AND Ligne = ?""", (ville,ligne,))

    for row in cursor.fetchall():
        res.append((dict(row)))
    return res


def request_next_to_direction(cursor,ville, station, ligne, direction):
    """ This function configure the argument 'time'
    this function request
    the database for recuperate the line in the column
    (Station , line and direction) and return the request
    cursor : It acts like a position indicator and will be mostly use to
    retrieve data.
    database : Search in the SQlite database
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