<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>Admin síða</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" type="text/css" media="screen" href="/static/Verkefni_6_gamalt/main.css" />
<body>
    <header class="header_admin">
        <h1>Velkomin/n {{ u }}</h1>
        <h3><a href="/Verkefni_6/utskra?u={{ u }}">Útskrá</a></h3>
    </header>
    <table class="tafla_1">
        <thead>
            <tr>
                <th>Notendanafn</th>
                <th>Aðgangsorð</th>
                <th>Réttindi</th>
                <th>Breyta notandanafni</th>
                <th>Breyta aðgangsorð</th>
                <th>Eyða</th>
            </tr>
        </thead>
        <tbody>
            % for n in o:
                <tr>
                    <td data-label="Notendanafn">{{ n[0] }}</td>
                    <td data-label="Aðgangsorð">{{ n[1] }}</td>
                    % if n[2] == "0":
                        <td data-label="Réttindi">notandi</td>
                    % elif n[2] == "1":
                        <td data-label="Réttindi">stjórnandi</td>
                    % end
                    <td data-label="Breyta notendanafni">Breyta</td>
                    <td data-label="Breyta notendanafni">Breyta</td>
                    <td data-label="Eyða">X</td>
                </tr>
            % end
        </tbody>
    </table>
</body>
</html>