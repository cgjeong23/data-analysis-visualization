import csv
import requests
from bs4 import BeautifulSoup

result = []

with open('./news_results.csv', 'w', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['news_title','news_link'])
    