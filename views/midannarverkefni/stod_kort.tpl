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
    <!-- Fyrir Leaflet -->
    <!-- <link rel="stylesheet" href="https://unpkg.com/leaflet@1.3.4/dist/leaflet.css"
    integrity="sha512-puBpdR0798OZvTTbP4A8Ix/l+A4dHDD0DGqYW6RQ+9jxkRFclaxxQb/SJAWZfWAkuyeQUytO7+7N4QKrDh+drA=="
    crossorigin=""/>
    <script src="https://unpkg.com/leaflet@1.3.4/dist/leaflet.js"
    integrity="sha512-nMMmRyTVoLYqjP9hrbed9S+FzjZHW5gY1TWCHA5ckwXZBadntCNs8kEqAWdrb9O7rxbCaA4lKTIWjDXZxflOcA=="
    crossorigin=""></script> -->

    <!-- Fyrir OpenLayers -->
    <!-- <link rel="stylesheet" href="https://openlayers.org/en/v5.2.0/css/ol.css" type="text/css"> -->
    <!-- The line below is only needed for old environments like Internet Explorer and Android 4.x -->
    <!-- <script src="https://cdn.polyfill.io/v2/polyfill.min.js?features=requestAnimationFrame,Element.prototype.classList,URL"></script> -->
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
<!-- OpenLayers -->
<!-- <section class="kort">
    <div id="map" class="map"></div>
    <script>
      import Map from 'ol/Map.js';
      import View from 'ol/View.js';
      import TileLayer from 'ol/layer/Tile.js';
      import OSM from 'ol/source/OSM.js';

      var map = new Map({
        layers: [
          new TileLayer({
            source: new OSM()
          })
        ],
        target: 'map',
        view: new View({
          projection: 'EPSG:4326',
          center: [0, 0],
          zoom: 2
        })
      });
    </script>
</section> -->

<!-- Pure OpenStreetMap -->
<!-- <iframe width="425" height="350" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" src="https://www.openstreetmap.org/export/embed.html?bbox=-21.894142627716068%2C64.1269747201129%2C-21.8658185005188%2C64.13505438466328&amp;layer=cyclemap" style="border: 1px solid black"></iframe>
<small><a href="https://www.openstreetmap.org/#map=16/64.1310/-21.8800&amp;layers=C">Skoða stærra kort</a></small> -->


<!-- LeafLet -->
<!-- <div id="mapid" style="position: relative; outline: currentcolor none medium;" class="leaflet-container leaflet-touch leaflet-fade-anim leaflet-grab leaflet-touch-drag leaflet-touch-zoom" tabindex="0"></div>
<script>
    var mymap = L.map('mapid').setView([51.505, -0.09], 13);
    L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={pk.eyJ1IjoiaHJvbGZ1cmd5bGZhIiwiYSI6ImNqbXFpY2p2MjFhNmEzcW96Y2w1NG42cXIifQ.EB6zvVKSY_hicJf1Rqidkg}', {
        attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
        maxZoom: 18,
        id: 'mapbox.streets',
        accessToken: 'your.mapbox.access.token'
    }).addTo(mymap);
</script> -->

% include("midannarverkefni/fotur.tpl", sott = gogn["timestampPriceCheck"])
