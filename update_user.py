import csv

def update_user(old_first, old_last, new_first, new_last):
    with open("users.csv") as file:

        csv_reader = csv.reader(file)
        users = list(csv_reader)

        count = 0

        with open("users.csv", "w") as file:

            csv_writer = csv.writer(file)
            for row in users:
                if row[0] == old_first and row[1] == old_last:
                    csv_writer.writerow([new_first, new_last])
                    count += 1
                else:
                    csv_writer.writerow(row)
    return f"Users updated: {count}."

print(update_user("Colt", "Steele", "John", "Smith"))     

