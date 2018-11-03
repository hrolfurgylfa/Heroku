<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>Netbúð - {{ allar_vorur[0][vara] }}</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" type="text/css" media="screen" href="/static/Verkefni_6/main.css" />
</head>
<body>
    % include("Verkefni_6/haus.tpl")
    <div class="AdalView">      
        <section class="adalmynd_vara">
            <img src="/static/Verkefni_6/fot/{{ vara }}.jpg" alt="">
        </section>  
        <section class="texti_vara">
            <h1 class="nafn_vara">{{ allar_vorur[0][vara] }}</h1>
            <h3 class="verd_vara">{{ allar_vorur[2][vara] }}kr.</h3>
            <p class="lysing_vara">{{ allar_vorur[1][vara] }}</p>
            <a href="/Verkefni_6/kaupa_voru?i={{ vara }}">Kaupa</a>
        </section>
    </div>
</body>
</html>