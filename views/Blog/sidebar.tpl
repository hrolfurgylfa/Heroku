<section class="sidebar">
    <h1><a class="ny_blog_titill" href="/blog/oll?sort=nyjast">Nýjustu blog</a></h1>
    <hr>
    % for i in f_d:
        <h2>{{ i["TITILL"] }}</h2>
        % try:
            % print(i["TEXTI"][100])
            <p>{{ i["TEXTI"][0:200] }}...</p>
        % except:
            <p>{{ i["TEXTI"][0:200] }}</p>
        % end
        <section class="sidebar_split">
            <p>{{ i["DAGSETNING"] }}</p>
            <p class="like_a_sidebar">{{ i["LIKES"] }}<img class="like_takki" src="/static/Blog/Myndir/Takkar/like_button.svg" alt="sem líkar þetta"></p>
        </section>
        <hr>
    % end
</section>