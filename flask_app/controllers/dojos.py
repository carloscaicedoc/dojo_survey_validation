from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.dojo import Dojo

@app.route('/')
def index():
    return render_template("survey.html")


@app.route('/intake', methods=['POST'])
def intake():
    # if there are errors:
    # We call the staticmethod on Dojo model to validate
    if not Dojo.validate_dojo(request.form):
        # redirect to the route where the burger form is rendered.
        return redirect('/')
    # else no errors:
    
    session["dojo_id"] = Dojo.save(request.form)
    return redirect("/received")


@app.route('/received')
def success():
    data = {
        "id" : session["dojo_id"]
    }
    dojo = Dojo.get_one(data)
    return render_template('display_info.html', dojo=dojo)
