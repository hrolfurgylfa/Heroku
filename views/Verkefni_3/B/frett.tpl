<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>{{ titill }}</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" type="text/css" media="screen" href="/static/Verkefni_3/main.css" />
</head>
<body>
    <h1>{{ titill }}</h1>
    <hr>
    <section>
        <div><p><img class="forsogu_mynd" src="{{ mynd }}">{{ texti_frettar }}</p></div>
        <h6><a href="/Verkefni_3/Lidur_B">Aftur á forsíðu</a></h6>
        <hr>
        <h5 class="netfang_hofundar">{{ netfang_hofundar }}</h5>
    </section>
    %include("Verkefni_3/B/fotur.tpl")
</body>
</html>