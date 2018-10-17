<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>Niðurstöður</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" type="text/css" media="screen" href="/static/Verkefni_5/main.css" />
</head>
<body>
    <h1>Niðurstöður</h1>
    <p>Fullt nafn: {{ nafn }}</p>
    <p>Námskeið: {{ oll_namskeid }}</p>
    <p>Gata: {{ gata }}</p>
    <p>Bær: {{ baer }}</p>
    <p>Póstnúmer: {{ postnumer }}</p>
    <p>Tölvupóstur: {{ tolvupostur }}</p>
    <p>Símanúmer: {{ simanumer[0:3] }}-{{ simanumer[3:7] }}</p>
    <p>Matur: {{ matur }}</p>
    <p>Verð án VSK: {{ verdAnVSK }}</p>
    <p>Verð með VSK: {{ round(verdAnVSK * 1.245) }}</p>
</body>
</html>