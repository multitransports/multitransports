import urllib.request
from back.load_csv import load_csv

def refresh(ville, cursor, conn):
    """This function download the csv file and
    add rows in the csv file

    ville : is the city if you want download the csv
    exemple : ville(0) is Montpellier

    cursor : It acts like a position indicator and will be mostly use to
    retrieve data.
    
    """
    urllib.request.urlretrieve(ville[2], ville[1])
    load_csv(ville[1], cursor, ville[0])
    conn.commit()