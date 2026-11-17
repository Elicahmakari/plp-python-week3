# Week 3 Assignment: Grade Reporter

# List of learner scores
scores = [72, 45, 90, 61, 38]

# Initialize counters and total
passed = 0
failed = 0
total = 0

# Loop through each score
for score in scores:

    # Determine the grade
    if score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 50:
        grade = "C"
    else:
        grade = "F"

    # Print the score and grade
    print(f"Score: {score}, Grade: {grade}")

    # Count passes and failures
    if score >= 50:
        passed += 1
    else:
        failed += 1

    # Calculate total scores
    total += score

# Calculate average
average = total / len(scores)

# Display results
print("\n----- CLASS SUMMARY -----")
print(f"Number of learners passed: {passed}")
print(f"Number of learners failed: {failed}")
print(f"Average score: {round(average, 1)}")
