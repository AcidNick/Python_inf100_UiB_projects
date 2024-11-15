from pathlib import Path
import json
import csv

def convert_students_to_csv(students, csv_file):
    json_string = Path(students).read_text(encoding='utf-8')
    data = json.loads(json_string)
    csv_content = [list(data['students'][0].keys())]
    csv_content += [list(student.values()) for student in data['students']]
    write_csv_file(csv_file, csv_content, delimiter=";", quotechar="'")


def write_csv_file(path, table_content, encoding='utf-8', **kwargs):
    r""" Given a file path and a 2D list representing the content, this
    method will create a csv file with the contents formatted as csv.
    By defualt the delimiter is a comma and the quote character is
    the double quote, but this can be overridden with named parameters
     "delimiter" and "quotechar". """
    with open(path, "wt", encoding=encoding, newline='') as f:
        writer = csv.writer(f, **kwargs)
        for row in table_content:
            writer.writerow(row)

if __name__ == "__main__":
    convert_students_to_csv("students.json", "students.csv")
    convert_students_to_csv("students2.json", "students2.csv")
