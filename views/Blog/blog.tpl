<%
if n is False:
    include("Blog/haus.tpl", t = "Allir blog póstar", i = False)
else:
    include("Blog/haus.tpl", t = "Allir blog póstar", i = True)
end
%>

<h1>{{ p["TITILL"] }}</h1>

<p>{{ !p["TEXTI"] }}</p>

% include("Blog/fotur.tpl")