"""Write a program that prompts the user to enter a number. Check whether the number falls within any of the following ranges:
0-10: "Low Range"
11-50: "Medium Range"
51-100: "High Range"
Outside of 0-100: "Out of Range"
"""

num = input("Enter a number: ")
num=int(num)
if 0<= num and num <=10 :
    print ("Low Range")
elif 11<= num and num <=50 :
    print("Medium Range")
elif 51<= num and num <=100 :
    print("High Range")
else:
    print("Out of Range")
