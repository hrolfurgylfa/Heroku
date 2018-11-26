% include("Blog/haus.tpl", t = "Forsíða", i = False)

<h2 class="innskraning_fyrirsogn">Innskráning</h2>
<form class="innskraning" action="/blog/innskra_notenda" method="POST">
    <h3>Notendanafn</h3>
    <input type="text" name="notendanafn"><br>
    <h3>Aðgangsorð</h3>
    <input type="password" name="adgangsord"><br>
    <input class="linkur_takki innskra_takki" type="submit" value="Innskrá" />
</form>

% include("Blog/fotur.tpl")