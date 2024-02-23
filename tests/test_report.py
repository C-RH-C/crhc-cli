"""
.. code-block:: text

    Test to check the Inventory Report
"""
import json
import csv
import tempfile
from pathlib import Path
from crhc_cli.report import report


INPUT_JSON = "tests/data/inventory.json"

p = Path(tempfile.gettempdir())
OUTPUT_CSV = (p / "inventory_report.csv").resolve()


def calling_csv_report_inventory():
    """
    Function responsible to read the template data and push against the
    function.
    """

    # Reading the Input data that will be used in this test
    with open(INPUT_JSON, "r") as file_obj:
        aux = json.load(file_obj)
        number_of_entries = len(aux['results'])
        report.csv_report_inventory(aux)
        return number_of_entries


def test_csv_report_inventory_counting_number_of_columns():
    """
    Testing the csv_report_inventory feature.
    Here we are passing the input file, generating the output and
    counting the # of fields of each row
    """

    calling_csv_report_inventory()

    #  Counting 41 fields from Inventory Report
    with open(OUTPUT_CSV, "r") as file_obj:
        aux = csv.reader(file_obj)
        for line in aux:
            print(line)
            assert len(line) == 41


def test_csv_report_inventory_counting_number_of_rows():
    """
    Testing the # of rows, which should be the # of elements in the
    sample + 1 of header
    """
    number_of_entries = calling_csv_report_inventory()

    # Counting 3 rows, header + 2 lines from the input data
    with open(OUTPUT_CSV, "r") as file_obj:
        aux = file_obj.readlines()
        assert len(aux) == number_of_entries + 1
