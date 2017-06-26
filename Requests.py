
# coding: utf-8

from lxml import html
import requests

page = requests.get('https://news.google.de/')
response = html.fromstring(page.content)

schlagzeilen = response.xpath('//div[@class="section top-stories-section section-toptop"]//h2[@class="esc-lead-article-title"]')
schlagzeilen_dict = {}

for i in range(len(schlagzeilen)):
    titel = schlagzeilen[i].xpath('.//span[@class="titletext"]/text()')[0]
    url = schlagzeilen[i].xpath('.//a/@href')[0]
    schlagzeilen_dict[titel] = url

international = response.xpath('//div[@class="section story-section section-de_de-w"]//h2[@class="esc-lead-article-title"]')
international_dict = {}

for i in range(len(international)):
    titel = international[i].xpath('.//span[@class="titletext"]/text()')[0]
    url = international[i].xpath('.//a/@href')[0]
    international_dict[titel] = url

deutschland = response.xpath('//div[@class="section story-section section-de_de-n"]//h2[@class="esc-lead-article-title"]')
deutschland_dict = {}

for i in range(len(deutschland)):
    titel = deutschland[i].xpath('.//span[@class="titletext"]/text()')[0]
    url = deutschland[i].xpath('.//a/@href')[0]
    deutschland_dict[titel] = url

wirtschaft = response.xpath('//div[@class="section story-section section-de_de-b"]//h2[@class="esc-lead-article-title"]')
wirtschaft_dict = {}

for i in range(len(wirtschaft)):
    titel = wirtschaft[i].xpath('.//span[@class="titletext"]/text()')[0]
    url = wirtschaft[i].xpath('.//a/@href')[0]
    wirtschaft_dict[titel] = url

technologie = response.xpath('//div[@class="section story-section section-de_de-t"]//h2[@class="esc-lead-article-title"]')
technologie_dict = {}

for i in range(len(technologie)):
    titel = technologie[i].xpath('.//span[@class="titletext"]/text()')[0]
    url = technologie[i].xpath('.//a/@href')[0]
    technologie_dict[titel] = url

print('************************************************************************************************************')
print('Schlagzeilen:')
print('--------------')
for i in schlagzeilen_dict.keys():
    print(i)
    print(schlagzeilen_dict[i])
    print('')
    
print('************************************************************************************************************')
print('International:')
print('--------------')
for i in international_dict.keys():
    print(i)
    print(international_dict[i])
    print('')

print('************************************************************************************************************')
print('Deutschland:')
print('--------------')
for i in deutschland_dict.keys():
    print(i)
    print(deutschland_dict[i])
    print('')

print('************************************************************************************************************')
print('Wirtschaft:')
print('--------------')
for i in wirtschaft_dict.keys():
    print(i)
    print(wirtschaft_dict[i])
    print('')

print('************************************************************************************************************')
print('Technologie:')
print('--------------')
for i in technologie_dict.keys():
    print(i)
    print(technologie_dict[i])
    print('')