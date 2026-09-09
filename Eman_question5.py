# Question 5: Type Conversion Explanation
# What does the following python code do?

age = 20
item = 5
print("age : ", age)
print("items: ", item)

# Type Conversion (Type Casting from integer to float)
age = float(age)
item = float(item)
print("age : ",age)
print("item : ", item)

"""
Explanation:
1. Initially, 'age' and 'item' are defined as integers (int) with values 20 and 5.
   The first two print statements output:
   age : 20
   item : 5
2. Next, explicit type casting is performed using the float() function.
  - float(age) converts integer 20 to 20.0
  - float(item) converts integer 5 to 5.0

3. The last two print statements output the floating-point values:
   age : 20.0
   item : 5.0


Conclusion:
This program demonstrates explicit type conversion (type casting) from integer (int) to floating-point (float) numbers.
"""