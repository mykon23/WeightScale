class WeightScale:
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
