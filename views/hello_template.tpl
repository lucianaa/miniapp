%if name == 'World':
    <h1>Hello {{name}}!</h1>
    <p>This is a test.</p>
%else:
    <h1>Olá, {{name.title()}}!</h1>
    <p>Como está?</p>
    <a href="/logout"> Sair </a><!--link de logout-->
%end
