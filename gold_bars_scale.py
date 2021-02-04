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
		coins = scales_driver._get_weights()
		
		## Do the case where one is left out and check for equality
		mid_pt = len(coins)//2
		left = list( range(0, mid_pt) )
		right = list( range(mid_pt, 2 * mid_pt) )
		
		scales_driver._set_weights('left', left)
		scales_driver._set_weights('right', right)
		scales_driver._do_weigh()
		result = scales_driver._get_weigh_result()

		if result == '=':
			coins[-1].click()
		else:
			while mid_pt//2 > 0:
				mid_pt //= 2
				##The lightest weight is on the right so split again
				if result == '>':
					left = right[0: mid_pt]
					right = right[mid_pt:]
				else:
					right = left[mid_pt:]
					left = left[0:mid_pt]
				
				scales_driver._do_reset()
				scales_driver._set_weights('left', left)
				scales_driver._set_weights('right', right)
				scales_driver._do_weigh()
				result = scales_driver._get_weigh_result()

			if result == '>':
				coins[ right[0] ].click()
			else: 
				coins[ left[0] ].click()

		##Verify that the correct element was selected
		alert = driver.switch_to_alert()
		assert( alert.text == 'Yay! You find it!')
		alert.accept()
		
	finally:	
		##Terminate the driver
		driver.close()
