import requests
from bs4 import BeautifulSoup
import time

def scrape_quotes():
    # 1. 目标网址 (这是一个专门供爬虫练习的网站)
    url = "http://quotes.toscrape.com/"
    
    # 2. 伪装成浏览器 (User-Agent)
    # 很多真实网站会拦截没有“身份证”的Python脚本，加上这个Header是工程实战的第一课
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    print(f"正在抓取页面: {url} ...")
    
    try: # 异常处理
        # 发送 GET 请求
        response = requests.get(url, headers=headers) # 调用requests工具箱里面的get
        
        # 检查请求是否成功 (200 代表成功, 403/404 代表失败)
        if response.status_code == 200:
            print("请求成功！开始解析数据...\n")
            
            # 3. 解析网页内容
            soup = BeautifulSoup(response.text, "html.parser")   # response.text 获取response的文本内容
            
            # 找到所有的名言卡片 (div class="quote")
            quotes = soup.find_all("div", class_="quote") # 锁定对应的地方
            
            for index, quote in enumerate(quotes, 1):
                # 提取名言内容 (span class="text")
                text = quote.find("span", class_="text").get_text()
                # 提取作者 (small class="author")
                author = quote.find("small", class_="author").get_text()
                
                print(f"{index}. {author} 说: {text}")
                
        else:
            print(f"请求失败，状态码: {response.status_code}")
            
    except Exception as e:
        print(f"发生错误: {e}")

if __name__ == "__main__": # 可以从别的地方调用这个函数，这样就不会执行
    scrape_quotes()