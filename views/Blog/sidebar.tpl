<section class="{{ k_nafn }}">
    <h1><a class="ny_blog_titill" href="{{ l }}">{{ t }}</a></h1>
    % tel = 1
    % for i in f_listi:
        % if tel >= 5:
            % break
        % end
        <section class="frett_{{ k_nafn }}_{{ tel }}">
            <h2>{{ i["TITILL"] }}</h2>
            % try:
                <p>{{ !i["TEXTI"][0:200] }}...</p>
            % except:
                <p>{{ !i["TEXTI"][0:200] }}</p>
            % end
            <section class="sidebar_split">
                % dagsetning = str(i["DAGSETNING"])
                % ny_dagsetning = dagsetning[8:10]+"/"+dagsetning[5:7]+"/"+dagsetning[0:4]+" "+dagsetning[11:16]
                <p>{{ ny_dagsetning }}</p>
                <p class="like_a_sidebar">{{ i["LIKES"] }}<img class="like_takki" src="/static/Blog/Myndir/Takkar/like_button2.svg" alt="sem líkar þetta"></p>
            </section>
        </section>
        % tel += 1
    % end
</section>