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
    <form method="POST" action="/Verkefni_5/nidurstada">
        <p>Fullt nafn:</p>
        <input name="fullt_nafn" type="text" /><br>

        <p>Námskeið:</p>
        <input type="radio" name="namskeid" value="Python"> Python<br>
        <input type="radio" name="namskeid" value="JavaScript"> JavaScript<br>
        <input type="radio" name="namskeid" value="Gagnasöfn"> Gagnasöfn<br>
        
        <p>Götu nafn og númer:</p>
        <input name="gata" type="text" /><br>

        <section class="stadsetning">            
            <p>Bær:</p>
            <input name="baer" type="text" /><br>

            <p>Póstnúmer:</p>
            <input name="postnumer" type="text" /><br>
        </section>
        
        <p>Tölvupóstur:</p>
        <input name="tolvupostur" type="email" />

        <p>Símanúmer:</p>
        <input name="tolvupostur" type="tel" />

        <p>Hádegismatur:</p>
        <input type="radio" name="matur" value="nei" checked> Nei<br>
        <input type="radio" name="matur" value="ja"> Já<br>
        
        <input type="submit" value="Senda" />
    </form>
</body>
</html>