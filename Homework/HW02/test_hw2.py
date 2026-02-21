import unittest
from hw2 import Profile, Activity, Post, Message, User

class TestProfile(unittest.TestCase):
    """Test cases for the Profile class."""
    def setUp(self):
        self.test_user = Profile('user1','pass1','username1','email1@example.com')
    
    def test_profile_str(self):
        self.assertEqual(str(self.test_user),"Profile - Username: user1, Screen Name: username1, Email: email1@example.com")
    
    def test_modify_profile(self):
        self.test_user.modify_profile('mod_pass1','mod_username1','mod_email1@example.com')
        self.assertEqual(str(self.test_user),"Profile - Username: user1, Screen Name: mod_username1, Email: mod_email1@example.com")
    

class TestActivity(unittest.TestCase):
    """Test cases for the Activity class."""
    def setUp(self):
        self.test_user = User('user1','pass1','username1','email1@example.com')
        self.test_activity = Activity(self.test_user,'testcontent123')
    
    def test_activity_str(self):
        self.assertEqual(f'{self.test_activity}',"Activity - User: user1, Content: testcontent123")
#                                           "Activity - User: {self.user.profile.username}, Content: {self.content}"

class TestPost(unittest.TestCase):
    """Test cases for the Post class."""
    def setUp(self):
        self.test_user = User('user1','pass1','username1','email1@example.com')
        self.test_post = Post(self.test_user,'testcontent123')
    
    def test_activity_str(self):
        self.assertEqual(f'{self.test_post}',"Post - Activity - User: user1, Content: testcontent123")
        

class TestMessage(unittest.TestCase):
    """Test cases for the Message class."""
    def setUp(self):
        self.test_user = User('user1','pass1','username1','email1@example.com')
        self.test_receiver = User('user2','pass2','username2','email2@example.com')
        # requires 2 users
        self.test_message = Message(self.test_user, 'testmessage123', self.test_receiver)

    def test_activity_str(self):
        self.assertEqual(f'{self.test_message}',"Message - Activity - User: user1, Content: testmessage123, Receiver: user2")
        # "Message - Activity - User: {self.user.profile.username}, Content: {self.content}, Receiver: {self.receiver.profile.username}"

class TestUser(unittest.TestCase):
    """Test cases for the User class."""
    # Add more test cases for other methods and classes
    
    def setUp(self):
        self.user = User("user1", "password1", "User One", "user1@example.com")
        self.user2 = User("user2", "password1", "User Two", "user2@example.com")
        
    def test_create_post(self):
        """Test creating a post for a user."""
        
        post = self.user.create_post("Test Post Content")

        # Check if the post is added to the user's posts list
        self.assertIn(post, self.user.posts)
        # Check if the user is correct
        self.assertEqual(post.user, self.user)
        # Check if the content of the post is correct
        self.assertEqual(post.content, "Test Post Content")
    
    def test_create_message(self):

        mess = self.user.send_message(self.user2,"Test Message Content")

        # Check if the post is added to the user's posts list
        self.assertIn(mess, self.user.messages)
        # Check if the user is correct
        self.assertEqual(mess.user, self.user)
        # Check if the content of the post is correct
        self.assertEqual(mess.content, "Test Message Content")
    
    def test_str_output(self):
        self.assertEqual(str(self.user), "User - Profile - Username: user1, Screen Name: User One, Email: user1@example.com")

    

if __name__ == "__main__":
    unittest.main()
    
