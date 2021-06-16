import requests
from bs4 import BeautifulSoup
import pprint

my_response = requests.get('https://news.ycombinator.com/news')
my_response2 = requests.get('https://news.ycombinator.com/news?p=2')
my_response3 = requests.get('https://news.ycombinator.com/news?p=3')
my_soup = BeautifulSoup(my_response.text, 'html.parser')
my_soup2 = BeautifulSoup(my_response2.text, 'html.parser')
my_soup3 = BeautifulSoup(my_response3.text, 'html.parser')

story_links = my_soup.select('.storylink')
story_text = my_soup.select('.subtext')
story_links2 = my_soup2.select('.storylink')
story_text2 = my_soup2.select('.subtext')
story_links3 = my_soup3.select('.storylink')
story_text3 = my_soup3.select('.subtext')

more_page_story_links = story_links + story_links2 + story_links3
more_page_story_text = story_text + story_text2 + story_text3

def sorted_by_votes(x):
  return sorted(x, key= lambda k:k['votes'], reverse=True) #using Lambda to sort by votes

#the following function takes links and underlines and returns the stories with more than 50 votes
def my_web_crawler(links, underlines):
  my_arr = []
  for i, item in enumerate(links):
    story_title = item.getText()
    href = item.get('href', None)
    story_vote = underlines[i].select('.score')
    if len(story_vote) != 0:
      points = int(story_vote[0].getText().replace(' points', ''))
      if points > 50:
        my_arr.append({'story_title': story_title, 'link': href, 'votes': points})
  return sorted_by_votes(my_arr)
 
pprint.pprint(my_web_crawler(more_page_story_links, more_page_story_text))