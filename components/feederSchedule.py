__author__ = 'ningxinliao'
from time import sleep
from projectBase import ProjectBase
import string
import random

class FeederSchedule(object):

    def __init__(self, testCase):
        # type: (ProjectBase) -> None
        """
        :param testCase: will be the ProjectBase object when a test is run.
        """
        self.testCase = testCase

    def getCreateCircuit(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '//button[@class="add"]')
        el = self.testCase.UIType.Button(el)
        return el

    def tapCreateCircuit(self):
        el = self.getCreateCircuit()
        el.tap()
        sleep(2)
