life = []
years = []
country = []
codes = []
highest_value = None
lowest_value = None
keep_researching = "yes"
input_year = ""

while keep_researching.lower() == "yes" :
    
    input_year = int(input("Enter the year of interest: "))

    with open("life-expectancy.csv") as life_data :
        for line in life_data: 
            clean_line = line.strip()
            each_line = clean_line.split(",")
            entity = each_line[0]
            code = each_line[1]
            year = each_line[2]
            life_expectancy = each_line[3]

            if life_expectancy != "Life expectancy (years)":
                life.append(life_expectancy)
                years.append(year)
                country.append(entity)
                codes.append(code)
                highest_value = max(life)
                lowest_value = min(life)

        print(f"The overall max life expectancy is: {highest_value} ")
        print(f"The overall min life expectancy is: {lowest_value} ")

    keep_researching = input("Would you like to make a new search (yes/no)? ")

print("\nIt was nice having you with us! Come back at any time!")