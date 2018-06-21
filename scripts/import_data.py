import csv


def run():
    with open("scripts/dapps.csv", newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        # spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in reader:
            print(row)
