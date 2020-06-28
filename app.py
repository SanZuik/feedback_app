from flask import Flask,render_template,request,url_for,flash,redirect
from flask_sqlalchemy import SQLAlchemy
from send_main import send_mail



app =Flask(__name__)
app.config['SECRET_KEY'] = "Iwanttodeploy"

ENV = 'prod'

if ENV == 'dev':
    app.debug=True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost/p_1'

else:
    app.debug=False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://hkmxeflurnmgri:dacc44a3ea2a17074f9986b1591875163a57901e9503c3bc334445cae58119ab@ec2-54-236-169-55.compute-1.amazonaws.com:5432/d70navkdg9labe'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)

class Feedback(db.Model):
    __tablename__ = 'feedback'
    id = db.Column(db.Integer,primary_key=True)
    customer = db.Column(db.String(200),unique=True)
    dealer = db.Column(db.String(200))
    rating = db.Column(db.Integer)
    comments = db.Column(db.Text())


    def __init__(self,customer,dealer,rating,comments):
        self.customer = customer
        self.dealer = dealer
        self.rating = rating
        self.comments = comments


    def __repr__(self):
        return self.customer
















@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit",methods=['GET','POST'])
def submit():
    if request.method =='POST':
        customer = request.form['customer']
        dealer = request.form['dealer']
        rating = request.form['rating']
        comments = request.form['comments']
        if customer=="" or dealer=="" or rating=="" or comments=="":
            
            return render_template('index.html',messages="please enter all the fields")

        if db.session.query(Feedback).filter(Feedback.customer== customer).count() == 0:
            data = Feedback(customer,dealer,rating,comments)
            db.session.add(data)
            db.session.commit()
            send_mail(customer,dealer,rating,comments)

            return render_template("success.html")
        return render_template('index.html',messages="you have already submmited the form")

        
    


if __name__=="__main__":
    app.run()


