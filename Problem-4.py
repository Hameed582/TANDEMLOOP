input_str = input("Enter numbers separated by commas: ")

input_list = [int(x.strip()) for x in input_str.split(",")]

multiples_count = {}

for i in range(1, 10):
    count = 0
    for num in input_list:
        if num % i == 0:
            count += 1
    multiples_count[i] = count

print(multiples_count)
