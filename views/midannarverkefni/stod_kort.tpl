<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>{{ bensinstod_nafn }}</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" type="text/css" media="screen" href="/static/midannarverkefni/main.css" />
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.3.4/dist/leaflet.css"
    integrity="sha512-puBpdR0798OZvTTbP4A8Ix/l+A4dHDD0DGqYW6RQ+9jxkRFclaxxQb/SJAWZfWAkuyeQUytO7+7N4QKrDh+drA=="
    crossorigin=""/>
    <script src="https://unpkg.com/leaflet@1.3.4/dist/leaflet.js"
    integrity="sha512-nMMmRyTVoLYqjP9hrbed9S+FzjZHW5gY1TWCHA5ckwXZBadntCNs8kEqAWdrb9O7rxbCaA4lKTIWjDXZxflOcA=="
    crossorigin=""></script>
</head>
<body>
<header class="haus">
    <h1>{{ bensinstod_nafn }}</h1>
</header>

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
    end
end
%>
<h3>{{ nafn_stodvar }}</h3>
<!-- <iframe width="425" height="350" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" src="https://www.openstreetmap.org/export/embed.html?bbox=-21.894142627716068%2C64.1269747201129%2C-21.8658185005188%2C64.13505438466328&amp;layer=cyclemap" style="border: 1px solid black"></iframe>
<small><a href="https://www.openstreetmap.org/#map=16/64.1310/-21.8800&amp;layers=C">Skoða stærra kort</a></small> -->

 <div id="mapid"></div>

<script>
    var mymap = L.map('mapid').setView([51.505, -0.09], 13);
    L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
        attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
        maxZoom: 18,
        id: 'mapbox.streets',
        accessToken: 'your.mapbox.access.token'
    }).addTo(mymap);
</script>

% include("midannarverkefni/fotur.tpl", sott = gogn["timestampPriceCheck"])
