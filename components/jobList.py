from time import sleep
from projectBase import ProjectBase
import string
import random
from southwire_pkg_uiautomation_webdriver.components.project import Project

class JobList(object):
    def __init__(self, testCase):
        # type: (ProjectBase) -> None
        """
        :param testCase: will be the ProjectBase object when a test is run.
        """
        self.testCase = testCase

    def getAJob(self, rowOrder):
        # get table
        table = self.testCase.app.findElement(self.testCase.app.getStrategy().CSS_SELECTOR, 'tbody')
        # get the list of rows from the table
        rows = table.find_elements(self.testCase.app.getStrategy().CSS_SELECTOR, 'tr')

        selectedRow = rows[rowOrder]
        return selectedRow

    def getJobCount(self):
        # get table
        table = self.testCase.app.findElement(self.testCase.app.getStrategy().CSS_SELECTOR, 'tbody')
        # get the list of rows from the table
        rows = table.find_elements(self.testCase.app.getStrategy().CSS_SELECTOR, 'tr')
        return len(rows)

    def getJobName(self, rowOrder=0):
        row = self.getAJob(rowOrder)
        jobName= row.find_element(self.testCase.app.getStrategy().CSS_SELECTOR,'th')
        jobName = self.testCase.UIType.Element(jobName)
        return jobName.getLabel()

    def getJobCreatedDate(self, rowOrder=0):
        row = self.getAJob(rowOrder)
        jobCreatedDate= row.find_element(self.testCase.app.getStrategy().CSS_SELECTOR,'td')
        jobCreatedDate = self.testCase.UIType.Element(jobCreatedDate)
        return jobCreatedDate.getLabel()

    def getJobModifiedDate(self, rowOrder=0):
        row = self.getAJob(rowOrder)
        allTds = row.find_elements(self.testCase.app.getStrategy().CSS_SELECTOR,'td')
        jobModifiedDate = allTds[1]
        jobModifiedDate = self.testCase.UIType.Element(jobModifiedDate)
        return jobModifiedDate.getLabel()

    def getNumberOfCircuits(self, rowOrder=0):
        row = self.getAJob(rowOrder)
        allTds = row.find_elements(self.testCase.app.getStrategy().CSS_SELECTOR,'td')
        numCircuits = allTds[2]
        numCircuits = self.testCase.UIType.Element(numCircuits)
        return numCircuits.getLabel()

    def getNumberOfReels(self, rowOrder=0):
        row = self.getAJob(rowOrder)
        allTds = row.find_elements(self.testCase.app.getStrategy().CSS_SELECTOR,'td')
        numCircuits = allTds[3]
        numCircuits = self.testCase.UIType.Element(numCircuits)
        return numCircuits.getLabel()

    def selectAJob(self, rowOrder=0):
        # This is a work-around for MicrosoftEdge not displaying the project table in the timely manner
        count = 0
        while not self.testCase.app.findElement(self.testCase.app.getStrategy().CSS_SELECTOR, 'tbody') or count <= 100:
            count += 1
            continue
        el = self.getAJob(rowOrder)
        el = self.testCase.UIType.Element(el)
        # This is a work-around for not being able to tap the element in Firefox
        if self.testCase.app.isFirefox():
            el.tapByLocation()
        else:
            el.tap()
        sleep(3)

    def tapCreateJob(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '//a[text()="Create Job"]')
        el = self.testCase.UIType.Button(el)
        el.tap()

    def getOverflow(self):
        els = self.testCase.app.findElements(self.testCase.app.getStrategy().XPATH, '//div[@class="overflow"]')
        if len(els) > 1:
            el = els[1]
        else:
            el = els[0]
        return el

    def tapOverflow(self):
        el = self.getOverflow()
        el = self.testCase.UIType.Button(el)
        el.tap()

    def tapEditSettings(self):
        overflow = self.getOverflow()
        el = overflow.find_element(self.testCase.app.getStrategy().XPATH, './/*[text()="Edit Settings"]')
        el = self.testCase.UIType.Button(el)
        el.tap()

    def tapDeleteJob(self):
        overflow = self.getOverflow()
        el = overflow.find_element(self.testCase.app.getStrategy().XPATH, './/*[text()="Delete Job"]')
        el = self.testCase.UIType.Button(el)
        el.tap()

    def tapDuplicateJob(self):
        overflow = self.getOverflow()
        el = overflow.find_element(self.testCase.app.getStrategy().XPATH, './/*[text()="Duplicate Job"]')
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