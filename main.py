from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
#creating a user model
class Events(db.Model):
  event_id = db.Column(db.Integer, primary_key = True)
  event_name = db.Column(db.String(100))
  event_place = db.Column(db.String(100))
  event_url = db.Column(db.String(1000))
  event_img_url = db.Column(db.String(1000))
  event_desc = db.Column(db.String(1000))

  def __init__(self, event_name, event_place, event_url, event_img_url, event_desc):
    self.event_name = event_name
    self.event_place = event_place
    self.event_url = event_url
    self.event_img_url = event_img_url
    self.event_desc = event_desc

def create_tables():
  with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/form", methods = ["POST", "GET"])
def form():
   if request.method == "POST":
    name = request.form["name"]
    place = request.form["place"]
    url = request.form["url"]
    img = request.form["img"]
    desc = request.form["desc"] 
    event = Events(event_name = name, event_place = place, event_url=url, event_img_url=img, event_desc=desc )
    db.session.add(event)
    db.session.commit()
    return redirect(url_for("views"))
   else:
     return render_template("form.html")

@app.route("/get-event/<event_id>", methods=["GET"])
def get_event(event_id):
    event_data = Events.query.get(event_id)
    if event_data:
        return jsonify({"id": event_data.event_id, 
        "name": event_data.event_name,
        "place": event_data.event_place,
        "img": event_data.event_img_url,
        "url": event_data.event_url,
        "desc": event_data.event_desc,}), 200
    else:
       return "404 page not found", 404

@app.route("/get-all-events", methods=["GET"])
def get_all_events():
    events = db.session.query(Events)
    if events:
        
        return jsonify([{"id": event.event_id, 
        "name": event.event_name,
        "place": event.event_place,
        "img": event.event_img_url,
        "url": event.event_url,
        "desc": event.event_desc,} for event in events]), 200
    else:
       return "404 page not found", 404


if __name__ == "__main__":
    create_tables()
    app.run(debug=True)