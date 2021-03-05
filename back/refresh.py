import urllib.request
from load_csv import load_csv

def refresh(ville, cursor, conn):
    urllib.request.urlretrieve(ville[2], ville[1])
    load_csv(ville[1], cursor, ville[0])
    conn.commit()