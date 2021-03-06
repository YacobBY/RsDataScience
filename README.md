### Data Science for OSRS

With this scraper you can automatically find out which items are profitable to buy from shops and sell to the GE.
 
 Searching, compiling and neatly presenting you with what you want to know
 for your merching adventures.

![alt text](https://github.com/YacobBY/RsDataScience/blob/master/assets/Scraper.gif)

### Instructions:
First install the Pandas and beautifulsoup4 dependencies needed to run the program. 
This can be done through the pip installer.

Then run WikiTableScraper.py in order to start the webscraping. This will run through every shop
in the rswiki and compile all items matching a certain table layout from the wiki.

Then run the CSVCleaner.py file in order to clean remaining false-positives from the list.

![alt text](https://github.com/YacobBY/RsDataScience/blob/master/assets/Cleaner.gif)

You will now have a PythonExportCopy.csv file which contains all Runescape purchasable items and their profit
margins by buying and selling them on the GE. Next up you can load this CSV into 

### Google Sheets.

In order to calculate extra values, you can use the following formulas and drag them down to fill
all respective indices in that column

Column F, buy from GE sell to shop:  =D1-E1

Column G, buy from GE sell to shop:  =E1-C1

Column H, profit ratio  on GE-Shop: =D1/E1

![alt text](https://github.com/YacobBY/RsDataScience/blob/master/assets/Margins.png)
