import csv
import faker

def generate_csv(file_name, num_records):
    fake = faker.Faker()
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["first_name", "last_name", "address", "date_of_birth"])
        for _ in range(num_records):
            writer.writerow([fake.first_name(), fake.last_name(), fake.address(), fake.date_of_birth()])

if __name__ == "__main__":
    generate_csv("data.csv", 1000)  # Generate a CSV with 1000 records
