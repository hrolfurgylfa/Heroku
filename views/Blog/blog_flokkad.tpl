<%
if n is False:
    include("Blog/haus.tpl", t = "Allir blog póstar", i = False)
else:
    include("Blog/haus.tpl", t = "Allir blog póstar", i = True)
end
%>

<h1 class="center oflokkad_fyrirsogn">{{ t }}</h1>
<section class="flokkad_efni">
    % include("Blog/sidebar.tpl", f_listi = listi, l = "", k_nafn = "", t = "")
</section>

% include("Blog/fotur.tpl")