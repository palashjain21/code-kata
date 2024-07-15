How to Run
- Build the Docker Image:
>> sh
- Copy code
>> docker build -t fixed-width-parser .
- Run the Docker Container:
sh
- Copy code
>> docker run --rm fixed-width-parser
Testing Strategies
1. Unit Tests: Create unit tests for each function (read_spec_file, parse_fixed_width_file, write_to_csv).
2. Edge Cases: Test with different lengths of fields, special characters, and empty fields.
3. Integration Tests: Ensure the whole process from reading the spec file to writing the CSV works seamlessly.