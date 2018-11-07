<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>Verkefni 7</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" type="text/css" media="screen" href="/static/Verkefni_7/main.css" />
</head>
<body>
    <h1>Innskráning</h1>
    <h5>EKKI nota aðgangsorð að öðrum síðum hérna vegna þess að það geta allir séð öll aðgangsorð og notandanöfn.</h5>
    <h4>Ertu ekki með aðgang? Búðu til aðgang <a href="/Verkefni_7/bua_til_adgang">hérna</a>.</h4>
    <form class="innskraning" action="/Verkefni_7/innskraning" method="POST">
        <p>Notendanafn:</p>
        <input name="username" type="text" required><br>
        <p>Aðgangsorð:</p>
        <input name="password" type="password" required><br>
        
        <input type="submit" value="Skrá inn" />
    </form>
</body>
</html>