from flask import Flask, render_template
from data import db_session
from data.users import User
from data.jobs import Jobs
import datetime as dt
from sqlalchemy import not_


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init('db/mars_explorer.db')

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


if __name__ == '__main__':
    main()
