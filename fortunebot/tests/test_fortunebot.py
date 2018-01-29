from django.test import TestCase
import unittest 
from unittest.mock import patch

# Create your tests here.
from fortunebot import fortunebot as fb
from fortunebot.fortunebot import getIndex
from fortunebot import webhooks
from fortunebot import watson_message
from fortunebot import config
from fortunebot import weather
from fortunebot import auth

class FBTest(TestCase):


    def test_init(self):
        print(fb.getNumFortunes())
        fb.getFortune()
        assert fb.getNumFortunes() > 0


    def test_getFortune_repeatable(self):
        for i in range(100):
            assert fb.getFortune() != None


    def test_indexFortune(self):
        myindex = {}
        saying1 = "one two three four five"
        fb.indexData(myindex, saying1, 8)
        saying2 = "one two three four"
        fb.indexData(myindex, saying2, 10)
        assert myindex["one"][0] == 8
        assert myindex["one"][1] == 10
        assert len(myindex["five"]) == 1


    def test_index(self):
        for key in ["computer", "nerd", "future", "black"]:
            assert fb.getFortuneWIndex(key) != None

    @patch('fortunebot.watson_message.sendSimpleMessage')
    @patch('fortunebot.auth.authenticateApp')
    def test_webhook_oscar(self, mock_auth, mock_send):
        mock_auth.return_value = 'MOCK_TOKEN'
        msg = {'spaceId': 'test_space', 'content' : config.OSCAR_TRIGGER}
        webhooks._parseMessage(msg)
        mock_send.assert_called_once_with('test_space', unittest.mock.ANY)

    @patch('fortunebot.watson_message.sendSimpleMessage')
    @patch('fortunebot.weather.process')
    @patch('fortunebot.auth.authenticateApp')
    def test_webhook_weather(self, mock_auth, mock_process, mock_send):
        mock_auth.return_value = 'MOCK_TOKEN'
        msg = {'spaceId': 'test_space',
               'content' : config.WEATHER_TRIGGER +' IE'}
        webhooks._parseMessage(msg)
        mock_process.assert_called_once_with(unittest.mock.ANY)
