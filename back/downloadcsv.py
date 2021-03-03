import urllib.request
import logging

def download_csv(fichiertam, url):
    """Cette fonction se charge du téléchargement du fichier CSV TAM actuel"""
    logging.info('Téléchargement du fichier CSV depuis la TAM API')
    # url = 'https://data.montpellier3m.fr/sites/default/files/ressources/TAM_MMM_TpsReel.csv'
    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11'
           ' (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
           'Accept': 'text/html,application/xhtml+xml,'
           'application/xml;q=0.9,*/*;q=0.8',
           'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
           'Accept-Encoding': 'none',
           'Accept-Language': 'en-US,en;q=0.8',
           'Connection': 'keep-alive'}
    request = urllib.request.Request(url, headers=hdr)
    data = urllib.request.urlopen(request).read().decode('utf-8')
    data_str = str(data)
    file = open(fichiertam, 'w')
    file.write(data_str)
    file.close()
    logging.info("fichier csv téléchargé")

#download_csv("montpellier.csv","https://data.montpellier3m.fr/sites/default/files/ressources/TAM_MMM_TpsReel.csv")