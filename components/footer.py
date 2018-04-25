__author__ = 'ningxinliao'
from time import sleep
from projectBase import ProjectBase
import string
import random

class Footer(object):

    def __init__(self, testCase):
        # type: (ProjectBase) -> None
        """
        :param testCase: will be the ProjectBase object when a test is run.
        """
        self.testCase = testCase

    def getContractorSolutionsLink(self):
        footerList = self.testCase.app.findElements(self.testCase.app.getStrategy().CSS_SELECTOR, 'a.footer-item')
        el = footerList[4]
        el = self.testCase.UIType.Element(el)
        return el.getLabel()

    def tapContractorSolutionsLink(self):
        el = self.getContractorSolutionsLink()
        el.tap()

    def getLegalDisclaimer(self):
        footerList = self.testCase.app.findElements(self.testCase.app.getStrategy().CSS_SELECTOR, 'a.footer-item')
        el = footerList[5]
        el = self.testCase.UIType.Element(el)
        return el.getLabel()

    def tapLegalDisclaimer(self):
        el = self.getLegalDisclaimer()
        el.tap()

    def getContactEmail(self):
        email = self.testCase.app.findElement(self.testCase.app.getStrategy().CSS_SELECTOR, 'span.footer-item')
        email = self.testCase.UIType.Element(email)
        return email.getLabel()

    def getTwitterIcon(self):
        container = self.testCase.app.findElement(self.testCase.app.getStrategy().CSS_SELECTOR, 'div.footer-group.icons')
        icons = container.find_elements(self.testCase.app.getStrategy().CSS_SELECTOR, 'img')
        el = icons[0]
        el = self.testCase.UIType.Button(el)
        return el.ui_object.get_attribute('alt')

    def getFacebookIcon(self):
        container = self.testCase.app.findElement(self.testCase.app.getStrategy().CSS_SELECTOR, 'div.footer-group.icons')
        icons = container.find_elements(self.testCase.app.getStrategy().CSS_SELECTOR, 'img')
        el = icons[1]
        el = self.testCase.UIType.Button(el)
        return el.ui_object.get_attribute('alt')

    def getLinkedinIcon(self):
        container = self.testCase.app.findElement(self.testCase.app.getStrategy().CSS_SELECTOR, 'div.footer-group.icons')
        icons = container.find_elements(self.testCase.app.getStrategy().CSS_SELECTOR, 'img')
        el = icons[2]
        el = self.testCase.UIType.Button(el)
        return el.ui_object.get_attribute('alt')

    def getYoutubeIcon(self):
        container = self.testCase.app.findElement(self.testCase.app.getStrategy().CSS_SELECTOR, 'div.footer-group.icons')
        icons = container.find_elements(self.testCase.app.getStrategy().CSS_SELECTOR, 'img')
        el = icons[2]
        el = self.testCase.UIType.Button(el)
        return el.ui_object.get_attribute('alt')
