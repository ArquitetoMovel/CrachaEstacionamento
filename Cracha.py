from __future__ import print_function
import pandas as pd
import numpy as np
df = pd.read_excel("Vagas.xlsx", sheet_name="Sheet1", usecols=["Bloco", "Vaga", "Apartamento"])
#skiprow=1

from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template("cracha.html")

#print (df.count())

#print (df[df["Apartamento"] == 32])

html_out = ""

for index, rw in df.iterrows():
   template_vars = {"bloco" : rw[0], "apto": rw[1], "Vaga": rw[2]}
   html_out = html_out + template.render(template_vars) 
   
   
from weasyprint import HTML
HTML(string=html_out).write_pdf("crachas.pdf")

#print(df.head(33))

#print(df["Bloco"])
#print(df["Vaga"])
#print(df["Apartamento"])