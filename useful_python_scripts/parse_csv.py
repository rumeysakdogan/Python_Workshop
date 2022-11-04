"""
This script is very handy when you need a lightweight module for reading and writing multiple CSV files.

Light-weight module for CSV
Can be used in your Python Projects
"""

# Parse CSV
import csv


def parse_csv(filename):
    with open(filename, 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in reader:
            print(', '.join(row))


def write_csv():
    with open('test.csv', 'wb') as csvfile:
        w = csv.writer(csvfile, delimiter=',')
        w.writerow(['Name', 'Age'])
        w.writerow(['John', '23'])
        w.writerow(['Mary', '22'])


parse_csv("test.csv")
write_csv()