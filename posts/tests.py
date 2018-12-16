from django.test import TestCase
from .models import Profile, Image, Comments
from django.contrib.auth.models import User

class ProfileTestClass(TestCase):
    """
    Test profile class and its functions
    """
    def setUp(self):
      
        #creating an new profile
        self.profile = Profile(bio='This is my bio', dp='name.jpg')

    def test_instance(self):
        self.assertTrue(isinstance(self.profile, Profile))

    def test_save_method(self):
        """
        Function to test that profile is being saved
        """
        self.profile.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)

    def test_delete_method(self):
        """
        Function to test that a profile can be deleted
        """
        self.profile.save_profile()
        self.profile.del_profile()

    def test_update_method(self):
        """
        Function to test that a profile's details can be updated
        """
        self.profile.save_profile()
        new_profile = Profile.objects.filter(bio='This is my bio').update(bio='Now this is the real bio')
        profiles = Profile.objects.get(bio='Now this is the real bio')
        self.assertTrue(profiles.bio, 'Now this is the real bio')


