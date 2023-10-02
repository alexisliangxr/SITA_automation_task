from selenium.webdriver.common.by import By

class MainPageLocators():
    """A class for main page locators. All main page locators should come here"""

    HOME_BUTTON = (By.CSS_SELECTOR,
                   'body > header > div > div > div > nav > ul > li:nth-child(1) > a')
    EXPLORE_MORE = (By.XPATH,
                    '/html/body/div[2]/div/div[2]/div[1] \
                     /div/div/div[2]/div/div/div[2]/div/div[1]/a')

class FindResultsPageLocators():
    """A class for find page locators. All find page locators should come here"""

    MAKE_A_RESERVATION = (By.XPATH,
                          '/html/body/div[4]/div[2]/div/div/div/div[1] \
                           /div/div[5]/div/div/div/div[2]/a')

class MakeReservationPageLocators():
    """A class for make a reservation page locators.
       All make a reservation page locators should come here"""

    NAME = (By.XPATH, '//*[@id="reservation-form"] \
                          /div/div[2]/fieldset/input')
    PHONE = (By.XPATH, '//*[@id="reservation-form"]/div/div[3]/fieldset/input')
    GUEST = (By.ID, 'chooseGuests')
    DESTINATION = (By.ID, 'chooseCategory')
    DATE = (By.CLASS_NAME, 'date')
    SUBMIT = (By.XPATH, '//*[@id="reservation-form"]/div/div[7]/fieldset/button')
