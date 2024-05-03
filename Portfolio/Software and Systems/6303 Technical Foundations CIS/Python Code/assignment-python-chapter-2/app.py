# chapter 2.1 and 2.2 variables
import math
student_count = 1000
rating = 4.99
is_published = True
course_name = "Python Programming"
print(student_count)
print(rating, is_published, course_name)
print("." * 10)

# chapter 2.3 strings
course = "Python Programming"
print(len(course))
print(course[0])
print(course[-1])
print(course[0:3])
print(course[0:])
print(course[:3])
print(course[:])
print("." * 10)

# chapter 2.4 Escaping Sequences
# \"
course = "Python \"programming"
print(course)
# \'
course = "Python \'programming"
print(course)
# \\
course = "Python \\programming"
print(course)
print("." * 10)

# chapter 2.5 Formatted Strings
first = "Sean"
last = "Humpherys"
full = f"{len(first)} {2 + 2}"
print(full)
print("." * 10)

# Chapter 2.6 String Methods
print("Chapter 2.6 String Methods")
course = "  python programming"
print(course.upper())
print(course.lower())
print(course.title())
print(course.rstrip())
print(course.find("pro"))
print(course.replace("p", "j"))
print("pro" in course)
print("swift" not in course)
print("." * 10)

# Chapter 2.7 Bymbers"
print("Chapter 2.7 Bymbers")
x = 1  # integer
x = 1.1  # float with decimals
print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)
print(10 // 3)
print(10 % 3)  # modulous or mod
print(10 ** 3)  # exponent

x = 10
x = x + 3
print(x)
x = 10
x += 3  # augmented operator add
print(x)

y = 20
y -= 3  # argumented operator subtract
print(y)

z = 30
z *= 3  # augmented operator multiply
print(z)


# Chapter 2.8 Working with Numbers
print("Chapter 2.8 Working with Numbers")

print(round(2.9))
print(abs(-2.0))
print(math.ceil(2.2))
print("." * 10)


# Chapter 2.9 Type Converstion
x = input("Enter a value for x: ")
y = int(x) + 1
print(f"x: {x}, y: {y}")
print("." * 10)

rate = input("Enter interst rate,e.g. 0.5: ")
rate = float(rate)  # may resuse the  same varible
# Critical Knowledge
# three different ways to output a number variable with text
print(f"Borrow does not qualify at {rate}")  # string interpolation
print("Borrow does not qualify at ", rate)
print("Borrow does not qualify at ", str(rate))  # convert to string
print()
# Dr. Humphery's likes string interpolation the best!

# Displaying decimals in Strings

grams = 15.125
print(f"Weight is{grams}")  # no formatting
print(f"Weight is{grams:.2f}")  # two decimals, f means float
print(f"Weight is{grams:.4f}")  # Four decimals
print(f"Weight is{grams:.0f}")  # zero decimals

# Task G
card_number = "xxx8974"
date = "9\\7\\2020"
cookies_cost = 3.15
chips_cost = 4.58
salsa_cost = 5.10
total_cost = cookies_cost + chips_cost + salsa_cost

print("." * 15)
print("Receipt")
print(f"Date: {date}")
print(f"Cookies: $ {cookies_cost:.2f}")
print(f"Chips: $ {chips_cost:.2f}")
print(f"Salsa: $ {salsa_cost:.2f}")
print(f"Total: $ {total_cost:.2f}")
print("." * 15)
