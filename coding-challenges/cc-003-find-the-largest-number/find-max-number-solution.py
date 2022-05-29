numbers=[]

for i in range(0,5):
    num=int(input("Please enter number: "))
    numbers.append(num)

def maximum(arr):
    max=arr[0]
    for num in arr:
        if num > max:
            max = num
    return max

print(maximum(numbers))


