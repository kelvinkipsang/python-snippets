


import csv  
with open('MOCK_DATA.csv', 'r') as csvfile:  
    id_number = raw_input('Enter your id please: ')  
    data_reader = csv.reader(csvfile, delimiter=',')  # delimiter-slicing the commas

    for row in data_reader:  # iterate through
        if id_number == row[0]:
            
            print row[1] +" "row[3]+" "+row[5]

        else:
            pass










