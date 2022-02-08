##file_obj=open("writingFile.txt","w")
##file_obj.write("India is My Country")
##file_obj.close()



##file_obj=open("writingFile.txt","w")
##file_obj.write("Kholi and Dhoni makes the Partnership strong")
##file_obj.close()



##file_obj=open(r"D:\ZONE C FOR WORKSPACE\PYTHON\writingFile.txt","w")
##file_obj.write("Kholi and Dhoni makes the Partnership strong")
##file_obj.close()



##import tkinter  #tkinter is a library fro creating GUI only using python
##from tkinter import filedialog
##import os
##
###To not show the driver
##root=tkinter.Tk()
##root.withdraw()
##
###getting the folder by enabling the filedialog
##folder=filedialog.askdirectory()
##print(folder)
##
##file=os.path.join(folder,"writingFile.txt")
##file_obj=open(file,"w")
##file_obj.write("Dhoni finishes  off in his style")
##file_obj.close()







##file_obj=open("writingFile.txt","a")
##file_obj.write("\n")
##file_obj.write("This is vignesh")
##file_obj.close()


##file_obj=open("writingFile.txt","a")
##file_obj.write("\n")
##file_obj.writne("This is vignesh")
##file_obj.close()



#context Manager
##with open("writingFile.txt","a") as file_obj:
##    file_obj.write("\n")
##    file_obj.write("This is Randy Orton")





##with open("writingFile.txt","x") as file_obj:  
##    file_obj.write("\n")   #FileExistsError: [Errno 17] File exists: 'writingFile.txt'
##    file_obj.write("This is Randy Orton")


"""Reading"""
##with open("writingFile.txt","r") as file_obj:  
##    file_content=file_obj.read()
##    print(file_content)



##with open("writingFile.txt","r") as file_obj:  
##    file_content=file_obj.read(4)
##    print(file_content)
##    file_content=file_obj.read()
##    print(file_content)


##with open("writingFile.txt","r") as file_obj:  
##    file_content=file_obj.readline()
##    print(file_content)


"""Readline will read only one line per call. if you readd only half of the line in first call and in second call it will only read remaining half of the line"""
##with open("writingFile.txt","r") as file_obj:
##    file_content=file_obj.readline(2)
##    print(file_content)
##    file_content2=file_obj.readline()
##    print(file_content2)



##with open("writingFile.txt","r") as file_obj:
##    file_content=file_obj.readlines()
##    print(file_content)



##import tkinter
##from tkinter import filedialog
##file=filedialog.askopenfilename()
##with  open(file,"r") as file_obj:
##    filecontent=file_obj.readlines()
##    print(filecontent)



##with open("writingFile.txt","w+") as file_obj:
##    file_obj.write("\n")
##    file_obj.write("Today i am going to Chennai")
##    file_content=file_obj.read()
##    print(file_content)



##with open("writingFile.txt","a+") as file_obj:
##    file_obj.write("\n")
##    file_obj.write("Today i am going to Chennai")
##    file_obj.seek(0)   #seek is  to move the  cursor to the first place
##    file_content=file_obj.read()
##    print(file_content)



##with open("writingFile.txt","r+") as file_obj:
##    file_content=file_obj.read()
##    print(file_content)
##    file_obj.write("\n")
##    file_obj.write("Today i am going to Madurai")


##with open("attendance.txt","a") as file_obj:
####    we should store DataTime while storing daily attendance for that see below example.
##    file_obj.write("")
##    content=input("Number of students present")
##    file_obj.write(content)




"""Time Format"""
##from datetime import datetime
##
##current_time=datetime.now()
##print(current_time)
##print(type(current_time))
##
##
##trunc_current_time=current_time.replace(microsecond=0)
##print(trunc_current_time)
##print(type(trunc_current_time))
##
##
###existing_time=2022-02-04 11:01:42.080392
##time_Format="%Y_%B_%d_%H_%M_%S"
##
##modified_time=datetime.strftime(trunc_current_time,time_Format)
##print(modified_time)
##print(type(modified_time))


##import csv
##with open("writingFile.csv","w") as file_obj:
##    csv_file_obj=csv.writer(file_obj)
##    csv_file_obj.writerow(["name","age"])
##    csv_file_obj.writerows([["dhoni","33"],["kholi","22"]])


##with open("writingFile.csv","w",newline="") as file_obj:
##    csv_file_obj=csv.writer(file_obj)
##    csv_file_obj.writerow(["name","age"])
##    csv_file_obj.writerows([["dhoni","33"],["kholi","22"]])





##import pandas
##my_data=[["name","age"],["dhoni","35"],["kholi","29"]]
##my_csv_data=pandas.DataFrame(my_data)
##my_csv_data.to_csv('cnation.csv')



##import pandas
##my_data=[["name","age"],["dhoni","35"],["kholi","29"]]
##my_csv_data=pandas.DataFrame(my_data)
##my_csv_data.to_csv('cnation.csv',index=None)



# writing csv file with dict values
# import csv
#
# my_input_dict = [{"name": "dhoni", "age": 33}, {"name": "kholi", "age": 34}, {"name": "ashwin", "age": 35}]
# my_input_header = ["name", "age"]
# with open("dictCNation.csv", "w", newline="") as file_obj:
#     csv_file_obj = csv.DictWriter(file_obj, fieldnames=my_input_header)
#     csv_file_obj.writeheader()
#     csv_file_obj.writerows(my_input_dict)


# In Previous example we have used pandas with In this example we will use pandas with dictionary


# import pandas
# my_data = {"name": ["Dhoni", "Kholi"], "age": [33, 34]}
# my_csv_data = pandas.DataFrame(my_data)
# my_csv_data.to_csv("DictionaryCnation.csv", index=None)

# Reading csv File
# import csv
#
# with open("dictCNation.csv", "r") as csvfile:
#     csv_file_obj = csv.reader(csvfile)
#     csv_header = next(csv_file_obj)
#     print(csv_header)
#     print(csv_file_obj)
#     for rows in csv_file_obj:
#         print(rows)


# Reading csv file using pandas
# import pandas
#
# output = pandas.read_csv('DictionaryCnation.csv')
# print(output)

