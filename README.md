# albion_project
Price checker, profit calculator

Projekta uzdevums bija izveidot programmu, kas iegūst informāciju no "Albion Online" spēles tirgus un aprēķina, cik izdevīgi ir izgatavot noteiktu preci šajā spēlē. ( Bear Paws )
Programma saņem informāciju no west.albion-online-data.com api, aprēķina iztērēto materiālu daudzumu, ņemot vērā tirdzniecības platformas komisijas maksu 5,5%, resursu atdevi pec izveidosanas 37,1%. Preču, materiālu cenas un rezultāts ( ieguvums no veidosanas ) tiek reģistrēti log-failos data, data_material, data_metal, data_wood, profit_list.

Lai saprast ko es skaitu:
1 izgatavotajā priekšmetā ir 20 metāla, 12 koka, 1 īpašs materiāls
37.1% tiek atgriezts pēc izveides ( neskaitot īpašo materialu )
5.5% tirgus nodoklis
1 priekšmetam ir:
    Tier : T4 - T8
    Enchance : 0 - 4
    Quality : 1 - 5

Aktuālas problemas:
1) albion-online-data.com/api nav oficiāls spēles Albion Online resurss, tāpēc cenas tiek atjaunotas ar nokavēšanu vai ar problēmām ( materiāls vai prece nav redzama noliktavā ).
2) Nav ņemts vērā pieprasījums pēc ražojamās preces un no tā  iespējamais cenas samazinājums.

Programmas lietošana nav sarežģīta, main.py failā jau ir ietverta nepieciešamā informācija, vajag tikai palaist programmu. Failā profit_list.txt būs saraksts ar visiem iespējamajiem priekšmetu izveides variantiem un ienākumu, kas sakārtoti pēc tier, enchance un quality.

Tika izmantotas bibliotēkas json, request lai saglabāt salasāmu informāciju un parasti iegūt to ar API
