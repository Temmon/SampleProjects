
def mySession(**kwargs):
    kwargs['verify'] = False
    return requests.Session(**kwargs)
    
import requests
requests.session = mySession
from jira.client import JIRA

def connectToJira():
    options = {'server': 'URL'}
    return JIRA(options, basic_auth=('USER', 'PASSWORD'))
    