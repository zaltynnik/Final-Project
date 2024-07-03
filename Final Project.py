import csv
import os


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


data_sources = {
    "1": {"Datasource:": "MicrosoftLTVs2020-2023.csv", "Metric:": "Average LTV = 720$"},
    "2": {"Datasource:": "MicrosoftLTVs2015-2019.csv", "Metric:": "Average LTV = 700$"},
    "3": {"Datasource:": "MicrosoftLTVs2010-2014.csv", "Metric:": "Average LTV = 550$"},
}

write_csv_headers()

print("Welcome user, you entered data sources database.")
action = str()

while action != 6:
    action = input("Welcome user, that is a list of actions:\n"
                   "1. Check existing information\n"
                   "2. Add new data source\n"
                   "3. Calculate metric	\n"
                   "4. End the program\n"
                   "Choose your action (enter a number):").strip()

    # if action == "1":
    #     add_item()
    # elif action == "2":
    #     add_ds()
    # elif action == "3":
    #     calc_m()
    # elif action == "4":
    #     print("Closing database...")
    #     break
    # else:
    #     print("Invalid action! Enter a valid action.")
