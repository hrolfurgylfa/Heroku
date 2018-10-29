<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>{{ t }}</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" type="text/css" media="screen" href="/static/Verkefni_5/error.css" />
    <link href="https://fonts.googleapis.com/css?family=Roboto" rel="stylesheet"> 
</head>
<body>
    <h2>{{ t }}</h2>
    % try: 
        <a href="/Verkefni_6/utskra?u={{ u }}">Fara til baka</a>
    % except NameError:
        <a href="/Verkefni_6">Fara til baka</a>
    % end
</body>
</html>