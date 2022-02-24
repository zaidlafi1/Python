from seleniumbase import BaseCase
import random

s = random.randint(1, 20)


class MyTestClass(BaseCase):
    def test_basics(self):
        url = "https://zaid.elevatus.io/jobs"
        email = 'z.lafi@elevatus.io'
        self.open(url)
        self.maximize_window()
        self.click('/html/body/div[3]/div/div[2]/div[2]/i')  # click on the X button
        self.click('//*[@id="__next"]/div[4]/div/div/div/div/a[' + str(s) + ']')  # click on View
        self.assert_text("Description", '//*[@id="__next"]/div[3]/div/div[2]/div/div[2]/h5')
        self.assert_text("Requirements", '//*[@id="__next"]/div[3]/div/div[2]/div/div[3]/h5')
        self.assert_no_404_errors()
        self.assert_no_js_errors()
        self.assert_element('//*[@id="__next"]/div[3]/div/div[2]/div/div[6]/div')
        self.click('//*[@id="__next"]/div[3]/div/div[2]/div/div[6]/button')
        self.sleep(4)




        '''
        self.click('//*[@id="__next"]/div[3]/div/div[2]/div/div[6]/button')  # click on apply
        self.sleep(2)
        self.click('// *[ @ id = "__next"] / div / div / div / div[2] / div / a')  # already have an email button
        self.sleep(2)
        self.type('input[name="email"]', email)
        self.type('input[name="password"]', "Zaid123123$")
        self.click('//*[@id="__next"]/div/div/div/div[1]/div/form/div[4]/button')  # already have an email button
        self.click('//*[@id="__next"]/div[3]/div/div[2]/div/div[6]/button')
        self.assert_text('// *[ @ id = "__next"] / div[3] / div / div[2] / div / div[6] / button')
        self.sleep(2)
        # self.assert_title("xkcd: Python")
        # self.assert_element('img[alt="Python"]')
        # self.click('a[rel="license"]')
        # self.assert_text("free to copy and reuse")
        # self.go_back()
        # self.click_link("About")
        # self.assert_exact_text("xkcd.com", "h2")
        '''
