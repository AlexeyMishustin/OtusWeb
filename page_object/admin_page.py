from faker import Faker
import random

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AdminPage:
    def __init__(self, browser):
        self.browser = browser
        self.fake = Faker()

    def login_for_admin(self, login, password):
        self.browser.find_element(By.CSS_SELECTOR, "#input-username").send_keys(f"{login}")
        self.browser.find_element(By.CSS_SELECTOR, "#input-password").send_keys(f"{password}")
        self.browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()



    def open_catalog_product(self):
        self.browser.find_element(By.CSS_SELECTOR, "#menu-catalog").click()

        WebDriverWait(self.browser, timeout=3).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"#collapse-1")))
        self.browser.find_element(By.CSS_SELECTOR, "#menu-catalog").find_element(By.CSS_SELECTOR,"#collapse-1").find_element(By.CSS_SELECTOR, "li:nth-child(2)").click()


    def add_product(self):
        self.browser.find_element(By.CSS_SELECTOR,"#content > div.page-header > div > div > a").click()
        self.browser.find_element(By.CSS_SELECTOR,"#input-name-1").send_keys(f"{self.fake.text(max_nb_chars=20)}")
        self.browser.find_element(By.CSS_SELECTOR, "#input-meta-title-1").send_keys(f"{self.fake.name()}")
        self.browser.find_element(By.CSS_SELECTOR, "#form-product > ul > li:nth-child(2)").click()
        self.browser.find_element(By.CSS_SELECTOR, "#input-model").send_keys(f"{self.fake.text(max_nb_chars=20)}")
        self.browser.find_element(By.CSS_SELECTOR, "#form-product > ul > li:nth-child(11) > a").click()
        self.browser.find_element(By.CSS_SELECTOR, "#input-keyword-0-1").send_keys(f"{self.fake.random_int(1,100)}")
        self.browser.find_element(By.CSS_SELECTOR, "#content > div.page-header > div > div > button").click()


    def use_filter_price(self):
        self.browser.find_element(By.CSS_SELECTOR, "#input-price").send_keys("0.00")
        self.browser.find_element(By.CSS_SELECTOR, "#button-filter").click()


    def del_element(self):
        random_element = self.get_random_product()
        random_element.find_element(By.CSS_SELECTOR, ".form-check-input").click()
        self.browser.find_element(By.CSS_SELECTOR, "#content").find_element(By.CSS_SELECTOR, "button.btn.btn-danger").click()



    def get_random_product(self):
        return random.choice(self.browser.find_element(By.CSS_SELECTOR, "#product").find_element(By.CSS_SELECTOR, "tbody").find_elements(By.CSS_SELECTOR, "tr"))


