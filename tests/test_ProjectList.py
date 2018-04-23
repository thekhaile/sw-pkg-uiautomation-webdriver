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
        email = 'ningxin.liao+test3@mutualmobile.com'
        password = 'password'
        self.caseId = 1301862

        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        oldValue = self.projectList.getProjectCount()
        self.projectList.tapCreateProject()
        sleep(2)
        self.project.enterRandomProjectName()
        sleep(3)
        self.project.tapSubmit()
        sleep(2)
        newValue = self.projectList.getProjectCount()
        self.assertion.assertEqual(oldValue, newValue - 1 )

    @pytest.mark.ac
    def testProjectNameIsPresented(self):
        email = 'ningxin.liao+test3@mutualmobile.com'
        password = 'password'
        self.caseId = 1301863

        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        sleep(2)
        name = self.projectList.getProjectName()
        self.assertion.assertExists(name)

    @pytest.mark.ac
    def testNumberOfJobIsPresented(self):
        email = 'ningxin.liao+test3@mutualmobile.com'
        password = 'password'
        self.caseId = 1301864

        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        sleep(2)
        self.projectList.tapCreateProject()
        sleep(2)
        self.project.enterRandomProjectName()
        sleep(3)
        self.project.tapSubmit()
        sleep(2)
        self.projectList.selectAProject()
        self.job.createAJob()
        self.navigation.navigateToProjectsPage()
        sleep(2)
        jobCount = self.projectList.getProjectJobCount()
        self.assertion.assertEqual(jobCount, '1')

    @pytest.mark.ac
    def testCreatedDateIsPresented(self):
        email = 'ningxin.liao+test3@mutualmobile.com'
        password = 'password'
        self.caseId = 1301865

        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        date = self.projectList.getProjectDate()
        self.assertion.assertExists(date)

    @pytest.mark.ac
    def testMostRecentProjectIsOnTheTopOfProjectList(self):
        email = 'ningxin.liao+test3@mutualmobile.com'
        password = 'password'
        self.caseId = 1301866

        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        sleep(2)
        oldValue = self.projectList.getProjectName()
        self.projectList.tapCreateProject()
        sleep(2)
        self.project.enterRandomProjectName()
        sleep(3)
        self.project.tapSubmit()
        sleep(2)
        newValue = self.projectList.getProjectName()
        self.assertion.assertNotEqual(oldValue, newValue)