import os
import psycopg2
import psycopg2.extras

from flask import Flask, render_template, request, session
app = Flask(__name__)

app.secret_key = os.urandom(24).encode('hex')

def connectToDB():
    connectionString = 'dbname=[INSERT DB] user=[INSERT USER] password=[INSERT PASSWORD] host=localhost'
    print connectionString
    try:
        return psycopg2.connect(connectionString)
    except:
        print("Can't connect to Database")

@app.route('/')
def mainIndex():
    return render_template('index.html')
	
	
@app.route('/home')
def home():
    if request.method == 'POST':
        session['name'] = request.form['name']
        session['userID'] = request.form['userID']
    
    albumWeek = "John Mayer Trio"
    return render_template('home.html', album=albumWeek)


@app.route('/photos')
def showPhotos():
    isPhotoMonday = True
    return render_template('photos.html', photoMonday=isPhotoMonday)
    
    
@app.route('/aboutMe')
def showAboutMe():
    return render_template('aboutMe.html')
    
    
@app.route('/register', methods=['GET','POST'])
def showRegister():
    
    con = connectToDB()
    cur = con.cursor()
    if request.method == 'POST':
        try:
            cur.execute("""INSERT INTO regmembers (first, last, age, email) VALUES (%s, %s, %s, %s);""" ,(request.form['first'], request.form['last'], request.form['age'] ,request.form['email']))
            con.commit()
            print("Great Success!")
        except:
            print("ERROR inserting into regmembers")
            print("Tried: INSERT INTO regmembers (first, last, age, email) VALUES (%s, %s, %s) ,(request.form['first'],request.form['last'],request.form['age'],request.form['email']")
            con.rollback()
    
    try:
        cur.execute("select first,last from regmembers")
    except:
        print("Error executing select")
    results = cur.fetchall()
    return render_template('register.html',name=results)
    
    
@app.route('/register2', methods=['POST'])
def showRegister2():
    firstName = request.form['first']
    lastName = request.form['last']
    email = request.form['email']
    return render_template('register2.html',firNa = firstName, name=email)
    
@app.route('/contact')
def showContact():
    contact = {'insta':'deeee_a_go', 'cell':'123-456-7890', 'email':'thisisafakeemail@fake.com'}
    
    videos = [{'title':'Canon 5D Mk3 vs Mk2', 'vidLink':'OPnQiNUttl0', 'description':'(Same Price Kit) - Which One is Better?'},
    {'title':'Sigma 150-600 Contemporary "Real World Review"', 'vidLink':'F6tCUFXiDws', 'description':'The BEST Wildlife / Sports lens for under $1,000?'},
    {'title':'5 Reasons Why You Need a 50mm lens', 'vidLink':'PwmCrGVS3ZQ', 'description':'Everyone needs a 50mm lens'}]
    
    return render_template('contact.html', contact=contact, posts=videos)
    
# start the server
if __name__ == '__main__':
    app.run(host=os.getenv('IP', '0.0.0.0'), port =int(os.getenv('PORT', 8080)), debug=True)
