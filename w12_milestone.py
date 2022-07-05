life = []
years = []
country = []
codes = []
output = []
highest_value = None
lowest_value = None
higher_life = None
lower_life = None
total = 0
average = 0
keep_researching = "yes"
input_year = ""

while keep_researching.lower() == "yes" :
    
    input_year = int(input("Enter the year of interest: ")
)
    with open("life-expectancy.csv") as life_data :
        next(life_data)

        for line in life_data: 
            clean_line = line.strip()
            each_line = clean_line.split(",")
            entity = each_line[0]
            code = each_line[1]
            year = int(each_line[2])
            life_expectancy = float(each_line[3])

            if life_expectancy != "Life expectancy (years)":
                life.append(life_expectancy)
                years.append(year)
                country.append(entity)
                codes.append(code)
                highest_value = max(life)
                lowest_value = min(life)

                if life_expectancy == highest_value :
                    highest_country = entity
                    highest_year = year
                elif life_expectancy == lowest_value :
                    lowest_country = entity
                    lowest_year = year

            if year != "Year" :
                if input_year == year :
                    output.append(life_expectancy)
                    higher_life = max(output)
                    lower_life = min(output)
                    total = sum(output)
                    average = total / len(output)   
                if life_expectancy == higher_life :
                    higher_country = entity
                elif life_expectancy == lower_life:
                    lower_country = entity

                

        print(f"\nThe overall max life expectancy is: {highest_value} from {highest_country} in {highest_year}")
        print(f"\nThe overall min life expectancy is: {lowest_value} from {lowest_country} in {lowest_year} ")
        print(f"\nFor the year {input_year}: ")
        print(f"\nThe average life expectancy across all countries was {average:.2f}")
        print(f"The max life expectancy was in {higher_country} with {higher_life}")
        print(f"The min life expectancy was in {lower_country} with {lower_life}")
        print()
        keep_researching = input("\nWould you like to make a new search (yes/no)? ")

print("\nIt was nice having you with us! Come back at any time!")