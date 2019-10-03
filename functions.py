import banco_dados

def check_login(db, username, password):
    
    if banco_dados.consulta(db, username, password):
        return 1
    else: return 0
    
def check_login_API(db, name):
    if banco_dados.consulta_API(db,name):
        return 1
    else: return 0