<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>Blog - {{ t }}</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" type="text/css" media="screen" href="/static/Blog/main.css" />
    <link href="https://fonts.googleapis.com/css?family=Ubuntu" rel="stylesheet">
    <!-- TinyMCE -->
    <script src="https://cloud.tinymce.com/stable/tinymce.min.js"></script>
    <script>tinymce.init({ selector:".text_input_tinymce" });</script>
</head>
<body>
    % if i == True:
        <nav class="topnav">
            <input type="checkbox" id="toggle">
            <label for="toggle">Efnisyfirlit &#9776;</label>
            <ul class="topmenu">
                <li><a href="">Skrifa nýjan póst</a></li>
                <li><a href="">Breyta nafni</a></li>
                <li><a href="">Breyta lykilorði</a></li>
                <li><a href="">Útskrá</a></li>
            </ul>
        </nav>
    % else:
        <nav class="topnav">

        </nav>
    % end
    <span class="nav_whitespace"></span>