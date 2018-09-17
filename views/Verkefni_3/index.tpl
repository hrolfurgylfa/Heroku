<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>Hasarfréttir</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" type="text/css" media="screen" href="/static/Verkefni_3/main.css" />
</head>
<body>
    %include("Verkefni_3/B/haus.tpl")

    <div class="rod">
        <section class="vinstri_section"><a class="titil_linkur" href="/Verkefni_3/Lidur_B/frett_{{ id_1 }}"><h3>{{ titill_1 }}</h3></a></section>
        <section class="haegri_section nyjustu_frettir"><h3>Nýjustu fréttir</h3></section>
        <section class="vinstri_section"><a href=""><img class="forsidumynd" src="{{ allarFrettir[-1][2] }}"></a></section>
        <section class="haegri_section nyjustu_frettir">
            <ul class="fretta_valmynd">
                <li><a href="/Verkefni_3/Lidur_B/frett_{{ id_1 }}">{{ titill_1 }}</a></li>
                <li><a href="/Verkefni_3/Lidur_B/frett_{{ id_2 }}">{{ titill_2 }}</a></li>
                <li><a href="/Verkefni_3/Lidur_B/frett_{{ id_3 }}">{{ titill_3 }}</a></li>
            </ul>
            <h3>Allar fréttir</h3>
            <ul class="fretta_valmynd">
                % tel = len(allarFrettir)
                % for frett in allarFrettir[::-1]:
                    <li>
                        <a href="/Verkefni_3/Lidur_B/frett_{{ tel }}">{{ frett[1] }}</a>
                    </li>
                    % tel -= 1
                % end
            </ul>
        </section>
    </div>

    %include("Verkefni_3/B/fotur.tpl")
</body>
</html>