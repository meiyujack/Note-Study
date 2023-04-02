from apiflask import APIFlask
from user import user


app=APIFlask(__name__)

app.register_blueprint(user,url_index="/")

@app.route('/')
def index():
    return "Hello, World"
