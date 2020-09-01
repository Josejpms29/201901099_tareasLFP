import json
import webbrowser

with open('Reporte.json') as file:
    data = json.load(file)

new_webpage = open('Archivohtml.html', 'w')
new_webpage.write(str(data))
new_webpage.close()

webbrowser.open_new_tab('Archivohtml.html')