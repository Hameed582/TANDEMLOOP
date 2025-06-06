num = int(input("Enter the number : "))

if num%2==0:
    num -= 1

odd_lst = []

for i in range(num):
    odd_lst.append(2*i+1)

print(", ".join(map(str, odd_lst)))

