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

		##Ensure that positive number of bars are available
		assert( len(bars) > 0 )

		##Set the working weights
		work = list( range(0, len(bars)) )

		##Process the weights until only the single, fake remains
		while len(work) > 1:

			##Partition the group of weights into three categories for weighing
			split_pt = math.ceil(len(work)/3)
			left = work[0: split_pt]
			right = work[split_pt: 2 * split_pt]
			holdon = work[2 * split_pt:]

			##Weight the items to determine the next set of working weights
			scales_driver.do_reset()
			scales_driver.set_weights('left', left)
			scales_driver.set_weights('right', right)
			scales_driver.do_weigh()
			result = scales_driver.get_weigh_result()

			##Update the working weights according to the left/right results
			if result == '>':
				work = right
			elif result == '<':
				work = left
			else:
				work = holdon

		##Only the fake should be leftover
		fake_index = work[0]

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
		print(f'Number of weighings that occured: {len(weighings)}')
		print('\n'.join( w for w in  weighings ))

	def tearDown(self):
		self.driver.close()

if __name__ == '__main__':
	unittest.main()
