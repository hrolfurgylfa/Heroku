<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>Verkefni 6</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" type="text/css" media="screen" href="/static/Verkefni_6_gamalt/main.css" />
</head>
<body>
    <h1>Innskráning</h1>
    <h5>EKKI nota aðgangsorð að öðrum síðum hérna vegna þess að það geta allir séð öll aðgangsorð og notandanöfn <a href="/static/Verkefni_6/password.txt">hérna</a></h5>
    <form class="innskraning" action="/Verkefni_6/innskraning" method="POST">
        <p>Notendanafn:</p>
        <input name="username" type="text" required><br>
        <p>Aðgangsorð:</p>
        <input name="password" type="password" required><br>
        
        <input type="submit" value="Skrá inn" />
    </form>
</body>
</html>