import requests
import json

url = "https://west.albion-online-data.com/api/v2/stats/prices/T4_2H_DUALAXE_KEEPER,T4_2H_DUALAXE_KEEPER@1,T4_2H_DUALAXE_KEEPER@2,T4_2H_DUALAXE_KEEPER@3,T4_2H_DUALAXE_KEEPER@4,T5_2H_DUALAXE_KEEPER,T5_2H_DUALAXE_KEEPER@1,T5_2H_DUALAXE_KEEPER@2,T5_2H_DUALAXE_KEEPER@3,T5_2H_DUALAXE_KEEPER@4,T6_2H_DUALAXE_KEEPER,T6_2H_DUALAXE_KEEPER@1,T6_2H_DUALAXE_KEEPER@2,T6_2H_DUALAXE_KEEPER@3,T6_2H_DUALAXE_KEEPER@4,T7_2H_DUALAXE_KEEPER,T7_2H_DUALAXE_KEEPER@1,T7_2H_DUALAXE_KEEPER@2,T7_2H_DUALAXE_KEEPER@3,T7_2H_DUALAXE_KEEPER@4,T8_2H_DUALAXE_KEEPER,T8_2H_DUALAXE_KEEPER@1,T8_2H_DUALAXE_KEEPER@2,T8_2H_DUALAXE_KEEPER@3,T8_2H_DUALAXE_KEEPER@4.json?locations=4002&qualities="
response = requests.get(url)
data1 = response.json()
with open("data.json", "w") as file:
    json.dump(data1, file, indent=2)
url_metal = "https://west.albion-online-data.com/api/v2/stats/prices/T4_METALBAR,T4_METALBAR_LEVEL1@1,T4_METALBAR_LEVEL2@2,T4_METALBAR_LEVEL3@3,T4_METALBAR_LEVEL4@4,T5_METALBAR,T5_METALBAR_LEVEL1@1,T5_METALBAR_LEVEL2@2,T5_METALBAR_LEVEL3@3,T5_METALBAR_LEVEL4@4,T6_METALBAR,T6_METALBAR_LEVEL1@1,T6_METALBAR_LEVEL2@2,T6_METALBAR_LEVEL3@3,T6_METALBAR_LEVEL4@4,T7_METALBAR,T7_METALBAR_LEVEL1@1,T7_METALBAR_LEVEL2@2,T7_METALBAR_LEVEL3@3,T7_METALBAR_LEVEL4@,T8_METALBAR,T8_METALBAR_LEVEL1@1,T8_METALBAR_LEVEL2@2,T8_METALBAR_LEVEL3@3,T8_METALBAR_LEVEL4@4.json?locations=4002"
response = requests.get(url_metal)
data2 = response.json()
with open("data_metal.json", "w") as file:
    json.dump(data2, file, indent=2)
url_wood = "https://west.albion-online-data.com/api/v2/stats/prices/T4_PLANKS,T4_PLANKS_LEVEL1@1,T4_PLANKS_LEVEL2@2,T4_PLANKS_LEVEL3@3,T4_PLANKS_LEVEL4@4,T5_PLANKS,T5_PLANKS_LEVEL1@1,T5_PLANKS_LEVEL2@2,T5_PLANKS_LEVEL3@3,T5_PLANKS_LEVEL4@4,T6_PLANKS,T6_PLANKS_LEVEL1@1,T6_PLANKS_LEVEL2@2,T6_PLANKS_LEVEL3@3,T6_PLANKS_LEVEL4@4,T7_PLANKS,T7_PLANKS_LEVEL1@1,T7_PLANKS_LEVEL2@2,T7_PLANKS_LEVEL3@3,T7_PLANKS_LEVEL4@4,T8_PLANKS,T8_PLANKS_LEVEL1@1,T8_PLANKS_LEVEL2@2,T8_PLANKS_LEVEL3@3,T8_PLANKS_LEVEL4@4.json?locations=4002"
response = requests.get(url_wood)
data3 = response.json()
with open("data_wood.json", "w") as file:
    json.dump(data3, file, indent=2)
url_material = "https://west.albion-online-data.com/api/v2/stats/prices/T4_ARTEFACT_TOKEN_FAVOR_3,T5_ARTEFACT_TOKEN_FAVOR_3,T6_ARTEFACT_TOKEN_FAVOR_3,T7_ARTEFACT_TOKEN_FAVOR_3,T8_ARTEFACT_TOKEN_FAVOR_3,T4_ARTEFACT_2H_DUALAXE_KEEPER,T5_ARTEFACT_2H_DUALAXE_KEEPER,T6_ARTEFACT_2H_DUALAXE_KEEPER,T7_ARTEFACT_2H_DUALAXE_KEEPER,T8_ARTEFACT_2H_DUALAXE_KEEPER.json?locations=4002"
response = requests.get(url_material)
data4 = response.json()
with open("data_material.json", "w") as file:
    json.dump(data4, file, indent=2)

mid_price = [43600, 62000, 90000, 230000, 2900000,      85000, 77000, 77000, 100000, 600000]
#T4 - T8 magic -> T4 - T8 axe material

# 12 wood + 20 metal + 1 material
# +4% premium fee, +1.5% market fee, +37.1% metal, wood recovery bonus
# Worth it?
# Sometimes server has no data, so profit could be unknown
# Middle price is only for materials

def material_price(tier):
    arr = [data4[tier]["sell_price_min"], data4[tier+5]["sell_price_min"], mid_price[tier], mid_price[tier+5]] # lowest in 4 prices
    arr.sort()
    for i in arr:
        if(i > 0):
            return i

i = 0
res_i = 0
f = open("profit_list.txt", "w")
f.write(" ")
f.close()

for tier in range(5): #tier 4,5,6,7,8
    for ench in range(5): # enchantment 0,1,2,3,4
        if(data2[res_i]["sell_price_min"] != 0 and data3[res_i]["sell_price_min"] != 0):
            for qual in range(5): # quality 1,2,3,4,5
                if(data1[i]["sell_price_min"] != 0):
                    price = data2[res_i]["sell_price_min"] * (20 - 20 * 0.371) + data3[res_i]["sell_price_min"] * (12 - 12 * 0.371) + material_price(tier) # material recovery
                    sold_for = data1[i]["sell_price_min"] - 0.055 * data1[i]["sell_price_min"] # fee
                    with open("profit_list.txt", "a") as file:
                        file.write("T"+str(tier+4) + "E" + str(ench) + " Paws | quality :" + str(qual) + "\n" + "Metal(1) : " + str(data2[res_i]["sell_price_min"]) + "\n" + "Wood(1) : " + str(data3[res_i]["sell_price_min"]) + "\n" + "Material : " + str(material_price(tier)) + "\n" + "Profit : " + str(round(sold_for-price)))
                        file.write("\n---------")
                i+=1
        else:
            i+=5
        res_i+=1