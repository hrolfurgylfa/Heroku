% include("Blog/haus.tpl", t = "Forsíða", i = True)

<section class="sidebar_holder">
    <section class="content">
        <h1 class="forsida_titill">Blog - Forsíða</h1>
        <form class="skraning_a_namskeid" action="/blog/add_post" method="POST">
            <h3 class="h_newpost">Fyrirsögn</h3>
            <input class="fyrirsogn_newpost" type="text" name="fyrirsogn" required><br>
            <h3 class="h_newpost">Meginmál</h3>
            <input class="meginmal_newpost" type="text" name="efni" required><br>
            
            <input class="send_newpost" type="submit" value="Senda" />
        </form>
    </section>
    % include("Blog/sidebar.tpl", f_d = f_d)
    % include("Blog/sidebar2.tpl", f_l = f_l)
</section>

% include("Blog/fotur.tpl")