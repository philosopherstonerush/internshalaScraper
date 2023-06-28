from bs4 import BeautifulSoup
import requests
import csv_part.csv_part as csv_part
import pathlib
import job_site.internshala as internshala
from alive_progress import alive_bar

# pre-requisites
path = csv_part.path
if(path.is_file()):
    path.unlink()

#internshala
skills_internshala = {"python", "django", "flutter", "flutter-development", "c-programming", "sql", "mysql", "bash", "java", "hibernate-java", "rust", "javascript", "javascript-development", "data-analytics", "data-science", "database-building", "embedded-systems", "arduino", "machine-learning", "artificial-intelligence-ai"}
web_internshala = "https://internshala.com/internships/work-from-home-{}-internships-in-chennai/"

# alive_bar gives a visual indication about the progress of scraping
with alive_bar(len(skills_internshala)) as bar: # Initialize with how many processes it has to perform
    for elem in skills_internshala:
        page = requests.get(web_internshala.format(elem))
        internshala.scrape_em_internshala(page) 
        bar() # increment the bar at the end of every calculation

# cleanup
csv_part.sort_temp()
csv_part.remove_duplicates()
print("press Y to write finally") # Check temp file, apply to internships and then press Y 
yes = str(input())
if yes == "Y": # checks if the internship is applied to before it gets added to the final list
    csv_part.final_write()

