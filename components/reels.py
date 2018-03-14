__author__ = 'ningxinliao'
from time import sleep
from projectBase import ProjectBase
import string
import random

class Reels(object):

    def __init__(self, testCase):
        # type: (ProjectBase) -> None
        """
        :param testCase: will be the ProjectBase object when a test is run.
        """
        self.testCase = testCase

    # Required Fields
    def getRandomName(self):
        randomName = ''.join([random.choice(string.letters + string.digits + " " + " " + " ") for i in range(30)])
        return randomName

    def enterRandomReelName(self):
        name = self.getRandomName()
        self.enterReelName(name)

    def enterReelName(self, text):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '//input[@label="Reel Name"]')
        el = self.testCase.UIType.text(el)
        el.tap()
        el.clearText()
        el.enterText(text)

    def 



