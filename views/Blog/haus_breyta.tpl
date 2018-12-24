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
    <!-- Pell -->
    <link rel="stylesheet" type="text/css" href="https://unpkg.com/pell/dist/pell.min.css">
    <script>
        import pell from 'pell'
        // Initialize pell on an HTMLElement
        pell.init({
        // <HTMLElement>, required
        element: document.getElementById('pell'),

        // <Function>, required
        // Use the output html, triggered by element's `oninput` event
        onChange: html => console.log(html),

        // <string>, optional, default = 'div'
        // Instructs the editor which element to inject via the return key
        defaultParagraphSeparator: 'p',

        // <boolean>, optional, default = false
        // Outputs <span style="font-weight: bold;"></span> instead of <b></b>
        styleWithCSS: false,

        // <Array[string | Object]>, string if overwriting, object if customizing/creating
        // action.name<string> (only required if overwriting)
        // action.icon<string> (optional if overwriting, required if custom action)
        // action.title<string> (optional)
        // action.result<Function> (required)
        // Specify the actions you specifically want (in order)
        actions: [
            'bold',
            {
            name: 'custom',
            icon: 'C',
            title: 'Custom Action',
            result: () => console.log('Do something!')
            },
            'underline'
        ],

        // classes<Array[string]> (optional)
        // Choose your custom class names
        classes: {
            actionbar: 'pell-actionbar',
            button: 'pell-button',
            content: 'pell-content',
            selected: 'pell-button-selected'
        }
        })
    </script>
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