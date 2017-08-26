def centuryFromYear(year):

	year =  year - 1

	century = (year //100) + 1
	

	return century


print(centuryFromYear(1701))

