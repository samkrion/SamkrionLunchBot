# -*- coding: utf-8 -*- 
import json, random
import http.client
import requests
def lambda_handler(event, context):
    slack_url = "https://hooks.slack.com/services/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"
    
    eat_list = getRandomDatas()
    fields = []
    
    for data in eat_list:
        tmp_title = data['title']
        title_link = data['url']
        if data['url'] != "":
            tmp_title += "<{}>".format(data['url'])
        fields.append({
            "title":tmp_title,
            "value":"{}\n{}\n".format(data['menu'], data['description']),
            "short":False
        })
    title = "오늘의 점심 메뉴를 추천합니다!"
    title_url = title_link

    payloads = {
        "attachments":[{
            "pretext": title,
            "color":"#0099A6",
            "title_link":title_url,
            "fields": fields
        }]
    }

    response = requests.post(
        slack_url, data=json.dumps(payloads),
        headers={'Content-Type': 'application/json'}
    )



def getRandomDatas():
    json_data=open('data.json').read()
    datas = json.loads(json_data)
    random.shuffle(datas)
    tmp = random.sample(datas, 1)
    return tmp