import webbrowser

css_styles = """
<style>
/* Estilos CSS */
body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background-color: #f8f9fa;
    margin: 0;
    padding: 0;
}

.container {
    width: 80%;
    margin: 50px auto;
    background-color: #fff;
    border: 1px solid #ccc;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0,0,0,0.1);
    padding: 30px;
    text-align: center;
}

h1 {
    color: #333;
}

p {
    color: #666;
    font-size: 18px;
}
</style>
"""

html_content = """<HTML>
  <head>
    <title>¡Hola Mundo!</title>
    <!-- Enlace al archivo de estilos CSS -->
    {css_styles}
  </head>
  <body>
    <div class="container">
      <h1>¡Hola Mundo!</h1>
      <p>Este es un ejemplo de cómo crear una página web con Python y CSS.</p>
    </div>
  </body>  
</HTML>""".format(css_styles=css_styles)

with open('Hola-Mundo.html', 'w') as f:
    f.write(html_content)

webbrowser.open_new_tab('Hola-Mundo.html')
