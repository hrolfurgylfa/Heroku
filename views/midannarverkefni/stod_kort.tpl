<!DOCTYPE html>
<html>
<head>
    <%
    allir_stodvakodar = []
    teljari = 1
    
    for bensinstod in gogn["results"]:
        if bensinstod["company"] == bensinstod_nafn:
            allir_stodvakodar.append(bensinstod["key"])
        end
    end
    
    stodvarkodi =  allir_stodvakodar[stod_numer - 1]
    
    for bensinstod in gogn["results"]:
        if bensinstod["key"] == stodvarkodi:
            nafn_stodvar = bensinstod["name"]
            lat = bensinstod["geo"]["lat"]
            lng = bensinstod["geo"]["lon"]
        end
    end
    %>
    <meta charset="utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>{{ bensinstod_nafn }} - {{ nafn_stodvar }}</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" type="text/css" media="screen" href="/static/midannarverkefni/main.css" />
</head>
<body>
<header class="haus">
    <h1>{{ bensinstod_nafn }} - {{ nafn_stodvar }}</h1>
</header>

<section class="kort_og_fleira">
    <h3>Kort</h3>
    <iframe class="kort" src="http://maps.google.com/maps?q={{ lat }},{{ lng }}&z=15&output=embed"></iframe>
    <br>
    <a target="_blank" href="http://www.google.com/maps/place/{{ lat }},{{ lng }}">Stærra kort á Google Maps</a>
</section>

% include("midannarverkefni/fotur.tpl", sott = gogn["timestampPriceCheck"])
