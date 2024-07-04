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
def write_csv_headers():
    if not os.path.exists("data_sources.csv"):
        headers = ["Num", "Datasource", "Metric"]
        with open("data_sources.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(headers)
            for item, info in data_sources.items():
                writer.writerow([item, info["Datasource:"], info["Metric:"]])



# def check_ex_ds():


# def add_ds():


# def calc_m():
def exit():
    exit_value = input("Enter {yes} to exit or {no} to continue: ")
    if exit_value == "yes":
        stop.append(0)
    else:
        return None

data_sources = {
    "1": {"Datasource:": "MicrosoftLTVs2020-2023.csv", "Metric:": "Average LTV = 720$"},
    "2": {"Datasource:": "MicrosoftLTVs2015-2019.csv", "Metric:": "Average LTV = 700$"},
    "3": {"Datasource:": "MicrosoftLTVs2010-2014.csv", "Metric:": "Average LTV = 550$"},
}

write_csv_headers()

print("Welcome user, you entered data sources database.")


MENU_OPTIONS_SHOP = {
    # 0: add_item,
    # 1: add_ds,
    # 2: calc_m,
    3: exit
}

stop = []
while len(stop) == 0:
    selected_action = get_menu_action()
    MENU_OPTIONS_SHOP[selected_action]()