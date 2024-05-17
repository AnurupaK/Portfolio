from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates', static_folder='static')



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_email', methods=['POST'])
def send_email():
    fullname = request.form['fullname']
    email = request.form['email']
    subject = request.form['subject']
    mobile = request.form['mob_number']
    message_body = request.form['message']

    

    return render_template('index.html', fullname=fullname, email=email, subject=subject, mobile=mobile, message=message_body, success=True)
    

if __name__ == '__main__':
    app.run(debug=True)
