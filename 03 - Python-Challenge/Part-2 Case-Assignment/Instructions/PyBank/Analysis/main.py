import os
import csv

input_budgetdata = os.path.join("..","Resources", "budget_data.csv")
def Average(lst): 
    return sum(lst) / len(lst) 

with open(input_budgetdata) as csvfile:
    readcsv = csv.reader(csvfile)
    #print(readcsv)
    header = next(readcsv)
    no_ofMonths = 0    
    Total = 0 
    Plvalue = []
    Monthvalue = []
    changesarray = []
    newarray = []
    difference = 0 
    changesarray1 = []
    newarray1 = []
    #print(numberofmonths)
    for line in readcsv:
        
        #The total number of months included in the dataset
        no_ofMonths = no_ofMonths + 1
        #The net total amount of "Profit/Losses" over the entire period
        Plvalue.append(float(line[1]))
        Monthvalue.append(line[0])
        Total = Total + float(line[1])
        newarray1 = zip(Plvalue, Plvalue[1:])  

    #changesarray = ([v2 - v1 for v1, v2 in zip(Plvalue, Plvalue[1:])])
    for i in newarray1:
        difference = i[1] - i[0] 
        changesarray1.append(difference)
            
    #print(changesarray1)                
    #print(changesarray)            
        
    newarray = zip(Monthvalue[1:],changesarray1)
    #print(newarray)


    average = Average(changesarray1)
    #print("Average Change: $"+str(round(average,2)))
    greatestincrease = 0 
    greatestdecrease = 0 
    greatestincrease = round(max(changesarray1))
    greatestdecrease = round(min(changesarray1))
    
    for i in newarray:
        if greatestincrease == i[1]:
            Monthinc = i[0]
            #print(Monthinc)
        if greatestdecrease == i[1]:
            Monthdec = i[0]
            #print(Monthdec)    
    
    #Print to terminal 
    print("  Financial Analysis")
    print("------------------------")
    print(f" Total Months: {no_ofMonths}")
    print(f" Total: ${round(Total,0)}")
    print(f" Average Change: ${round(average,2)}")
    print(f" Greatest Increase in Profits: {Monthinc} (${greatestincrease})")
    print(f" Greatest Descrease in Profits: {Monthdec} (${greatestdecrease})")
    
    #Print to file
    file1 = open("output_PyBank.txt","w") 
    #with open(file1, "w") as datafile:
        #writer = csv.writer(datafile)
    file1.write("  Financial Analysis\n")
    file1.write("------------------------\n")
        
    file1.write(f" Total Months: {no_ofMonths}\n")
    file1.write(f" Total: ${round(Total,0)}\n")
    file1.write(f" Average Change: ${round(average,2)}\n")
    file1.write(f" Greatest Increase in Profits: {Monthinc} (${greatestincrease})\n")
    file1.write(f" Greatest Descrease in Profits: {Monthdec} (${greatestdecrease})\n")
    file1.close ()   

