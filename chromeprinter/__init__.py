import time
from selenium import webdriver
from PIL import Image

class Client():
    def __init__(self):
        options = webdriver.FirefoxOptions()
        options.add_argument('lang=pt-br')
        options.headless = True
        self.driver = webdriver.Firefox(
            firefox_options=options)

    def make_screenshot(self,url, output):
        driver = self.driver
        driver.get(url)
        time.sleep(3)
        driver.save_screenshot(output)
        driver.close()

    def make_google(self, query):
        driver = self.driver
        driver.get('https://www.google.com/search?q='+query)
        S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
        driver.set_window_size(1080+S('Width'),720+S('Height'))
        element = driver.find_element_by_xpath('/html/body/div[7]/div[2]/div[10]/div[1]/div[2]/div/div[2]/div[2]/div/div/div[1]/div[1]')
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
