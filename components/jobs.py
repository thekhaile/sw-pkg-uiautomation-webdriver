from time import sleep
from projectBase import ProjectBase
import string
import random
from southwire_pkg_uiautomation_webdriver.components.projects import Projects

class Jobs(object):
    def __init__(self, testCase):
        # type: (ProjectBase) -> None
        """
        :param testCase: will be the ProjectBase object when a test is run.
        """
        self.testCase = testCase
        self.projects = Projects(self.testCase)

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

    def selectAJob(self, rowOrder=0):
        # This is a work-around for MicrosoftEdge not displaying the project table in the timely manner
        if self.testCase.app.isMicrosoftEdge():
            count = 0
            while not self.testCase.app.findElement(self.testCase.app.getStrategy().CSS_SELECTOR,'tbody') or count <= 100:
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

    def enterJobName(self, text):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '//input[@label="Job Name*"]')
        el = self.testCase.UIType.TextField(el)
        el.tap()

        el.clearText()
        el.enterText(text)

    def enterHeight(self, text):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().CSS_SELECTOR, 'input.height')
        el = self.testCase.UIType.TextField(el)
        el.tap()

        el.clearText()
        el.enterText(text)

    def enterWidth(self, text):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().CSS_SELECTOR, 'input.width')
        el = self.testCase.UIType.TextField(el)
        el.tap()

        el.clearText()
        el.enterText(text)

    def enterWeight(self, text):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().CSS_SELECTOR, 'input.weight')
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
        if self.testCase.isSafari:
            el.tapByLocation()
        else:
            el.tap()

    def getSubmitButton(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '//button[@type="submit"]')
        el = self.testCase.UIType.Button(el)
        return el

    def tapSubmit(self):
        el = self.getSubmitButton()
        el.tap()
        sleep(3)

    def tapCancel(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '//button[@class="secondary"]')
        el = self.testCase.UIType.Button(el)
        el.tap()
        sleep(3)

    def tapOverflow(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '//div[@class="overflow"]')
        el = self.testCase.UIType.Button(el)
        el.tap()

    def tapEditSettings(self):
        overflow = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '//div[@class="overflow"]')
        el = overflow.find_element(self.testCase.app.getStrategy().CSS_SELECTOR, 'a')
        el = self.testCase.UIType.Button(el)
        el.tap()

    def tapDeleteJob(self):
        overflow = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '//div[@class="overflow"]')
        el = overflow.find_elements(self.testCase.app.getStrategy().CSS_SELECTOR, 'li.actionable')
        delete = el[1]
        delete = self.testCase.UIType.Button(delete)
        delete.tap()

    def tapDuplicateJob(self):
        overflow = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '//div[@class="overflow"]')
        el = overflow.find_elements(self.testCase.app.getStrategy().CSS_SELECTOR, 'li.actionable')
        duplicate = el[0]
        duplicate = self.testCase.UIType.Button(duplicate)
        duplicate.tap()

    def tapConfirmDelete(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().CSS_SELECTOR, 'button.confirm')
        el = self.testCase.UIType.Button(el)
        el.tap()

    def tapCancelDelete(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().CSS_SELECTOR, 'button.cancel')
        el = self.testCase.UIType.Button(el)
        el.tap()

    def getErrorMsg(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().CSS_SELECTOR, 'div.field-alert.alerted')
        el = self.testCase.UIType.Element(el)
        return el.getLabel()

    def generateRandomName(self):
        randomName = ''.join([random.choice(string.letters + string.digits + " " + " ") for i in range(30)])
        stripName = randomName.strip()
        replaceName = stripName.replace('  ',' ')
        return replaceName

    def enterRandomJobName(self):
        name = self.generateRandomName()
        self.enterJobName(name)

    def tapConfigureJob(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().CSS_SELECTOR, 'button.tertiary')
        el = self.testCase.UIType.Button(el)
        el.tap()

    def createAJob(self):
        self.tapCreateJob()
        sleep(2)
        self.enterRandomJobName()
        sleep(2)
        self.tapSubmit()




