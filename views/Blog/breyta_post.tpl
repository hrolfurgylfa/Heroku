<%
if n is False:
    include("Blog/haus.tpl", t = "Allir blog póstar", i = False)
else:
    include("Blog/haus.tpl", t = "Allir blog póstar", i = True)
end
%>

<section class="breyta_post">
    <h1 class="forsida_titill">Blog - Forsíða</h1>
    <h2 class="forsida_titill">Skrifa nýjann póst</h2>
    <form class="skrifa_nyjan_post" action="/blog/uppfaera_post" method="POST">
        <h3 class="h_newpost">Fyrirsögn</h3>
        <input class="fyrirsogn_newpost" type="text" name="fyrirsogn_breytapost" value="{{ p["TITILL"] }}"><br>
        <h3 class="h_newpost">Meginmál</h3>
        <textarea name="efni_breytapost" class="pell">{{ p["TEXTI"] }}</textarea>
        
        <input class="send_newpost" type="submit" value="Birta" />
    </form>
</section>

% include("Blog/fotur.tpl")