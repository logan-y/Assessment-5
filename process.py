log_file = open("um-server-01.txt") #define the var log_file as the open file to pull data from.


def sales_reports(log_file): #creates a function that uses the now open file
    for line in log_file: #creates a loop that iterates through each row in um-server-01
        line = line.rstrip() #removes trailing characters at the end of the row
        day = line[0:3] #creates a var whose value is three elements in the string, starting from 0
        if day == "Mon": #creates a cond. statement to compare day to "Mon"
            print(line) #output the entire row of data, end of fn


sales_reports(log_file) # invoke the function using um-server-01 as the db
