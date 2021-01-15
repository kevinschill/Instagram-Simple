import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

import random

class Instabot():
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.browser = webdriver.Chrome("./chromedriver.exe")     

    def WaitForObject(self, type, string):
        try:
            return WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((type, string)))
        except Exception as _error:
            return False

    def WaitForObjectData(self, dataset, type, string):
        try:
            return WebDriverWait(dataset, 5).until(EC.presence_of_element_located((type, string)))
        except Exception as _error:
            return False

    def WaitForObjects(self, type, string):
        try:
            return WebDriverWait(self.browser, 5).until(EC.presence_of_all_elements_located((type, string)))
        except Exception as _error:
            return False

    def login(self):
        self.browser.get("https://www.instagram.com/accounts/login")

        cookies_accept_button = self.WaitForObject(
            By.CLASS_NAME, "aOOlW.bIiDR")

        if cookies_accept_button != False:
            cookies_accept_button.click()

        login_objects = self.WaitForObjects(
            By.CSS_SELECTOR, "input._2hvTZ.pexuQ.zyHYP")

        if login_objects != False:

            login_objects[0].send_keys(self.username)
            login_objects[1].send_keys(self.password)
            login_objects[1].send_keys(Keys.ENTER)

            _wait_for_loading_login_info = self.WaitForObject(
                By.CLASS_NAME, "coreSpriteKeyhole")

            login_info_save_button = self.WaitForObject(
                By.CSS_SELECTOR, "button.sqdOP.yWX7d.y3zKF")

            if login_info_save_button != False:
                login_info_save_button.click()

            notification_info_button = self.WaitForObject(
                By.CSS_SELECTOR, "button.aOOlW.HoLwm")

            if notification_info_button != False:
                notification_info_button.click()

            
            return True

    def SearchHashtag(self,hashtag):
        search_bar = self.WaitForObject(By.CLASS_NAME,"XTCLo.x3qfX")
        if search_bar != False:
            search_bar.send_keys(hashtag)

            search_results = self.WaitForObjects(By.CLASS_NAME,"z556c")
            if search_results != False:
                search_results[0].click()

                return True
        
        return False
    
    def Like(self):
        like_button_div = self.WaitForObject(By.CLASS_NAME,"fr66n")
        if like_button_div != False:
            like_button_x = self.WaitForObjectData(like_button_div, By.CLASS_NAME,"wpO6b")
            if like_button_x != False:
                like_button_x.click()

                return True
        return False

    def Comment(self):
        comment_button = self.WaitForObject(By.CSS_SELECTOR, "[aria-label='Kommentar']")
        if comment_button != False:
            comment_button.click()

            comment_text_box = self.WaitForObject(By.CLASS_NAME,"Ypffh.focus-visible")

            if comment_text_box != False:
                comment_text_box.send_keys("Nice ! Keep going :D")
                comment_text_box.send_keys(Keys.ENTER)

                return True
        
        return False
    
    def ClosePopupPhotoWindow(self):
        close_window = self.WaitForObject(By.CSS_SELECTOR, "[aria-label='Schließen']")
        if close_window != False:
            close_window.click()

    def FollowProfile(self):
        abo_buttons = self.WaitForObjects(By.CLASS_NAME,"sqdOP.yWX7d.y3zKF")
        if abo_buttons != False:
            abo_buttons[0].click()

            return True
        
        return False
        
    def collect_photos(self):
        photos_on_page = self.WaitForObjects(By.CSS_SELECTOR, "div.v1Nh3.kIKUG._bz0w")

        if photos_on_page != False:
            for photo in photos_on_page:
                photo.click()
                time.sleep(2)
                
                self.Like()
                
                time.sleep(random.randint(2,10))
                self.Comment()
                time.sleep(random.randint(2,6))
                self.ClosePopupPhotoWindow()

                time.sleep(random.randint(10,30))
                


bot = Instabot("Username" , " Password")

if bot.login() == True:
    if bot.SearchHashtag('#coding') == True:
        bot.collect_photos()
