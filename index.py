from bottle import route, run, template, request, error, abort, redirect

import login


@route('/')
def index():
    if login.esta_logado():
        return template('hello_template', name= login.retorna_nome_login())
    else:
        redirect("/login")
        
@error(404)
def error404(error):
    return 'Página não encontrada.'

@route('/restricted')
def restricted():
    abort(401, "Sorry, access denied.")
  
    
    
    

#outras ideias
'''@route('/my_ip')
def show_ip():
    ip = request.environ.get('REMOTE_ADDR')
    # or ip = request.get('REMOTE_ADDR')
    # or ip = request['REMOTE_ADDR']
    return template("Your IP is: {{ip}}", ip=ip)


@route('/template/<name>')
def hello(name):
    return template('hello_template', name=name)

'''

'''@route('/hello/<name>')
def index(name):
    if login.esta_logado():
        return template('<b>Hello {{name}}</b>!', name=name)
    else:
        redirect("/login")
'''
run(host='localhost', port=8080)



    