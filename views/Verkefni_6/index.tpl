<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>Netbúð</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" type="text/css" media="screen" href="/static/Verkefni_6/main.css" />
</head>
<body>
    <h1>Netbúð</h1>
    <hr>
    <div class="oll_fot">
        % for tel in range(1,7):
        <section class="fot_{{ tel }}">
            <section class="fot2">
                <a href="/Verkefni_6/bud?i={{ tel }}">
                    <img class="mynd_1" src="/static/Verkefni_6/fot/{{ tel }}.jpg">
                </a>
                <h3 class="fyrirsogn">
                    {{ allar_vorur[0][str(tel)] }}
                    <span class="verd">{{ allar_vorur[2][str(tel)] }}kr.</span>
                </h3>
                
                <p class="lysing">{{ allar_vorur[1][str(tel)] }}</p>
            </section>
        </section>
        % end
    </div>
</body>
</html>