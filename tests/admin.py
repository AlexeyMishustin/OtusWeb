from selenium.webdriver.common.by import By
class TestAdmin:
    def test_check_exists_element(self, browser):
        browser.get("http://192.168.1.147:8081/administration/")
        browser.find_element(By.CSS_SELECTOR, "#header")
        browser.find_element(By.CSS_SELECTOR, "#content")
        browser.find_element(By.CSS_SELECTOR, "#footer")

    def test_set_user_name(self, browser):
        browser.get("http://192.168.1.147:8081/administration/")
        browser.find_element(By.CSS_SELECTOR, "#input-username").send_keys("admin")

    def test_set_password(self, browser):
        browser.get("http://192.168.1.147:8081/administration/")
        browser.find_element(By.CSS_SELECTOR, "#input-username").send_keys("1234")

    def test_check_enabled_button(self, browser):
        browser.get("http://192.168.1.147:8081/administration/")
        browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary").is_enabled()

    def test_check_title(self, browser):
        browser.get("http://192.168.1.147:8081/administration/")
        assert browser.title == "Administration"