import requests
import json
import keys
news_api_key = str(keys.get_news_api_key())
headers={'X-Api-Key':news_api_key}


def get_news_from_keyword(keyword, n_news=8):
    news_url = 'https://newsapi.org/v2/everything?language=en&q='+keyword
    response = requests.get(news_url,headers=headers).text
    response = json.loads(response)['articles']
    return_list=[]
    for r in response:
        title=r['title']
        url=r['url']
        return_list.append(title+ '\n read here: '+str(url) + "\n\n")
    if len(return_list)>n_news:
        return str(' '.join(return_list[:n_news]))
    return str(' '.join(return_list))

