from time import sleep
from projectBase import ProjectBase
import pytest
from southwire_pkg_uiautomation_webdriver.components.navigation import Navigation
from southwire_pkg_uiautomation_webdriver.components.authentication import Authentication
from southwire_pkg_uiautomation_webdriver.components.project import Project
from southwire_pkg_uiautomation_webdriver.components.projectList import ProjectList
from southwire_pkg_uiautomation_webdriver.components.job import Job


class TestProjectList(ProjectBase):

    def __init__(self, *args, **kwargs):
        super(TestProjectList, self).__init__(*args, **kwargs)
        self.navigation = Navigation(self)
        self.authentication = Authentication(self)
        self.project = Project(self)
        self.projectList = ProjectList(self)
        self.job = Job(self)


    @pytest.mark.ac
    def testCurrentProjectListIsPresented(self):
        email = 'ningxin.liao+testProjectList@mutualmobile.com'
        password = 'password'
        self.caseId = 1301862

        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        projectCount = self.projectList.getProjectCount()
        self.assertion.assertEqual(projectCount, 3)

    @pytest.mark.ac
    def testProjectNameIsPresented(self):
        email = 'ningxin.liao+testProjectList@mutualmobile.com'
        password = 'password'
        self.caseId = 1301863

        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        sleep(2)
        name = self.projectList.getProjectName()
        self.assertion.assertEqual(name, 'project 3')

    @pytest.mark.ac
    def testNumberOfJobIsPresented(self):
        email = 'ningxin.liao+testProjectList@mutualmobile.com'
        password = 'password'
        self.caseId = 1301864

        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        sleep(2)
        jobCount = self.projectList.getProjectJobCount()
        self.assertion.assertEqual(jobCount, '2')

    @pytest.mark.ac
    def testCreatedDateIsPresented(self):
        email = 'ningxin.liao+testProjectList@mutualmobile.com'
        password = 'password'
        self.caseId = 1301865

        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        date = self.projectList.getProjectDate()
        self.assertion.assertEqual(date, '4/23/2018')

    @pytest.mark.ac
    def testMostRecentProjectIsOnTheTopOfProjectList(self):
        email = 'ningxin.liao+testProjectList@mutualmobile.com'
        password = 'password'
        self.caseId = 1301866

        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        sleep(2)
        name = self.projectList.getProjectName()
        self.assertion.assertEqual(name, 'project 3')