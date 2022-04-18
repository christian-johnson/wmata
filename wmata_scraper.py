import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import requests
from bs4 import BeautifulSoup

from tqdm import trange

from tqdm import tqdm


class Scraper():

    def __init__(self, url = 'https://www.wmata.com/service/daily-report/index.cfm?ReportID='):
        self.url = url

    def load_page(self, i):
        page = requests.get(self.url + str(i), verify=False)
        soup = BeautifulSoup(page.content, 'html.parser')
        return page, soup

    def get_incidents(self, i):
        df = pd.DataFrame(columns = ['date','text'])
        page, soup = self.load_page(i)
        j = 0
        for entry in soup.find(class_ = 'cs_control CS_Element_CustomCF').decode_contents().split('<p>'):
            if '<br/>' in entry:
                for element in [item for sublist in [e.split('\\n') for e in entry.replace('\t', ' ').split('<br/>')] for item in sublist]:
                    try:
                        if ':' in element and np.logical_or('a.m.' in element[:20], 'p.m' in element[:20]):
                            event_date = pd.to_datetime(str(date) + ' ' + ' '.join(element.replace('\\n','').replace('\\r','').split(' ')[:2]))
                            event_text =  ' '.join(element.strip('\n').split(' ')[2:])
                            df.loc[j] = [event_date, event_text]
                            j += 1
                        if 'day,'  in element and '<h3>' in element:
                            date = pd.to_datetime(BeautifulSoup(element, 'html.parser').find_all('h3')[0].contents[0])
                    except:
                        print('Error. Details:')
                        print('i = ' + str(i))
                        print('Problematic text: ' + element)
                        pass

            else:
                if ':' in entry and np.logical_or('a.m.' in entry[:20], 'p.m' in entry[:20]):
                    try:
                        event_date = pd.to_datetime(str(date) + ' ' + ' '.join(entry.replace('\\n','').replace('\\r','').replace('\t', ' ').replace('\n', '').split(' ')[:2]))
                        event_text =  ' '.join(entry.strip('\\n').split(' ')[2:])
                        df.loc[i] = [event_date, event_text]
                        i += 1
                    except:
                        print('Error. Details:')
                        print('i = ' + str(i))
                        print('Problematic text: ' + entry)
                        pass
                if 'day,'  in entry and '<h3>' in entry:
                    date = pd.to_datetime(BeautifulSoup(entry, 'html.parser').find_all('h3')[0].contents[0])
        return df

if __name__ == '__main__':
    df = pd.DataFrame(columns = ['date','text'])

    for i in trange(13, 3781):
        df_temp = scraper.get_incidents(i = i)
        df = pd.concat([df, df_temp], axis = 0)
        time.sleep(1)
    df.to_json('wmata_data.jsonl', lines = True)

    
