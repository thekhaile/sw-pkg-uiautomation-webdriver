from projectBase import ProjectBase
import os



class FeederSchedule(object):

    def __init__(self, testCase):
        # type: (ProjectBase) -> None
        """
        :param testCase: will be the ProjectBase object when a test is run.
        """
        self.testCase = testCase

    def getFeederScheduleTab(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '//span[text()="Feeder Schedule"]')
        el = self.testCase.UIType.Element(el)
        return el

    def tapFeederSchedule(self):
        el = self.getFeederScheduleTab()
        el.tap()

    def switchToFeederScheduleTab(self):
        el = self.getFeederScheduleTab()
        if el.ui_object.get_attribute('class') != 'selected':
            el.tap()

    def getFeederScheduleEmptyState(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().CSS_SELECTOR, 'p.important-message')
        el = self.testCase.UIType.Element(el)
        return el.getLabel()

    # get the feeder schedule table info
    def getACircuit(self, rowOrder):
        # get table
        table = self.testCase.app.findElement(self.testCase.app.getStrategy().CSS_SELECTOR, 'tbody')
        # get the list of rows from the table
        rows = table.find_elements(self.testCase.app.getStrategy().CSS_SELECTOR, 'tr')

        selectedRow = rows[rowOrder]
        return selectedRow

    def getCircuitFrom(self, rowOrder=0):
        row = self.getACircuit(rowOrder)
        circuitFrom = row.find_element(self.testCase.app.getStrategy().CSS_SELECTOR, 'td.from-cell')
        circuitFrom = self.testCase.UIType.Element(circuitFrom)
        return circuitFrom.getLabel()

    def getCircuitTo(self, rowOrder=0):
        row = self.getACircuit(rowOrder)
        allTds = row.find_elements(self.testCase.app.getStrategy().CSS_SELECTOR, 'td')
        circuitTo = allTds[1]
        circuitTo = self.testCase.UIType.Element(circuitTo)
        return circuitTo.getLabel()

    def getCircuitSize(self, rowOrder=0):
        row = self.getACircuit(rowOrder)
        allTds = row.find_elements(self.testCase.app.getStrategy().CSS_SELECTOR, 'td')
        circuitSize = allTds[2]
        circuitSize = self.testCase.UIType.Element(circuitSize)
        return circuitSize.getLabel()

    def getCircuitLength(self, rowOrder=0):
        row = self.getACircuit(rowOrder)
        allTds = row.find_elements(self.testCase.app.getStrategy().CSS_SELECTOR, 'td')
        circuitLength = allTds[3]
        circuitLength = self.testCase.UIType.Element(circuitLength)
        return circuitLength.getLabel()

    def getCircuitReelName(self, rowOrder=0):
        row = self.getACircuit(rowOrder)
        allTds = row.find_elements(self.testCase.app.getStrategy().CSS_SELECTOR, 'td')
        circuitReel = allTds[4]
        circuitReel = self.testCase.UIType.Element(circuitReel)
        return circuitReel.getLabel()

    def getNumberOfRows(self):
        # get table
        table = self.testCase.app.findElement(self.testCase.app.getStrategy().CSS_SELECTOR, 'tbody')
        # get the list of rows from the table
        rows = table.find_elements(self.testCase.app.getStrategy().CSS_SELECTOR, 'tr')
        return len(rows)

    def getExpandArrow(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().CSS_SELECTOR, 'div.expand.down')
        return el

    def tapExpandArrow(self):
        el = self.getExpandArrow()
        el = self.testCase.UIType.Element(el)
        el.tap()

    def getMetal(self):
        container = self.testCase.app.findElement(self.testCase.app.getStrategy().CSS_SELECTOR, 'div.expanded-header')
        el = container.find_element(self.testCase.app.getStrategy().CSS_SELECTOR, 'span')
        text = el.text
        metal = text.split(' ')[3]
        return metal

    def getInsulation(self):
        container = self.testCase.app.findElement(self.testCase.app.getStrategy().CSS_SELECTOR, 'div.expanded-header')
        el = container.find_element(self.testCase.app.getStrategy().CSS_SELECTOR, 'span')
        text = el.text
        insulation = text.split(' ')[5]
        return insulation

    def getColor(self):
        container = self.testCase.app.findElement(self.testCase.app.getStrategy().CSS_SELECTOR, 'div.selected-color')
        el = container.find_element(self.testCase.app.getStrategy().CSS_SELECTOR, 'div.color-label')
        el = self.testCase.UIType.Element(el)
        return el.getLabel()

    def getSIMpullHeadsText(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().CSS_SELECTOR, 'span.simpull-text')
        return el


