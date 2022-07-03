import requests
import json
import numpy as np

def applied():
    while True:
        reply = {
            'content': np.random.choice(['Hi','Oh Hello','Hello','Sup']) # Text to reply with
        }
        header = {
        'authorization': 'AABBBBCCCCDDEEEFGG' # Authorization
        }  
        req = requests.get(f'https://discord.com/AAABBCCC,headers=header) # Request URL, (retrieve message)
        m = json.loads(req.text)
    
        payload = {
            'content': m[0]['content'] # Get the latest message 
        }
        words = ['Hi','Hello','AAA','ok']
        print(payload['content'])
        for i in words:
            if payload['content'].lower() in i.lower():
                requests.post("https://discord.com/api/v9/channels/896100152819978270/messages",
                                data=reply,headers=header) # Send the text to reply with if certain message is sent
applied()
