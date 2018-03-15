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
        randomName = ''.join([random.choice(string.letters + string.digits + " ") for i in range(30)])
        return randomName

    def enterRandomReelName(self):
        name = self.getRandomName()
        self.enterReelName(name)

    def enterReelName(self, text):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '//input[@label="Reel Name"]')
        el = self.testCase.UIType.TextField(el)
        el.tap()
        el.clearText()
        el.enterText(text)

    def getRandomHeight(self):
        randomHeight = ''.join([random.choice(string.digits) for i in range(10)])
        return randomHeight

    def enterRandomHeight(self):
        height = self.getRandomHeight()
        self.enterHeight(height)

    def enterHeight(self, text):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '//input[@label="Height"]')
        el = self.testCase.UIType.TextField(el)
        el.tap()
        el.clearText()
        el.enterText(text)

    def getRandomWidth(self):
        randomWidth = ''.join([random.choice(string.digits) for i in range(10)])
        return randomWidth

    def enterRandomWidth(self):
        width = self.getRandomWidth()
        self.enterWidth(width)

    def enterWidth(self, text):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '//input[@label="Width"]')
        el = self.testCase.UIType.TextField(el)
        el.tap()
        el.clearText()
        el.enterText(text)

    def getRandomWeight(self):
        randomWeight = ''.join([random.choice(string.digits) for i in range(10)])
        return randomWeight

    def enterRandomWeight(self):
        weight = self.getRandomWeight()
        self.enterWeight(weight)

    def enterWeight(self, text):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '//input[@label="Weight"]')
        el = self.testCase.UIType.TextField(el)
        el.tap()
        el.clearText()
        el.enterText(text)

    def getSIMpullReelToggle(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '//input[@type="checkbox"]')
        el = self.testCase.UIType.Switch(el)
        return el

    def toggleSIMpullReel(self):
        el = self.getSIMpullReelToggle()
        el.tap()

    def getReelNameErrorMsg(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().CSS_SELECTOR, 'div.field-alert.alerted')
        el = self.testCase.UIType.Element(el)
        return el.getLabel()

    def getHeightErrorMsg(self):
        container = self.testCase.app.findElement(self.testCase.app.getStrategy().CSS_SELECTOR, 'div.form-field.height')
        el = container.find_element(self.testCase.app.getStrategy().CSS_SELECTOR, 'div.field-alert.alerted.delay-alert')
        el = self.testCase.UIType.Element(el)
        return el.getLabel()

    def getWidthErrorMsg(self):
        container = self.testCase.app.findElement(self.testCase.app.getStrategy().CSS_SELECTOR, 'div.form-field.width')
        el = container.find_element(self.testCase.app.getStrategy().CSS_SELECTOR, 'div.field-alert.alerted.delay-alert')
        el = self.testCase.UIType.Element(el)
        return el.getLabel()

    def getWeightErrorMsg(self):
        container = self.testCase.app.findElement(self.testCase.app.getStrategy().CSS_SELECTOR, 'div.form-field.weight')
        el = container.find_element(self.testCase.app.getStrategy().CSS_SELECTOR, 'div.field-alert.alerted.delay-alert')
        el = self.testCase.UIType.Element(el)
        return el.getLabel()

    def tapCancel(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '//button[@class="secondary"]')
        el = self.testCase.UIType.Button(el)
        el.tap()
        sleep(3)

    def getSubmitButton(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '//button[@type="submit"]')
        el = self.testCase.UIType.Button(el)
        return el

    def tapSubmit(self):
        el = self.getSubmitButton()
        el.tap()









