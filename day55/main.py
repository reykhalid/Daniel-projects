from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import pandas as pd
import time



options = Options()

options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=options)
driver.get("https://www.thenetnaija.net/music/afro")
musics = driver.find_elements(By.XPATH, "//a/span[text()='Nigerian / African Music']")
driver.maximize_window()
for music in musics:
    print(music.text) 