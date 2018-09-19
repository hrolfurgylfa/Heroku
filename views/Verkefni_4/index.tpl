<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>Local currentcy</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" type="text/css" media="screen" href="/static/Verkefni_4/main.css" />
</head>
<body>
    <%
    import json
    with open("Verkefni_4/gengi.json", "r") as skra:
        gengi = json.load(skra)
    end
    %>
    <div class="row">
        <section>
            <h1>Gengi gjaldmiðla (Local og ekki uppfært)</h1>
            % for stak in gengi["results"]:
                <h3>{{ stak["shortName"] }} - {{ stak["longName"] }}</h3>
                <ul>
                    <li>Gengi: {{ stak["value"] }}</li>
                    <li>Ask value: {{ stak["askValue"] }}</li>
                    <li>Bid value: {{ stak["bidValue"] }}</li>
                    <li>Change cur: {{ stak["changeCur"] }}</li>
                    <li>Breytingarprósenta: {{ stak["changePer"] }}</li>
                </ul>
            % end
        </section>
    </div>
</body>
</html>