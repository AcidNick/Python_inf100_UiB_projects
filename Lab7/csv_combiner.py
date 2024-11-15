import csv
import os

def combine_csv_in_dir(dirpath: str, result_path: str):
    result_table = [["uibid", "karakter", "kommentar"]]
    for dirpath, dirnames, filenames in os.walk(dirpath):
        for filename in filenames:
            if filename.endswith(".csv"):
                data = read_csv_file(os.path.join(dirpath, filename))
                merge_table_into(result_table, data)
    write_csv_file(result_path, result_table)

def merge_table_into(master_table: list, new_table: list):
    for i in range(1, len(new_table)):
        master_table.append(new_table[i])


def read_csv_file(path, encoding="utf-8", **kwargs):
    r""" Reads a csv file from the provided path, and returns its
    content as a 2D list. The default encoding is utf-8, the default
    column delimitier is comma and the default quote character is the
    double quote character ("), though this can be overridden with
    named parameters "delimiter" and "quotechar"."""
    with open(path, "rt", encoding=encoding, newline='') as f:
        return list(csv.reader(f, **kwargs))

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



def test_combine_csv_in_dir():
    print("Tester combine_csv_in_dir... ", end="")
    # Mappen samples må ligge i samme mappe som denne filen
    dirpath = os.path.join(os.path.dirname(__file__), "samples")
    combine_csv_in_dir(dirpath, "combined_table.csv")
    with open("combined_table.csv", "rt", encoding='utf-8') as f:
        content = f.read()
        assert ("""\
    uibid,karakter,kommentar
    abc104,C,hei
    abc105,D,"med komma, her er jeg"
    abc106,E,tittit
    abc101,A,Her er min kommentar
    abc102,B,"Jeg er glad, men her er komma"
    abc103,C,Katching
    """ == content or """\
    uibid,karakter,kommentar
    abc101,A,Her er min kommentar
    abc102,B,"Jeg er glad, men her er komma"
    abc103,C,Katching
    abc104,C,hei
    abc105,D,"med komma, her er jeg"
    abc106,E,tittit
    """ == content)
    print("OK")

if __name__ == "__main__":
    test_combine_csv_in_dir()