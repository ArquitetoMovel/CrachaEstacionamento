from __future__ import print_function
from weasyprint import HTML
from jinja2 import Environment, FileSystemLoader
import pandas as pd
import numpy as np
df = pd.read_excel("Vagas2.xlsx", sheet_name="VG1",
                   usecols=["Bloco", "Vaga", "Apartamento", "Nbloco"])

env = Environment(loader=FileSystemLoader('.'))
template = env.get_template("cracha3.html")

html_out = "<!DOCTYPE html>"
html_out = html_out + "<html>"
html_out = html_out + "<header>"
html_out = html_out + "<style type='text/css'>"
html_out = html_out + ".mysvg {"
html_out = html_out + "width: 298px;"
html_out = html_out + "height: 318px;"
html_out = html_out + "margin-top: 15px;"
html_out = html_out + "margin-right: 4px;"
html_out = html_out + \
    "background-image: url(file:///Users/alexandredanelon/Develop/CrachaEstacionamento/logo_cracha.svg);"
html_out = html_out + "background-position: 0 0;"
html_out = html_out + "background-repeat: no-repeat;"
html_out = html_out + "background-size: 95%;"
html_out = html_out + "}"
html_out = html_out + "@page {"
html_out = html_out + "margin: 0.5cm"
html_out = html_out + "}"
html_out = html_out + "</style>"
html_out = html_out + "</header>"
html_out = html_out + "<body>"
#ml_out + "<div style='margin-top:5px;' />"

second_card = False
last_row = len(df.index)

for index, rw in df.iterrows():
    #bloco1 = rw[0]
    id_bloco = rw[1]
    apto1 = rw[2]
    Vaga1 = rw[3]
    bloco1 =rw[0]

    if id_bloco == 2:
        iterator = (index + 1)
        template_vars1 = {"bloco": bloco1, "apto": apto1, "Vaga": Vaga1}
        html_out = html_out + template.render(template_vars1)


html_out = html_out + "</body>"
html_out = html_out + "</html>"

HTML(string=html_out).write_pdf("crachas_bloco2.pdf")
#print(iterator , "cartões de estacionamento foram gerados.")
