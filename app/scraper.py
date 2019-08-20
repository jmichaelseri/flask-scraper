from bs4 import BeautifulSoup
import requests



def juno():
    result = requests.get('https://www.junomagazine.com')
    src = result.content
    soup = BeautifulSoup(src, 'lxml')

    h3_tag = soup.find_all('h3')
    juno_urls = []
    juno_titles = []
    for link in h3_tag:
        if not "category" in link.a.attrs['href']\
            and not "subscriptions" in link.a.attrs['href']\
            and not "win" in link.a.attrs['href']:
                juno_urls.append(link.a.attrs['href'])
                juno_titles.append(link.a.attrs['title'])
    link_dict = dict(zip(juno_urls, juno_titles))


def bbc_uk():
    result = requests.get('ur://www.bbc.com/news/uk')
    src = result.content
    soup = BeautifulSoup(src, 'lxml')

    anchor_tag = soup.find_all('a')
    bbc_urls = []
    for link in anchor_tag:
        if 'class' in link.attrs:
            if 'gs-c-promo-heading' in link.attrs['class']:
                bbc_urls.append(link.attrs['href'])


def reuters():
    result = requests.get('https://uk.reuters.com')
    src = result.content
    soup = BeautifulSoup(src, 'lxml')

    story_div = soup.find_all('div', attrs={'class': 'story-content'})
    reuter_urls = []
    reuter_titles = []
    for link in story_div:
        reuter_urls.append(link.a.attrs['href'])
        reuter_titles.append(link.a.string)

