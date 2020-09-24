from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from random import randint, choice
from time import sleep

class KahootBot():
    def play(self, kahoot_nickname, kahoot_pin, kahoot_url, is_realistic):

        # configure variables
        self.kahoot_pin = kahoot_pin
        self.kahoot_nickname = kahoot_nickname
        self.kahoot_url = kahoot_url
        self.kahoot_answers = []
        self.button_xpaths = {1: '''//*[@id="root"]/div/main/div[2]/div/div/button[1]''',
                              2: '''//*[@id="root"]/div/main/div[2]/div/div/button[2]''',
                              3: '''//*[@id="root"]/div/main/div[2]/div/div/button[3]''',
                              4: '''//*[@id="root"]/div/main/div[2]/div/div/button[4]'''}

        # start webdriver (firefox)
        self.driver = webdriver.Firefox(executable_path=r"geckodriver/geckodriver.exe")
        self.driver.get(self.kahoot_url)  # go to kahoot.com/ for answers

        # GET KAHOOT ANSWERS
        # show answers
        sleep(1)
        self.show_answers_button = self.driver.find_element_by_xpath('''//*[contains(text(), "Show answers")]''')
        self.show_answers_button.click()

        # get answers
        self.questions = self.driver.find_elements_by_class_name("choices")  # finds all questions
        for self.item_1 in self.questions:  # loop through questions
            self.choices = self.item_1.find_elements_by_tag_name("li")  # find possible answers
            i = 1  # number of the correct answer (1-4)
            for self.item_2 in self.choices: # loop through answers
                try:
                    self.correct_answer = self.item_2.find_element_by_class_name("choices__choice--correct")  # if --correct div found on choice, choice is correct.
                    self.kahoot_answers += [i]
                    break
                except:
                    i += 1 # --correct div wasn't found, choice was incorrect, continueing...

        # JOIN KAHOOT
        self.driver.get("https://kahoot.it/")  # go to kahoot.it/

        sleep(1)
        self.kahoot_pin_textbox = self.driver.find_element_by_id("game-input")  # find game pin input
        self.kahoot_pin_textbox.send_keys(self.kahoot_pin + Keys.RETURN)  # send game pin

        sleep(2)
        self.kahoot_nickname_textbox = self.driver.find_element_by_id("nickname")  # find nickname input
        self.kahoot_nickname_textbox.send_keys(self.kahoot_nickname + Keys.RETURN)  # send nickname

        # PLAY KAHOOT
        while True:

            # search for a button to confirm the round has started
            while True:
                try:
                    self.driver.find_element_by_xpath(self.button_xpaths[1])
                    break
                except:
                    pass

            # find round of max rounds for example 5 of 16
            try:
                self.round_of_max_rounds = self.driver.find_element_by_xpath("/html/body/div/div/main/div[1]/div[2]").text
            except:
                pass

            # split round of max rounds with " " and access first element in the list aka. the current round and convert it to a integer
            self.round = int(self.round_of_max_rounds.split(" ")[0])
            # access that rounds answer
            try:
                self.search_with_xpath = self.button_xpaths[self.kahoot_answers[self.round - 1]]
            except:
                break

            while True:  # loop till success
                try:
                    # find the correct button
                    self.button = self.driver.find_element_by_xpath(self.search_with_xpath)

                    # if bot is in realistic mode, wait few seconds
                    if is_realistic:
                        sleep(randint(1, 10))

                    self.button.click()  # click the button
                    break  # exit loop
                except:
                    pass

            while True:  # loop to avoid double clicking a button
                try:
                    self.driver.find_element_by_xpath(self.search_with_xpath)
                except:
                    break

