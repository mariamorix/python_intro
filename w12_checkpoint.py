people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

youngest_age = 200
yougest_person = ""

for item in people :
    each = item.split()
    name = each[0]
    age = int(each[1])

    if age < youngest_age :
        youngest_age = age
        yougest_person = name

print(f"The youngest person is: {yougest_person} with an age of {youngest_age}")        