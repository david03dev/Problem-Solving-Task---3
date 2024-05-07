#You have been given three lists. Your task is to find the duplicates in three lists.
#write a program for the same. You can choose your own python lists?

#Initialize the lists
list_1 = [11,88,36,74,33]
list_2 = [99,11,33,35,22]
list_3 = [33,42,36,35,11]

result=[]

#Identify the duplicates
for i in list_1:
    if i in list_2 and i in list_3:
        result.append(i)
        
#Print the results
print("Given lists are : \n",list_1,"\n",list_2,"\n",list_3,"\n")
print("Duplicate elements from given lists are : ",result)