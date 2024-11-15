import csv
from pathlib import Path


# Kopier gjerne funksjonene csv_dict_reader og csv_dict_writer herfra

def csv_dict_reader(path, encoding='utf-8', delimiter=',',
                    quotechar='"', quoting=csv.QUOTE_MINIMAL, **kwargs):
    '''Read a CSV file and return the headers as a list and the data as
    a list of dictionaries. Typical usage example:

        >>> headers, data = csv_dict_reader('foo.csv', delimiter=';')
        >>> headers
        ['Name', 'Age']
        >>> data
        [{'Name': 'Ola', 'Age': '74'}, {'Name': 'Kari', 'Age': '73'}]

    Args:
        path (str): The path to the CSV file.
        encoding (str, optional): The encoding of the CSV file. Default
            is 'utf-8'.
        delimiter (str, optional): The delimiter between cells used in
            the CSV file. Default is ','.
        quotechar (str, optional): The quote character used in the CSV
            file. Default is '"'.
        quoting (int, optional): The quoting style used in the CSV
            file. Default is csv.QUOTE_MINIMAL. Some other useful
            options are csv.QUOTE_ALL and csv.QUOTE_NONNUMERIC. See
            https://docs.python.org/3/library/csv.html#csv.QUOTE_ALL
            for more information.
        **kwargs: Additional keyword args to pass to csv.DictReader.

    Returns:
        headers (list): The headers of the CSV file.
        data (list): The data of the CSV file as a list of dictionaries.
    '''
    with Path(path).open('rt', encoding=encoding, newline='') as f:
        reader = csv.DictReader(f, delimiter=delimiter, quotechar=quotechar,
                                quoting=quoting, **kwargs)
        headers = reader.fieldnames
        data = list(reader)
    return headers, data


def csv_dict_writer(path, headers, data, encoding='utf-8', delimiter=',',
                    quotechar='"', quoting=csv.QUOTE_MINIMAL, **kwargs):
    '''Write a CSV file with the specified headers and data. Typical
    usage example:

        >>> headers = ['Name', 'Age']
        >>> data = [
        ...     {'Name': 'Ola', 'Age': 74},
        ...     {'Name': 'Kari', 'Age': 73},
        ... ]
        >>> csv_dict_writer('foo.csv', headers, data, delimiter=';')

    Args:
        path (str): The path to the CSV file.
        headers (list): The headers of the CSV file.
        data (list): The data of the CSV file as a list of dictionaries.
        encoding (str, optional): The encoding of the CSV file. Default
            is 'utf-8'.
        delimiter (str, optional): The delimiter between cells used in
            the CSV file. Default is ','.
        quotechar (str, optional): The quote character used in the CSV
            file. Default is '"'.
        quoting (int, optional): The quoting style used in the CSV
            file. Default is csv.QUOTE_MINIMAL. Some other useful
            options are csv.QUOTE_ALL and csv.QUOTE_NONNUMERIC. See
            https://docs.python.org/3/library/csv.html#csv.QUOTE_ALL
            for more information.
        **kwargs: Additional keyword args to pass to csv.DictWriter.

    Returns:
        None
    '''
    with Path(path).open('wt', encoding=encoding, newline='') as f:
        writer = csv.DictWriter(f, fieldnames=headers, delimiter=delimiter,
                                quotechar=quotechar, quoting=quoting)
        writer.writeheader()
        writer.writerows(data)