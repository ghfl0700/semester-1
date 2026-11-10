# Week 1.3, Session 2: Print PGM image info

# Open a pgm image file

try:
    with open("feep.pgm", "r") as f:
        all_lines = f.readlines()

    clean_line = []
    for line in all_lines:
        text = line.strip()
        if text != "" and not text.startswith("#"):
            clean_line.append(text)

# You can use the relative path ../images/filename
# You could handle file errors with try/except.

    width, height = map(int, clean_line[1].split())
    max_gray = int(clean_line[2])

    print(f"Dimension: {width} * {height} pixels")
    print(f"Max Gray Value: {max_gray}")

except ValueError:
    print("Value error")

# Read the file content
# print image dimension (i.e., Dimensions: width x height pixels)
# print max gray value (i.e., Max Gray Value: max_gray_value)

    