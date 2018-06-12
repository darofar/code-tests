import csv


def read_csv(
        file_path="/tmp/users.csv",
        cloak="*****",
        sensible=('id', 'name', 'surname', 'identification_number', 'address')):
    """
    Renders information from csv file obscuring personal data that could lead to
    identifying an user.
    :param file_path: (str) path to CSV file
    :param sensible: (set) collection of keys that appears in CSV file consider  sensible data.
    :param cloak: (str) string with which replace sensible user data.
    """
    with open(file_path, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        print(",".join(reader.fieldnames))
        for row in reader:
            print(",".join([row[key] if key not in sensible else cloak for key in reader.fieldnames]))


if "__main__" in __name__:
    read_csv()
