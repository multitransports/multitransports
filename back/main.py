import sqlite3
import sys
from liste_ville import list_ville
from create_schema import create_schema  
from refresh import refresh


def main():
    conn = sqlite3.connect('transport.db')
    c = conn.cursor()
    create_schema(c)
    refresh(list_ville[0], c, conn)
    refresh(list_ville[1], c, conn)    

if __name__ == "__main__":
    sys.exit(main())