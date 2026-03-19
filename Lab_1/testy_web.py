import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class webtest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.USOS = "https://login.pwr.edu.pl/auth/realms/pwr.edu.pl/protocol/cas/login?service=https%3A%2F%2Fweb.usos.pwr.edu.pl%2Fkontroler.php%3F_action%3Dlogowaniecas%2Findex%26callback%3DK7YyNrZS0s%252FOzyspys9JLdIryCiwj09MLsnMz7PNyM9N1c%252FMS0mtULIGAA%253D%253D7fc14535936bb7d75fef4a2ef4eec809fa6c3e45&locale=pl"
        self.LOGIN = "username"

    def tearDown(self):
        self.driver.close()

    def test_usos(self):
        driver = self.driver
        driver.get(self.USOS)
        try:
            login_box = driver.find_element(By.NAME,self.LOGIN)
        except:
             self.fail("Login not found")
        login_box.send_keys("matmul")
        self.assertEqual(login_box.get_attribute("value"),"matmul")

        try:
            clear = driver.find_element(By.NAME,"clear")
            clear.click()
        except:
            self.fail("Clear failed")

        self.assertEqual(login_box.get_attribute("value"),"")

if __name__ == '__main__':
    unittest.main()
