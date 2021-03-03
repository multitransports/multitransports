import sqlite3
import sys
from liste_ville import list_ville 
from create_schema import create_schema 
from update_db import update_db 
from load_csv import load_csv 

def main():
    conn = sqlite3.connect('transport.db')
    c = conn.cursor()
    create_schema(c)
    if list_ville(0) == list_ville(0):
        update_db('https://data.montpellier3m.fr/sites/default/files/ressources/TAM_MMM_TpsReel.csv', list_ville(0)+'.csv')
        load_csv(list_ville(0)+'.csv', c, list_ville(0))
        conn.commit()
    if list_ville(1) == list_ville(1):
        update_db('https://data.rennesmetropole.fr/explore/dataset/prochains-passages-des-lignes-de-metro-du-reseau-star-en-temps-reel/download/?format=csv&timezone=Europe/Berlin&lang=fr&use_labels_for_header=true&csv_separator=%3B', list_ville(1)+'.csv')
        load_csv(list_ville(1)+'.csv', c, list_ville(1))
        conn.commit()
    # if ville == 'Toulouse':
    #     load_csv(l.list_ville(2)+'.csv', c, l.list_ville(2))
    #     conn.commit()
    # if ville == 'Lyon':
    #     load_csv(l.list_ville(3)+'.csv', c, l.list_ville(3))
    #     conn.commit()



if __name__ == "__main__":
    sys.exit(main())