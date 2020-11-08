import time
from selenium import webdriver
from PIL import Image
from urllib.parse import quote

class Client():
    def __init__(self):
        options = webdriver.FirefoxOptions()
        options.set_preference("intl.accept_languages", 'pt-br')
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
        driver.get('https://duckduckgo.com/?q='+quote(query))
        S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
        driver.set_window_size(S('Width'),S('Height'))
        a = ['//*[@id="zero_click_wrapper"]/div', '/html/body/div[2]/div[5]/div[3]/div/div[2]', '//*[@id="r1-0"]']
        time.sleep(3)
        for i in a:
            try:
                element = driver.find_element_by_xpath(i)
                break
            except Exception as e:
                print(f'{i}: {e}')
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
