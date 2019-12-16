from time import sleep
from selenium import webdriver  
from selenium.webdriver.chrome.options import Options

class Client():
    def __init__(self,CHROME_PATH='/usr/bin/google-chrome',CHROMEDRIVER_PATH='/usr/bin/chromedriver',WINDOW_SIZE = "1280,720"):
        self.chromedr = CHROMEDRIVER_PATH
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--hide-scrollbars")
        chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
        chrome_options.binary_location = CHROME_PATH
        self.chrome_options = chrome_options

    def make_screenshot(self,url, output):
        driver = webdriver.Chrome(
            executable_path=self.chromedr,
            chrome_options=self.chrome_options
            )
        driver.get(url)
        sleep(3)
        driver.save_screenshot(output)
        driver.close()