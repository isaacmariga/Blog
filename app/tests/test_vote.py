import unittest
from app.models import Vote

class TestVote(unittest.TestCase):
    def setUp(self):
        self.new_vote = Vote(vote_number=0 )


    def test_instance(self):
        self.assertTrue( isinstance( self.new_vote, Vote) )

    def test_save_vote(self):
        self.new_vote.save_vote()
        self.assertTrue( len(Vote.query.all()) > 0 )

    def test_get_votes(self):
        self.new_vote.save_vote()
        gotten_votes = Vote.get_votes(4,4)
        self.assertFalse( len(gotten_votes) , 1)

    def test_num_vote(self):
        self.new_vote.save_vote()
        gotten_votes = Vote.num_vote(1)

        self.assertEqual( gotten_votes , 0)


