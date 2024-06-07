from selenium import webdriver
from selenium.webdriver.common.by import By
from pprint import pprint
from selenium.webdriver.common.keys import Keys
import time
import os

# Declare Constants
SIMILAR_ACCOUNT = os.environ.get("Acct")
USERNAME = os.environ.get("PHn_no")
PASSWORD = os.environ.get("passwrd") 


class InstaFollower:
    def __init__(self):
        # Create webdriver specifically for chrome
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(self.chrome_options)

    def login(self):
        # Open instagram in chrome
        self.driver.get(url="https://www.instagram.com/accounts/login/")
        time.sleep(2)

        # Input username and password
        username_entry = self.driver.find_element(By.NAME, value="username")
        print("username")
        print(username_entry.get_attribute("outerHTML"))
        print(username_entry.get_attribute("innerHTML"))
        username_entry.send_keys(USERNAME)
        password_entry = self.driver.find_element(By.NAME, value="password")
        print("password")
        print(password_entry.get_attribute("outerHTML"))
        print(password_entry.get_attribute("innerHTML"))
        password_entry.send_keys(PASSWORD)

        # Click login button
        login_button = self.driver.find_element(By.XPATH, value="//*[text() = 'Log in']")
        print("login_button")
        print(login_button.get_attribute("outerHTML"))
        print(login_button.get_attribute("innerHTML"))
        login_button.click()
        time.sleep(10)

        # Discard pop ups
        save_not = self.driver.find_element(By.XPATH, value="//*[text() = 'Not Now']")
        save_not.click()
        time.sleep(5)
        save_not = self.driver.find_element(By.XPATH, value="//*[text() = 'Not Now']")
        save_not.click()

    def find_followers(self):
        ff = 0
        time.sleep(2)
        # Go to sample account
        self.driver.get(url="https://www.instagram.com/python.hub/")
        time.sleep(4)

        # Open followers list
        follow_button = self.driver.find_element(By.XPATH, value="//*[contains(text(), 'followers')]")
        follow_button.click()
        time.sleep(4)
        pop_up_window = self.driver.find_element(By.XPATH, value="//*[@class='_aano']")
        while ff < 50:
            self.driver.execute_script(
                'arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;',
                pop_up_window)
            ff += 4

    def follow(self):
        pop_up_window = self.driver.find_element(By.XPATH, value="//*[@class='_aano']")
        # btns = pop_up_window.find_elements(By.TAG_NAME, value="button")
        # for index in range(3):
        #     btns[index].click()

        # Follow all displayed followers in followers list
        btn = self.driver.find_element(By.CLASS_NAME, value="_abl-")
        btn.click()
        profile = self.driver.find_element(By.XPATH, value="//*[@href='/ebifred_emma/']")
        profile.click()




insta_bot = InstaFollower()
insta_bot.login()
insta_bot.find_followers()
insta_bot.follow()
