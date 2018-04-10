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
        createButtons = self.testCase.app.findElements(self.testCase.app.getStrategy().XPATH, '//button[@class="add"]')
        el = createButtons[1]
        el = self.testCase.UIType.Button(el)
        return el

    def tapCreateCircuit(self):
        el = self.getCreateCircuit()
        el.tap()
        sleep(2)

    def getCreateReel(self):
        createButtons = self.testCase.app.findElements(self.testCase.app.getStrategy().XPATH, '//button[@class="add"]')
        el = createButtons[0]
        el = self.testCase.UIType.Button(el)
        return el

    def tapCreateReel(self):
        el = self.getCreateReel()
        el.tap()
        sleep(2)

    def getAddButton(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().CSS_SELECTOR,
                                           'button.icon-button.add-to-reel')
        el = self.testCase.UIType.Button(el)
        return el

    def tapAddCircuit(self):
        el = self.getAddButton()
        el.tap()

    def tapRemoveCircuit(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().CSS_SELECTOR,
                                           'button.icon-button.remove-from-reel')
        el = self.testCase.UIType.Button(el)
        el.tap()

    def getAvalableCircuitTab(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '//div[text()="Available Circuits"]')
        el = self.testCase.UIType.Element(el)
        return el

    def getCircuitsOnReelTab(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '//div[text()="Circuits on Reel"]')
        el = self.testCase.UIType.Element(el)
        return el

    def tapCircuitsOnReel(self):
        el = self.getCircuitsOnReelTab()
        el.tap()

    def switchToCircuitsOnReelTab(self):
        el = self.getCircuitsOnReelTab()
        if el.ui_object.get_attribute('class') != 'selected':
            el.tap()

    def getExceedsAlert(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().CSS_SELECTOR, 'tr.circuit-warning.exceeds')
        el = self.testCase.UIType.Button(el)
        return el

    def getIncompatibleAlert(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().CSS_SELECTOR, 'tr.circuit-warning.incompatible')
        el = self.testCase.UIType.Button(el)
        return el

    def uploadTemplate(self, filePath):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '//input[@type="file"]')

        el.send_keys(filePath)

