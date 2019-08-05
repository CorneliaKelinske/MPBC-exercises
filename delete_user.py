#should be the same as update user. I write identical row in case of no match and I just update the count if there is a match
import csv

def delete_users(first, last):
    with open("users.csv") as file:

        csv_reader = csv.reader(file)
        users = list(csv_reader)

        count = 0

        with open("users.csv", "w") as file:

            csv_writer = csv.writer(file)
            for row in users:
                if row[0] == first and row[1] == last:
                    count += 1
                else:
                    csv_writer.writerow(row)
    return f"Users deleted: {count}."

print(delete_users("Colt", "Steele"))