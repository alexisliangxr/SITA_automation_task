import unittest
import time
import datetime
import warnings
import logging

from selenium import webdriver

import page

logging.basicConfig(level=logging.INFO,
     format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
     datefmt='%a, %d %b %Y %H:%M:%S',
     filename='sitatesting.log',
     filemode='w')
logger = logging.getLogger()

class PythonSearch(unittest.TestCase):
    """automate the scenario -- a test class to show how to make a reservation"""

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://sitatesting.github.io/AutomationTest")
        warnings.simplefilter('ignore', ResourceWarning)

    def test_web_automation(self):
        """Tests make you reservation feature. Go to the Home page. 
           Click on “Explore More" beside “Caribbean” under visit 
           one of our countries now. Select the city “Kingston” 
           and click on “Make A Reservation”. And Enter the details, 
           the fields can be filled in as you wish. 
           Click on Make your Reservation Now.
        """

        #Load the main page. In this case the home page of
        #https://sitatesting.github.io/AutomationTest/index.html.
        main_page = page.MainPage(self.driver)
        main_page.click_home_button()
        #Check if the word "Sita Automation Test" is in title
        self.assertTrue(main_page.is_title_matches(), "Sitatesting home page title doesn't match.")
        logger.info("Home page opened successfully")
        #Click on "Explore More"
        main_page.click_explore_more()
        #Check if "Explore More for CARIBBEAN" is found
        self.assertTrue(main_page.is_explore_button_matches(), "Explore more button doesn't match.")
        logger.info("Explore more button clicked successfully")

        #Find "Kingston" and click on "make a reservation"
        find_page = page.FindResultsPage(self.driver)
        find_page.click_make_reservation()
        #Check if the reservation form is opened
        self.assertTrue(find_page.is_reservation_form(), "Make a reservation button doesn't match.")
        logger.info("Make a reservation page opened successfully")

        #Fill in the form and submit the reservation
        reservation_page = page.MakeReservationPage(self.driver)
        #Fill in name, phone, guest number, destination, check in date
        reservation_page.fill_in_name("Susan")
        reservation_page.fill_in_phone("0851112876")
        reservation_page.choose_guest(2)
        reservation_page.choose_destination(3)
        current_time = datetime.datetime.now()
        check_time = (current_time - datetime.timedelta(days=2)).strftime("%d/%m/%Y")
        reservation_page.choose_date(check_time)
        time.sleep(2)
        #Submit the reservation
        reservation_page.click_make_reservation_now()
        self.assertTrue(reservation_page.is_submitted_form(), "You didn't submit successful.")
        logger.info("Reservation submitted successfully")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
