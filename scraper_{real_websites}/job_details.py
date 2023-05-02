from bs4 import BeautifulSoup
import requests

URL = "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Data+Science&txtLocation="

html_text = requests.get(URL).text

soup = BeautifulSoup(html_text, 'lxml')

jobs = soup.find_all('li', class_="clearfix job-bx wht-shd-bx")
for job in jobs:
    published_date = job.find('span', class_="sim-posted").text.strip()
    
    if published_date == "Posted few days ago":
        job_name = job.find('a').text.strip()
        company = job.find('h3', class_="joblist-comp-name").text.strip()
        skills = job.find('span', class_="srp-skills").text.replace(" ", "").strip()

        print(f'''
Job Title: {job_name}
Company: {company}
Required Skills: {skills}
-------------------------------

''')

