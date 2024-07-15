import csv

def read_spec_file(spec_file):
    with open(spec_file, 'r') as file:
        spec = file.readlines()
    spec = [line.strip().split(':') for line in spec]
    return [(field[0], int(field[1])) for field in spec]

def parse_fixed_width_file(fixed_width_file, spec):
    parsed_data = []
    with open(fixed_width_file, 'r') as file:
        for line in file:
            record = []
            position = 0
            for field_name, field_length in spec:
                record.append(line[position:position + field_length].strip())
                position += field_length
            parsed_data.append(record)
    return parsed_data

def write_to_csv(parsed_data, csv_file, spec):
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        headers = [field[0] for field in spec]
        writer.writerow(headers)
        writer.writerows(parsed_data)

def main():
    spec_file = 'spec.txt'
    fixed_width_file = 'fixed_width_file.txt'
    csv_file = 'output.csv'

    spec = read_spec_file(spec_file)
    parsed_data = parse_fixed_width_file(fixed_width_file, spec)
    write_to_csv(parsed_data, csv_file, spec)

if __name__ == "__main__":
    main()
