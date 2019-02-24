### Data Science for OSRS

Have you ever thought "Wow, gathering data about shop prices and item profitability takes far too long"? Fear no longer because the future is now! Presenting: The RS Shop webscraper. 
 
 Searching, compiling and neatly presenting you with what you want to know
 for all your merching adventures.

![alt text](https://github.com/YacobBY/RsDataScience/blob/master/assets/Scraper.gif)

### Instructions:
First install the Pandas and beautifulsoup4 dependencies needed to run the program. 
This can be done through the pip installer.

Then run WikiTableScraper.py in order to start the webscraping. This will run through every shop
in the rswiki and compile all items matching a certain table layout from the wiki.

Then run the CSVCleaner.py file in order to clean remaining false-positives from the list.

You will now have a PythonExportCopy.csv file which contains all purchasable items and their profit
margins by buying and selling them on the GE. Next up you can load this CSV into google sheets.

In order to calculate extra values, you can use the following formulas and drag them down to fill
all respective indices in that column


### Sheets: 

Column F, buy from GE sell to shop:  =D1-E1

Column G, buy from GE sell to shop:  =E1-C1

Column H, profit ratio  on GE-Shop: =D1/E1

