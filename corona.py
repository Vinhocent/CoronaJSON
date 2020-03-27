#!/usr/bin/python3
from json import loads
from requests import get
from bs4 import BeautifulSoup

def dump_json():
    '''
        outputs a single-line dict for usage in other software
    '''
    url = 'https://www.worldometers.info/coronavirus'
    soup = BeautifulSoup(get(url).content, 'html.parser')
    stats = ("\"%s\": ",
             "{\"total_cases\": \"%s\", ",
             "\"new_cases\": \"%s\", ",
             "\"total_deaths\": \"%s\", ",
             "\"new_deaths\": \"%s\", ",
             "\"total_recovered\": \"%s\", ",
             "\"active_cases\": \"%s\", ",
             "\"critical\": \"%s\", ",
             "\"total_cases_per_million\": \"%s\", ",
             "\"total_deaths_per_million\": \"%s\"}, ")
    iter_ = ''
    table = soup.find_all('table', {'id':'main_table_countries_today'})
    for mytable in table:
        table_body = mytable.find('tbody')
        try:
            
            rows = table_body.find_all('tr')
            iter_ += '{'
            for tr in rows:
                cols = tr.find_all('td')
                num = 0
                for td in cols:
                    tdt = td.text
                    if num == 3: tdt = tdt.replace(' ', '')
                    iter_ += stats[num] % tdt
                    num += 1
            iter_ += '}'
            return loads(iter_.replace('}, }', '}}'))
        except:
            return ("scraper broke, needs updating!")
                    #+ str(soup.prettify())[400:2000])

if __name__ == '__main__':
    print(dump_json())
