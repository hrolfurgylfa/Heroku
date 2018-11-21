<section class="sidebar">
    <h1><a class="ny_blog_titill" href="/blog/oll?sort=mest_likad">Vinsælustu blog</a></h1>
    <hr>
    % for i in f_l:
        <h2>{{ i[TITILL] }}</h2>
        % try:
            % print(i[TEXTI][100])
            <p>{{ i[TEXTI][0:200] }}...</p>
        % except:
            <p>{{ i[TEXTI][0:200] }}</p>
        % end
        <hr>
    % end
</section>