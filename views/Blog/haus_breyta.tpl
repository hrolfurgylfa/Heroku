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
    <nav class="topnav">
        <ul class="topmenu">
            <li><a href="/blog">Heim</a></li>
            <li><a href="/blog">Skrifa nýjan póst</a></li>
            <!-- <li><a href="">Breyta nafni</a></li>
            <li><a href="">Breyta lykilorði</a></li> -->
            <li><a href="/blog/blog/utskra">Útskrá</a></li>
            <li><a href="/blog/breyta_post?id={{ id }}">Breyta pósti</a></li>
            <li><a href="/blog/eyda_post?id={{ id }}">Eyða pósti</a></li>
        </ul>
    </nav>
    <span class="nav_whitespace"></span>