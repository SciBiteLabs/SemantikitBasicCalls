"""

Example script for interacting with semantikit.

"""""

import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

username = ''  # we will give you this on the hackathon day
password = ''  # we will give you this on the hackathon day
url = 'http://ugm.scibite.com:8090/api'


def get_all_models():
    """
    Return a list of all the models available via semantikit.

    :return:
    """

    request_url = '{}/Get model names/1.0/get_models'.format(url)
    models = requests.get(request_url, verify=False, auth=(username, password)).json()['models']

    return models


def get_possible_syns(query, syns_limit=10, models=['MedLine_Basic']):
    """
    Get possible syns for a query string.
    
    :param query: a list of query strings, e.g. ['sildenafil']
    :param syns_limit: int, default 10
    :param models: list of models, default ['MedLine_Basic']
    :return: 
    """

    request_url = '{}/Synonym suggestions/1.0/suggest_synonyms?limit={}&sources={}&query={}'.format(
        url, syns_limit, ','.join(models), ','.join(query))
    synonyms = requests.get(request_url, verify=False, auth=(username, password)).json()['results']

    return synonyms


print(get_possible_syns(['sildenafil', 'tadalafil'], syns_limit=5, models=['MedLine_Basic', 'MedLine_Phrased']))
