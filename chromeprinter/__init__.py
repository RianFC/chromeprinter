import time
from selenium import webdriver  
from selenium.webdriver.chrome.options import Options
from PIL import Image

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
        time.sleep(3)
        driver.save_screenshot(output)
        driver.close()

    def make_google(self, query):
        driver = webdriver.Chrome(
            executable_path=self.chromedr,
            chrome_options=self.chrome_options
            )
        driver.get('https://www.google.com/search?q='+query)
        S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
        driver.set_window_size(1080+S('Width'),720+S('Height'))
        element = driver.find_element_by_xpath('/html/body/div[5]/div[2]/div[9]/div[1]/div[2]/div/div[2]/div[2]/div/div/div[1]')
        location = element.location
        size = element.size
        ctime = time.time()
        driver.save_screenshot(f"{ctime}.png")

        x = location['x']
        y = location['y']
        width = location['x']+size['width']
        height = location['y']+size['height']
        im = Image.open(f"{ctime}.png")
        im = im.crop((int(x), int(y), int(width), int(height)))
        im.save(f"{ctime}.png")

        driver.quit()
        
        return f"{ctime}.png"
