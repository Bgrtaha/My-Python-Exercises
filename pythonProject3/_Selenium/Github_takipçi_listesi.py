from Github_user_info import username, password
from selenium import webdriver
import time

class Github:
    def __init__(self,username,password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password
        self.followers = []

    def sign_in(self):
        self.browser.get("https://github.com/login")
        time.sleep(1)
        self.browser.maximize_window()
        time.sleep(2)

        self.browser.find_element("xpath","//*[@id='login_field']").send_keys(self.username)
        self.browser.find_element("xpath","//*[@id='password']").send_keys(self.password)
        time.sleep(1)
        self.browser.find_element("xpath", "//*[@id='login']/div[4]/form/div/input[12]").click()
        time.sleep(1)

    def load_followers(self):
        items = self.browser.find_elements("css selector", ".d-table.table-fixed")
        for i in items:
            self.followers.append(i.find_element("css selector", ".Link--secondary").text)

    def get_followers(self):
        self.browser.get("https://github.com/sadikturan")
        time.sleep(2)
        self.browser.find_element("xpath", "//*[@id='js-pjax-container']/div[2]/div/div[1]/div/div[2]/div[2]/div[2]/div[2]/div/a[1]").click()
        time.sleep(1)
        items = self.browser.find_elements("css selector",".d-table.table-fixed")

        for i in items:
            self.followers.append(i.find_element("css selector",".Link--secondary").text)

        while True:
            links = self.browser.find_element("class name", "pagination").find_elements("tag name", "a")

            if len(links) == 1:
                if links[0].text == "Next":
                    links[0].click()
                    time.sleep(1)

                    self.load_followers()

                else:
                    break
            else:
                for link in links:
                    if link.text == "Next":
                        link.click()
                        time.sleep(1)

                        self.load_followers()
                    else:
                        continue

github = Github(username,password)
github.sign_in()
github.get_followers()
print(len(github.followers))
print(github.followers)