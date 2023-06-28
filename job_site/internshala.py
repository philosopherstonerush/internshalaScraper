from bs4 import BeautifulSoup
import csv_part.csv_part as csv_part
import pandas as pd
import helpers.constants as constant

# List of offers that we already already applied to
df = pd.read_csv(constant.FINAL_FILE)
ids_already_scraped = df["id"].tolist()

# List of offers that we scrapped
internships_offers = []


def scrape_em_internshala(page): # requests object
    soup = BeautifulSoup(page.text, 'html.parser')
    all_meta = soup.find_all(class_="internship_meta", limit=5)
    if all_meta:
        for elem in all_meta:
            x = {}
            name_internship = elem.find(class_="view_detail_button")
            if name_internship:
                x["position"] = name_internship.text
            else:
                x["position"] = "unknown"
            company = elem.find(class_="link_display_like_text view_detail_button")
            if company:
                x["company"] = company.text.strip()
            else:
                x["company"] = "unknown"
            sti = elem.find(class_="stipend")
            if sti:
                x["stipend"] = sti.text.strip()
            else:
                x["stipend"] = "unknown"
            day = elem.find(class_="status status-small status-success")
            if day:
                x["posted"] = day.text.strip()
            else:
                x["posted"] = "unknown"
            id = elem.parent['internshipid']
            if int(id) in ids_already_scraped:
                continue
            x["id"] = id
            link = elem.find(class_="view_detail_button")
            x["link"] = link["href"]
            internships_offers.append(x)
            
        # At the end, write the offers into the temp file
        csv_part.write_temp(internships_offers)
    else:
        return