<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>Netbúð - Karfa</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" type="text/css" media="screen" href="/static/Verkefni_6/main.css" />
</head>
<body>
    % include("Verkefni_6/haus.tpl")
    <h1 class="karfa_titill">Karfa</h1>
    % for vara in a_vorur_radad:
        <section class="vara_karfa">
            <section class="x_karfa">
                <a href="/Verkefni_6/eyda_ur_korfu?i={{ vara[0][1] }}">
                    <h1>X</h1>
                </a>
            </section>
            <section class="mynd_karfa">
                <img src="/static/Verkefni_6/fot/{{ vara[0][1] }}.jpg" alt="">
            </section>
            <h3 class="titill_karfa">
                {{ allar_vorur[0][vara[0][1]] }} x{{ len(vara) }}
                <span class="verd_karfa">{{ int(allar_vorur[2][vara[0][1]]) * int(len(vara)) }}kr.</span>
            </h3>
            <p class="lysing_karfa">{{ allar_vorur[1][vara[0][1]] }}</p>
        </section>
    % end
    <hr class="karfa_samtals_skiptari">
    <section class="karfa_samtals">
        <h3 class="karfa_heildarverd_str">Samtals</h4>
        <span></span>
        <h3 class="karfa_heildarverd">{{ heildarverd }}kr.</h4>
    </section>
</body>
</html>