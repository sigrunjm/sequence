#Take input from a user
#The input is the lenght of sequence
#print first 3 numbers
# 

n = int(input("Enter the length of the sequence: ")) # Do not change this line

first_int = 1
second_int = 2
third_int = 3
print(first_int)
print(second_int)
print(third_int)

summ_of_tree = 0
for i in range(3, n):
    next = first_int+second_int+third_int
    print(next)
    first_int = second_int
    second_int = third_int
    third_int = next
    
    

