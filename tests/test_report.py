from report import report
import json
import csv

INPUT_JSON = "tests/data/inventory.json"
OUTPUT_CSV = "/tmp/inventory_report.csv"

def calling_csv_report_inventory():

    # Reading the Input data that will be used in this test
    with open(INPUT_JSON, "r") as file_obj:
        aux = json.load(file_obj)
        report.csv_report_inventory(aux)
        pass

def test_csv_report_inventory():
    """
    Testing the csv_report_inventory feature.
    Here we are passing the input file, generating the output and
    counting the # of fields of each row
    """

    calling_csv_report_inventory()

    #  Counting 41 fields from Inventory Report
    with open (OUTPUT_CSV, "r") as file_obj:
        aux = csv.reader(file_obj)
        for b in aux:
            print(b)
            assert len(b) == 41
            pass

    # Counting 3 rows, header + 2 lines from the input data
    with open (OUTPUT_CSV, "r") as file_obj:
        aux = file_obj.readlines()
        assert len(aux) == 3
        pass