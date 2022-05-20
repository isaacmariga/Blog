import unittest
from app.models import Group

class TestGroup(unittest.TestCase):
    def setUp(self):
        self.new_group = Group(name="Pick-up lines" )

    def test_instance(self):
        self.assertTrue( isinstance( self.new_group, Group) )

    def test_save_group(self):
        self.new_group.save_group()

        self.assertTrue( len(Group.query.all()) > 0 )

    def test_get_groups(self):
        self.new_group.save_group()

        test_group = Group(name="Product Pitches")

        test_group.save_group()

        gotten_groups = Group.get_groups()

        self.assertTrue( len(gotten_groups) == len(Group.query.all()) )

