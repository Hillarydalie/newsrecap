import unittest
from .app.models import Article

Sources = article.Sources

class SourcesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Article class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Sources(
            'abc-news',
            'ABC News',
            'Your trusted source for breaking news',
            'https://abcnews.go.com','general',
            'en',
            'us')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Sources))
