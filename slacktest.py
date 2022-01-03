import requests
 
def post_message(token, channel, text):
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel,"text": text}
    )
    print(response)
 
myToken = "xoxb-2902606417412-2897421597653-UyScHYtDZvq79gJbvwDtcBt0"
 
post_message(myToken,"#자동매매","jocoding")
