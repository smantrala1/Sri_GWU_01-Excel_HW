import os
import csv

cereal_csv = os.path.join("../Resources", "cereal.csv")


with open(cereal_csv,'r') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents(default delimiter is a comma)
    readcsv = csv.reader(csvfile)
    
    header = next(readcsv,None)
    #print(header)
    for lines in readcsv:
         if float(lines[7]) >= 5:
             print(f"{lines[0]} has {lines[7]}gms of fiber, {lines[3]}calories per serving.")
    # "100% Bran has 10 grams of fiber, 70 calories per serving.

    