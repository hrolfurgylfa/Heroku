<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>Json</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" type="text/css" media="screen" href="/static/Verkefni_4/main.css" />
</head>
<body>
    <div class="row">
        <section>
            <h1>Gengi gjaldmiðla frá apis.is (Landsbankanum)</h1>
            % for stak in gogn["results"]:
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