from flask import Flask, render_template, request
#from flask.ext.sqlalchemy import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
#from Send_email import send_email
from sqlalchemy.sql import func

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres123@localhost/height_collector'
db = SQLAlchemy(app)


class Data(db.Model):
    __tablename__ = "data"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    height = db.Column(db.Integer)

    def __init__(self, email, height):
        self.email = email
        self.height = height


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/success", methods=['POST'])
def success():
    if request.method == 'POST':
        email = request.form['email_name']
        height = request.form['height_name']
        print(email)
        print(height)
        #send_email(email,height)
        if db.session.query(Data).filter(Data.email==email).count()==0:
            data= Data(email,height)
            db.session.add(data)
            db.session.commit()
            average_height= db.session.query(func.avg(Data.height)).scalar()
            average_height=round(average_height)
            count=db.session.query(Data.height).count()
            print(count)
            print(average_height)
            return render_template("success.html")

        return render_template('index.html',text="Email already exists!!")




if __name__ == '__main__':
    app.debug = True
    app.run(port=5000,host="0.0.0.0")
