from flask import Flask, render_template
from contact import contact_app
from todo import todo_app
from finance import finance_app
from supply import supply_app


app = Flask(__name__)

app.register_blueprint(todo_app)
app.register_blueprint(contact_app)
app.register_blueprint(finance_app)
app.register_blueprint(supply_app)

@app.route("/")
def index():
  return render_template("index.html")


