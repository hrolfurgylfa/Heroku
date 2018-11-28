% include("Blog/haus.tpl", t = "Forsíða", i = True)

<section class="sidebar_holder">
    <section class="content">
        <h1 class="forsida_titill">Blog - Forsíða</h1>
        <h2 class="forsida_titill">Skrifa nýjann póst</h2>
        <form class="skrifa_nyjan_post" action="/blog/add_post" method="POST">
            <h3 class="h_newpost">Fyrirsögn</h3>
            <input class="fyrirsogn_newpost" type="text" name="fyrirsogn"><br>
            <h3 class="h_newpost">Meginmál</h3>
            <textarea name="efni" class="meginmal_newpost text_input_tinymce"></textarea>
            <!-- <textarea class="meginmal_newpost" type="text" name="efni" required></textarea><br> -->
            
            <input class="send_newpost" type="submit" value="Birta" />
        </form>
    </section>
    % include("Blog/sidebar.tpl", f_listi = f_d, l = "/blog/oll?f=nyjast", k_nafn = "sidebar", t = "Nýjustu blog")
    % include("Blog/sidebar.tpl", f_listi = f_l, l = "/blog/oll?f=mest_likad", k_nafn = "sidebar2", t = "Vinsælustu blog")
</section>

% include("Blog/fotur.tpl")