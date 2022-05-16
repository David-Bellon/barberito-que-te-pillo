import re
import pandas as pd
df1 = pd.read_csv("conversiones.csv")
df2 = pd.read_csv("navegacion.csv")


df1


df1.head()


df1._get_value(0,"date;hour;id_lead;id_user;gclid;lead_type;result")


df1.shape


lst_conver = []
lst_naveg = []
for i in range(df1.shape[0]):
    inf = df1._get_value(i, "date;hour;id_lead;id_user;gclid;lead_type;result")
    lst_conver.append(inf.split(";"))
for i in range(df2.shape[0]):
    inf = df2._get_value(i, "ts;uuid;id_user;gclid;user_recurrent;url_landing")
    lst_naveg.append(inf.split(";"))


conv = pd.DataFrame(lst_conver, columns = ["date", "hour ", "id_lead", "id_user", "gclid", "lead_type", "result"])


conv.to_csv("conversio.csv", index = False)


navega = pd.DataFrame(lst_naveg, columns = ["ts", "uuid", "id_user", "gclid", "user_recurrent", "url_landing"])

navega


navega.to_csv("naveg.csv", index = False)


#navega => navegacion
#conv => conversion

for i in range(conv.shape[0]):
    for j in range(navega.shape[0]):
        if conv._get_value(i, "id_user") == navega._get_value(j, "id_user"):
            print("igual", i, j)
            print(navega._get_value(j, "url_landing"))


conv


m = re.search("http(?:s?):\/(?:\/?)www\.metropolis\.com\/es\/(.+)\/.*", "https://www.metropolis.com/es/tria/gclid=Cj0KCQjw-NaJBhDsARIsAAja6dNimSUGFYxf8ytfPM_7MQ64eyzcrfYSEql3F8CSduFIkcOppkRlXwsaArHSEALw_wcB&idUser=87ba62b2-fcee-45ec-9dca-b15d8c57c908&uuid=dd0085c7-6ee5-4026-a136-a3335a22882f&camp=1648648995&adg=62589383945&device=m&sl=&adv=481025151787&rec=false&;")

#cuantas visitas recibe el cliente al dia
#el numero de visitas son el numero de filas del fichero, no deberia de haber ningun uuid igual ya que siempre es unico y puede haber mismo userid asi que eso
navega.shape[0]


number = 0
for i in range(conv.shape[0]):
    for j in range(navega.shape[0]):
        if conv._get_value(i, "id_user") == navega._get_value(j, "id_user"):
            number += 1
(number / navega.shape[0]) * 100
print(number)


l = []
for i in range(conv.shape[0]):
    if conv._get_value(i, "id_user") == "None":
        l.append(i)


l


conv.drop(conv.index[l], inplace = True)


conv


conv.to_csv("conversio.csv", index = False)


conv = pd.read_csv("conversio.csv")





call = 0
form = 0
for i in range(conv.shape[0]):
    if conv._get_value(i, "lead_type") == "CALL":
        call += 1
    else:
        form += 1

print("Call hay", call, "y form hay", form)


s_recurrent = {()}
s_users = {()}
for i in range(navega.shape[0]):
    s_users.add(navega._get_value(i, "id_user"))
    if navega._get_value(i, "user_recurrent") == "true":
        s_recurrent.add(navega._get_value(i, "id_user"))
        
print("El porcentaje es de", (len(s_recurrent) / len(s_users)) * 100)


cars = {
    
}
for i in range(navega.shape[0]):
    m = re.search("http(?:s?):\/(?:\/?)www\.metropolis\.com\/es\/(.+?)\/.*", navega._get_value(i, "url_landing"))
    if m != None:
        if m.groups()[0] in cars:
            cars[m.groups()[0]] += 1
        else:
            cars[m.groups()[0]] = 1
        

for car in cars.keys():
    print("El coche", car, "ha sido buscado", cars[car], "veces")


succes = {
    
}
for i in range(navega.shape[0]):
    m = re.search("http(?:s?):\/(?:\/?)www\.metropolis\.com\/es\/(.+?)\/.*", navega._get_value(i, "url_landing"))
    if m != None:
        user = navega._get_value(i, "id_user")
        for j in range(conv.shape[0]):
            if user == conv._get_value(j, "id_user"):
                if m.groups()[0] in succes:
                    succes[m.groups()[0]] += 1
                else:
                    succes[m.groups()[0]] = 1


succes


only_conv = navega["id_user"]


only_conv


user_conv = []
for user in only_conv:
    cond = False
    for i in range(conv.shape[0]):
        if user == conv._get_value(i, "id_user"):
            cond = True
    
    if cond:
        user_conv.append(1)
    else:
        user_conv.append(0)
            


df_all = navega


len(user_conv)


df_all = df_all.assign(Convert = pd.Series(user_conv).values)


df_all.to_csv("AllInfo.csv", index = False)