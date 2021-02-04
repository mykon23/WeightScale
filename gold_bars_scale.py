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

	##Returns the weighing results of the scale
	def _get_weigh_result(self):
		result = self.driver.find_element_by_xpath("//div[@class = 'result']//button")
		return result.text

	##Sets the weights to the corresponding side
	def _set_weights(self, side, weights):
		##TODO: Clean up this code so it doesn't check left or right
		side_grid = None
		if side == 'left':
			side_grid = self.driver.find_elements_by_xpath("//input[contains(@id, 'left')]")
		elif side == 'right':
			side_grid = self.driver.find_elements_by_xpath("//input[contains(@id, 'right')]")

		for i in range(len(weights)):
			side_grid[i].send_keys( weights[i] )

	##Weighs the gold bars on the scale
	def _do_weigh(self):
		weigh = self.driver.find_element_by_xpath("//button[ @id = 'weigh']")
		weigh.click()

	##Resets the scale
	def _do_reset(self):
		reset = self.driver.find_element_by_xpath("//button[. = 'Reset']")
		reset.click()

if __name__ == '__main__':
	##Set the driver
	driver = webdriver.Chrome( executable_path = path_to_chrome )
	driver.get(url)

	try:	
		scales_driver = GoldBarsScale(driver)
		print( len(scales_driver._get_weights()) )
		left = list( range(4) )
		right = list( range(4,8) )

		scales_driver._set_weights('left', left)
		scales_driver._set_weights('right', right)
		scales_driver._do_weigh()
		result = scales_driver._get_weigh_result()
		print( result )

	finally:	
		##Terminate the driver
		driver.close()
