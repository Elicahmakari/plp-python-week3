# Week 3 Assignment: Bug Hunt

count = 1
total = 0

# BUG 1: Added a colon (:) after the while condition
# because Python requires a colon to start a loop.
# BUG 2: Changed < 5 to <= 5 so the loop includes 5.
while count <= 5:

    total = total + count
    count = count + 1

# BUG 3: Converted total to a string using an f-string
# because Python cannot concatenate a string and an integer directly.
print(f"Sum of 1 to 5 is: {total}")
