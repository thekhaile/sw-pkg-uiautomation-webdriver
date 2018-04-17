from time import sleep
import random
from projectBase import ProjectBase
import pytest
from southwire_pkg_uiautomation_webdriver.components.navigation import Navigation
from southwire_pkg_uiautomation_webdriver.components.authentication import Authentication
from southwire_pkg_uiautomation_webdriver.components.projects import Projects

class TestProjects(ProjectBase):
    PROJECTS_PAGE = 'https://southwire-configurator-test.firebaseapp.com/projects'

    def __init__(self, *args, **kwargs):
        super(TestProjects, self).__init__(*args, **kwargs)
        self.navigation = Navigation(self)
        self.authentication = Authentication(self)
        self.projects = Projects(self)

    @pytest.mark.ac
    def testCreateAProjectSuccessfully(self):
        # Verify that user is able to create a project
        email = 'tuan.nguyen+15usa@mutualmobile.com'
        password = 'Test123!'

        self.caseId = 1301712
        randomNumber = random.random()
        projectName = ("Project %f" %randomNumber)

        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projects.tapCreateProject()
        sleep(2)
        self.projects.enterProjectName(projectName)
        sleep(3)
        self.projects.tapSubmit()

        viewProjectName = self.projects.getProjectName(rowOrder=0)

        self.assertion.assertEqual(projectName, viewProjectName)

    @pytest.mark.ac
    def testcancelProjectCreation(self):
        # Verify that user can cancel a project creation at anytime
        email = 'khai.le+SW1@mutualmobile.com'
        password = 'password'
        self.caseId = 1301717

        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projects.tapCreateProject()
        sleep(2)
        currentUrl = self.driver.current_url
        self.projects.tapCancelButton()
        sleep(2)
        newUrl = self.driver.current_url

        self.assertion.assertNotEqual(currentUrl, newUrl)

    @pytest.mark.ac
    def testUniqueProjectName(self):
        # Precondition: Account that had a project name = "Project one"
        # Verify that project name is unique
        email = 'tuan.nguyen+15usa@mutualmobile.com'
        password = 'Test123!'
        self.caseId = 1301713

        projectName = "Project one"
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projects.tapCreateProject()
        sleep(2)
        self.projects.enterProjectName(projectName)
        sleep(2)
        self.projects.tapSubmit()
        sleep(2)
        expectedErrorMsg = 'Project name already exists'
        actualErrorMsg = self.projects.getErrorMsg()

        self.assertion.assertEqual(expectedErrorMsg, actualErrorMsg)

    @pytest.mark.ac
    def testCreateProjectNameOver30characters(self):
        # Verify that when user entered more than 30 characters, error message is displayed
        email = 'tuan.nguyen+15usa@mutualmobile.com'
        password = 'Test123!'
        self.caseId = 1301719

        projectName = "Project that is over 30 characters"
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projects.tapCreateProject()
        sleep(2)
        self.projects.enterProjectName(projectName)
        sleep(2)
        expectedErrorMsg = 'Project Name cannot exceed 30 characters.'
        actualErrorMsg = self.projects.getErrorMsg()

        self.assertion.assertEqual(expectedErrorMsg, actualErrorMsg)

    @pytest.mark.ac
    def testEmptyProjectName(self):
        # Verify that when user did not enter project name(empty), the save button is disable
        email = 'tuan.nguyen+15usa@mutualmobile.com'
        password = 'Test123!'
        self.caseId = 1301727


        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projects.tapCreateProject()
        sleep(2)
        el = self.projects.getSubmitButton()
        self.assertion.assertFalse(el.isEnabled())


