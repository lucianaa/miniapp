from bottle import route, install, template
from bottle_sqlite import SQLitePlugin

install(SQLitePlugin(dbfile='bd.db'))

@route('/show/users')
def show(db):
    c = db.execute('SELECT * FROM usuario ')
    row = c.fetchone()
    return template('<b>Hello {{name}}</b>!', name=row['nome'])


def consulta(db, nome, senha):
    c = db.execute('SELECT * FROM usuario where nome = \'' + nome + '\' and senha = \''+senha +'\'')
    row = c.fetchone()
    if row:
        return True 
    else:
        return False
    
def consulta_API(db, token):
    c = db.execute('SELECT * FROM usuario where token = \'' + token + '\'')
    row = c.fetchone()
    if row:
        return True 
    else:
        return False
