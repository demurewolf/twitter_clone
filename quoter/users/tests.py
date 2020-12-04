from django.test import TestCase

from django.contrib.auth.models import User

from users.models import Profile, Follow

class FollowModelTestCase(TestCase):
    def setUp(self):
        u1 = User.objects.create(username="user_1")
        u2 = User.objects.create(username="user_2")
        u3 = User.objects.create(username="user_3")

        Profile.objects.create(user=u1)
        Profile.objects.create(user=u2)
        Profile.objects.create(user=u3)

        Follow.objects.create(dst_user=u1, src_user=u2)
        Follow.objects.create(dst_user=u1, src_user=u3)

    def test_follower_property(self):
        user = User.objects.get(username="user_1")
        user_profile = Profile.objects.get(user=user)
        
        follower_count = user_profile.follower_count

        self.assertEqual(follower_count, 2)

    def test_no_followers_property(self):
        user = User.objects.get(username="user_2")
        user_profile = Profile.objects.get(user=user)

        follower_count = user_profile.follower_count

        self.assertEqual(follower_count, 0)

class FollowViewTestCase(TestCase):
    def setUp(self):
        pass

    def test_view(self):
        pass