import sqlite3
import urllib.request
import sys


def list_ville(index):
    list_ville = ['Montpellier','Rennes','Toulouse', 'Lyon']
    return list_ville[index]

def update_db(csv_url, outputfile):
    """This function, retrieve the csv from url and download this csv file

    """
    urllib.request.urlretrieve(csv_url, outputfile)
    # logging.info('update_db: Mise a jour de la base de données')

update_db('https://data.montpellier3m.fr/sites/default/files/ressources/TAM_MMM_TpsReel.csv', list_ville(0)+'.csv')



def insert_csv_row(csv_row, cursor, ville):
    """ This function insert values in table 'infoarret'

    cursor : It acts like a position indicator and will be mostly use to
    retrieve data.

    csv_row : retrieve the lines on the csv file.

    """
    liste_row = csv_row.strip().split(";")
    new_row = [liste_row[3], liste_row[4], liste_row[5], liste_row[7], ville]

    cursor.execute("""INSERT INTO infoarret VALUES (?,?,?,?,?) """,
                   new_row)



def create_schema(cursor):
    """ This function create table 'infoarret' if not exist

    this table contains 11 columns and determinate the type.

    cursor : It acts like a position indicator and will be mostly use to
    retrieve data.

    """
    cursor.execute("""CREATE TABLE IF NOT EXISTS "infoarret" (
    "Station"	TEXT,
    "Ligne"	TEXT,
    "Direction"	TEXT,
    "Horaire"	TEXT,
    "Ville" TEXT
    );""")
    # logging.info('create_schema: on cree les colonnes de la base')


def load_csv(path, cursor, ville):
    """ This function load and read the csv file, and insert row in db file.

    cursor : It acts like a position indicator and will be mostly use to
    retrieve data.

    path : Source of the csv file.

    """
    with open(path, "r") as f:    
        f.readline()
        line = f.readline()
        while line:
            insert_csv_row(line, cursor, ville)
            line = f.readline()
    # logging.info('load_csv: Charge la base de données')



def main():
    conn = sqlite3.connect('transport.db')
    c = conn.cursor()
    create_schema(c)
    load_csv(list_ville(0)+'.csv', c, list_ville(0))
    conn.commit()
    conn.close()



if __name__ == "__main__":
    sys.exit(main())
