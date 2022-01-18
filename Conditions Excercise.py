# prints the sentence "Yes - Spathiphyllum is the best plant ever!" to the screen if the inputted string is "Spathiphyllum" (upper-case)
# prints "No, I want a big Spathiphyllum!" if the inputted string is "spathiphyllum" (lower-case)
# prints "Spathiphyllum! Not [input]!" otherwise. Note: [input] is the string taken as input.

a = input()

if a == "Spathiphyllum":
    print(Yes)
elif a == "spathiphyllum":
    print("No, Want Big")
else:
    print("Not "+ a)
print(type(a))

# Excercise 2 - The Test Case Data for Tax 


# income = float(input("Enter the annual income: "))
# if (10000<= income <= 85528):
#     Tax = ((income*18)/100)-556.2
# elif (-100 <= income<=1000): #based on the test data i just entered these no.
#     Tax = 0.0
# else:
#     Tax =((income- 85528)*32)/100+14839.2
# Tax = round(Tax, 0)
# print("The tax is:", Tax, "thalers")