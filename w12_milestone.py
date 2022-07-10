
new_search = "yes"
year_of_interest = ""
countries = []
codes = []
years = []
life_expectancies = []
highest_life_expectancy = 0
lowest_life_expectancy = 0
highest_country = ""
highest_year = 0
lowest_country = ""
lowest_year = 0
highest_life = 0
lowest_life = 0
output = []

while new_search.lower() == "yes" :
    year_of_interest = int(input("Enter the year of interest: ")) 

    with open("life-expectancy.csv") as life_data :
        next(life_data)

        for line in life_data :

            clean_line = line.strip()
            parts = clean_line.split(",")

            entity = parts[0]
            code = parts[1]
            year = int(parts[2])
            life_expectancy = float(parts[3])

            if life_expectancy != "Life expectancy (years)" :
                countries.append(entity)
                codes.append(code)
                years.append(year)
                life_expectancies.append(life_expectancy)
                highest_life_expectancy = max(life_expectancies)
                lowest_life_expectancy = min(life_expectancies)

                if life_expectancy == highest_life_expectancy :
                    highest_country = entity
                    highest_year = year
                elif life_expectancy == lowest_life_expectancy :
                    lowest_country = entity
                    lowest_year = year

            if year != "Year" :
                if year_of_interest == year :
                    output.append(life_expectancy)
                if life_expectancy == highest_life :
                    highest_country = entity
                elif life_expectancy == lowest_life :
                    lowest_country = entity

        highest_life = max(output)
        lowest_life = min(output)
        total = sum(output)
        average = total / len(output) 

        print(f"\nThe overall max life expectancy is: {highest_life_expectancy} from {highest_country} in {highest_year}")
        print(f"The overall min life expectancy is: {lowest_life_expectancy} from {lowest_country} in {lowest_year} ")
        print(f"\nFor the year {year_of_interest}: ")
        print(f"\nThe average life expectancy across all countries was {average:.2f}")
        print(f"The max life expectancy was in {highest_country} with {highest_life}")
        print(f"The min life expectancy was in {lowest_country} with {lowest_life}")
        print()

        new_search = input("\nWould you like to make a new search (yes/no)? ")

print("\nIt was nice having you with us! Come back at any time!")


            



