import requests
from bs4 import BeautifulSoup
import schedule
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# 目标URL
url = "https://www.stories.com/en_gbp/accessories/scarves/fall-winterscarves/product.two-tone-wool-scarf-blue.1238202001.html"  # 将此替换为你要监控的商品页面

# 邮件通知设置（可选）
def send_email(subject, body):
    sender_email = "lu.yanting925@gmail.com"
    receiver_email = "lu.yanting925@gmail.com"
    password = "LYT31415926"

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, password)
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)

def check_for_discount():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    # 获取页面内容
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    # 查找折扣信息的标识，例如 "Sale" 或 "折扣"
    # 这一步需要根据页面实际的HTML结构来修改
    discount_tag = soup.find(text=lambda t: "Sale" in t)

    if discount_tag:
        print("有折扣活动！")
        # 如果有折扣，可以发邮件通知
        send_email("折扣通知", f"产品有折扣了！查看页面：{url}")
    else:
        print("没有折扣")

# 定时任务，每隔一小时检查一次
schedule.every(1).hours.do(check_for_discount)

# 无限循环执行任务
while True:
    schedule.run_pending()
    time.sleep(1)
