__author__ = 'ningxinliao'
from time import sleep
from projectBase import ProjectBase
import string
import random
import os

class FeederSchedule(object):

    def __init__(self, testCase):
        # type: (ProjectBase) -> None
        """
        :param testCase: will be the ProjectBase object when a test is run.
        """
        self.testCase = testCase

    def getCreateCircuit(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '//button[text()="Create Circuit"]')
        el = self.testCase.UIType.Button(el)
        return el

    def tapCreateCircuit(self):
        if self.testCase.isChromium:
            self.testCase.driver.refresh()
            sleep(7)
        el = self.getCreateCircuit()
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

    def confirmRemoval(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().CSS_SELECTOR, 'button.confirm')
        el = self.testCase.UIType.Button(el)
        el.tap()

    def getAvalableCircuitTab(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '//div[text()="Available Circuits"]')
        el = self.testCase.UIType.Element(el)
        return el

    def tapAvalableCircuit(self):
        el = self.getAvalableCircuitTab()
        el.tap()

    def switchToAvailableCircuitTab(self):
        el = self.getAvalableCircuitTab()
        if el.ui_object.get_attribute('class') != 'selected':
            el.tap()

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

    # Overflow & edit/duplicate/delete button
    def tapOverflow(self, rowNumber=0):
        els = self.testCase.app.findElements(self.testCase.app.getStrategy().XPATH, '//div[@class="overflow"]')
        el = els[rowNumber]
        el = self.testCase.UIType.Button(el)
        el.tap()

    def tapEditCircuit(self, rowNumber=0):
        overflow = self.testCase.app.findElements(self.testCase.app.getStrategy().XPATH, '//div[@class="overflow"]')
        overflow = overflow[rowNumber]
        el = overflow.find_element(self.testCase.app.getStrategy().XPATH, './/*[text()="Edit"]')
        el = self.testCase.UIType.Button(el)
        el.tap()

    def tapDeleteCircuit(self):
        overflow = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '//div[@class="overflow"]')
        el = overflow.find_element(self.testCase.app.getStrategy().XPATH, './/*[text()="Delete"]')
        el = self.testCase.UIType.Button(el)
        el.tap()

    def tapDuplicateCircuit(self):
        overflow = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '//div[@class="overflow"]')
        el = overflow.find_element(self.testCase.app.getStrategy().XPATH, './/*[text()="Duplicate"]')
        el = self.testCase.UIType.Button(el)
        el.tap()

    def tapConfirmDelete(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().CSS_SELECTOR, 'button.confirm')
        el = self.testCase.UIType.Button(el)
        el.tap()

    def tapCancelDelete(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().CSS_SELECTOR, 'button.cancel')
        el = self.testCase.UIType.Button(el)
        el.tap()

    # get available circuit info from table
    def getACircuit(self, rowOrder=0):
        # get table
        table = self.testCase.app.findElement(self.testCase.app.getStrategy().CSS_SELECTOR, 'tbody')
        # get the list of rows from the table
        rows = table.find_elements(self.testCase.app.getStrategy().CSS_SELECTOR, 'tr')

        selectedRow = rows[rowOrder]
        return selectedRow

    def getCircuitFrom(self, rowOrder=0):
        row = self.getACircuit(rowOrder)
        circuitFrom= row.find_element(self.testCase.app.getStrategy().CSS_SELECTOR,'td.from-cell')
        circuitFrom = self.testCase.UIType.Element(circuitFrom)
        return circuitFrom.getLabel()

    def getCircuitTo(self, rowOrder=0):
        row = self.getACircuit(rowOrder)
        allTds = row.find_elements(self.testCase.app.getStrategy().CSS_SELECTOR,'td')
        circuitTo = allTds[1]
        circuitTo = self.testCase.UIType.Element(circuitTo)
        return circuitTo.getLabel()

    def getCircuitSize(self, rowOrder=0):
        row = self.getACircuit(rowOrder)
        allTds = row.find_elements(self.testCase.app.getStrategy().CSS_SELECTOR,'td')
        circuitSize = allTds[2]
        circuitSize = self.testCase.UIType.Element(circuitSize)
        return circuitSize.getLabel()

    def getCircuitLength(self, rowOrder=0):
        row = self.getACircuit(rowOrder)
        allTds = row.find_elements(self.testCase.app.getStrategy().CSS_SELECTOR,'td')
        circuitLength = allTds[3]
        circuitLength = self.testCase.UIType.Element(circuitLength)
        return circuitLength.getLabel()

    def getNumberOfRows(self):
        # get table
        table = self.testCase.app.findElement(self.testCase.app.getStrategy().CSS_SELECTOR, 'tbody')
        # get the list of rows from the table
        if table:
            rows = table.find_elements(self.testCase.app.getStrategy().CSS_SELECTOR, 'tr')
            return len(rows)
        else:
            return 0
