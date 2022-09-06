n = int(input("Enter N value: "))

i = 0
for i in range(n):
    if i == 0 or i == n-1:
        print("*"*n)
    else:
        print("*"+(n-2)*" "+"*")

