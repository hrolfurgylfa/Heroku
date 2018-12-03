<%
if n is False:
    include("Blog/haus.tpl", t = "Allir blog póstar", i = False)
else:
    include("Blog/haus.tpl", t = "Allir blog póstar", i = True)
end
%>

<section class="content_holder_postur">
    <h1 class="titill_postur">{{ p["TITILL"] }}</h1>
    <p class="meginmal_postur">{{ !p["TEXTI"] }}</p>
</section>

% include("Blog/fotur.tpl")