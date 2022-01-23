# Comet Halley is visible to the naked eye from Earth every 76 years. Its last appearance was in 1986. Given any year after 1986 as input, can you 
# compute the next time Halley will be seen again? If Halley is visible in the given year, please provide the next one.
# 1. The program takes a given year as input. It computes the next appearance year and prints the obtained value.
# 2. The program cannot use loops (for, while, do/while) to accomplish the described task.
# 3. Input validation: the program validates the input year. If the value is smaller than or equal to 1986, the program continously asks the user 
#   to re-enter the input.

while True:
	try:
		year = int(input("Enter year: "))
		if year > 1986:
			break
		else:
			print("Enter a year after 1986! Try again...")
	except:
		print("Invalid input! Try again...")



years_passed = (year - 1986)%76
years_to_pass = 76 - years_passed
next_appearance = years_to_pass + year

print(f"Next appearance: {next_appearance}")


