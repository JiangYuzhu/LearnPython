#http://python.jobbole.com/87309/?utm_source=blog.jobbole.com&utm_medium=relatedPosts
#其中一节关于数据库连接的装饰器
# import 
def connect_db():
    print('connect db')
    # dbname = input()
    # connect()
def close_db():
    print('Close the db ....')
    # close()
def decorator_db(f):
    def wrapper(*args,**kwargs):
        connect_db()
        f(*args,**kwargs)
        close_db()
    return wrapper
@decorator_db
def query_user():
    print('query some user')
query_user()