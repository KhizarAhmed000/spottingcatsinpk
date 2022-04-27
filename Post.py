
from instagramy import InstagramPost
class Post:#person is just a string to add in the post table
    #named it person to resolve some readability conflicts 
    #but on creation of object it is necessary to mention the correct user 
  
    def __init__(self,person,postID):
        self.person = person
        self.postID = postID

   # post = InstagramPost(postID)

    def addPost():
        #add to the database
        #to table 'post', add likes and comments and username
        #and um increment number of posts in table 'user'
        pass

    def updatePost():
        #update post likes n comments?
        pass

    def getLikes():
        #return post.number_of_likes
        print(person)
        

    def getComments():
        pass

    def getAuthor():
        pass

blabla = Post('khizar','aksjrlakjs')
blabla.getLikes()
    