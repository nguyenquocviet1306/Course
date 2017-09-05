from project.tests import *

class TestStudentsController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='students', action='index'))
        # Test response...
