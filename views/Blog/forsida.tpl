% include("Blog/haus.tpl", t = "Forsíða", i = True)

<section class="sidebar_holder">
    <section class="content">
        <h1 class="forsida_titill">Blog - Forsíða</h1>
    </section>
    % include("Blog/sidebar.tpl", f_d = f_d)
    % include("Blog/sidebar2.tpl", f_l = f_l)
</section>

% include("Blog/fotur.tpl")