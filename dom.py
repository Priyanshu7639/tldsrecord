import time
import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

website="https://instantdomainsearch.com/domain-extensions"
#path="D:\seleniumdrivers"
driver=webdriver.Chrome()
driver.get(website)
driver.implicitly_wait(100)
batch_size=1
with open('output.csv', mode='a', newline='') as output_file:
    writer = csv.writer(output_file)
with open(r'E:\C++\Domain\testbot1.csv', mode='r') as file:
    csv_reader = csv.reader(file)
    # next(csv_reader)

    batch = []

    for i, row in enumerate(csv_reader):
        batch.append(row)
        if len(batch) == batch_size:
            for data_row in batch:
                data_to_enter = data_row[0]
                input_field = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/main[1]/main[1]/section[1]/main[1]/section[1]/div[1]/section[1]/div[1]/form[1]/input[1]")
                input_field.send_keys(Keys.CONTROL + "a")
                input_field.send_keys(Keys.BACKSPACE)
                input_field.send_keys(data_to_enter)
                time.sleep(2)
                tld = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/main[1]/main[1]/section[1]/main[1]/section[2]/div[3]/div[1]/div[1]/span[1]"))).text
        
                tld=driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/main[1]/main[1]/section[1]/main[1]/section[2]/div[3]/div[1]/div[1]/span[1]").text
                print(tld)
                with open('output.csv', mode='a', newline='') as file:
                  writer = csv.writer(file)
                  writer.writerow([data_to_enter, tld])
                  time.sleep(2)
                input_field.send_keys(Keys.CONTROL + "a")  # Select all text
                input_field.send_keys(Keys.BACKSPACE)
                batch=[]



                
                   
                 

            