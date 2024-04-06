from unittest import TestCase, main
from project.social_media import SocialMedia


class TestSocialMedia(TestCase):
    def setUp(self):
        self.sm = SocialMedia("Ivan",
                              "Instagram",
                              20,
                              "Sport")

    def test__init__(self):
        self.assertEqual("Ivan", self.sm._username)
        self.assertEqual("Instagram", self.sm._platform)
        self.assertEqual(20, self.sm._followers)
        self.assertEqual("Sport", self.sm._content_type)
        self.assertEqual([], self.sm._posts)

    def test__incorrect_platform_type(self):
        with self.assertRaises(ValueError) as ve:
            sm = SocialMedia("Ivan",
                             "Facebook",
                             20,
                             "Sport")

        self.assertEqual(f"Platform should be one of ['Instagram', 'YouTube', 'Twitter']", str(ve.exception))

    def test_correct_platform_with_youtube(self):
        self.sm._validate_and_set_platform("YouTube")
        self.assertEqual("YouTube", self.sm._platform)

    def test_correct_platform_with_instagram(self):
        self.sm._validate_and_set_platform("Instagram")
        self.assertEqual("Instagram", self.sm._platform)

    def test_incorrect_platform_with_facebook_to_set_platform(self):
        with self.assertRaises(ValueError) as ve:
            self.sm._validate_and_set_platform("Facebook")

        self.assertEqual(f"Platform should be one of ['Instagram', 'YouTube', 'Twitter']", str(ve.exception))

    def test_with_negative_followers(self):
        with self.assertRaises(ValueError) as ve:
            self.sm.followers = -10

        self.assertEqual("Followers cannot be negative.", str(ve.exception))

    def test_with_correct_followers(self):
        self.sm.followers = 10

        self.assertEqual(10, self.sm._followers)

    def test_create_post(self):
        result = self.sm.create_post("Manchester United")
        expected_result = f"New {self.sm._content_type} post created by {self.sm._username} on {self.sm._platform}."
        self.assertEqual([{'content': "Manchester United", 'likes': 0, 'comments': []}], self.sm._posts)
        self.assertEqual(expected_result, result)

    def test_like_post_with_incorrect_index(self):
        self.sm.create_post("Manchester United")
        result = self.sm.like_post(10)
        self.assertEqual("Invalid post index.", result)

    def test_like_post_with_lower_likes_than_10(self):
        self.sm.create_post("Manchester United")
        result = self.sm.like_post(0)

        self.assertEqual(f"Post liked by {self.sm._username}.", result)

    def test_like_second_post_with_lower_likes_than_10(self):
        self.sm.create_post("Manchester United")
        self.sm.create_post("Arsenal")
        result = self.sm.like_post(1)

        self.assertEqual(f"Post liked by {self.sm._username}.", result)

    def test_like_post_with_10_likes(self):
        self.sm.create_post("Manchester United")
        for _ in range(10):
            self.sm.like_post(0)

        result = self.sm.like_post(0)
        self.assertEqual(f"Post has reached the maximum number of likes.", result)

    def test_comment_on_post_with_more_than_10_chars(self):
        self.sm.create_post("Manchester United")
        result = self.sm.comment_on_post(0, "Best team in the world")

        self.assertEqual(f"Comment added by {self.sm._username} on the post.", result)

    def test_comment_with_exactly_10_chars(self):
        self.sm.create_post("Manchester United")
        result = self.sm.comment_on_post(0, "1234567899")

        self.assertEqual("Comment should be more than 10 characters.", result)


if __name__ == "__main__":
    main()
