"""Given a python list [10,501,22,37,100,999,87,351] Your task is to count all the prime numbers and 
create a new python list which will contain all the prime numbers in it?"""

given_list = [10,501,22,37,100,999,87,351]

prime_list = []
non_prime_list = []

#identify prime and non-prime numbers and append the list
for number in given_list:
    for i in range(2,number+1):
        if i == number:
            #print(number,"is a prime")
            prime_list.append(number)
        elif number % i == 0:
            #print(number,"not a prime", i)
            non_prime_list.append(number)
            break

#print the results
print("Given list is : ",given_list)
print("Prime number list is: ", prime_list)
print("Non Prime number list is : ",non_prime_list)