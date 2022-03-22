from flask import *

app=Flask(__name__)
@app.route('/login',methods=['POST'])
def login():
    #return render_template('base.html') # redering html content
     uname=request.form['uname']
     passwrd=request.form['pass']
     if uname=='cherry'and passwrd=="google":
         return "welcome %s"%uname
     else:
        return 'invalid'

"""def admin():
    return 'i am admin'
    app.add_url_rule('/admin','admin',admin) #accessing pages by using add_url_rule.....
@app.route('/student/<int:sub>')            #integer passing through URL
def student(sub):
    return 'i am student=%d'%sub
@app.route('/staff')                       #accessing pages by using app.route........
def staff():
    return 'i am staff'
@app.route('/user/<name>')
def user(name):
    if name=='admin':
        return redirect(url_for('admin'))
    if name=='student':
        return redirect(url_for('student'))
    if name=='staff':
        return redirect(url_for('staff'))"""

if __name__=='__main__':
    app.run(debug=True)