import unittest
from app.models import Pitch

class TestPitch(unittest.TestCase):
    def setUp(self):
        self.new_pitch = Pitch( pitch_content="I am Groot")


    def test_instance(self):
        self.assertTrue( isinstance( self.new_pitch, Pitch) )

    def test_save_pitch(self):
        self.new_pitch.save_pitch()
        self.assertTrue( len(Pitch.query.all()) > 0)

    def test_get_pitches(self):
        self.new_pitch.save_pitch()
        gotten_pitches = Pitch.get_pitches(4990826417581240726341234)
        self.assertFalse( len(gotten_pitches) == 1)



