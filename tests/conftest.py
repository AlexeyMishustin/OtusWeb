import time,logging

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options



@pytest.fixture()
def parser(request):
    return request.config.getoption


def pytest_addoption(parser):
    parser.addoption("--url", help="set url browser", default="http://localhost:8081/")
    parser.addoption("--browser", choices=["edge", "chrome"], help="set browser", default="chrome")
    parser.addoption("--level_log", choices=["info","debug","warning","error","critical"],default="DEBUG")

@pytest.fixture()
def browser_dynamic(parser):
    browser_name = parser("--browser")
    url = parser("--url")
    options = Options()
    if browser_name == "edge":
        options.binary_location = 'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
        browser = webdriver.Edge(service=Service(),options=options)
    elif browser_name == "chrome":
        browser = webdriver.Chrome(service=Service(), options=options)
    else:
        raise ValueError(f"Browser {browser_name} not used")
    browser.get(f"{url}")
    yield browser
    browser.close()

@pytest.fixture()
def browser(parser,request):
    browser_name = parser("--browser")

    level_log = parser("--level_log")
    logger = logging.getLogger(request.node.name)
    file_handler = logging.FileHandler(f"../logs/{request.node.name}.log")
    file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(message)s'))
    logger.addHandler(file_handler)
    logger.setLevel(level=f"{level_log}")

    logger.info("config browser start")
    options = Options()
    if browser_name == "edge":
        options.binary_location = 'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
        browser = webdriver.Edge(service=Service(),options=options)
    elif browser_name == "chrome":
        browser = webdriver.Chrome(service=Service(), options=options)
    else:
        raise ValueError(f"Browser {browser_name} not used")
    browser.get("http://192.168.1.147:8081/en-gb?route=common/home")
    browser.logger = logger

    logger.info("browser start")

    yield browser
    browser.close()

