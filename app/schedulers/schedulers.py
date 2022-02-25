from flask_apscheduler import APScheduler

scheduler = APScheduler()


@scheduler.task('interval', id='hello_world', seconds=5)
def hello_world():
    app = scheduler.app
    with app.app_context():
        print('hello world!')
