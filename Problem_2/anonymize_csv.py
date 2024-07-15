import csv
import faker

def anonymize_csv(input_file, output_file):
    fake = faker.Faker()
    with open(input_file, mode='r') as infile, open(output_file, mode='w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        
        # Write header
        headers = next(reader)
        writer.writerow(headers)
        
        # Write anonymized data
        for row in reader:
            row[0] = fake.first_name()  # Anonymize first_name
            row[1] = fake.last_name()   # Anonymize last_name
            row[2] = fake.address()     # Anonymize address
            writer.writerow(row)

if __name__ == "__main__":
    anonymize_csv("data.csv", "anonymized_data.csv")
