from selenium import webdriver
import config
import math
import unittest
import weightscale

class GoldTestRunner(unittest.TestCase):

	def setUp(self):
		##Set the driver
		self.driver = webdriver.Chrome( executable_path = config.path_to_chrome )

	def test_find_fake(self):

		##Set the scales driver to interact with the webpage
		scales_driver = weightscale.WeightScale( self.driver )
		bars = scales_driver.get_weights()
		
		##Partition the group of weights into three categories for weighing
		split_pt = math.ceil(len(bars)/3)
		left = list( range(0, split_pt) )
		right = list( range(split_pt, 2 * split_pt) )
		holdon = list( range(2 * split_pt, len(bars)) )
	
		##Do an initial comparison	
		scales_driver.set_weights('left', left)
		scales_driver.set_weights('right', right)
		scales_driver.do_weigh()
		result = scales_driver.get_weigh_result()

		##Add +1 to ensure the two weight case is handled
		while (split_pt + 1)//3 > 0:
				##Split the weights of interest based on the weighing result to work with lighter side as it is the one with the fake weight
				split_pt = math.ceil(split_pt/3)
				if result == '>':
					holdon = right[2 * split_pt:]
					left = right[0: split_pt]
					right = right[split_pt: 2 * split_pt]
				elif result == '<':
					holdon = left[2 * split_pt:]
					right = left[split_pt: 2 * split_pt]
					left = left[0: split_pt]
				else:
					if len(holdon) == 1:
						break
					left = holdon[0: split_pt]
					right = holdon[split_pt: 2 * split_pt]
					holdon = holdon[2 * split_pt:]
				
				##Weigh the items again for next comparison
				scales_driver.do_reset()
				scales_driver.set_weights('left', left)
				scales_driver.set_weights('right', right)
				scales_driver.do_weigh()
				result = scales_driver.get_weigh_result()

		##Set the fake index according to the results
		fake_index = -1
		if result == '<':
			fake_index = left[0]
		elif result == '>':
			fake_index = right[0]
		else:
			fake_index = holdon[0]

		##Select the fake weight
		bar_number = bars[ fake_index ].text
		bars[ fake_index ].click()

		##Verify that the correct element was selected
		alert = self.driver.switch_to_alert()
		assert( alert.text == 'Yay! You find it!')
		print(f'Fake one is {bar_number}')
		print( alert.text )
		alert.accept()

		##Get the weighings that occurred
		weighings = scales_driver.get_weighings()
		assert( len(weighings) > 0 )
		print(f'Number of weighings that occured: {len(weighings)}')
		print('\n'.join( w for w in  weighings ))

	def tearDown(self):
		self.driver.close()

if __name__ == '__main__':
	unittest.main()
