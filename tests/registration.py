from selenium.webdriver.common.by import By
class TestRegistration:
    def test_CheckExistsElement(self, browser):
        browser.get("http://192.168.1.147:8081/en-gb?route=account/register")
        browser.find_element(By.CSS_SELECTOR, "#top")
        browser.find_element(By.CSS_SELECTOR, "#header-cart")
        browser.find_element(By.CSS_SELECTOR, "#account-register")
        browser.find_elements(By.CSS_SELECTOR, ".container")

    def test_CheckEnabledCheckBox(self, browser):
        browser.get("http://192.168.1.147:8081/en-gb?route=account/register")
        checkbox = browser.find_elements(By.CSS_SELECTOR, ".form-check-input")
        for element in checkbox:
            element.is_enabled()

    def test_CheckNeedWrite(self, browser):
        browser.get("http://192.168.1.147:8081/en-gb?route=account/register")
        check_items = ["input-firstname", "input-lastname", "input-email", "input-password"]
        for element in check_items:
            browser.find_element(By.CSS_SELECTOR, f"#{element}").send_keys("test")
            browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()