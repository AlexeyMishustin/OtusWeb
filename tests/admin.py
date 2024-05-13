from selenium.webdriver.common.by import By
class TestAdmin:
    def test_CheckExistsElement(self, browser):
        browser.get("http://192.168.1.147:8081/administration/")
        browser.find_element(By.CSS_SELECTOR, "#header")
        browser.find_element(By.CSS_SELECTOR, "#content")
        browser.find_element(By.CSS_SELECTOR, "#footer")

    def test_SetUserName(self, browser):
        browser.get("http://192.168.1.147:8081/administration/")
        browser.find_element(By.CSS_SELECTOR, "#input-username").send_keys("admin")

    def test_SetPassword(self, browser):
        browser.get("http://192.168.1.147:8081/administration/")
        browser.find_element(By.CSS_SELECTOR, "#input-username").send_keys("1234")

    def test_CheckEnabledButton(self, browser):
        browser.get("http://192.168.1.147:8081/administration/")
        browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary").is_enabled()

    def test_CheckTitle(self, browser):
        browser.get("http://192.168.1.147:8081/administration/")
        assert browser.title == "Administration"