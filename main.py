import mysql.connector
from instagramy import InstagramPost
import Post
print("hello")
print("i dont know if this is being commitedd")

connection = mysql.connector.connect(host='localhost',
                                         database='cats',
                                         user='root',
                                         )
if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)                                         

                            
post = InstagramPost("Ccx1A_cIXVl")

#print(post.author)
#print(post.number_of_comments)
#print(post.number_of_likes)
#aPost = Post('khizar','Ccx1A_cIXVl')
#aPost.getLikes

