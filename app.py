from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
  'id': 1,
  'title': 'Trader',
  'location': 'Paris, FR',
  'salary': '$400,000',
}, {
  'id': 2,
  'title': 'Energy Trader',
  'location': 'Dubai, UAE',
  'salary': '$550,000'
}, {
  'id': 3,
  'title': 'Oil Trader',
  'location': 'London, UK',
  'salary': '$1,000,000'
}]


@app.route("/")
def hello_job():
  return render_template('home.html', jobs=JOBS, company_name="Finance")


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0', debug=True)
