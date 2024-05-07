#Write a python program to find the first non-repeating elements in a given list of integers?


given_list = []
length = int(input("Enter the length of the list: "))
print("Enter the elements of an integer list one by one")

#get input list from user
for i in range(length):
    num = int(input())
    given_list.append(num)

print("Given list is : ",given_list)

#identify first non-repeating element
for num in given_list:
    result = 0
    for i in range(len(given_list)):
        if given_list[i] == num:
            result += 1
    #print the result
    if result == 1:
        print("The first non-repeating element from given list is : ",num)
        break
    