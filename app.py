from flask import Flask, render_template, jsonify
app = Flask(__name__)

jobs=[
    {
        'id':1,
        'title':'Data Analyst',
        'Location':'Bengaluru',
        'Salary':'Rs 1,000,000'
    },
    {
        'id':2,
        'title':'Python developer',
        'Location':'Mumbai',
        'Salary':'Rs 1,000,000'
    },
    {
        'id':3,
        'title':'Data science',
        'Location':'USA',
    },
    {
        'id':4,
        'title':'Java developer',
        'Location':'Hybrabad',
        'Salary':'3.5 LPA'
    }
]


@app.route("/")
@app.route("/home")
def homePage():
    return render_template("home.html", jobs = jobs)

@app.route("/api/jobs")
def list_jobs():
    return jsonify(jobs)

if __name__=="__main__":
    app.run(debug=True)