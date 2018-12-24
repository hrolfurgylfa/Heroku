% include("Blog/haus.tpl", t = "Forsíða", i = False)

<h2 class="innskraning_fyrirsogn">Búa til aðgang</h2>
<form class="innskraning" action="/blog/bua_til_adganginn" method="POST">
    <h3>Nafn</h3>
    <input type="text" name="nafn"><br>
    <h3>Notendanafn</h3>
    <input type="text" name="notendanafn"><br>
    <h3>Aðgangsorð</h3>
    <input type="password" name="adgangsord"><br>
    <h3>Aðgangsorð aftur</h3>
    <input type="password" name="adgangsord2"><br>
    <input class="linkur_takki innskra_takki" type="submit" value="Búa til aðgang" />
</form>

% include("Blog/fotur.tpl")