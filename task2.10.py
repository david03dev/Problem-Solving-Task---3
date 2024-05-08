#Given a list [4,2,-3,1,6] write a python program to find if there is a sub-list with sum equal to zero?

given_list = [4,2,-3,1,6]

result_list = []
result = ""

print("Given list is : ", given_list)

for i in range(len(given_list)):
        if result == "done":
             break
        result_list = []
        result = given_list[i]
        result_list.append(given_list[i])

        for j in range(i + 1, len(given_list)):
            result += given_list[j]
            result_list.append(given_list[j])
            
            if result == 0:
                print("The sub-list with sum equal to zero is ",result_list)
                result = "done"
                break

if result != "done":
     print("There is no sub-list with sum equal to zero")