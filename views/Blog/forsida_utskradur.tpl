% include("Blog/haus.tpl", t = "Forsíða", i = False)

<section class="sidebar_holder_half">
    % include("Blog/sidebar.tpl", f_listi = f_d, l = "/blog/oll?f=nyjast", k_nafn = "sidebar", t = "Nýjustu blog")
    % include("Blog/sidebar.tpl", f_listi = f_l, l = "/blog/oll?f=mest_likad", k_nafn = "sidebar2", t = "Vinsælustu blog")
</section>

% include("Blog/fotur.tpl")