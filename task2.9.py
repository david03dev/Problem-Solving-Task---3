#You have been given a python list [10,20,30,9] and a value of 59. 
#Write a python program to find the triplet in the list whose sum is equal to the given value?

given_list = [10,20,30,9]
length = len(given_list)
triplet_list = []

#
for i in range(0, length -2):
    
    for j in range(i+1, length-1):
        
        for k in range(j+1, length):
            
            if (given_list[i] + given_list[j] + given_list[k] == 59):  
                triplet_list.append([given_list[i], given_list[j], given_list[k]])

print("Given list is : ",given_list)
print("The triplet which equal to 59 is : ",triplet_list)