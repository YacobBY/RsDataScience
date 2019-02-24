import pandas as pd
import requests
from bs4 import BeautifulSoup


def getWikiLinks(urlBegin, urlEnd, wikiLink):
    wikiText = requests.get(wikiLink)
    soup = BeautifulSoup(wikiText.text, features="lxml")
    links = [a.get('href') for a in soup.find_all('a', href=True)]
    urlBegin2 = "http://oldschoolrunescape.wikia.com/wiki/Petrified_Pete%27s_Ore_Shop"
    urlEnd2 = "http://oldschoolrunescape.wikia.com/wiki/Zenesha%27s_Plate_Mail_Body_Shop"
    listIndexes = [0, 0]
    allLinks = []
    for link in links:
        url = "http://oldschoolrunescape.wikia.com%s" % link
        url = url.strip()
        if url == urlBegin:
            listIndexes[0] = links.index(link)

        if url == urlEnd:
            listIndexes[1] = links.index(link)
    print(listIndexes)
    return links[listIndexes[0]:listIndexes[1]]


shops = getWikiLinks("http://oldschoolrunescape.wikia.com/wiki/Aaron%27s_Archery_Appendages",
                     "http://oldschoolrunescape.wikia.com/wiki/Perry%27s_Chop-chop_Shop",
                     "http://oldschoolrunescape.wikia.com/wiki/Category:Shops?from=*")
shops += getWikiLinks("http://oldschoolrunescape.wikia.com/wiki/Petrified_Pete%27s_Ore_Shop",
                      "http://oldschoolrunescape.wikia.com/wiki/Zenesha%27s_Plate_Mail_Body_Shop",
                      "http://oldschoolrunescape.wikia.com/wiki/Category:Shops?from=Petrified+Pete%27s+Ore+Shop")
for link in shops:
    print(link)
    if "TzHaar" in link:
        shops.remove(link)
    # Begin Dataframe
shops.remove("/wiki/Shop")
shops.remove("/wiki/Kjut%27s_Kebabs")
shops.remove("/wiki/Stall")
dfFinal = pd.DataFrame()

print("Total amount of shops: %d" % len(shops))
for link in shops:
    url = "http://oldschoolrunescape.wikia.com%s" % link

    print(url)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, features="lxml")
    table = soup.find("table", {"class": "wikitable sortable"})

    if table:
        dft = pd.read_html(str(table), header=0, index_col=0, flavor='bs4')
        dfTemp = dft[0]
        if dfFinal.empty:
            print("aaa")
            dfFinal = dfTemp
            print(dfFinal)

        else:
            dfFinal = pd.concat([dfFinal, dfTemp], sort=False)
            print(dfFinal)
            dfFinal.ix[~(dfFinal['GE price'] == 'Not sold')]
            # sdf = dfFinal['Item', 'Numberin stock', 'Pricesold at', 'Pricebought at', 'GE price']
            dfFinal.to_csv('PythonExport.csv',index=False, sep=',')

            print(dfFinal)

        print("Added %s shop tot table" % link)
# dfFinal = dfFinal['Item':'GE price']
# dfFinal.to_csv('resultList.csv', sep=',')
