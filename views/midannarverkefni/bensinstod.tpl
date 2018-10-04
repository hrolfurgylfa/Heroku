% include("midannarverkefni/haus.tpl", titill = bensinstod_nafn)

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
