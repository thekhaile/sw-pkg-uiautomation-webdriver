from projectBase import ProjectBase
import os



class JobSummary(object):

    def __init__(self, testCase):
        # type: (ProjectBase) -> None
        """
        :param testCase: will be the ProjectBase object when a test is run.
        """
        self.testCase = testCase

    def uploadTemplate(self, filePath):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '//input[@type="file"]')
        cwd = os.getcwd()
        path = os.path.abspath(cwd+filePath)
        el.send_keys(path)

    def getUploadTemplateOption(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().ID, 'upload-file')
        return el

    def getConfigureJob(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().CSS_SELECTOR, 'button.tertiary')
        el = self.testCase.UIType.Button(el)
        return el

    def tapConfigureJob(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().CSS_SELECTOR, 'button.tertiary')
        el = self.testCase.UIType.Button(el)
        el.tap()

    def getJobNameOnViewJobSummary(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().CSS_SELECTOR, 'h2')
        el = self.testCase.UIType.Element(el)
        return el.getLabel()

    def getDateCreated(self):
        dates = self.testCase.app.findElements(self.testCase.app.getStrategy().CSS_SELECTOR, 'dd')
        el = dates[0]
        el = self.testCase.UIType.Element(el)
        return el.getLabel()

    def getDateModified(self):
        dates = self.testCase.app.findElements(self.testCase.app.getStrategy().CSS_SELECTOR, 'dd')
        el = dates[1]
        el = self.testCase.UIType.Element(el)
        return el.getLabel()

    def getQuoteSubmittedDate(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().CSS_SELECTOR, 'div.quote-submitted')
        # get submitted date
        text = el.text
        date = text.split(' ')[-1]
        return date

    def getRequestQuote(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '//button[text()="Request Quote"]')
        el = self.testCase.UIType.Button(el)
        return el

    def tapRequestQuote(self):
        el = self.getRequestQuote()
        el.tap()
