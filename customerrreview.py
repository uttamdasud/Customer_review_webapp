from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
@app.route('/review')
def review():
    return render_template('review.html')

@app.route('/submit',methods = ['POST','GET'])
def submit():
   if request.method == 'POST':
      success = request.form
      return render_template("success.html",success=success) 

if __name__ == '__main__':
    app.run(debug=True)