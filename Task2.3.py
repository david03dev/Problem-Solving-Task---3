"""Given a python list [10,501,22,37,100,999,87,351] 
Find out how many numbers are there in the given python list which are happy numbers?"""


given_list = [10,501,22,37,100,999,87,351]

print("Given list is : ", given_list,"\n")
sum_sq_digits = 0
happy = []
unhappy = []

for i in given_list:
    number = i
    # convert number to list of integers and find sum of square of each digit
    while(sum_sq_digits != 1 and sum_sq_digits != 4):
        sum_sq_digits = sum([pow(int(x),2) for x in str(number)])
        #print(sum_sq_digits)
        number = sum_sq_digits

    #indentify happy and unhappy numbers and prepare list
    if sum_sq_digits == 1:
        print(i, " is a happy number")
        happy.append(i)
    else:
        print(i, " is a unhappy number")
        unhappy.append(i)
    sum_sq_digits = 0

#print the results
print("\n")
print("Number of Happy numbers from given list is ",len(happy))
print("Number of Unhappy numbers from given list is ",len(unhappy))
    
