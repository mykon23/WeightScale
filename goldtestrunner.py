from selenium import webdriver
import os
import unittest
import weightscale

##Propertier for the driver
path_to_chrome = os.path.join('.', 'chromedriver')
url = 'http://ec2-54-208-152-154.compute-1.amazonaws.com/'

class GoldTestRunner(unittest.TestCase):

	def setUp(self):
		##Set the driver
		self.driver = webdriver.Chrome( executable_path = path_to_chrome )
		self.driver.get(url)

	def test_find_fake(self):

		##Set the scales driver to interact with the webpage
		scales_driver = weightscale.WeightScale( self.driver )
		bars = scales_driver.get_weights()
		
		##Default the fake index to the last one for the odd case
		fake_index = len(bars) - 1
		
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
			bars[fake_index].click()
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
		alert = self.driver.switch_to_alert()
		assert( alert.text == 'Yay! You find it!')
		print(f'Fake one is {fake_index}')
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