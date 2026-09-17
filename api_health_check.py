import requests
import pandas as pd

url = "https://getmfdata.com/api/health"


api_health_check = requests.get(url)
api_health_check_data =  api_health_check.json()
# print(api_health_check_data)

api_df = pd.DataFrame([api_health_check_data])

print(api_df)








