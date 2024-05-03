from os import listdir
from os.path import isfile, join
from stegano import lsb
import csv

directory_path = "./files to analyze"

output_csv_file = "output_hidden_messages.csv"

png_files = [f for f in listdir(directory_path) if isfile(
    join(directory_path, f)) and f.lower().endswith(".png")]

with open(output_csv_file, "w", newline="") as csv_file:
    csv_writer = csv.writer(csv_file)

    csv_writer.writerow(["PNG File", "Hidden Message"])

    for png_file in png_files:
        modified_image_path = join(directory_path, png_file)
        hidden_message = lsb.reveal(modified_image_path)

        csv_writer.writerow([png_file, hidden_message])

print("Hidden messages extracted and saved to:", output_csv_file)
