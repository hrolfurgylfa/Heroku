% include("midannarverkefni/haus.tpl", titill = bensinstod_nafn)
<!-- AIzaSyDu6tALJE-febpmkmjP1s1vu5bqaIeggPY -->
<!DOCTYPE html>
<html>
  <head>
    <style>
       /* Set the size of the div element that contains the map */
      #map {
        height: 400px;  /* The height is 400 pixels */
        width: 100%;  /* The width is the width of the web page */
       }
    </style>
  </head>
  <body>
    <h3>My Google Maps Demo</h3>
    <!--The div element for the map -->
    <div id="map"></div>
    <script>
// Initialize and add the map
function initMap() {
  // The location of Uluru
  var uluru = {lat: 64.136318, lng: -21.899678};
  // The map, centered at Uluru
  var map = new google.maps.Map(
      document.getElementById('map'), {zoom: 4, center: uluru});
  // The marker, positioned at Uluru
  var marker = new google.maps.Marker({position: uluru, map: map});
}
    </script>
    <!--Load the API from the specified URL
    * The async attribute allows the browser to render the page while the API loads
    * The key parameter will contain your own API key (which is not needed for this tutorial)
    * The callback parameter executes the initMap() function
    -->
    <script async defer
    src="https://maps.googleapis.com/maps/api/js?key=AIzaSyDu6tALJE-febpmkmjP1s1vu5bqaIeggPY&callback=initMap">
    </script>
  </body>
</html>

<table class="tafla_1">
    <tr>
        <th>Bensínstöð</th>
        <th>95-oktan</th>
        <th>95-oktan m. kykli</th>
        <th>dísil</th>
        <th>dísil m. lykli</th>
    </tr>
    <%
    for bensinstod in gogn["results"]:
        if bensinstod["bensin95"] is None:
            bensinstod["bensin95"] = "Ekkert"
        end
        if bensinstod["bensin95_discount"] is None:
            bensinstod["bensin95_discount"] = "Ekkert"
        end
        if bensinstod["diesel"] is None:
            bensinstod["diesel"] = "Ekkert"
        end
        if bensinstod["diesel_discount"] is None:
            bensinstod["diesel_discount"] = "Ekkert"
        end
    %>
        <tr>
            <td>{{ bensinstod["name"] }}</td>
            <td>{{ bensinstod["bensin95"] }}</td>
            <td>{{ bensinstod["bensin95_discount"] }}</td>
            <td>{{ bensinstod["diesel"] }}</td>
            <td>{{ bensinstod["diesel_discount"] }}</td>
        </tr>
    % end
</table>
% include("midannarverkefni/fotur.tpl", sott = gogn["timestampPriceCheck"])
