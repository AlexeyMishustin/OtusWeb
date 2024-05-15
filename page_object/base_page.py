from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def get_value_first_price(self):
        return self.browser.find_element(By.CSS_SELECTOR, '.price-new').text

    def set_currency_for_euro(self, value):
        AC(self.browser).move_to_element(self.browser.find_element(By.CSS_SELECTOR, ".dropdown")).click().perform()
        AC(self.browser).move_to_element(self.browser.find_element(By.LINK_TEXT, f"{value}")).click().perform()

    def wait_load_title(self, timeout, title_name):
        WebDriverWait(self.browser, timeout=timeout).until(EC.title_is(f"{title_name}"))

    def switch_and_accept_alert(self):
        self.alert = self.browser.switch_to.alert
        self.alert.accept()

    def set_new_window(self, title):
        self.browser.switch_to.window(self.browser.window_handles[0])
        WebDriverWait(self.browser, timeout=3).until(EC.title_is(f"{title}"))
