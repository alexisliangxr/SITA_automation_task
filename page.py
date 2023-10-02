from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

from locators import MainPageLocators, FindResultsPageLocators, MakeReservationPageLocators

class BasePage():
    """Base class to initialize the base page and actions that will be called from all
    pages"""

    def __init__(self, driver):
        self.driver = driver

    def click_button(self, *locator):
        """click button"""

        self.driver.find_element(*locator).click()

    def hidden_button(self, *locator):
        """click hidden button"""

        self.driver.find_element(*locator).send_keys(Keys.ENTER)

    def send_text(self, item, *locator):
        """send text"""

        self.driver.find_element(*locator).send_keys(item)

    def select_list(self, index, *locator):
        """select item in select list"""

        element = self.driver.find_element(*locator)
        new_element = Select(element)
        new_element.select_by_index(index)


class MainPage(BasePage):
    """Home page action methods come here."""

    def is_title_matches(self):
        """Verifies that the hardcoded text "Sita Automation Test" appears in page title"""

        return "Sita Automation Test" in self.driver.title

    def click_home_button(self):
        """Triggers the process"""

        self.click_button(*MainPageLocators.HOME_BUTTON)

    def click_explore_more(self):
        """Find Explore More beside Caribbean"""

        self.hidden_button(*MainPageLocators.EXPLORE_MORE)

    def is_explore_button_matches(self):
        """Verifies that click the explore more button and explore more appears in page title"""

        return "Welcome To Caribbean" in self.driver.page_source


class FindResultsPage(BasePage):
    """Find results page action methods come here"""

    def click_make_reservation(self):
        """Select the city Kingston 
           and click on Make A Reservation"""

        self.hidden_button(*FindResultsPageLocators.MAKE_A_RESERVATION)

    def is_reservation_form(self):
        """ Probably should go to the reservation page"""

        return "Make Your Reservation Now" in self.driver.page_source


class  MakeReservationPage(BasePage):
    """Fill in the form and submit the reservation"""

    def fill_in_name(self, name):
        """Fill in Your Name"""

        self.send_text(name, *MakeReservationPageLocators.NAME)

    def fill_in_phone(self, phone):
        """Fill in Your Phone Number"""

        self.send_text(phone, *MakeReservationPageLocators.PHONE)

    def choose_guest(self, index):
        """Choose which one in the Number Of Guests list"""

        self.select_list(index, *MakeReservationPageLocators.GUEST)

    def choose_destination(self, index):
        """Choose which one in the Choose Your Destination list"""

        self.select_list(index, *MakeReservationPageLocators.DESTINATION)

    def choose_date(self, time):
        """Choose date"""

        self.send_text(time, *MakeReservationPageLocators.DATE)

    def click_make_reservation_now(self):
        """Click on Make A Reservation Now"""

        self.hidden_button(*MakeReservationPageLocators.SUBMIT)

    def is_submitted_form(self):
        """ Probably should go to the next page"""

        return "No results found." not in self.driver.page_source
    