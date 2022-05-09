from flask import Flask, redirect, render_template, request, url_for
from flask_bcrypt import Bcrypt
from data import db_session
from data.users import User
from data.jobs import Jobs
from data.departments import Department
import datetime as dt
import sqlalchemy


app = Flask(__name__)
bcrypt = Bcrypt(app)
app.config["SECRET_KEY"] = "yandexlyceum_secret_key"


def main():
    db_session.global_init("db/mars_explorer.db")

    app.run(debug=True)


@app.route("/")
@app.route("/index")
def job_journal():
    db_sess = db_session.create_session()
    job_list = [
        {
            "job": job.job,
            "team_leader": (
                db_sess.query(User).filter(User.id == job.team_leader).first()
            ),
            "duration": job.work_size,
            "collaborators": job.collaborators,
            "is_finished": job.is_finished,
        }
        for job in db_sess.query(Jobs).all()
    ]
    return render_template("job_journal.html", job_list=job_list)


@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "GET":
        return render_template("register.html")

    elif request.method == "POST":
        if request.form["password"] == request.form["confirmed_password"]:
            db_sess = db_session.create_session()
            user = User()
            user.name = request.form["name"]
            user.surname = request.form["surname"]
            user.age = int(request.form["age"])
            user.position = request.form["position"]
            user.speciality = request.form["specialty"]
            user.address = request.form["address"]
            pw_hash = bcrypt.generate_password_hash(request.form["password"])
            print(pw_hash)
            user.hashed_password = pw_hash
            db_sess.add(user)
            db_sess.commit()
        return render_template("register.html")


if __name__ == "__main__":
    main()
