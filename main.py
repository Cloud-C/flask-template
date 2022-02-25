from app import create_app, init_scheduler

app = create_app()
init_scheduler(app)


@app.before_request
def before_request():
    """
        before request
    """


@app.after_request
def after_request(response):
    """
        after request
    """
    return response


if __name__ == '__main__':
    app.run(debug=app.config.get('DEBUG'), host=app.config.get('HOST'), port=app.config.get('PORT'))
