# contains Unittest and HTML report

from selenium import webdriver
import unittest
import HtmlTestRunner

class OrangeHRMtest(unittest.TestCase):
#if a function is defined under class, then it is called method
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=r"C:\Users\HP\Desktop\Learning\QA\chrome\chromedriver.exe")
        cls.driver.maximize_window()

    def test_homePageTitle(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com")
        self.assertEqual("OrangeHRM123",self.driver.title)

    def test_login(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com")
        self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        self.driver.find_element_by_name("Submit").click()
        self.assertEqual("OrangeHRM",self.driver.title)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("Test Completed")

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C://Users/HP/Google Drive/Learning/PythonUnittestProject/Reports"))


