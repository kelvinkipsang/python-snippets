


def get_search():
    holder = input("input somethin?:")  
    data = open('some.txt', 'r')  
    data_list = data.readlines()   # save each line in data_list
    data.close()  

    found = False  # 
    for item in range(0,len(course_list)):
        if holder == data_list[item]:
            print data_list[item]
          



            found = True  

        if holder != course_list[item]:
            new_data = open('some.txt', 'a')
            save_data = new_data.write(degree)  
            new_data.close()
    return new_data


print get_search()

