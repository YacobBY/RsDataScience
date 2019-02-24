import pandas as pd

# CURRENTLY READS FROM COPIED FILE TO PREVENT BREAKING ON FIRST INDEX
dataFrame = pd.read_csv("PythonExportCopy.csv")

# print(data.head())
dataFrame = dataFrame.loc[:, 'Item':]
print(dataFrame)
filteredFrame = dataFrame
dataFrame['GE profit'] = 0
def isInt(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

for index, row in dataFrame.iterrows():
    if isInt(row['Pricebought at']) and isInt(row['GE price']):
        price = int(row['Pricebought at']) - int(row['GE price'])
        if  int (row['GE price']) > 0:
            dataFrame.set_value(index, "GE profit", price)
            print(row['Item'])
            print(price)



    elif index< len(dataFrame.index):
        print("looooooooool")
        dataFrame.drop(dataFrame.index[[index]], inplace=False)
        print("dropped index %d"%index)


print(dataFrame.to_string())
dataFrame.to_csv('PythonExport.csv')


# dfFinal = data['Item':'GE price']
# print(dfFinal)
# dfFinal.to_csv('resultList.csv', sep=',')

