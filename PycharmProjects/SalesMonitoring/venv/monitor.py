from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time


# 设置 ChromeDriver 的路径
chrome_driver_path = "/Users/yanting/Downloads/chromedriver-mac-arm64/chromedriver"

# 设置浏览器选项（可选，headless模式让浏览器在后台运行）
chrome_options = Options()
chrome_options.add_argument("--headless")  # 无头模式，后台运行

# 启动 ChromeDriver
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# 打开目标网页
url = " https://www.stories.com/en_gbp/accessories/scarves/fall-winterscarves/product.two-tone-wool-scarf-blue.1238202001.html"  # 替换为你要检测的页面URL
url_with_discount = "https://www.stories.com/en_gbp/clothing/jeans/slim-fit/product.slim-jeans-blue.1016785020.html"
driver.get(url)

# 等待页面加载
time.sleep(30)  # 可调整等待时间，确保页面加载完毕

# 获取整个页面的HTML内容
page_content = driver.page_source


# 查找是否包含 "Sale" 或相关折扣信息
if "percentageDiscount" in page_content:
    print("该商品有折扣！")
else:
    print("该商品暂无折扣！")

# 关闭浏览器
driver.quit()



