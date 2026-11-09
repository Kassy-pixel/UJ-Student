
#UNIT 1

# STUDENT INFO FORMATTER
first_name = input(" Please enter your first name:")
surname = input(" Please enter your surname:")
age = int(input(" Please enter your age:"))
favorite_number = float(input("Please enter your favorite number:"))

# Display user details
full_name = first_name + " " + surname

print(f"{full_name.upper()}")

age_months = age * 12
print(f"You are {age}years old.")
rounded_number = round(favorite_number, 2)
print(f"Rounded favorite number: {rounded_number}")

#----------------------------------------------------

# Task two: Digital ticket holder.

artist = input("Enter the name of the artist you booked:")
print(f"Hey {full_name}! Your ticket to see {artist} is booked successfully.")

#---------------------------------------------------------------------------------------------

#UNIT 2

#TASK 1:USSERNAME AND MESSAGE FORMATTer

message = input( "     I am a VIP ticket holder.     ")
print(message.strip())
print(f"first_name[0]lower() + surname.lower"())
print(f"first_name.title() + surname.title()")
print(len.message())
print(f" i am.replace" "i'am")
