from decouple import config
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


class Lookup:
    def __init__(self, word, letter_arr):
        self.app_key = config('SECRET_DICTIONARY_API_KEY')
        self.word = word
        self.letters = letter_arr

    def check_word_is_in_dictionary(self):
        response = requests.get(f"https://www.dictionaryapi.com/api/v3/references/collegiate/json/{self.word}"
                                f"?key={self.app_key}")
        return True if "meta" in response.json()[0] else False

    def get_longest_possible_word(self):
        driver = self.configure_web_driver()
        driver.get("https://www.dcode.fr/longest-word-solver")
        WebDriverWait(driver, 10).until((EC.presence_of_element_located((By.CLASS_NAME, "css-143z3ww")))).click()
        text_area = WebDriverWait(driver, 10).until((EC.presence_of_element_located((By.ID, "longest_word_letters"))))
        text_area.click()
        text_area.clear()
        text_area.send_keys(self.letters)
        text_area.send_keys(Keys.ENTER)
        longest_word = WebDriverWait(driver, 10).until((EC.presence_of_element_located((By.CLASS_NAME, "result")))).get_attribute("innerHTML")
        return longest_word

    def configure_web_driver(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
        return driver
