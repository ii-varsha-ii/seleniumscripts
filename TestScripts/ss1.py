import json

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

EXECUTABLE_PATH = "C:\geckodriver.exe"
FIREFOX_USER_DATA = r'C:\Users\sreya\AppData\Roaming\Mozilla\Firefox\Profiles\69sjgy2p.'
PROFILE = "Profile1"


class LoginTestSection:
    def __init__(self):
        self.options = webdriver.FirefoxOptions()
        self.options.add_argument(fr'--user-data-dir={FIREFOX_USER_DATA}')
        self.options.add_argument(fr'--profile-directory={PROFILE}')
        self.driver = webdriver.Firefox(executable_path=EXECUTABLE_PATH, options=self.options)
        self.wait = WebDriverWait(self.driver, 10)

    def connect_with_url(self, url: str):
        self.driver.maximize_window()
        self.driver.get(url)
        return self

    def enter_credentials(self, userid: str, password: str):
        login_element = self.driver.find_element(by=By.NAME, value="uid")
        login_element.send_keys(userid)

        pass_element = self.driver.find_element(by=By.NAME, value="password")
        pass_element.send_keys(password)

        submit_btn = self.driver.find_element(by=By.XPATH, value="/html/body/form/table/tbody/tr[3]/td[2]/input[1]")
        submit_btn.click()
        return self

    def validate_results(self, userid: str):
        try:
            if self.wait.until(EC.alert_is_present()) is not None:
                alert_text = self.driver.switch_to.alert.text
                print(alert_text)
                print("Login Failed")
        except TimeoutException:
            name_element = self.driver.find_element(By.XPATH, "/html/body/table/tbody/tr/td/table/tbody/tr[3]/td")
            assert name_element.text == f"Manger Id : {userid}"
            print("Login Successful")
        self.driver.quit()


def handlers():
    with open('utils.json') as f:
        data = json.loads(f.read())
        for item in data:
            URL = item['URL']
            userid = item['userid']
            password = item['password']
            LoginTestSection().connect_with_url(URL).enter_credentials(userid=userid,
                                                                       password=password).validate_results(
                userid)


if __name__ == '__main__':
    handlers()
