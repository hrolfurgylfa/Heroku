<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>Netbúð</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" type="text/css" media="screen" href="/static/Verkefni_6/main.css" />
    <link href="https://fonts.googleapis.com/css?family=Ubuntu" rel="stylesheet"> 
</head>
<body>
    <!-- <nav class="topnav">
        <input type="checkbox" id="toggle">
        <label for="toggle">Efnisyfirlit &#9776;</label>
        % include("Aðaltemplates/menu.tpl")
    </nav>
    <section class="karfa_hover">
        <h5>Karfa</h5>
    </section> -->
    % include("Verkefni_6/haus.tpl")
    <div class="oll_fot">
        % for tel in range(1,7):
            <section class="fot_{{ tel }}">
                <section class="fot2">
                    <a class="fot_linkur" href="/Verkefni_6/vara?i={{ tel }}">
                        <img class="mynd_1" src="/static/Verkefni_6/fot/{{ tel }}.jpg">
                    </a>
                    <h3 class="fyrirsogn">
                        <a class="fot_linkur" href="/Verkefni_6/vara?i={{ tel }}">
                            {{ allar_vorur[0][str(tel)] }}
                        </a>
                        <span class="verd">{{ allar_vorur[2][str(tel)] }}kr.</span>
                    </h3>
                    <a class="fot_linkur" href="/Verkefni_6/vara?i={{ tel }}">
                        <p class="lysing">{{ allar_vorur[1][str(tel)] }}</p>
                    </a>
                </section>
            </section>
        % end
    </div>
    <footer class="fotur">
        <h4>&copy; 2018 Hrólfur Gylfason</h4>
    </footer>
</body>
</html>