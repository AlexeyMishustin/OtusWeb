from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains as AC


class Test_MainPage:

    def test_CheckMainPage(self, browser):
        browser.get("http://192.168.1.147:8081/en-gb?route=common/home")
        WebDriverWait(browser, 1).until(EC.title_is("Your Store"))
        WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#logo")))
        WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#search")))
        WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#header-cart")))
        WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#content")))

    def test_CheckNagivationBar(self, browser):
        browser.get("http://192.168.1.147:8081/en-gb?route=common/home")
        list_item_bar = ["Desktops", "Laptops & Notebooks", "Components", "Tablets", "Software", "Phones & PDAs",
                         "Cameras",
                         "MP3 Players"]
        navigation = WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#menu")))
        for item in list_item_bar:
            navigation.find_element(By.LINK_TEXT, f"{item}")

    def test_OpenCatalog(self, browser):
        browser.get("http://192.168.1.147:8081/en-gb?route=common/home")
        WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#narbar-menu")))
        AC(browser).move_to_element(browser.find_element(By.LINK_TEXT, "Desktops")).perform()
        AC(browser).move_to_element(browser.find_element(By.LINK_TEXT, "Show All Desktops")).click().perform()
