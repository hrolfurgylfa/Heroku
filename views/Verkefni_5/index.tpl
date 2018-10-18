<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>Skráning á Námskeið</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" type="text/css" media="screen" href="/static/Verkefni_5/main.css" />
</head>
<body>
    <h1 class="titill">Skráning á Námskeið</h1>
    <form class="skraning_a_namskeid" action="/Verkefni_5/nidurstada" method="POST">
        <p>Fullt nafn:</p>
        <input name="fullt_nafn" type="text" required><br>

        <section class="namskeid">
            <div class="namskeid1">
                <p>Námskeið fyrir hádegi:</p>
                <input type="checkbox" name="namskeid" value="Python 1"> Python 1<br>
                <input type="checkbox" name="namskeid" value="JavaScript 1"> JavaScript 1<br>
                <input type="checkbox" name="namskeid" value="Gagnasofn 1"> Gagnasöfn 1<br>
            </div>
            <div class="namskeid2">
                <p>Námskeið eftir hádegi:</p>
                <input type="checkbox" name="namskeid" value="Python 2"> Python 2<br>
                <input type="checkbox" name="namskeid" value="JavaScript 2"> JavaScript 2<br>
                <input type="checkbox" name="namskeid" value="Gagnasofn 2"> Gagnasöfn 2<br>
            </div>
        </section>
        
        <section class="heimilisfang">
            <div class="gata">
                <p>Götu nafn og númer:</p>
                <input name="gata" type="text" required><br>
            </div>
            <div class="baer">
                <p>Bær:</p>
                <input name="baer" type="text" required><br>
            </div>
            <div class="postnumer">
                <p>Póstnúmer:</p>
                <input name="postnumer" type="text" required><br>
            </div>
        </section>

        <section class="samskipti">
            <div class="tolvupostur">
                <p>Tölvupóstur:</p>
                <input name="tolvupostur" type="email" required>
            </div>
            <div class="simanumer">
                <p>Símanúmer:</p>
                <input name="simanumer" type="tel" required>
            </div>
        </section>
        <p>Hádegismatur:</p>
        <input type="radio" name="matur" value="Nei" required checked> Nei<br>
        <input type="radio" name="matur" value="Já" required> Já<br>
        
        <input type="submit" value="Senda" />
    </form>
</body>
</html>