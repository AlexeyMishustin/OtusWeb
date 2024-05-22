import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    def __init__(self, browser):
        self.browser = browser

    def add_to_list_product(self):
        elements_product = self.browser.find_element(By.CSS_SELECTOR, "#content").find_element(By.CSS_SELECTOR,
                                                                                               ".row.row-cols-1.row-cols-sm-2.row-cols-md-3.row-cols-xl-4").find_elements(
            By.CSS_SELECTOR, ".col.mb-3")
        random_element = random.choice(elements_product)
        random_element.find_element(By.CSS_SELECTOR, ".button-group").find_element(By.CSS_SELECTOR,
                                                                                   ".fa-solid.fa-shopping-cart").click()

    def wait_alert_success(self):
        WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible")))
