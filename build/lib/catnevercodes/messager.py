from . import json
from . import requests
from . import Union

from . import default_message, dingtalk_webhook, dingtalk_mobiles

def send_dingtalk(
    content: Union[str, dict] = None or default_message,
    atMobiles: Union[str, list] = None or dingtalk_mobiles,
    webhook: str = None or dingtalk_webhook,
    atAll: bool = True
    ) -> None:
    
    if str == type(atMobiles):
        atMobiles = [atMobiles]

    if dict == type(content):
        content = "\n".join([f"{k}: {v}" for k,v in content.items()])

    headers = {'Content-Type': 'application/json; charset=utf-8'}
    data = {
            "msgtype": "text",
            "text": {
                "content": content},
            "at": {
                "atMobiles": atMobiles,
                "isAtAll": atAll}}

    requests.post(webhook, headers=headers, data=json.dumps(data))