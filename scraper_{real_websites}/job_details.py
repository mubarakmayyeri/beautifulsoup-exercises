from bs4 import BeautifulSoup
import requests

URL = "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Data+Science&txtLocation="

html_text = requests.get(URL).text

soup = BeautifulSoup(html_text, 'lxml')

jobs = soup.find('li', class_="clearfix job-bx wht-shd-bx")
job_name = jobs.find('a').text
company = jobs.find('h3', class_="joblist-comp-name").text.strip().split()[:2]
company_name = ''.join(company)
skills = jobs.find('span', class_="srp-skills").text.replace(" ", "").strip()
post_day = jobs.find('span', class_="sim-posted").text.split()[1]

print(f'''
Job Title: {job_name}
Company: {company_name}
skills: {skills}
Posting Day: {post_day} ago
''')