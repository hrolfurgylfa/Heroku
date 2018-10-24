<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>Forsíða</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" type="text/css" media="screen" href="/static/forsida/forsida.css" />
    <link href="https://fonts.googleapis.com/css?family=Roboto" rel="stylesheet"> 
</head>
<body>
    <nav class="topnav">
        <input type="checkbox" id="toggle">
        <label for="toggle">Efnisyfirlit &#9776;</label>
        % include("Aðaltemplates/menu.tpl")
    </nav>
    <header>
        
        <h1><img class="linux-morges" src="/static/forsida/myndir/linux-morges.svg">Aðalvalmynd<br class="enter_i_titli"><span class="bil_i_titli"> - </span>Vefforritun 1</h1>
        <picture class="Cover-mynd">
                <source srcset="/static/forsida/myndir/Cover_mynd/snow_480.jpg" media="(max-width: 30em)">
            <source srcset="/static/forsida/myndir/Cover_mynd/snow_960.jpg" media="(max-width: 37.5em)">
            <source srcset="/static/forsida/myndir/Cover_mynd/snow_960.jpg" media="(max-width: 60em)">
            <source srcset="/static/forsida/myndir/Cover_mynd/snow_1600.jpg" media="(max-width: 80em)">
            <source srcset="/static/forsida/myndir/Cover_mynd/snow_1920.jpg">
            <img src="/static/forsida/myndir/Cover_mynd/snow_1920.jpg">
        </picture>
    </header>
    <main>
        <section class="um_mig"><!--Um mig-->
            <div>
                <h2>Um mig</h2>
                <p>Ég heiti Hrólfur ég er 16 ára og ég bý í vesturbænum í Kópavogi. Ég hef mjög mikinn áhuga á öllu tengdu tölvum, ég á fullt af gömlum tölvum og símum heima hjá mér og ég setti tölvuna mína saman sjálfur. Ég er líka mikið í skátunum og ég byrjaði þar í sjötta bekk og svo varð ég foringi í janúar í 10 bekk. </p>
            </div>
            <img class="selfie" src="/static/forsida/myndir/portrait.jpg" alt="Mynd af mér">
        </section>
        <section class="ahugamal"><!--Áhugamál-->
            <h2>Áhugamál</h2>
            <p>Áhugamál mín eru skátarnir og Tölvuleikir, líka flest annað sem tengist tölvum. </p>
            <p>Ég hef verið í skátunum síðan ég var í miðjum sjötta bekk, svo í janúar þegar ég var í 10 varð ég foringi yfir fálkaskáta stelpu hópnum Hattífattar, fálkaskátar eru fyrir fimmta til sjötta bekk, og ég er ennþá foringinn þeirra. Svo mæti ég líka á fundi sjálfur, þar sem ég er ekki foringi, og svo mæti ég líka oft í útilegur með Kópum.</p>
            <p>Mér finnst tölvuleikir líka mjög skemmtilegir þótt að ég hafi bara nýlega fengið tölvu sem getur spilað eitthvað annað en einn ákveðin leik, leikirnir sem ég spila eru aðallega Ghost Recon: Wildlands, Assassins Creed serían, Overwatch og Titanfall 2 sem ég var að fá nýlega.</p>
        </section>
        <div class="myndir">
            <img src="/static/forsida/myndir/Til_Bler.JPG">
        </div>
    </main>
    <footer>
        <div class="sMedia">
            <a href="https://www.facebook.com/">
                <div class="facebook">
                    <span class="icon-facebook"></span>
                </div>
            </a>
            <a href="https://twitter.com/">
                <div class="twitter">
                    <span class="icon-twitter"></span>
                </div>
            </a>
            <a href="https://www.snapchat.com/">
                <div class="snapchat">
                    <span class="icon-snapchat"></span>
                </div>
            </a>
            <a href="https://allo.google.com/">
                <div class="allo">
                    <span class="icon-googleallo"></span>
                </div>
            </a>
        </div>
    </footer>
</body>
</html>