# Import dependencies
import csv
import os

# Assign file location with the csv library
poll_data=os.path.join("election_data.csv")

with open(poll_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #skip the header
    header= next(csvreader)

    #Declare Variables
    total_vt = 0
    khan_vt = 0
    correy_vt = 0
    li_vt = 0
    otooley_vt = 0




    for row in csvreader:

        # Count the unique Voter ID's and store in variable  called total_votes
        total_vt +=1
        if row[2] == "Khan":
            khan_vt+=1
        elif row[2] == "Correy":
            correy_vt +=1
        elif row[2] == "Li":
            li_vt +=1
        elif row[2] == "O'Tooley":
            otooley_vt +=1

khan_perc = '{0:.3f}'.format((khan_vt/total_vt) * 100)
corr_perc = '{0:.3f}'.format((correy_vt/total_vt) * 100)
li_perc = '{0:.3f}'.format((li_vt/total_vt) *100)
otool_perc = '{0:.3f}'.format((otooley_vt/total_vt) * 100)


print("Election Results")
print("Total Votes:" + str(total_vt)) 
print("Khan: " + str(khan_vt) + " " + str(khan_perc) + "%")
print("Correy: " + str(correy_vt) +  "  " + str(corr_perc) + "%")
print("Li: " + str(li_vt) +  " " + str(li_perc) + "%")
print("O'Tooley: " + str(otooley_vt) +  " " + str(otool_perc) + "%")



csvfile = open ("newpoll.txt", 'w')
csvfile.write("Election Results\n")
csvfile.write("Total Votes:" + str(total_vt) + "\n")
csvfile.write("Khan: " + str(khan_vt) + " " + str(khan_perc) + "%\n")
csvfile.write("Correy: " + str(correy_vt) +  "  " + str(corr_perc) + "%\n")
csvfile.write("Li: " + str(li_vt) +  " " + str(li_perc) + "%\n")
csvfile.write("O'Tooley: " + str(otooley_vt) +  " " + str(otool_perc) + "%\n")
csvfile.close()
