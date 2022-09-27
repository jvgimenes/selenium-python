# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from webdriver_manager.chrome import ChromeDriverManager
import time

class TestGetdolar():
  def setup_method(self, method):
    # self.driver = webdriver.Chrome()
    self.driver = webdriver.Chrome(ChromeDriverManager().install())
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_getdolar(self):
    self.driver.get("https://www.google.com/")
    self.driver.set_window_size(1936, 1056)
    self.driver.find_element(By.NAME, "q").send_keys("dolar")
    self.driver.find_element(By.NAME, "q").send_keys(Keys.ENTER)
    dolar = self.driver.find_element(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').text
    dolar = dolar.replace(",", ".")
    assert float(dolar) > 5

  
