from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

# [1] 브라우저 옵션 설정
# 브라우저가 실행되자마자 닫히는 것을 방지 ("detach" 옵션)
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# [불필요한 로그 제거 옵션 - 선택사항]
chrome_options.add_argument("--log-level=3")

# [2] 브라우저 실행 (Selenium Manager가 드라이버 자동 설치함)
print("브라우저를 실행합니다...")
driver = webdriver.Chrome(options=chrome_options)

# [3] 웹페이지 이동
url = "https://kream.co.kr/"
driver.get(url)
sleep(2)

driver.find_element(By.CSS_SELECTOR, "button.btn_search").click()
sleep(1)
input_tag = driver.find_element(By.CSS_SELECTOR, "input.input_search")
input_tag.send_keys("슈프림")
input_tag.send_keys(Keys.ENTER)
sleep(1)

# counter = 0
# while counter <= 20:
#     driver.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.PAGE_DOWN)
#     sleep(1.5)
#     counter += 1

# dynamic rendering, 동적 콘텐츠 접근, 제품에 대한 정보, 무한 스크롤
for i in range(15):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(1.5)

# ================================ #
# bs4
# ================================ #

html = driver.page_source
html = BeautifulSoup(html, "lxml")

wrapper = html.find("div", {"class": "layout-grid-horizontal-equal"})
items = wrapper.find_all("a", {"class": "product_card"})
for item in items:
    # return 2개 줄꺼임, 바로 자시으로 div 가 2개
    product_link = "https://kream.co.kr" + item.get("href").strip()
    product_detail_div = item.find("div", {"class": "layout_list_vertical"})
    product_strings: list[str] = [
        p.get_text(strip=True) for p in product_detail_div.find_all("p")
    ]

    if len(product_strings) != 6:
        continue

    brand, name, price, likes, review, trade = product_strings

    if "후드" in product_strings[1]:
        print("============================================")
#print(product_link)
        print(
            brand,
            name,
            price,
            likes,
            review,
            trade,
        )

# driver.close()
driver.quit()
from concurrent.futures import ThreadPoolExecutor, as_completed


def fetch_product_page(link: str):
    try:
        res = requests.get(link, timeout=5)
        res.raise_for_status()
        return res.content[100:200]
    except Exception as e:
        print(f"에러 발생 >> {e}")


results = list()

# product_links 길이가 20개
# 4개 -> 5번 / 10개 -> 2번
with ThreadPoolExecutor(max_workers=4) as ex:
    futures = [ex.submit(fetch_product_page, link) for link in product_links]

    for fut in as_completed(futures):
        try:
            results.append(fut.result())
        except Exception as e:
            print(f"동시 실행에 에러 발생 >> {e}")

print(results)


def fetch_product_page(link: str):
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
        "cache-control": "max-age=0",
        "priority": "u=0, i",
        "sec-ch-ua": '"Not(A:Brand";v="8", "Chromium";v="144", "Google Chrome";v="144"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"macOS"',
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36",
    }

    try:
        res = requests.get(link, headers=headers, timeout=5)
        res.raise_for_status()
        return res.content[100:200]
    except Excep
try