age = int(input("Enter your age: "))
if age%2 == 0:
    print("Your age is an even number.")
if age < 0:
    print("Invalid age! Age cannot be negative.")
elif age < 18:
    print("You are a minor.")
if age >= 18 and age <= 85:
    print("You are an adult.")
elif age <= 85:
    print("You are a senior citizen.")

print("Thank you for using the age classifier!")    