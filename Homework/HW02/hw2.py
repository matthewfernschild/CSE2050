###############################################################################
# Collaboration                                                               #
# -------------                                                               #
# You can collaborate with your classmates. If you do so, remember not to     #
# share code directly. Discussions are fine, code sharing is not. Also note   #
# that all have to submit individually.                                       #
###############################################################################

class Profile:
    """Class representing a user's profile. Incl username, password, screen name, and email"""
    # TODO :Implement __init__ method
    # Make sure you add a docstring to all methods.
    def __init__(self,username,password,screen_name,email):
        '''Initializes the Profile Class & its' variables'''
        self.username = username
        self.password = password
        self.screen_name = screen_name
        self.email = email

    def __str__(self):
        """ Return a string representation of the Profile."""
        return f"Profile - Username: {self.username}, Screen Name: {self.screen_name}, Email: {self.email}"
   
    def modify_profile(self, password=None, screen_name=None, email=None):
        self.password = password
        self.screen_name = screen_name
        self.email = email

class Activity:
    """Base class representing an activity."""
    # TODO :Implement __init__ method
    def __init__(self, user, content):
        self.user = user
        self.content = content
    
    def __str__(self):
        """ Return a string representation of the Activity."""
        return f"Activity - User: {self.user.profile.username}, Content: {self.content}"


class Post(Activity):
    """Class representing a user's post."""
    def __init__(self, user, content):
        """ Initialize a Post instance. """
        super().__init__(user, content)

    def __str__(self):
        """ Return a string representation of the Post. """
        return f"Post - {super().__str__()}"
    

class Message(Activity):
    """Class representing a user's message to another user."""
    # TODO :Implement __init__ method
    def __init__(self, user, content, receiver):
        super().__init__(user, content)
        self.receiver = receiver

    def __str__(self):
        """ Return a string representation of the Message."""
        return f"Message - {super().__str__()}, Receiver: {self.receiver.profile.username}"


class User:
    """Class representing a user in the social network."""
    # TODO :Implement __init__ method
    def __init__(self,username, password, screen_name, email):
             self.profile = Profile(username, password, screen_name, email)
             self.posts = []
             self.messages = []
             

    def create_post(self, content):
        """Create a new post for the user.
        Args:
            content (str): The content of the post.

        Returns:
            Post: The created post.

        Raises:
            ValueError: If the content of the post is empty.
        """
        # TODO :Implement create_post method
        if content == '':
            raise ValueError("Post content cannot be empty")
        
        post = Post(self, content) # after staring at my code for 
        # 25 minutes i finally realized that i need to actually call the classes i coded. 
        # this fixed the remaining issues

        self.posts.append(post)
        return post


    def send_message(self, receiver, content):
        """Send a message from the user to the specified receiver.

        Args:
            receiver (User): The user receiving the message.
            content (str): The content of the message.

        Returns:
            Message: The created message.

        Raises:
            ValueError: If the receiver ID or message content is empty.
        """
        # TODO :Implement send_message method
        if receiver == '' or content == '':
            raise ValueError("Post content cannot be empty")
        # thought this part wasnt working. it was working i just misread, 
        # but it told me to use raise instead of return. sounds right

        message = Message(self,content,receiver) # creates Message obj

        self.messages.append(message)
        return message

    def __str__(self):
        """ Return a string representation of the User."""
        return f"User - {self.profile}"

# Example usage:
if __name__ == "__main__":
    user1 = User("user1", "password1", "User One", "user1@example.com")
    user2 = User("user2", "password2", "User Two", "user2@example.com")

    post1 = user1.create_post("This is my first post!")
    message1 = user2.send_message(user1, "Hi User One! How are you?")
    print(post1)
    print(message1)
    user1.profile.modify_profile(email="User1_1@uconn.edu")
    print(user1)
    print(user2)

