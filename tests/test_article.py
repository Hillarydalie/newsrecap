import unittest
from .app import models

class ArticleTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Article class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Article(
            "Emily Price",
            "How to Get the Twitch Apple TV App Now", 
            "Twitch’s Apple TV app is in public beta now, which means anyone can get the beta version of the app on their Apple TV. Read more...", 
            "https://lifehacker.com/how-to-get-the-twitch-apple-tv-app-now-1837952341", 
            "https://i.kinja-img.com/gawker-media/image/upload/s--2PItfuaw--/c_fill,fl_progressive,g_center,h_900,q_80,w_1600/obehcypyngupxysabz6h.jpg", 
            "2019-09-07T13:40:00Z")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))