# Week 1.5, Session 2: Task 5

# Write a program here to create a Dataset containing data
# from a file named by the user

# Your program should display dataset size, mean and median,
# followed by the individual values (using a for loop)

import statistics

class Dataset:
    def __init__(self, filename):
        self.values = []
        with open(filename, "r") as f:
            for lines in f:
                num = float(lines.strip())

                self.values.append(num)

    def size(self):
        return len(self.values)

    def mean(self):
        return statistics.mean(self.values)

    def median(self):
        return statistics.median(self.values)
    
try:
    filename = input("Enter the filename: ")
    ds = Dataset(filename)

    print("Dataset size:", ds.size())
    print("Mean:", ds.mean())
    print("Median:", ds.median())

    for v in ds.values:
        print(v)
except ValueError:
    print("Value error")