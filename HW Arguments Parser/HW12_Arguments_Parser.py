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
parser.add_argument("--destination_filename", required=False, default=f"2020_june_mini.csv", help="Name of new file")
args = parser.parse_args()

if args.age is None:
    args.age = ""
if args.city is None:
    args.city = ""
if args.position is None:
    args.position = ""
if args.sex is None:
    args.sex = ""

list_with_arg = []
path_to_open = "2020_june_mini.csv"
with open(path_to_open, 'r', encoding="utf8") as file:
    reader = csv.DictReader(file)
    head = reader.fieldnames
    for dictates in reader:
        if dictates['exp'] == args.exp and dictates['Город'] == args.city and dictates['Пол'] == args.sex and \
                dictates['Должность'] == args.position:
            list_with_arg.append(dictates)

path_to_create = f'{args.destination_path}/{args.destination_filename}'
with open(args.destination_path + "2020_june_mini_2.csv", "w", encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=head)
    for j in list_with_arg:
        writer.writerow(j)