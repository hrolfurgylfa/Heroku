% include("midannarverkefni/haus.tpl", titill = "Bensín verð")

<section class="oll_fyrirtaeki">
% tel = 0
% for fyrirtaeki in oll_fyrirtaeki:
    <a href="/midannarverkefni/{{ oll_fyrirtaeki_linkar[tel] }}/">{{ fyrirtaeki }}</a>
%   tel += 1
% end
</section>
<section class="odyrasta_bensin">
    <div>
        <p>Ódýrasta 95 oktan bensín án lykils er hjá: {{ bensin_listi[0][0] }}<br>Verð: {{ bensin_listi[0][1] }}kr.</p>
        <p>Ódýrasta 95 oktan bensín með lykli er hjá: {{ bensin_listi[1][0] }}<br>Verð: {{ bensin_listi[1][1] }}kr.</p>
    </div>
    <div>
        <p>Ódýrasta dísel án lykils er hjá: {{ bensin_listi[2][0] }}<br>Verð: {{ bensin_listi[2][1] }}kr.</p>
        <p>Ódýrasta dísel með lykli er hjá: {{ bensin_listi[3][0] }}<br>Verð: {{ bensin_listi[3][1] }}kr.</p>
    </div>
</section>
<img width="100%" src="/static/midannarverkefni/gasoline-175122_1280.jpg">

% include("midannarverkefni/fotur.tpl", sott = gogn["timestampPriceCheck"])
