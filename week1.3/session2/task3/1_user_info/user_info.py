# Week 1.3, Session 2: Write User Information to a File


# Prompt the user for their name, age, and favorite colour.

while True:
    name = input("Enter your name:")
    if name == "stop":
        break
    age = input("Enter your age:")
    colour = input("Enter your favourite colour:")

# Open a file called 'user_info.txt' for reading

with open("user_info.txt", "w") as f:
    f.write(name + "\n")
    f.write(age + "\n")
    f.write(colour + "\n")



# Write each piece of information to the file, each on a new line.

# Hints:
# - Remember to add \n for new lines when writing to files


# Optional: extend this by using a loop to allow multiple people to enter their info in a row
# If you want multiple people to add info without overwriting, consider append mode 'a'
