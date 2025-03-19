import sys
import requests

from get_reporters_Yin_Chen_news import check_news  # 匯入函式



def notify_discord_Lees_webhook(msg):
    url = 'https://discord.com/api/webhooks/1337265139006705746/0vCqO_wv0lTLCRPaHkQ5B3PsclH85MS3tx2xkWt2PHEOY3YAm2MwHlvpXbGAD2pB9PLb'
    headers = {"Content-Type": "application/json"}
    data = {"content": msg, "username": "新新聞通知"}
    res = requests.post(url, headers = headers, json = data) 
    if res.status_code in (200, 204):
            print(f"Request fulfilled with response: {res.text}")
    else:
            print(f"Request failed with response: {res.status_code}-{res.text}")


def generate_Lees_msg():
    new_announcements = check_news()  # 呼叫函式取得新公告
    if new_announcements:
        msg = '\n\n'.join(
            f"{announcement['title']} {announcement['summary']} \n{announcement['url']}"
            for announcement in new_announcements
        )
        return msg
    return None

def job_Lee():
    
    msg = generate_Lees_msg()
    if msg:
        notify_discord_Lees_webhook(msg)


def signal_handler(sig, frame):
    global running
    print('Stopping the scheduler...')
    running = False
    sys.exit(0)

if __name__ == "__main__":

    job_Lee()

