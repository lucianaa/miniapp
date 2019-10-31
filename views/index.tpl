<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8" />
    <title></title>
    <link rel="stylesheet" href="logout.css" />
  </head>
  <body>
  <form action="/logout">
    <div class="login-case">
      <div class="login-box">
        <h1>Bem Vindo</h1>
         <h2>Olá, {{name.title()}}!</h2>
        <div class="textbox">
          <i class="fas fa-user-cog"></i>
          <input type="text" value="Ready to logOUT?" />
        </div>
        <div class="btn">          
          <input type="submit" value="Getting OUT of here" />
          <i class="fas fa-angle-double-left"></i>
        </div>
      </div>
    </div>
    </form>
  </body>
</html>

