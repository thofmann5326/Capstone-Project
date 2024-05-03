student_count = 1000
rating = 4.99
is_published = True
course = "   Python \"Programming"
message = """
Hi john
"""

#print(len(course))
#print(course[0])
#print(course[-1])
#print(course[0:3])
#print(course[:3])
#print(course[:])
#print(student_count)


# comment
# \" prints ""
# \' prints '
# \\ prints \
# \n new line

first = "Trevor"
last = "Hofmann"
full = f"{len(first)} {last}"
#print(full)

print(course.upper())
print(course.lower())
print(course.title())
print(course.strip())
print(course.find("Pro")) #returns index
print(course.replace("P", "j"))
print("pro" in course) #returns true or false
print("swift" not in course)

x = 10
x = x + 3
x += 3
