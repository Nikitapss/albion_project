from bs4 import BeautifulSoup
import requests
import json

# paws 4.0 - 8.4
# without fees
# including 37.1% recovery

url = "https://west.albion-online-data.com/api/v2/stats/prices/T4_2H_DUALAXE_KEEPER,T4_2H_DUALAXE_KEEPER@1,T4_2H_DUALAXE_KEEPER@2,T4_2H_DUALAXE_KEEPER@3,T4_2H_DUALAXE_KEEPER@4,T5_2H_DUALAXE_KEEPER,T5_2H_DUALAXE_KEEPER@1,T5_2H_DUALAXE_KEEPER@2,T5_2H_DUALAXE_KEEPER@3,T5_2H_DUALAXE_KEEPER@4,T6_2H_DUALAXE_KEEPER,T6_2H_DUALAXE_KEEPER@1,T6_2H_DUALAXE_KEEPER@2,T6_2H_DUALAXE_KEEPER@3,T6_2H_DUALAXE_KEEPER@4,T7_2H_DUALAXE_KEEPER,T7_2H_DUALAXE_KEEPER@1,T7_2H_DUALAXE_KEEPER@2,T7_2H_DUALAXE_KEEPER@3,T7_2H_DUALAXE_KEEPER@4,T8_2H_DUALAXE_KEEPER,T8_2H_DUALAXE_KEEPER@1,T8_2H_DUALAXE_KEEPER@2,T8_2H_DUALAXE_KEEPER@3,T8_2H_DUALAXE_KEEPER@4.json?locations=4002&qualities="
response = requests.get(url)
data1 = response.json()
#with open("data.json", "w") as file:
#    json.dump(data1, file, indent=2)
url_metal = "https://west.albion-online-data.com/api/v2/stats/prices/T4_METALBAR,T4_METALBAR_LEVEL1@1,T4_METALBAR_LEVEL2@2,T4_METALBAR_LEVEL3@3,T4_METALBAR_LEVEL4@4,T5_METALBAR,T5_METALBAR_LEVEL1@1,T5_METALBAR_LEVEL2@2,T5_METALBAR_LEVEL3@3,T5_METALBAR_LEVEL4@4,T6_METALBAR,T6_METALBAR_LEVEL1@1,T6_METALBAR_LEVEL2@2,T6_METALBAR_LEVEL3@3,T6_METALBAR_LEVEL4@4,T7_METALBAR,T7_METALBAR_LEVEL1@1,T7_METALBAR_LEVEL2@2,T7_METALBAR_LEVEL3@3,T7_METALBAR_LEVEL4@,T8_METALBAR,T8_METALBAR_LEVEL1@1,T8_METALBAR_LEVEL2@2,T8_METALBAR_LEVEL3@3,T8_METALBAR_LEVEL4@4.json?locations=4002"
response = requests.get(url_metal)
data2 = response.json()
#with open("data_metal.json", "w") as file:
#    json.dump(data2, file, indent=2)
url_wood = "https://west.albion-online-data.com/api/v2/stats/prices/T4_PLANKS,T4_PLANKS_LEVEL1@1,T4_PLANKS_LEVEL2@2,T4_PLANKS_LEVEL3@3,T4_PLANKS_LEVEL4@4,T5_PLANKS,T5_PLANKS_LEVEL1@1,T5_PLANKS_LEVEL2@2,T5_PLANKS_LEVEL3@3,T5_PLANKS_LEVEL4@4,T6_PLANKS,T6_PLANKS_LEVEL1@1,T6_PLANKS_LEVEL2@2,T6_PLANKS_LEVEL3@3,T6_PLANKS_LEVEL4@4,T7_PLANKS,T7_PLANKS_LEVEL1@1,T7_PLANKS_LEVEL2@2,T7_PLANKS_LEVEL3@3,T7_PLANKS_LEVEL4@4,T8_PLANKS,T8_PLANKS_LEVEL1@1,T8_PLANKS_LEVEL2@2,T8_PLANKS_LEVEL3@3,T8_PLANKS_LEVEL4@4.json?locations=4002"
response = requests.get(url_wood)
data3 = response.json()
#with open("data_wood.json", "w") as file:
#    json.dump(data3, file, indent=2)
url_material = "https://west.albion-online-data.com/api/v2/stats/prices/T4_ARTEFACT_TOKEN_FAVOR_3,T5_ARTEFACT_TOKEN_FAVOR_3,T6_ARTEFACT_TOKEN_FAVOR_3,T7_ARTEFACT_TOKEN_FAVOR_3,T8_ARTEFACT_TOKEN_FAVOR_3,T4_ARTEFACT_2H_DUALAXE_KEEPER,T5_ARTEFACT_2H_DUALAXE_KEEPER,T6_ARTEFACT_2H_DUALAXE_KEEPER,T7_ARTEFACT_2H_DUALAXE_KEEPER,T8_ARTEFACT_2H_DUALAXE_KEEPER.json?locations=4002"
response = requests.get(url_material)
data4 = response.json()
#with open("data_material.json", "w") as file:
#    json.dump(data4, file, indent=2)

min_price = 999999999
mid_price = []
# 12 wood + 20 metal + 1 material
# +4% premium fee, +1.5% market fee
# Worth it?
# Sometimes server has no data, so profit could be unknown

for i in range(125):
    if(data1[i]["sell_price_min"] > 0):
        if(data1[i]["sell_price_min"] < min_price):
            min_price = data1[i]["sell_price_min"]
if(data4[0]["sell_price_min"] < data4[1]["sell_price_min"]):
    print(20*data2[0]["sell_price_min"] + 12*data3[0]["sell_price_min"] + data4[0]["sell_price_min"])
else:
    print(20*data2[0]["sell_price_min"] + 12*data3[0]["sell_price_min"] + data4[1]["sell_price_min"])

# print(data1[i]["item_id"] + " " + str(data1[i]["sell_price_min"]))