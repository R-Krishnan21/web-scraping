import requests
import json
from bs4 import BeautifulSoup

def scrape():
    questions_data = []

    res = requests.get("https://stackoverflow.com/questions/tagged/django?tab=Votes").text
    soup = BeautifulSoup(res,'lxml')
    questions = soup.find_all(class_='question-summary')
    for question in questions:
        q = question.find(class_="question-hyperlink").text
        detail = question.find(class_="excerpt").text.strip()
        link = "https://stackoverflow.com{}".format(question.find(class_="question-hyperlink").get('href'))
        votes = int(question.find(class_="vote-count-post").text)
        views = int(question.find(class_="views").attrs['title'].replace(" views","").replace(',',''))
        tags = [i.text for i in question.find_all(class_="post-tag")]

        questions_data.append({
            "question": q,
            "detail": detail,
            "link": link,
            "votes": votes,
            "views": views,
            "tags": tags
        })
    return questions_data
