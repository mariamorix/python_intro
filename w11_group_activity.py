
with open("hr_system.txt") as rh_system:
    for line in rh_system :
        clean_line = line.strip()
        each_line = clean_line.split()
        name = each_line[0]
        id = each_line[1]
        job_title = each_line[2]
        salary = each_line[3]
        amount = float(salary) / 24

        if job_title.lower() == "engineer" :
            amount = amount + 1000

        print(f"Name: {name} (ID: {id}), Job Title: {job_title} - ${amount:.2f}")
