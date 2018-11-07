<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>Verkefni 7 - Admin síða</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" type="text/css" media="screen" href="/static/Verkefni_7/main.css" />
<body>
    <header class="header_admin">
        <h2>Velkomin/n {{ n }}</h1>
        <h3><a href="/Verkefni_7/utskra?u={{ u }}">Útskrá</a></h3>
    </header>
    <table class="tafla_1">
        <thead>
            <tr>
                <th>Nafn</th>
                <th>Notendanafn</th>
                <th>Aðgangsorð</th>
            </tr>
        </thead>
        <tbody>
            % for notandi in o:
                <tr>
                    <td data-label="Nafn">{{ notandi[2] }}</td>
                    <td data-label="Notendanafn">{{ notandi[0] }}</td>
                    <td data-label="Aðgangsorð">{{ notandi[1] }}</td>
                </tr>
            % end
        </tbody>
    </table>
</body>
</html>