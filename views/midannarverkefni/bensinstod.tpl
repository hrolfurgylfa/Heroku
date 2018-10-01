% include("midannarverkefni/haus.tpl", titill = bensinstod_nafn)
<!-- AIzaSyDu6tALJE-febpmkmjP1s1vu5bqaIeggPY -->

<!-- <iframe width="425" height="350" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" src="https://www.openstreetmap.org/export/embed.html?bbox=-123.812866210937504%2C63.51794993019517%2C-19.226074218750004%2C64.55552125118271&amp;layer=mapnik" style="border: 1px solid black"></iframe><br/><small><a href="https://www.openstreetmap.org/#map=9/64.0417/-21.5195">Skoða stærra kort</a></small> -->

<table class="tafla_1">
    <tr>
        <th>Bensínstöð</th>
        <th>95-oktan</th>
        <th>95-oktan m. kykli</th>
        <th>dísil</th>
        <th>dísil m. lykli</th>
    </tr>
    <%
    teljari = 1

    for bensinstod in gogn["results"]:
        if bensinstod["company"] == bensinstod_nafn:
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
                <td><a href="/midannarverkefni/{{ numer }}/stod_{{ teljari }}">{{ bensinstod["name"] }}</a></td>
                <td>{{ bensinstod["bensin95"] }}</td>
                <td>{{ bensinstod["bensin95_discount"] }}</td>
                <td>{{ bensinstod["diesel"] }}</td>
                <td>{{ bensinstod["diesel_discount"] }}</td>
            </tr>
            % teljari += 1
        % end
    % end
</table>
% include("midannarverkefni/fotur.tpl", sott = gogn["timestampPriceCheck"])
