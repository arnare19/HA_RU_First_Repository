n = int(input("Enter the length of the sequence: ")) # Do not change this line
# Vantar algoríma sem að prentar n margar tölur í röð þar sem að frá 0 hverjar þrjár tölur jafngilda fjórðu tölunni, þ.e. 0,1,2,3,6,11,20,37,...
# Ef talan er orðin sú smæsta á bætast við hinar tvær
n -= 1
n1 = 1
n2 = 2
n3 = 3
print(n1)
print(n2)
for i in range(1, n):
    if n1 > n2 and n1 > n3:
        print(n1)
    elif n2 > n1 and n2 > n3:
        print(n2)
    elif n3 > n1 and n3 > n2:
        print(n3)
    if n1 < n3:
        n1 = n1 + n2 + n3
    elif n2 < n1:
        n2 = n1 + n2 + n3
    elif n3 < n2:
        n3 = n1 + n2 + n3