from selenium import webdriver
import os

path_to_chrome = os.path.join('.', 'chromedriver')
url = 'http://ec2-54-208-152-154.compute-1.amazonaws.com/'

class GoldBarsScale: 
	def __init__ (self, driver):
		self.driver = driver

	##Returns the number of coins/bars to work with
	def get_weights(self):
		weights = self.driver.find_elements_by_xpath("//button[ contains( @id, 'coin_') ]")
		return weights

	##Returns the weighing results of the scale
	def get_weigh_result(self):
		result = self.driver.find_element_by_xpath("//div[@class = 'result']//button")
		return result.text

	##Returns the weighings that occured throughout the session
	def get_weighings(self):
		weighing_items = self.driver.find_elements_by_xpath("//div[@class = 'game-info']//ol//li")

		weighings = []
		for i in range(len(weighing_items)):
			weighings.append( weighing_items[i].text )

		return weighings

	##Sets the weights to the corresponding side
	def set_weights(self, side, weights):
		side_grid = None
		if side == 'left':
			side_grid = self.driver.find_elements_by_xpath("//input[contains(@id, 'left')]")
		elif side == 'right':
			side_grid = self.driver.find_elements_by_xpath("//input[contains(@id, 'right')]")

		for i in range(len(weights)):
			side_grid[i].send_keys( weights[i] )

	##Weighs the gold bars on the scale
	def do_weigh(self):
		weigh = self.driver.find_element_by_xpath("//button[ @id = 'weigh']")
		weigh.click()

	##Resets the scale
	def do_reset(self):
		reset = self.driver.find_element_by_xpath("//button[. = 'Reset']")
		reset.click()

if __name__ == '__main__':
	##Set the driver
	driver = webdriver.Chrome( executable_path = path_to_chrome )
	driver.get(url)

	try:	
		scales_driver = GoldBarsScale(driver)
		bars = scales_driver.get_weights()
		
		##Do an initial comparison between of two equal sized partitions regardless of even or odd number of bars
		mid_pt = len(bars)//2
		left = list( range(0, mid_pt) )
		right = list( range(mid_pt, 2 * mid_pt) )
		
		scales_driver.set_weights('left', left)
		scales_driver.set_weights('right', right)
		scales_driver.do_weigh()
		result = scales_driver.get_weigh_result()

		##The equality case will only occur for the odd case if fake is witheld
		if result == '=':
			bars[-1].click()
		else:
			while mid_pt//2 > 0:
				##Split the weights of interest based on the weighing result to work with lighter side as it is the one with the fake weight
				mid_pt //= 2
				if result == '>':
					left = right[0: mid_pt]
					right = right[mid_pt:]
				else:
					right = left[mid_pt:]
					left = left[0:mid_pt]
				
				##Weigh the results again for next comparison
				scales_driver.do_reset()
				scales_driver.set_weights('left', left)
				scales_driver.set_weights('right', right)
				scales_driver.do_weigh()
				result = scales_driver.get_weigh_result()

			##At this point there is only one item on each side of the scale
			fake_index = right[0] if result == '>' else left[0]
			bars[ fake_index ].click()

		##Verify that the correct element was selected
		alert = driver.switch_to_alert()
		assert( alert.text == 'Yay! You find it!')
		print( alert.text )
		print(f'Fake one is {fake_index}')
		alert.accept()

		##Get the weighings that occurred
		weighings = scales_driver.get_weighings()
		assert( len(weighings) > 0 )
		print( weighings )
		
	finally:	
		##Terminate the driver
		driver.close()
