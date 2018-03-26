__author__ = 'ningxinliao'
from time import sleep
from projectBase import ProjectBase
import string
import random

class Circuits(object):

    def __init__(self, testCase):
        # type: (ProjectBase) -> None
        """
        :param testCase: will be the ProjectBase object when a test is run.
        """
        self.testCase = testCase

    # Required Fields
    def getFrom(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '//input[@label="From"]')
        el = self.testCase.UIType.TextField(el)
        return el

    def enterFrom(self, text):
        el = self.getFrom()
        el.tap()
        el.clearText()
        el.enterText(text)

    def getTo(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '//input[@label="To"]')
        el = self.testCase.UIType.TextField(el)
        return el

    def enterTo(self, text):
        el = self.getTo()
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

    def getCircuitLength(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '//input[@label="Length"]')
        el = self.testCase.UIType.TextField(el)
        return el

    def enterCircuitLength(self, text):
        el = self.getCircuitLength()
        el.tap()
        el.clearText()
        el.enterText(text)

    def getNumOfConductorPicker(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '//select[@id="conductors"]')
        el = self.testCase.UIType.Picker(el)
        return el

    def selectNumOfConductor(self, NOC):
        el = self.getNumOfConductorPicker()
        el.scrollToValue(NOC)

    def getCommonPreset(self, preset):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '//input[@id="%s"]' % preset)
        el = self.testCase.UIType.Button(el)
        return el

    def selectCommonPreset(self, preset):
        el = self.getCommonPreset(preset)
        el.tap()

    def getSelectedColorCircle(self, circleOrder):
        selectedColors = self.testCase.app.findElements(self.testCase.app.getStrategy().XPATH, '//li[@class="selected-color"]')
        selectedColor = selectedColors[circleOrder]
        selectedColor= self.testCase.UIType.Element(selectedColor)

        return selectedColor

    def tapSelectedColorCircle(self, circleOrder):
        el = self.getSelectedColorCircle(circleOrder)
        el.tap()


    def getColorOption(self, color):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '//input[@type="button" and @id= "%s"]' % color)
        el = self.testCase.UIType.Element(el)
        return el

    def selectColorOption(self, color):
        el = self.getColorOption(color)
        el.tap()

    # Not Required field
    def getSIMpullHeadToggle(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '//input[@type="checkbox"]')
        el = self.testCase.UIType.Switch(el)
        return el

    def toggleSIMpullHead(self):
        el = self.getSIMpullHeadToggle()
        if self.testCase.isSafari:
            el.tapByLocation()
        else:
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

    # Overflow & edit/duplicate/delete button
    def tapOverflow(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '//div[@class="overflow"]')
        el = self.testCase.UIType.Button(el)
        el.tap()

    def tapEditCircuit(self):
        overflow = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '//div[@class="overflow"]')
        el = overflow.find_element(self.testCase.app.getStrategy().CSS_SELECTOR, 'a')
        el = self.testCase.UIType.Button(el)
        el.tap()


