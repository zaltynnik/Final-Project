import csv
import os

MENU_OPTIONS = [
    '1. Check existing information',
    '2. Add new data source',
    '3. Calculate metric',
    '4. End the program',
]

def get_menu_action():
    print("\n".join(MENU_OPTIONS))
    selected_option = input("Select an option: ")
    while selected_option not in ["1", "2", "3", "4"]:
        print("Invalid option. Try again.")
        selected_option = input("Select an option: ")
    return int(selected_option) - 1
def check_ex_ds():
    try:
        with open("data_sources.csv", mode="r") as file:
            reader = csv.DictReader(file)
            data_sources = list(reader)
        if not data_sources:
            print("No data sources found.")
            return

        print("\nExisting data sources:")
        for data_source in data_sources[:3]:
            print(f"Datasource: {data_source['Datasource']} | Metric: {data_source['Metric']}")

    except FileNotFoundError:
        print("No data sources found.")
    except csv.Error:
        print("Error: Could not read data sources.")
def add_ds():
    path = input("Enter the path of the data source: ")
    try:
        with open(path, mode="r") as file:
            reader = csv.reader(file)
            rows = list(reader)
        if not rows:
            print("Error: The file is empty.")
            return

        column_names = rows[0]
        total_records = len(rows) - 1

        print("\nDatasource structure:")
        print(" | ".join(column_names))
        print(f"Total records: {total_records}")

        name = path.split("\\")[-1]
        data_source_info = {
            "Datasource": name,
            "Metric": "Net Profit Margin"
        }

        with open("data_sources.csv", mode='a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["Datasource", "Metric"])
            if file.tell() == 0:
                writer.writeheader()
            writer.writerow(data_source_info)

    except FileNotFoundError:
        print(f"Error: File not found at {path}")
    except csv.Error:
        print(f"Error: Could not read file at {path}")

# def calc_m():
def exit():
    exit_value = input("Enter {yes} to exit or {no} to continue: ")
    if exit_value == "yes":
        stop.append(0)
    else:
        return None


MENU_OPTIONS_SHOP = {
    0: check_ex_ds,
    1: add_ds,
    # 2: calc_m,
    3: exit
}


stop = []
while len(stop) == 0:
    selected_action = get_menu_action()
    MENU_OPTIONS_SHOP[selected_action]()