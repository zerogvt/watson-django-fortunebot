from django.test import TestCase


# Create your tests here.
from fortunebot import fortunebot as fb
from fortunebot.fortunebot import getIndex

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