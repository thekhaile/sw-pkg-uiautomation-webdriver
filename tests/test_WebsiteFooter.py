__author__ = 'ningxinliao'
import sys, os
from time import sleep
from projectBase import ProjectBase
import pytest
from southwire_pkg_uiautomation_webdriver.components.navigation import Navigation
from southwire_pkg_uiautomation_webdriver.components.authentication import Authentication
from southwire_pkg_uiautomation_webdriver.components.project import Project
from southwire_pkg_uiautomation_webdriver.components.footer import Footer


import unidecode

class TestWebsiteFooter(ProjectBase):
    PROJECTS_PAGE = 'https://southwire-configurator-test.firebaseapp.com/projects'

    def __init__(self, *args, **kwargs):
        super(TestWebsiteFooter, self).__init__(*args, **kwargs)
        self.navigation = Navigation(self)
        self.authentication = Authentication(self)
        self.projects = Project(self)
        self.footer = Footer(self)

    @pytest.mark.ac
    def testContractorSolutionsLinkIsDisplayed(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1381322
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        sleep(3)
        footer = self.footer.getContractorSolutionsLink()

        self.assertion.assertEqual(footer, 'ContractorSolutions.Southwire.com')

    @pytest.mark.ac
    def testLegalDisclaimerIsDisplayed(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1381324
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        sleep(3)
        footer = self.footer.getLegalDisclaimer()

        self.assertion.assertEqual(footer, 'Legal Disclaimer')

    @pytest.mark.ac
    def testContactEmailIsDisplayed(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1381326
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        sleep(3)
        footer = self.footer.getContactEmail()

        self.assertion.assertEqual(footer, 'ProjectConstructionTeam@Southwire.com')

    @pytest.mark.ac
    def testTwitterIconIsDisplayed(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1381327
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        sleep(3)
        footer = self.footer.getTwitterIcon()

        self.assertion.assertExists(footer)

    @pytest.mark.ac
    def testFacebookIconIsDisplayed(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 138129
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        sleep(3)
        footer = self.footer.getFacebookIcon()

        self.assertion.assertExists(footer)

    @pytest.mark.ac
    def testLinkedinIconIsDisplayed(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 138131
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        sleep(3)
        footer = self.footer.getLinkedinIcon()

        self.assertion.assertExists(footer)

    @pytest.mark.ac
    def testYoutubeIconIsDisplayed(self):
        email = 'ningxin.liao@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 138133
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        sleep(3)
        footer = self.footer.getYoutubeIcon()

        self.assertion.assertExists(footer)