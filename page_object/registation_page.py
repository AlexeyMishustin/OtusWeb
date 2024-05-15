from faker import Faker
import random

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class RegistrPage:
    def __init__(self, browser):
        self.browser = browser
        self.fake = Faker()


    def set_data_user(self):
        self.browser.find_element(By.CSS_SELECTOR, "#input-firstname").send_keys(f"{self.fake.first_name()}")
        self.browser.find_element(By.CSS_SELECTOR, "#input-lastname").send_keys(f"{self.fake.last_name()}")
        self.browser.find_element(By.CSS_SELECTOR, "#input-email").send_keys(f"{self.fake.email()}")
        self.browser.find_element(By.CSS_SELECTOR, "#input-password").send_keys(f"{self.fake.password(length=10)}")
        AC(self.browser).move_to_element(self.browser.find_element(By.CSS_SELECTOR, "#form-register").find_element(By.CSS_SELECTOR, ".text-end").find_element(By.CSS_SELECTOR, ".form-check-input")).click().perform()
        self.browser.find_element(By.CSS_SELECTOR, "#form-register").find_element(By.CSS_SELECTOR, "button").click()


    def continue_after_registr(self):
        self.browser.find_element(By.CSS_SELECTOR, "#content > div > a").click()