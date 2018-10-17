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
    <h1>Skráning á Námskeið</h1>
    <hr>
    <form class="skraning_a_namskeid" action="/Verkefni_5/nidurstada" method="POST">
        <p>Fullt nafn:</p>
        <input name="fullt_nafn" type="text" required><br>

        <p>Námskeið fyrir hádegi:</p>
        <input type="checkbox" name="namskeid" value="Python 1"> Python 1<br>
        <input type="checkbox" name="namskeid" value="JavaScript 1"> JavaScript 1<br>
        <input type="checkbox" name="namskeid" value="Gagnasofn 1"> Gagnasöfn 1<br>

        <p>Námskeið eftir hádegi:</p>
        <input type="checkbox" name="namskeid" value="Python 2"> Python 2<br>
        <input type="checkbox" name="namskeid" value="JavaScript 2"> JavaScript 2<br>
        <input type="checkbox" name="namskeid" value="Gagnasofn 2"> Gagnasöfn 2<br>
        
        <p>Götu nafn og númer:</p>
        <input name="gata" type="text" required><br>
          
        <p>Bær:</p>
        <input name="baer" type="text" required><br>

        <p>Póstnúmer:</p>
        <input name="postnumer" type="text" required><br>
        
        <p>Tölvupóstur:</p>
        <input name="tolvupostur" type="email" required>

        <p>Símanúmer:</p>
        <input name="simanumer" type="tel" required>

        <p>Hádegismatur:</p>
        <input type="radio" name="matur" value="Nei" required checked> Nei<br>
        <input type="radio" name="matur" value="Já" required> Já<br>
        
        <input type="submit" value="Senda" />
    </form>
</body>
</html>