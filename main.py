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






# now let's check the selection
total_charge = 0
if selection == 1:
	total_charge = total_calc(months_rented,60, 45, 450)
elif selection == 2:
	total_charge = total_calc(months_rented, 45, 30, 280)
elif selection == 3:
	total_charge = total_calc(months_rented, 55, 38, 350)
elif selection == 4:
	total_charge = total_calc(months_rented, 28, 25, 200)
else:
	total_charge = total_calc(months_rented, 35, 20, 220)

print(f"\nAmount due ($): {total_charge}")

