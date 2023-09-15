import csv
import argparse


def csv_to_markdown_table(csv_file, md_file):
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        headers = next(reader)

        # Create the markdown table headers
        table = " | ".join(headers) + "\n"
        table += " | ".join(['---'] * len(headers)) + "\n"

        for row in reader:
            table += " | ".join(row) + "\n"

    with open(md_file, 'a') as mdf:
        mdf.write(table)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert a CSV file to Markdown table and append it to a Markdown file.')
    parser.add_argument('csv_file', type=str, help='Path to the CSV file')
    parser.add_argument('md_file', type=str, help='Path to the Markdown file where the table will be appended')

    args = parser.parse_args()
    csv_to_markdown_table(args.csv_file, args.md_file)
