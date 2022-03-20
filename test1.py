from seleniumbase import BaseCase
import random

s = random.randint(1, 20)


class MyTestClass(BaseCase):
    def test_test1(self):
        url = "https://zaid.elevatus.io/jobs"
        email = 'z.lafi@elevatus.io'
        self.open(url)
        self.maximize_window()
        self.click('/html/body/div[3]/div/div[2]/div[2]/i')  # click on the X button
        self.click('//*[@id="__next"]/div[4]/div/div/div/div/a[' + str(s) + ']')  # click on View
        self.assert_text("Description", '//*[@id="__next"]/div[3]/div/div[2]/div/div[2]/h5')
        self.assert_text("Requirements", '//*[@id="__next"]/div[3]/div/div[2]/div/div[3]/h5')
        self.assert_element('//*[@id="__next"]/div[3]/div/div[2]/div/div[6]/div')
        self.execute_script('jQuery, window.scrollTo(0, 600)')
        self.click('//*[@id="__next"]/div[3]/div/div[2]/div/div[6]/button')
        self.click('//*[@id="__next"]/div/div/div/div[2]/div/a')

        self.sleep(4)
