num_int = int(input("Input a number: "))    # Do not change this line
max_int = 0
#Ef num_int er stærra en eða jafnt og 0 þá ef num_int er stærra en max_int fær max_int gildi num_int
# Fill in the missing code
while num_int >= 0:
    if max_int < num_int:
        max_int = num_int
    num_int = int(input("Input a number: "))    
print("The maximum is", max_int)    # Do not change this line