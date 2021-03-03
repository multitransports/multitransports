

def insert_csv_row(csv_row, cursor, ville):
    """ This function insert values in table 'infoarret'

    cursor : It acts like a position indicator and will be mostly use to
    retrieve data.

    csv_row : retrieve the lines on the csv file.

    """
    
    if ville == 'Montpellier':
        liste_row = csv_row.strip().split(";")
        new_row = [liste_row[3], liste_row[4], liste_row[5], liste_row[7], ville]
        cursor.execute("""INSERT INTO infoarret VALUES (?,?,?,?,?) """,
                    new_row)
    elif ville == 'Rennes':
        liste_row = csv_row.strip().split(";")
        horaire = ''.join(liste_row[7].split('T')[-1]).split('+')[0]
        new_row = [liste_row[5], liste_row[1], liste_row[3], horaire, ville]
        cursor.execute("""INSERT INTO infoarret VALUES (?,?,?,?,?) """,
                    new_row)
    # elif ville == 'Toulouse':
    #     liste_row = csv_row.strip().split(";")
    #     new_row = [liste_row[3], liste_row[4], liste_row[5], liste_row[7], ville]
    #     cursor.execute("""INSERT INTO infoarret VALUES (?,?,?,?,?) """,
    #                 new_row)
    # elif ville == 'Lyon':
    #     liste_row = csv_row.strip().split(";")
    #     new_row = [liste_row[3], liste_row[4], liste_row[5], liste_row[7], ville]
    #     cursor.execute("""INSERT INTO infoarret VALUES (?,?,?,?,?) """,
    #                 new_row)