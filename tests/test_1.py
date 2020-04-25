import pytest
from model.group import group
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_test_add_empty_group(self):
    self.app.login(user='admin', password='secret')
    self.app.create_group(group(name='', header='', footer=''))
    self.app.logout()

def test_test_add_group(self):
    self.app.login(user='admin', password='secret')
    self.app.create_group(group(name='ljfsalrekj', header=';lkj', footer='lkjh'))
    self.app.logout()
