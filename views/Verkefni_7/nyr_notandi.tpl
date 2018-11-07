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
    <h1>Búa til aðgang</h1>
    <h5>EKKI nota aðgangsorð að öðrum síðum hérna vegna þess að það geta allir séð öll aðgangsorð og notandanöfn.</h5>
    <h4>Ertu núþegar með aðgang? Skráðu þig inn <a href="/Verkefni_7">hérna</a>.</h4>
    <form class="innskraning" action="/Verkefni_7/gera_notanda" method="POST">
        <p>Nafn:</p>
        <input name="nafn" type="text" required><br>
        <p>Notendanafn:</p>
        <input name="username" type="text" required><br>
        <p>Aðgangsorð:</p>
        <input name="password" type="password" required><br>
        <p>Aðgangsorð aftur:</p>
        <input name="password2" type="password" required><br>
        <input type="submit" value="Búa til aðgang" />
    </form>
</body>
</html>