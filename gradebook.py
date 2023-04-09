#!/bin/python3

# 1. Create a list called subjects

subjects = ["physics", "calculus", "poetry", "history"]

# 2. Create a list called grades

grades = [98, 97, 85, 88]

# 3. Manually create a two-dimensional list to combine subjects and grades

gradebook = [["physics", 98], ["calculus", 97], ["poetry", 85], ["history", 88]]

# 4. Print gradebook

print(gradebook)

# 5. Use the .append() method to add a list with the values of "computer science" and an associated grade value of 100 to our two-dimensional list of gradebook

gradebook.append(["computer science", 100])

# 6. Use append to add ["visual arts", 93] to gradebook

gradebook.append(["visual arts", 93])

# 7. Access the index of the grade for your visual arts class and modify it to be 5 points greater

gradebook[4][1] += 5

# 8. Find the grade value in your gradebook for your poetry class and use the .remove() method to delete it

poetry_grade = grades[2]

grades.remove(poetry_grade)

# 9. Use the .append() method to then add a new "Pass" value to the sublist where your poetry class is located

gradebook[2].append("Pass")

# 10. Create a new variable full_gradebook that combines both last_semester_gradebook and gradebook using + to have one complete grade book

last_semester_gradebook = [["Biology", 90], ["History", 80]]

full_gradebook = last_semester_gradebook + gradebook

# Print full_gradebook

print(full_gradebook)
