# -*- coding: utf-8 -*- 
import json, random
import requests
import os
from notion.client import NotionClient
import re

def safe_get(item, attrname):
    try:
        return item.get_property(attrname)
    except:
        return ''

def lambda_handler(event, context):
    slack_url = os.environ['SLACK_URL']
    notion = NotionClient(token_v2=os.environ['NOTION_TOKEN'])
    page = notion.get_block('https://www.notion.so/e33512afda4746c1b8e9ac9d35eaa706?v=c738af75da0a4cd1888ef87eba073fa2', force_refresh=True)
    rows = list(page.collection.get_rows())
    
    item = random.choice(rows)
    while len(item.sigdang) == 0:
        item = random.choice(rows)

    title = safe_get(item, 'sigdang')
    location = safe_get(item, 'wici')
    menus = safe_get(item, 'kiweodeu')
    main_menu = safe_get(item, 'jumenyu')

    location_url = ''
    
    if location != '':
        search_result = re.search(r'\[(.+)\](.+)', location)
        if search_result is not None:
            location_url = search_result.group(1)
            title += f'<{location_url}>'
        else:
            title += f'({location})'

    fields = [{
        'title': title,
        'value': f'{", ".join(menus)}\n{main_menu}',
        'short': False
    }]

    payloads = {
        'attachments':[{
            'pretext': '오늘의 점심 메뉴를 추천합니다!',
            'color': '#0099A6',
            'title_link': location_url,
            'fields': fields
        }]
    }

    response = requests.post(
        slack_url, data=json.dumps(payloads),
        headers={'Content-Type': 'application/json'}
    )

if __name__ == '__main__':
    lambda_handler(None, None)