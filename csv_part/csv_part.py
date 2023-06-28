import csv
import pathlib
import datetime
import re
import pandas as pd
import helpers.constants as constant

path = pathlib.Path(constant.TEMP_FILE)
path_final = pathlib.Path(constant.FINAL_FILE)

def unlink():
    path.unlink()

def write_temp(list_of_offers):
    # Internshala is hardcoded
    if(path.is_file()):
        with open(constant.TEMP_FILE, mode='a', encoding="utf-8") as intern_file:
            field_names=["id", "name", "company","stipend", "posted", "link", "applied"]
            writer = csv.DictWriter(intern_file, fieldnames=field_names)
            for elem in list_of_offers:
                writer.writerow({"id": elem["id"], "name": elem["position"], "company": elem["company"], "stipend": elem["stipend"], "posted": elem["posted"], "link": "www.internshala.com/{}".format(elem["link"]), "applied": ""})
    else:
        with open(constant.TEMP_FILE, mode='w', encoding="utf-8") as intern_file:
            field_names=["id", "name", "company","stipend", "posted", "link", "applied"]
            writer = csv.DictWriter(intern_file, fieldnames=field_names)
            writer.writeheader()
            for elem in list_of_offers:
                writer.writerow({"id": elem["id"], "name": elem["position"], "company": elem["company"], "stipend": elem["stipend"], "posted": elem["posted"], "link": "www.internshala.com/{}".format(elem["link"]), "applied": ""})
        


def final_write():
    # Doesnt create a new final file if its not there
    if path_final.is_file():
        with open(constant.FINAL_FILE, mode='a') as final_file:
            with open(constant.TEMP_FILE, mode='r') as temp_file:
                field_names_temp=["id", "name", "company","stipend", "posted", "link", "applied"]
                reader = csv.DictReader(temp_file, fieldnames=field_names_temp)
                field_names_final=["id", "internship_name", "company", "stipend", "posted", "portal", "applied_date", "call_back"]
                writer = csv.DictWriter(final_file, fieldnames=field_names_final)
                date = datetime.date.today()

                for elem in reader:
                    res=re.findall(r"(?<=\.)([^.]+)(?:\.(?:co\.uk|ac\.us|[^.]+(?:$|\n)))", elem["link"])
                    if elem["applied"] == "Y":
                        writer.writerow({"id": elem["id"], "internship_name": elem["name"], "company": elem["company"], "stipend": elem["stipend"], "posted": elem["posted"], "portal": res[0], "applied_date": date, "call_back": ""})
        path.unlink()

def sort_temp():
    df = pd.read_csv(constant.TEMP_FILE)
    print(len(df.index))
    sorted_df = df.sort_values(by=["stipend"], ascending=False)
    sorted_df.to_csv(constant.TEMP_FILE, index=False)

def remove_duplicates():
    df = pd.read_csv(constant.TEMP_FILE)
    removed_df = df.drop_duplicates(["id"], keep="first")
    removed_df.to_csv(constant.TEMP_FILE, index=False)