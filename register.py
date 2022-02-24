import pytest
from seleniumbase import BaseCase
import random


class register(BaseCase):

    def test_register(self):
        n = random.randint(0, 1000000000)
        url = "https://bbrnach.elevatustesting.xyz/register"
        email = 'z.lafi+' + str(n) + '@elevatus.io'
        self.open(url)
        self.maximize_window()
        self.click('/html/body/div[3]/div/div[2]/div[2]/i')  # click on the X button
        self.type('input[name="firstName"]', "love u")
        self.type('input[name="lastName"]', "last name")
        self.type('input[name="email"]', email)
        self.type('input[name="password"]', "Zaid123123$")
        # self.type('input[name="confirmPassword"]', "Zaid123123$")
        self.type('input[name="phoneNumber"]', "0708986489")
        # self.click('//*[@id="__next"]/div/div/div/div[1]/div/form/div[7]')
        # self.click('//*[@id="__next"]/div/div/div/div[1]/div/form/div[8]/button')
        # self.sleep(5)

    def test_Open_Email(self):
        url = "https://mail.google.com/mail/u/0/#inbox"
        email = 'z.lafi@elevatus.io'
        '''
       n = random.randint(0, 100000)
       print(n)
       '''
        self.open(url)
        self.type("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div["
                  "1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input", email)
        self.click('//*[@id="identifierNext"]')
        self.type('input[name="password"]', "zaid lafi5212014")
        self.click('//*[@id="passwordNext"]/div/button')
        # self.sleep(10)


