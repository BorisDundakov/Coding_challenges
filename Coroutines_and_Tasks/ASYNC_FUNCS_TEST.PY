print('this is a bug

import time
import asyncio
import geocoder

import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


async def get_my_location():
    myloc = geocoder.ip('me')
    current_loc = myloc.latlng
    await asyncio.sleep(0)
    return current_loc


async def chromedriver_setup(url):
    # TODO: This is very time consuming

    PATH = "C:\Program Files (x86)\chromedriver.exe"  # PATH TO THE chromedriver.exe downloaded (check requirements.txt)
    op = webdriver.ChromeOptions()
    op.add_argument('headless')
    driver = webdriver.Chrome(PATH, options=op)
    driver.get(url)
    await asyncio.sleep(0)
    return driver


# noinspection DuplicatedCode
async def sync_funcs(bing_address):
    start_time = time.time()
    task1 = asyncio.create_task(chromedriver_setup(bing_address))
    task2 = asyncio.create_task(get_my_location())
    await task2
    driver = task1.result()
    current_loc = task2.result()

    x, y = current_loc[0], current_loc[1]
    from_loc = f"{str(x)}, {str(y)}"

    await task1

    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#bnp_btn_accept"))).click()
    # 3 seconds --> 3000 miliseconds

    button = driver.find_element_by_css_selector(".directionsIcon")
    driver.execute_script("arguments[0].click();", button)

    start = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".start+ input")))

    ActionChains(driver).move_to_element(start)
    start.send_keys(from_loc)

    go_btn = driver.find_element_by_class_name("dirBtnGo.commonButton")
    go_btn.click()
    time_minutes = None
    time_hours = None
    while time_hours is None:
        try:
            time_hours = driver.find_element_by_class_name('drHours')
            time_minutes = driver.find_element_by_class_name('drMins')
        except selenium.common.exceptions.NoSuchElementException:
            pass

    if time_hours.text == "":
        travel_time = f"{time_minutes.text} min"
    else:
        travel_time = f"{time_hours.text} h: {time_minutes.text} min"

    end = time.time()

    print("Distance_to_stadium is :",
          (end - start_time) * 10 ** 3, "ms")

    return travel_time


asyncio.run(sync_funcs(
    'https://www.bing.com/maps?q=+Stadion+Bistritsa%2C+1+ulitsa+Sportist%2C+Pancharevo%2C+Bulgaria'))

# Conculsion -> both methods equally as (in)effective
