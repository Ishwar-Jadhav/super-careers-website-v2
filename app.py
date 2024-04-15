from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {'id' : 1, 
     'title' : 'Data Analyst', 
     'location' : 'Texas, USA',
     'salary' : '$90,000'
    },
    {'id' : 2, 
     'title' : 'Data Scientist', 
     'location' : 'Miami, USA',
     'salary' : '$115,000'
    },
    {'id' : 3, 
     'title' : 'Frontend Engineer', 
     'location' : 'Remote',
     'salary' : '$130,000'
    },
    {'id' : 4, 
     'title' : 'Backend Engineer', 
     'location' : 'San Fransico, USA',
     'salary' : '$150,000'
    },
]


@app.route("/")
def hello_super():
    return render_template('home.html', 
                           jobs = JOBS,
                          company_name = 'Super')

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
        app.run(host='0.0.0.0', debug = True)