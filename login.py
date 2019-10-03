import uuid
from bottle import route, request, response, get
from functions import check_login, check_login_API

SESSIONS = {}

@route('/login') #@get('/login') # or @route('/login')
def login():
    return '''
        <form action="/login" method="post">
            Usuário: <input name="username" type="text" /> <br />
            Senha: <input name="password" type="password" /> <br />
            <input value="Login" type="submit" />
        </form>
    '''

@route('/login', method='POST')#@post('/login') # or @route('/login', method='POST')
def do_login(db):
    username = request.forms.get('username') 
    password = request.forms.get('password')
    if check_login(db, username, password):
        registra_login(username)
        return "<p>Your login information was correct.</p> <a href='/'> Página principal </a>"
    else:
        return "<p>Login failed.</p> <a href='/login'> Tentar novamente </a>"

def registra_login(username):
    global SESSIONS
    session_id = str(uuid.uuid4())
    SESSIONS[session_id] = username
    response.set_header('Set-Cookie', 'session='+session_id)

def esta_logado():
    session_id = request.get_cookie('session')
    if session_id in SESSIONS:
        return True
    return False

def retorna_nome_login():
    session_id = request.get_cookie('session')
    return SESSIONS[session_id]

#REST API

@get('/usuario/<name>')
def get_usuario(db,name):    
    if check_login_API(db, name):
        return {'login' : True}
    return {'login' : False}