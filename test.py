import pytest
from seleniumbase import BaseCase
import random
from selenium.webdriver.common.keys import Keys

n = random.randint(0, 1000000000)
email = 'z.lafi+' + str(n) + '@elevatus.io'
password = 'Zaid123123$'


class register(BaseCase):

    @pytest.mark.run(order=1)
    def test_register(self):
        n = random.randint(0, 1000000000)
        url = "https://salahat.elevatustesting.xyz/register"

        self.open(url)
        self.maximize_window()
        self.click('/html/body/div[3]/div/div[2]/div[2]/i')  # click on the X button
        self.type('input[name="firstName"]', "love u")
        self.type('input[name="lastName"]', "last name")
        self.type('input[name="email"]', email)
        self.type('input[name="password"]', "Zaid123123$")
        self.type('input[name="confirmPassword"]', password)
        self.type('input[name="phoneNumber"]', "0708986489")
        self.click('//*[@id="__next"]/div/div/div/div[1]/div/form/div[7]/label')
        self.click('//*[@id="__next"]/div/div/div/div[1]/div/form/div[8]/button')
        self.sleep(5)

    @pytest.mark.run(order=2)
    def test_Open_Email(self):
        url = "https://mail.google.com/mail/u/0/#inbox"
        email = 'z.lafi@elevatus.io'
        '''
       n = random.randint(0, 100000)
       print(n)
       '''
        self.open(url)
        self.maximize_window()
        self.type("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div["
                  "1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input", email)
        self.click('//*[@id="identifierNext"]')
        self.type('input[name="password"]', "zaid lafi5212014")
        self.click('//*[@id="passwordNext"]/div/button')
        self.click('//*[@id=":1l"]')
        self.click_link('Click Here')
        self.switch_to_default_window()
        self.click_link('Inbox')
        self.click('//*[@id=":1l"]')
        self.hover_and_click('#\:4 > div:nth-child(2) > div.iH.bzn > div > div:nth-child(2)',
                             '//*[@id=":4"]/div[2]/div[1]/div/div[2]/div[3]/div')  # delete the email
        self.sleep(3)

    @pytest.mark.run(order=3)
    def test_login(self):
        url = 'https://salahat.elevatustesting.xyz/login'
        self.open(url)
        self.maximize_window()
        self.click('/html/body/div[3]/div/div[2]/div[2]/i')
        self.type('input[name="email"]', 'z.lafi+364658602@elevatus.io')
        self.type('input[name="password"]', password)
        self.click('button[type="submit"')
        self.sleep(5)

    def test_apply(self):
        self.test_login()
        self.assert_text('Signed In!', '/html/body/div[2]/div/div/div[2]')
        self.click('//*[@id="__next"]/div/div/div/div/div[2]/div[1]/div')
        z = 3
        for i in range(0, z):
            self.find_element('//*[@id="tags-outlined"]').send_keys(Keys.ARROW_DOWN)
            if z == 3:
                self.find_element('//*[@id="tags-outlined"]').send_keys(Keys.ENTER)
        self.click('//*[@id="__next"]/div/div/div/div/div[2]/div[2]/button')
        self.click('//*[@id="__next"]/div/div/div/div/div[2]/div[3]/button')
        self.assert_no_js_errors()
        self.sleep(6)
        '''
        self.find_element('//*[@id="tags-outlined"]').send_keys(Keys.ARROW_DOWN + Keys.ENTER)
        self.click('//*[@id="__next"]/div/div/div/div/div[2]/div[2]/button')
        self.click('//*[@id="__next"]/div/div/div/div/div[2]/div[3]/button')
        self.sleep(20)
        self.type('//*[@id="description"]', 'Hello world ')
        self.click('//*[@id="education"]/div[2]')
        self.type('//*[@id="education"]/div[2]/div/div/div[1]/div[1]/div/div/fieldset', 'zaidtest')
        self.click('//*[@id="education"]/div[2]/div/div/div[1]/div[2]/div/div/div')
        #  self.find_element('//*[@id="education"]/div[2]/div/div/div[1]/div[2]/div/div/div').send_keys(Keys.ARROW_DOWN + Keys.ENTER)

        self.sleep(6)dsdsd
        '''