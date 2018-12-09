<%
try:
    include("Blog/haus_breyta.tpl", t = p['TITILL'], e = e, id = p["ID"])
except:
    if n is False:
        include("Blog/haus.tpl", t = p['TITILL'], i = False)
    else:
        include("Blog/haus.tpl", t = p['TITILL'], i = True)
    end
end
%>

<section class="content_holder_postur">
    <h1 class="titill_postur">{{ p["TITILL"] }}</h1>
    <p class="meginmal_postur">{{ !p["TEXTI"] }}</p>
    <h4 class="hofundur"><a href="/blog/oll?u={{ p["POST_OWNER"] }}" class="nafna_linkur">{{ p["NAFN"] }}</a></h4>
    <section class="sidebar_split">
        % dagsetning = str(p["DAGSETNING"])
        % ny_dagsetning = dagsetning[8:10]+"/"+dagsetning[5:7]+"/"+dagsetning[0:4]+" "+dagsetning[11:16]
        <p>{{ ny_dagsetning }}</p>
        <p class="like_a_sidebar">{{ p["LIKES"] }}<a href="/blog/lika?id={{ p['ID']}}&rurl=postur?id={{ p['ID'] }}"><img class="like_takki" src="/static/Blog/Myndir/Takkar/like_button2.svg" alt="sem líkar þetta"></a></p>
    </section>
</section>

% include("Blog/fotur.tpl")