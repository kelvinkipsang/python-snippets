import os
# create a function that saves data


def save_data(data, filename):
    data = input("What's your job?: ")
    with open('job.txt', 'a') as dt:
        dt.write(string_from_data('\n'+data))


def retrieve_data(filename):
    with open('job.txt') as dt:
        return data_from_string(dt.read())


def string_from_data(data):
    return ''.join(data)


def data_from_string(s):
    return s.split('\n')


FILENAME = 'job.txt'
if os.path.isfile(FILENAME):
    mylist = retrieve_data(FILENAME)
else:
    mylist = []

save_data(mylist, FILENAME)


print retrieve_data('job.txt')

	
