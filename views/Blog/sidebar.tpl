<section class="sidebar">
    <h1><a class="ny_blog_titill" href="/blog/oll?sort=nyjast">Nýjustu blog</a></h1>
    <hr>
    % for i in l:
        <h2>{{ i[2] }}</h2>
        % try:
            % print(i[3][100])
            <p>{{ i[3][0:200] }}...</p>
        % except:
            <p>{{ i[3][0:200] }}</p>
        % end
        <hr>
    % end
</section>