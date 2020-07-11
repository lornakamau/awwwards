from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile, Project

class ProfileTestClass(TestCase):
    def setUp(self):
        self.lorna = User(username = "lorna", email = "lorna@gmail.com",password = "1234")
        self.profile = Profile(user= self.lorna, profile_pic='mepng',bio='bio', location='Nairobi, Kenya', email='lorna@gmail', link='www.profile.com')
        self.lorna.save()
        self.profile.save_profile()

    def tearDown(self):
        Profile.objects.all().delete()
        User.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.lorna, User))
        self.assertTrue(isinstance(self.profile, Profile))

    def test_edit_bio(self):
        self.profile.edit_bio('I am cool')
        self.assertEqual(self.profile.bio, 'I am cool')




