num = int(input("Enter a number between 1 and 255: "))

if(num <= 0 or num > 255):
    print("Out of range")

else:
    print(chr(num))
