# 1. Create a script with arguments:
#
# exp; required: false; default: min(exp)
# current_job_exp; required: false; default: max(current_job_exp)
# sex; required: false
# city; required: false
# position; required: false
# age; required: false
# path_to_source_files; required: true;
# destination_path; required: false; default: .
# destination_filename; required: false; default: f"2020_june_mini.csv".
# The script should read the .csv file and get the information based on your input and generate a new .csv
# file with that info
#
# Example of input:
# -exp 3 -sex female -position DevOps -city Kyiv --path_to_source_files . ...


import argparse
import csv

parser = argparse.ArgumentParser(
    description='The script should read the .csv file and get the information based on your input and generate a new .csv file with that info')
parser.add_argument("--exp", required=False, default=10, help="Experience")
parser.add_argument("--current_job_exp", required=False, default=0, help="Experience on current job")
parser.add_argument("--sex", "-s", required=False, help="Sex")
parser.add_argument("--city", required=False, help="City")
parser.add_argument("--position", "-p", required=False, help="Position")
parser.add_argument("--age", "-a", required=False, help="Age")
parser.add_argument("--path_to_source_files", required=True, help="Path to source file")
parser.add_argument("--destination_path", required=False, default=".", help="Path for new file")
parser.add_argument("--destination_filename", required=False, default="2020_june_mini.csv", help="Name of new file")
args = parser.parse_args()

if args.age is None:
    args.age = ""
if args.city is None:
    args.city = ""
if args.position is None:
    args.position = ""
if args.sex is None:
    args.sex = ""

file_len = 0
path_to_open = f'{args.path_to_source_files}/2020_june_mini.csv'
with open(path_to_open, 'r', encoding="utf8") as f:
    reader = csv.reader(f)
    for row in reader:
        if file_len == 0:
            header = row
        file_len += 1
new_el = [file_len, args.city, '', '', args.position, args.exp, args.current_job_exp, '', '', args.age, args.sex, '',
          '', '', '', '', '', '']

path_to_create = f'{args.destination_path}/{args.destination_filename}'
with open(path_to_create, 'a', encoding="utf8") as f:
    writer = csv.writer(f)
    if args.destination_filename != "2020_june_mini.csv":
        writer.writerow(header)
        new_el[0] = 2
    writer.writerow(new_el)