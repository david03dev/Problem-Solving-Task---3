#Write a python program to find the minimum element in a rated and sorted list?

length = int(input("Enter the length of the list: "))
print("Enter the elements of the list one by one")
given_list = []

#get input of a list from user
for i in range(length):
    num = int(input())
    given_list.append(num)

print("Given list is ", given_list)

#find the minimum element from given list
minimum = given_list[0]
for i in range(len(given_list)):
        if minimum > given_list[i]:
            minimum = given_list[i]
        

print("Minimum element in the given list is : ",minimum)