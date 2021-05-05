import os
from bottle import Bottle, default_app, run, hook, response

app = Bottle()

with app:
    assert app is default_app()

    @hook('after_request')
    def enable_cors():
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, OPTIONS'
        response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'

    # Capture routes defined in other modules
    import index

    # After first push to heroku, set environment variable with:
    # heroku config:set APP_LOCATION=heroku
    if os.environ.get('APP_LOCATION') == 'heroku':
        run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
    else:
        run(host='localhost', port=int(os.environ.get('PORT', 8000)), debug=True)