def get_user_input(prompt, default=None):
    response = input(prompt)
    return int(response) if response.strip() else default

def try_int(value):
    try:
        return int(value)
    except ValueError:
        return value

with open("file.csv", "r") as f:
    # Skip the header row
    header = next(f)
    num_columns = len(header.strip().split(","))

    # Ask the user which column to analyze
    column_to_analyze = get_user_input(f"Enter the column number to analyze (1-{num_columns}): ") - 1

    # Create a list to hold the values in the specified column
    column_values = []

    # Loop through the lines and add the specified column value to the list
    for line in f:
        values = line.strip().split(",")
        column_values.append(try_int(values[column_to_analyze]))


    # Ask the user for how many of the largest values to print, defaulting to 50 if no value is given
    num_largest_values = get_user_input("Enter the number of largest values to print (default 50): ", default=50)

    # Sort the values in descending order and print out the largest values specified by the user
    values = sorted(column_values, key=lambda x: (isinstance(x, int), x), reverse=True)[:num_largest_values]
    for value in values:
        print(value)

    # Print the total amount of lines in the file
    print("Total number of values:", len(column_values))
