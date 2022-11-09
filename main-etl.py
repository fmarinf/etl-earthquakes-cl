import os
import requests
import json
import datetime as dt
import pandas as pd
from pytz import timezone

CURRENT_PATH = '/home/runner/etl-earthquakes-cl/earthquakes_data'
if os.path.isdir(CURRENT_PATH):
  os.chdir(CURRENT_PATH)
else:
  os.mkdir(CURRENT_PATH)
  os.chdir(CURRENT_PATH)

response = requests.get("https://api.gael.cloud/general/public/sismos")

tz = timezone("America/Santiago")
today = dt.datetime.now(tz).strftime('%Y-%m-%d')

eqs = []
dataset_fields = ["Magnitude", "Depth", "GeographicalRef", "Date"]

for eq in response.json():
  dt = (eq['Fecha'])
  dp = eq['Profundidad']
  mag = eq['Magnitud']
  geo = eq['RefGeografica']
  up = eq['FechaUpdate']
  int_date = up[0:10]

  if int_date == today:
    up_magnitude = []
    up_depth = []
    up_geo = []

    up_depth.extend([mag, dp, geo])
    up_depth.append(int_date)

  eqs.append(up_depth)

    
earthquakes = pd.DataFrame(eqs, columns=dataset_fields)
earthquakes.to_csv(today + "_earthquales.csv", index=False)


if __name__ == '__main__':
  pass
  