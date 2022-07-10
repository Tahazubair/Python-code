largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        nums = int(num)
    except:
        print("Invalid input")
        continue
    if largest is None or nums > largest:
        largest = nums
    elif smallest is None or smallest > nums:
        smallest = nums
    elif nums < smallest:
        smallest = nums


print("Maximum is", largest)
print("Minimum is", smallest)
