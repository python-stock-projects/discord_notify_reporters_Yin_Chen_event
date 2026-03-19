'''
追縱經濟日報 財金記者 尹慧中與陳美玲的新聞。
新聞網址 尹慧中：https://udn.com/news/reporter/MDQwNDM=
        陳美玲：https://udn.com/news/reporter/MDUxNDg=
'''

import requests
from datetime import datetime
from bs4 import BeautifulSoup 
from pytz import timezone



# 聯合新聞網 尹慧中與陳美玲新聞網址
Yin_news_url = "https://udn.com/news/reporter/MDQwNDM="
Chen_news_url = "https://udn.com/news/reporter/MDUxNDg="


def get_Yin_news():

     # 設定台灣時區
    taiwan_tz = timezone('Asia/Taipei')
    now_taiwan_time = datetime.now(taiwan_tz)
    print(f"now_taiwan_time: {now_taiwan_time}")

    response = requests.get(Yin_news_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # 找到所有新聞的容器
    news_list = soup.find_all('div', class_='story-list__news')
    recent_news = []

    for news in news_list:
        # 提取標題
        title_tag = news.find('h2')
        if title_tag:
            title_link = title_tag.find('a')
            if title_link:
                title = title_link.get_text()

                # 提取部分文章開頭
                summary_tag = news.find('p')
                if summary_tag:
                    summary = summary_tag.get_text()

                    # 提取網址
                    url = title_link['href']

                    # 提取日期並檢查是否在 4 小時內
                    date_tag = news.find('time')
                    if date_tag:
                        date_str = date_tag.get_text()  # 提取日期字串
                        news_datetime = datetime.strptime(date_str, '%Y-%m-%d %H:%M').replace(tzinfo=taiwan_tz)
                        print(f"news_datetime: {news_datetime}")
                        time_diff = now_taiwan_time - news_datetime
                        print(f"time_diff: {time_diff}")

                        if time_diff.total_seconds() <= 4 * 3600:  # 4 小時內
                            recent_news.append({'title': title, 'summary': summary, 'url': url})
       

    return recent_news

def get_Chen_news():

    # 設定台灣時區
    taiwan_tz = timezone('Asia/Taipei')
    now_taiwan_time = datetime.now(taiwan_tz)
    print(f"now_taiwan_time: {now_taiwan_time}")


    response = requests.get(Chen_news_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # 找到所有新聞的容器
    news_list = soup.find_all('div', class_='story-list__news')
    recent_news = []

    for news in news_list:
        # 提取標題
        title_tag = news.find('h2')
        if title_tag:
            title_link = title_tag.find('a')
            if title_link:
                title = title_link.get_text()

                # 提取部分文章開頭
                summary_tag = news.find('p')
                if summary_tag:
                    summary = summary_tag.get_text()

                    # 提取網址
                    url = title_link['href']

                    # 提取日期並檢查是否在 4 小時內
                    date_tag = news.find('time')
                    if date_tag:
                        date_str = date_tag.get_text()  # 提取日期字串
                        news_datetime = datetime.strptime(date_str, '%Y-%m-%d %H:%M').replace(tzinfo=taiwan_tz)
                        print(f"news_datetime: {news_datetime}")
                        time_diff = now_taiwan_time - news_datetime
                        print(f"time_diff: {time_diff}")

                        if time_diff.total_seconds() <= 4 * 3600:  # 4 小時內
                            recent_news.append({'title': title, 'summary': summary, 'url': url})

    return recent_news



def check_news():

    new_news = get_Yin_news() + get_Chen_news()

    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
   
    if new_news:
        # 處理新公告，例如發送通知
        print(f"有新的news - {current_time}")
  
    else:
        print(f"沒有新的news - {current_time}")

    return new_news


if __name__ == "__main__":
    check_news()


    


    

