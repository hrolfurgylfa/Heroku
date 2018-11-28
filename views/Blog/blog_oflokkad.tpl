<%
if n is False:
    include("Blog/haus.tpl", t = "Allir blog póstar", i = False)
else:
    include("Blog/haus.tpl", t = "Allir blog póstar", i = True)
end
%>

<h1 class="center oflokkad_fyrirsogn">Allir blog póstar</h1>
<section class="sidebar_holder_half">
    % include("Blog/sidebar.tpl", f_listi = f_d, l = "/blog/oll?f=nyjast", k_nafn = "sidebar", t = "Nýjustu blog")
    % include("Blog/sidebar.tpl", f_listi = f_l, l = "/blog/oll?f=mest_likad", k_nafn = "sidebar2", t = "Vinsælustu blog")
</section>

% include("Blog/fotur.tpl")