#Write a python program to find the sum of the first and last digits of an integer?

#get input from user
inpnt_number = int(input("Enter the integer number: "))

# convert number to list of integers
num_list = [int(x) for x in str(inpnt_number)]
#add first and last numbers of list
result = num_list[0] + num_list[len(num_list)-1]
#print the result
print(result)