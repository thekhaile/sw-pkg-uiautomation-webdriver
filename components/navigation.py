from time import sleep
from projectBase import ProjectBase

class Navigation(object):
    LOGIN_PAGE = 'https://southwire-configurator-test.firebaseapp.com/login'
    PROJECTS_PAGE= 'https://southwire-configurator-test.firebaseapp.com/projects'
    REGISTRATION_PAGE = 'https://southwire-configurator-test.firebaseapp.com/register'
    ACCOUNT_PAGE = 'https://southwire-configurator-test.firebaseapp.com/account'

    def __init__(self, testCase):
        # type: (ProjectBase) -> None
        """
        :param testCase: will be the ProjectBase object when a test is run.
        """
        self.testCase = testCase

    def navigateToLoginPage(self):
        self.testCase.driver.get(Navigation.LOGIN_PAGE)

    def navigateToProjectsPage(self):
        self.testCase.driver.get(Navigation.PROJECTS_PAGE)

    def navigateToRegistrationPage(self):
        self.testCase.driver.get(Navigation.REGISTRATION_PAGE)

    def navigateToAccountPage(self):
        self.testCase.driver.get(Navigation.ACCOUNT_PAGE)

    # breadcrumbs
    def tapProjectBreadcrumb(self):
        container = self.testCase.app.findElement(self.testCase.app.getStrategy().CSS_SELECTOR, 'ul.breadcrumbs')
        breadcrumbs = container.find_elements(self.testCase.app.getStrategy().CSS_SELECTOR, 'a')
        el = breadcrumbs[0]
        el = self.testCase.UIType.Element(el)
        el.tap()

    def tapJobBreadcrumb(self):
        container = self.testCase.app.findElement(self.testCase.app.getStrategy().CSS_SELECTOR, 'ul.breadcrumbs')
        breadcrumbs = container.find_elements(self.testCase.app.getStrategy().CSS_SELECTOR, 'a')
        el = breadcrumbs[1]
        el = self.testCase.UIType.Element(el)
        el.tap()

    def tapJobDetailBreadcrumb(self):
        container = self.testCase.app.findElement(self.testCase.app.getStrategy().CSS_SELECTOR, 'ul.breadcrumbs')
        breadcrumbs = container.find_elements(self.testCase.app.getStrategy().CSS_SELECTOR, 'a')
        el = breadcrumbs[-1]
        el = self.testCase.UIType.Element(el)
        el.tap()

