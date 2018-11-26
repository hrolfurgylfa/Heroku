% include("Blog/haus.tpl", t = "Forsíða", i = False)

<form class="innskraning" action="/blog/innskra_notenda" method="POST">
    <h2>Innskráning</h2>
    <h3>Notendanafn</h3>
    <input type="text" name="notendanafn"><br>
    <h3>Aðgangsorð</h3>
    <input type="password" name="adgangsord"><br>
    <input type="submit" value="Innskrá" />
</form>

% include("Blog/fotur.tpl")