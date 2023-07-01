# internshalaScraper
A scraper made with python to extract internship offers from internshala

# How to use? 
1. Install python
2. Install pipenv
`pip install pipenv`
3. Initialize path name constants found here, helphers/constants.py
`C:\\path\to\where\you\want\the\files\to\be`
4. Execute started.cmd by double clicking it if you are on windows, or `python main.py`
5. Temporary file is where you get to see the current internship offers while final file is used for analysis and keeping track of internships you have already applied.
6. If you have applied to an internship in the temp csv file, then enter `Y` in the applied column for the internship details to be stored in the final csv file.

# Performance
It takes about 3 minutes to scrap, consider using [ asyncInternshalaScraper](https://github.com/philosopherstonerush/asyncInternshalaScraper) if you are comfortable with python or [go-internshalaScraper](https://github.com/philosopherstonerush/go-internshalaScraper) if you are comfortable with golang.