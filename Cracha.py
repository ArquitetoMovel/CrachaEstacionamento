from __future__ import print_function
from weasyprint import HTML
from jinja2 import Environment, FileSystemLoader
import pandas as pd
import numpy as np
df = pd.read_excel("Vagas.xlsx", sheet_name="Sheet2",
                   usecols=["Bloco", "Vaga", "Apartamento"])
#skiprow=1

env = Environment(loader=FileSystemLoader('.'))
template = env.get_template("cracha2.html")

#print (df.count())

#print (df[df["Apartamento"] == 32])

html_out = "<!DOCTYPE html>"
html_out = html_out + "<html>"
html_out = html_out + "<header>"
html_out = html_out + "<style type='text/css'>"
html_out = html_out + ".mysvg {"
html_out = html_out + "width: 298px;"
html_out = html_out + "height: 318px;"
html_out = html_out + "margin-top: 15px;"
html_out = html_out + "margin-right: 4px;"
html_out = html_out + "background-image: url(file:///Users/alexandredanelon/Develop/CrachaEstacionamento/logo_cracha.svg);"
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
   iterator = (index + 1)
   second_card = ((iterator % 2) == 0)
   if second_card == False:
      bloco1 = rw[0]
      apto1 = rw[1]
      Vaga1 = rw[2]
      if iterator == last_row:
         template_vars1 = {"bloco": bloco1, "apto": apto1, "Vaga": Vaga1}
         html_out = html_out + template.render(template_vars1)
   else:
      template_vars1 = {"bloco": bloco1, "apto": apto1, "Vaga": Vaga1, "bloco2": rw[0], "apto2": rw[1], "Vaga2": rw[2]}
      html_out = html_out + template.render(template_vars1)
   
html_out = html_out + "</body>"
html_out = html_out + "</html>"

HTML(string=html_out).write_pdf("crachas.pdf")
print(iterator , "cartões de estacionamento foram gerados.")
