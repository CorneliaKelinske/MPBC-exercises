from csv import DictReader

def print_user():
     with open('users.csv') as file:
          csv_reader = DictReader(file)
          
          for row in csv_reader:
               print(f"{row['First Name']} {row['Last Name']}")
               
print_user()