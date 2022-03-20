import pytest
from seleniumbase import BaseCase
import random
from selenium.webdriver.common.keys import Keys


class login(BaseCase):
    def test_test2(self):
        self.click('/html/body/div[3]/div/div[2]/div[2]/i')
        self.type('input[name="email"]', 'z.lafi+364658602@elevatus.io')
        self.type('input[name="password"]', 'Zaid123123$')
        self.click('button[type="submit"')
        self.sleep(5)

