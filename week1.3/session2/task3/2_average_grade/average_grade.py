# Week 1.3, Session 2: Calculate Average Grade and Write to a File

# Open 'student_data.csv' to read each student's grades
# hint: skip the header row with data[1:]
try:
    with open("student_data.csv", "r") as f:
        lines = f.readlines()

    with open("report.txt", "w") as final_file:
        for line in lines[1:]:
            line = line.strip()
            parts = line.split(",")
            ID= parts[0]
            Name = parts[1]
            Mathematics = int(parts[2])
            Science = int(parts[3])
            History = int(parts[4])

            average = (Mathematics + Science + History) / 3

            final_file.write(f"ID:{ID} {Name} average grade: {average:.2f}\n")

except ValueError:
    print("Value error")
            


# Read each student's grades and calculate their average grade
# hint: CSV data comes as strings, convert grade columns to int() for maths
# hint: student_data.csv has columns: ID, Name, Mathematics, Science, History
# hint: average = (maths + science + history) / 3


# Open a file called 'report.txt'
# Write each student's name and their average grade to the report
# hint: use 'w' mode to create a fresh report each time
# hint: format averages nicely, maybe to 2 decimal places with :.2f
