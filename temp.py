from selenium import webdriver
from selenium.webdriver.common.by import By
from pprint import pprint
from selenium.webdriver.common.keys import Keys
import time
import os

SIMILAR_ACCOUNT = os.environ.get("Acct")  #"python.hub"
USERNAME = os.environ.get("PHn_no")  #"07016988225"
PASSWORD = os.environ.get("passwrd")  #"Ibrahim sherifat169"


class InstaFollower:
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(self.chrome_options)

    def login(self):
        self.driver.get(url="https://www.instagram.com/accounts/login/")
        time.sleep(4)
        login_facebook = self.driver.find_element(By.XPATH, value="//*[text() = 'Log in with Facebook']")
        login_facebook.click()
        time.sleep(3)
        email_entry = self.driver.find_element(By.ID, value="email")
        email_entry.send_keys(USERNAME)
        password_entry = self.driver.find_element(By.ID, value="pass")
        password_entry.send_keys(PASSWORD)
        login_button = self.driver.find_element(By.XPATH, value="//*[text() = 'Log in']")
        login_button.click()
        time.sleep(3)
        otp = "none"
        while otp == "none":
            self.driver.find_element(By.LINK_TEXT, value="Didn't receive a code?").click()
            time.sleep(2)
            self.driver.find_element(By.LINK_TEXT, value="Text me a login code").click()
            self.driver.find_element(By.XPATH, value="//*[@title='Close']").click()
            otp = input("Input the one-time-password sent to your mobile device: ")

        # Escape two factor authentication
        otp_entry = self.driver.find_element(By.XPATH, value="//*[@name='approvals_code']")
        otp_entry.send_keys(otp)
        submit_button = self.driver.find_element(By.ID, value="checkpointSubmitButton")
        submit_button.click()
        time.sleep(2)
        save_button = self.driver.find_element(By.ID, value="checkpointSubmitButton").click()
    #     time.sleep(10)
    #     save_not = self.driver.find_element(By.XPATH, value="//*[text() = 'Not Now']")
    #     save_not.click()
    #     time.sleep(5)
    #     save_not = self.driver.find_element(By.XPATH, value="//*[text() = 'Not Now']")
    #     save_not.click()
    #
    # def find_followers(self):
    #     ff = 0
    #     time.sleep(2)
    #     self.driver.get(url="https://www.instagram.com/python.hub/")
    #     time.sleep(4)
    #     follow_button = self.driver.find_element(By.XPATH, value="//*[contains(text(), 'followers')]")
    #     follow_button.click()
    #     time.sleep(4)
    #     pop_up_window = self.driver.find_element(By.XPATH, value="//*[@class='_aano']")
    #     while ff < 50:
    #         self.driver.execute_script(
    #             'arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;',
    #             pop_up_window)
    #         ff += 4
    #
    # def follow(self):
    #     pop_up_window = self.driver.find_element(By.XPATH, value="//*[@class='_aano']")
    #     # btns = pop_up_window.find_elements(By.TAG_NAME, value="button")
    #     # for index in range(50):
    #     #     btns[index].click()
    #     btn = self.driver.find_element(By.CLASS_NAME, value="_abl-")
    #     btn.click()
    #     profile = self.driver.find_element(By.XPATH, value="//*[@href='/ebifred_emma/']")
    #     profile.click()




insta_bot = InstaFollower()
insta_bot.login()
# insta_bot.find_followers()
# insta_bot.follow()
