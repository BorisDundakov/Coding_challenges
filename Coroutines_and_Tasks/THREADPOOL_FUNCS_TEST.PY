import geocoder
import time

import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from concurrent.futures import ThreadPoolExecutor


def get_my_location():
    myloc = geocoder.ip('me')
    current_loc = myloc.latlng
    return current_loc


def chromedriver_setup(url):
    # TODO: This is very time consuming

    PATH = "C:\Program Files (x86)\chromedriver.exe"  # PATH TO THE chromedriver.exe downloaded (check requirements.txt)
    op = webdriver.ChromeOptions()
    op.add_argument('headless')
    driver = webdriver.Chrome(PATH, options=op)
    driver.get(url)
    return driver


def distance_to_stadium(bing_address):
    start_time = time.time()

    with ThreadPoolExecutor(max_workers=10) as executor:
        driver = executor.submit(chromedriver_setup, bing_address).result()
        current_loc = executor.submit(get_my_location)

    # Using Selenium
    # ACCEPTING COOKIES
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#bnp_btn_accept"))).click()
    # 3 seconds --> 3000 miliseconds

    button = driver.find_element_by_css_selector(".directionsIcon")
    driver.execute_script("arguments[0].click();", button)

    start = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".start+ input")))

    x, y = current_loc.result()
    from_loc = f"{str(x)}, {str(y)}"

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


distance_to_stadium('https://www.bing.com/maps?q=+Stadion+Bistritsa%2C+1+ulitsa+Sportist%2C+Pancharevo%2C+Bulgaria')
