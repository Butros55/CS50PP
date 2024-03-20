import sys
import csv

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    sort(sys.argv[1], sys.argv[2])


def sort(doc, new_file):
    try:
        after = []
        with open(doc) as file:
            reader = csv.DictReader(file)
            for row in reader:
                last, first = row["name"].strip().split(",")
                after.append({"first": first.strip(), "last": last, "house": row["house"]})

        with open(new_file, "w") as file:
            writer = csv.writer(file)
            writer.writerow(["first", "last", "house"])
            for names in after:
                writer.writerow([names['first'], names['last'], names['house']])



    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")


if __name__ == "__main__":
    main()