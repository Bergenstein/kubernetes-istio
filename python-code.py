from bs4 import BeautifulSoup
import requests
import time

print('Put the kind of job you are looking for')
required_job = input('>')
print(f'Filtering out {required_job}')

def find_employment():
    html_text = requests.get('https://www.amazon.jobs/en-gb/locations/virtual-locations').text
    soup = BeautifulSoup(html_text, 'lxml')
    soup.find("div")
    employments = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
    for index, job in enumerate(employment):
        #finds published date
        published_date = job.find('span', class_='sim-posted').span.text
        if 'months' in published_date: #finds companies that have months in them
            company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ','')
            skills = job.find('span', class_ = 'srp-skills').text.replace(' ','')
            more_info = job.header.h2.a['href']
            if required_job not in skills:
                with open(f'posts/{index}.txt', 'w') as f:
                    f.write(f"Company Name: {company_name.strip()} \n")
                    f.write(f"Required Skills: {skills.strip()} \n")
                    f.write(f'More Info: {more_info}')
                print(f'File saved: {index}')

if __name__ == '__main__':
    while True:
        find_employment()
        #IMPORTANT: KEEP THIS AMOUNT HIGHER AS POSSIBLE TO AVOID SCRAPING CONTINOUSLY A WEBSITE.
        #YOU DO NOT WANT TO BE CONSIDERED AS A BOT WHO TRIES TO ATTACK A WEBSITE BY REQUESTING FROM IT TOO MUCH
        time_wait = 10
        print(f'Waiting {time_wait} minutes...')
        time.sleep(time_wait * 60)

