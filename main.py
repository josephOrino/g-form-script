import math
import random
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

chrome_driver_path = "C:/Program Files/chromedriver-win64/chromedriver.exe"
service = Service(executable_path=chrome_driver_path)

url = "https://docs.google.com/forms/d/e/1FAIpQLSc7ppW4rjfa-URUHutPo4snjbqPO0xPw7QE2n32v0w528vK0g/viewform"

driver = webdriver.Chrome(service=service)
driver.get(url)

time.sleep(2)  # Wait for the form to load


def fill_form(name, raffle_ticket, contact, address):
    inputs = driver.find_elements(By.CLASS_NAME, "whsOnd")

    time.sleep(2)

    inputs[0].clear()
    inputs[0].send_keys(name)

    inputs[1].clear()
    inputs[1].send_keys(raffle_ticket)

    inputs[2].clear()
    inputs[2].send_keys(contact)

    inputs = driver.find_elements(By.CLASS_NAME, "KHxj8b")

    inputs[0].clear()
    inputs[0].send_keys(address)

    wait = WebDriverWait(driver, 10)

    # === STEP 1: CLICK THE DROPDOWN ===
    dropdown_box = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@role="listbox"]')))
    dropdown_box.click()
    time.sleep(1)  # let it open

    # === STEP 2: SELECT THE DESIRED OPTION ===
    # DEFAULT_BRANCH = "Brgy. Minante 1, Cauayan City"
    option_xpath = "//*[@id=\"mG61Hd\"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[2]/div[6]"
    option = wait.until(EC.element_to_be_clickable((By.XPATH, option_xpath)))
    option.click()

    time.sleep(2)
    submit_xpath = "//*[@id=\"mG61Hd\"]/div[2]/div/div[3]/div[1]/div[1]/div/span"
    submit = driver.find_element(By.XPATH, submit_xpath)
    submit.click()
    print("Finished Ticket: ", raffle_ticket)

    time.sleep(math.floor(random.random() * 20) + 2)
    submit_another_xpath = "/html/body/div[1]/div[2]/div[1]/div/div[4]/a"
    submit_another = driver.find_element(By.XPATH, submit_another_xpath)
    submit_another.click()


# Enter here the details
name = "Cristy B. Oriño"
raffle_ticket = ("164658-164664, 036932-036941, 076621-076632, 115273-115287, 014303-014312, 044034-044044, "
                 "164719-164723, 140751-140759")
contact = "09756575316"
address = "Purok 5, Pinoma, Cauayan City, Isabela"

raffle_tickets = raffle_ticket.split(", ")
all_raffle_tickets = []

for i in raffle_tickets:
    temp = i.split("-")
    if len(temp) == 1:
        all_raffle_tickets.append(temp[0])
    else:
        x = int(temp[0])
        y = int(temp[1])
        if len(str(x)) == 5:
            while x <= y:
                all_raffle_tickets.append("0" + str(x))
                x += 1
        else:
            while x <= y:
                all_raffle_tickets.append(str(x))
                x += 1

for raffle in all_raffle_tickets:
    fill_form(name, raffle, contact, address)

input("Press Enter to close...")
