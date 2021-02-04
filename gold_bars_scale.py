from selenium import webdriver
import os

path_to_chrome = os.path.join('.', 'chromedriver')
url = 'http://ec2-54-208-152-154.compute-1.amazonaws.com/'

class GoldBarsScale:
	def __init__ (self, driver):
		self.driver = driver

	##Returns the number of coins/bars to work with
	def _get_weights(self):
		coins = self.driver.find_elements_by_xpath("//button[ contains( @id, 'coin_') ]")
		return coins

if __name__ == '__main__':
	##Set the driver
	driver = webdriver.Chrome( executable_path = path_to_chrome )
	driver.get(url)
	
	scales_driver = GoldBarsScale(driver)
	print( len(scales_driver._get_weights()) )
	
	##Terminate the driver
	driver.close()
