import os
import csv

#countvotes
def countvotes(vlist, i): 
    count = 0
    for element in vlist: 
        if (element == i): 
            count = count + 1
    return count

#percentage 
def percentage(a,b):
    percent = 0 
    percent = round(a/b*100,2)
    return percent

#read file
input_electiondata = os.path.join("..","Resources", "election_data.csv")
with open(input_electiondata) as csvfile:
    readcsv = csv.reader(csvfile)
    
    #initialize variables
    votes_list = []
    vote_count =[0, 0, 0,0]
    Totalvotes=0
    count_votes = []
    percent_votes = []
    
    #exclude header
    header = next(readcsv,None)
    
    # reading the file
    for i in readcsv:
        votes_list.append(i[2])
        Totalvotes=Totalvotes + 1 
       
    # unique names
    votes_set = set(votes_list)
    unique_candidate = list(votes_set)
      
    # functions to count total votes
    for i in unique_candidate:
        count_votes.append(countvotes(votes_list,i))
        
    # use function to find percent of votes
    for i in count_votes:
        percent_votes.append(percentage(i,Totalvotes))
    
    # find the winner
    winnercount = round(max(count_votes))   
    final_array = zip(unique_candidate,percent_votes,count_votes)
    for i in final_array:
        #print(i[0])
        if winnercount == i[2]:
            Winner = i[0]
    
    #results
    print("  Election Results")
    print("-------------------------")
    print(f" Total Votes: {Totalvotes}")
    print("-------------------------")
    final_array = zip(unique_candidate,percent_votes,count_votes)
    for i in final_array:
        print(f" {i[0]} : {i[1]}% ({i[2]})")

    print("-------------------------")
    print(f" Winner: {Winner}")
    print("------------------------- ")
   
    #Print to file . need to redo zip as zip reads only once. 
    file1 = open("output_electionresults.txt","w") 
    file1.write("  Election Results\n")
    file1.write("------------------------\n")
        
    file1.write(f" Total Votes: {Totalvotes}\n")
    file1.write("------------------------\n")
    final_array = zip(unique_candidate,percent_votes,count_votes)
    for i in final_array:
        file1.write(f" {i[0]} : {i[1]}% ({i[2]})\n")
    file1.write("------------------------\n")
    file1.write(f" Winner: {Winner}\n")
    file1.write("------------------------\n")
    file1.close ()   

        
