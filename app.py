from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World"

@app.route("/about-us")
def about_us():
    about = '''
    Flask has become popular among Python enthusiasts. As of October 2020, it has second most stars on GitHub among Python web-development frameworks, only slightly behind Django,[13] and was voted the most popular web framework in the Python Developers Survey 2018.[14]
    
    '''
    return about

@app.route("/users/<int:id>")
def get_user_data_by_id(id):
    if id >=1 and id <=5:
        return "Welcome administrato"
    else:
        return "Welcome guesst"
        
  #  return "I am user with " + str(id)


if __name__ =='__main__':
    app.run(debug=True)