__author__ = 'ningxinliao'
from time import sleep
from projectBase import ProjectBase
import string
import random

class AddCircuits(object):

    def __init__(self, testCase):
        # type: (ProjectBase) -> None
        """
        :param testCase: will be the ProjectBase object when a test is run.
        """
        self.testCase = testCase

    # Required Fields
    def enterFrom(self,text):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '//input[@label="From"]')
        el = self.testCase.UIType.TextField(el)
        el.tap()
        el.clearText()
        el.enterText(text)

    def enterTo(self,text):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '//input[@label="To"]')
        el = self.testCase.UIType.TextField(el)
        el.tap()
        el.clearText()
        el.enterText(text)

    def getConductorTypePicker(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '//select[@label="Metal / Insulation"]')
        el = self.testCase.UIType.Picker(el)
        return el

    def selectConductorType(self, type):
        el = self.getConductorTypePicker()
        el.scrollToValue(type)

    def getConductorSizePicker(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '//select[@label="Size"]')
        el = self.testCase.UIType.Picker(el)
        return el

    def selectConductorSize(self, size):
        el = self.getConductorSizePicker()
        el.scrollToValue(size)

    def enterCircuitLength(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '//input[@label="Length"]')
        el = self.testCase.UIType.TextField(el)
        return el

    def getNumOfConductorPicker(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '//select[@id="conductors"]')
        el = self.testCase.UIType.Picker(el)
        return el

    def selectNumOfConductor(self, NOC):
        el = self.getNumOfConductorPicker()
        el.scrollToValue(NOC)

    # def getCommonPresets(self):
    #     el = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '//input[@id="Black-Red-Blue"]')
    #     el = self.testCase.UIType.Button(el)
    #     return el

    def getConductorColor(self):
        allColors = self.testCase.app.findElements(self.testCase.app.getStrategy().CSS_SELECTOR, 'li.pickable-color')
        pickOneColor = allColors.find_element(self.testCase.app.getStrategy().CSS_SELECTOR, 'label')
        pickOneColor = self.testCase.UIType.Element(pickOneColor)
        return pickOneColor.getLabel

    def selectConductorColor(self, color):
        color = self.getConductorColor()
        color.tap

    # Not Required field
    def getSIMpullHeadToggle(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '//input[@type="checkbox"]')
        el = self.testCase.UIType.Switch(el)
        return el

    def toggleSIMpullHead(self):
        el = self.getSIMpullHeadToggle()
        el.tap()

    # Cancel & Submit button
    def tapCancel(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '//button[@class="secondary"]')
        el = self.testCase.UIType.Button(el)
        if self.testCase.isChromium:
            el.tap()
        elif self.testCase.isMobile:
            el.tapHybrid()
        else:
            el.tap()
        sleep(3)

    def getSubmitButton(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '//button[@type="submit"]')
        el = self.testCase.UIType.Button(el)
        return el

    def tapSubmit(self):
        el = self.getSubmitButton()
        el.tap()

    # Error msg
    def getErrorMsg(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().CSS_SELECTOR, 'div.field-alert.alerted')
        el = self.testCase.UIType.Element(el)
        return el.getLabel()

