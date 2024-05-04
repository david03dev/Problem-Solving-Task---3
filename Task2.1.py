"""You have been given a python list [10,501,22,37,100,999,87,351] Your task is to create two list 
one which have all the EVEN numbers and another list which will have all ODD numbers in it?"""


given_list = [10,501,22,37,100,999,87,351]
#create empty lists for odd and even numbers
even_list = []
odd_list = []

#identify the odd and even numbers and append the respective lists
for i in given_list:
    if i % 2 == 0:
        even_list.append(i)
    else:
        odd_list.append(i)

#print the results
print("The given list is : ", given_list)
print("Odd number list is : ",odd_list)
print("Even number list is : ",even_list)