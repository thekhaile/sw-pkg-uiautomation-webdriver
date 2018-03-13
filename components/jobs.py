from time import sleep
from projectBase import ProjectBase
import string
import random


class Jobs(object):
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
            sleep(45)
        el = self.getAJob(rowOrder)
        el = self.testCase.UIType.Element(el)
        el.tap()
        sleep(3)

    def tapCreateJob(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().CSS_SELECTOR, 'a.action.create')
        el = self.testCase.UIType.Button(el)
        el.tap()


    def enterJobName(self, text):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().CSS_SELECTOR, 'input.job-name')
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
        if self.testCase.isSafari():
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


    '''Ningxin's code starts here'''

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

    def getErrorMsg(self):
        # get container
        container = self.testCase.app.findElement(self.testCase.app.getStrategy().CSS_SELECTOR, 'div.project.job')
        # find all the Ps listed in the container. Be careful this is finding Ps in Selenium, not our library!!
        allPs = container.find_elements(self.testCase.app.getStrategy().CSS_SELECTOR, 'p')
        #get the last P in the list
        p = allPs[-1]
        #assign P to an element type
        p = self.testCase.UIType.Element(p)
        #return the error message
        return p.getLabel()

    def getRandomName(self):
        randomName = ''.join([random.choice(string.letters + string.digits + " " + " " + " ") for i in range(30)])
        return randomName

    def enterRandomJobName(self):
        name = self.getRandomName()
        self.enterJobName(name)





