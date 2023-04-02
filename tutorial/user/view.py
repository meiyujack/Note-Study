from . import user
from apiflask.schemas import Schema
from apiflask.fields import String
from apiflask.validators import Length

class Hello(Schema):
    username=String(required=True,validate=Length(1,8))


@user.get("/")
def index():
    return "<form method='post'><input type='text' name='username'/><input type='submit'/></form>"


# @user.get("/")
# def index():
#     return "这是从user蓝图加载的视图函数"

@user.post('/')
@user.input(Hello,location="form")
def user(data):
    return f"<h1>你输入了{data['username']}</h1>"
