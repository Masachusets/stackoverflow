from stackapi import StackAPI
from datetime import timedelta, datetime
from pprint import pprint

def last_questions(resourse='stackoverflow', request='questions', days=2, tag='python'):
    SITE = StackAPI(resourse)
    fromdate = int(datetime.timestamp(datetime.now() - timedelta(days=days)))
    questions = SITE.fetch(request, fromdate=fromdate, tagged=tag)
    for question in questions['items']:
        pprint(question['title'])

if __name__ == '__main__':
    last_questions()
