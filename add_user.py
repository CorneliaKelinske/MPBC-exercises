from csv import writer, DictWriter

def add_user(first, last):
    with open('users.csv', 'a') as file:
        csv_writer = writer(file)
        csv_writer.writerow([first, last])

add_user("John", "Smith")