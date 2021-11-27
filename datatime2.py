# #labb 1
# from datetime import datetime
# nu_tid= datetime.now()
# tid_secoder= nu_tid.strftime("%Y-%m-%d-%X")
# tid_useconder=nu_tid.strftime("%Y-%m-%d")
# print(tid_secoder)
# print(tid_useconder)

# #labb2
# from datetime import datetime
# komp_tid=datetime(2016,8,16,3,57,32,11)
# print("year=", komp_tid.year)
# print("month=",komp_tid.month)
# print("day=",komp_tid.day)
# print("hour=",komp_tid.hour)
# print("minute=",komp_tid.minute)
# print("second=",komp_tid.second)
# print("millisecond=",komp_tid.microsecond)


# #labb3
# from datetime import datetime
# spesfick_datim_dag= datetime (2016,11,7)
# weekDays = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
# print(f"The day of the week for 7/11/2016 is {weekDays[spesfick_datim_dag.weekday()]}")
# veckodag=["måndag", "tisdag","onsdag","torsdag","fredag","lördag","söndag"]
# print(f"Dagen av veckan för 7/11/2016 är{veckodag[spesfick_datim_dag.weekday()]}")

# # #labb4
# from datetime import datetime, timedelta
# från_nu= datetime.now()
# org_tid= från_nu.strftime("%Y-%m-%d-%X%p")
# weekDays = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
# dag_efter40= från_nu+timedelta(days=40)
# print(f"idag{org_tid}")
# print(f"dagen efter 40 dagar är {weekDays[dag_efter40.weekday()]}")

# #labb 5
# from datetime import datetime
# inmataning_data= input("mata in ett datum")
# data= datetime.strptime(inmataning_data,"%Y-%m-%d")
# print(data)



# #labb 6
# from datetime import datetime , timedelta
# month1 = "2022-02-28"
# month2 = "2022-03-28"

# firstInMonth = datetime.strptime(month1,"%Y-%m-%d")
# firstInNextMonth = datetime.strptime(month2, "%Y-%m-%d")
# firstInNextMonth = datetime.replace(firstInNextMonth, day = 1)
# firstInMonth = firstInMonth.date()
# firstInNextMonth = firstInNextMonth.date()

# firstMonth= firstInMonth.strftime('%b')
# antaldagar = firstInNextMonth - timedelta(days = 1)
# print(antaldagar)

# print(f"Antal dagar i {firstMonth} är {antaldagar.day}")



# #labb7

from datatime import datetime

första= (input("mata in ett datum"))
andra = (input("mata in ett till datum"))
p_första = datetime.strptime(första, "%Y-%m-%d")
p_andra = datetime.strptime(andra, "%Y-%m-%d")
p_första = p_första.date()
p_andra = p_andra.date()
# print(p_första)
# print(p_andra)

mella_skilnad= p_första - p_andra
print(f"skilnad dagar mellan dessa datumen är{mella_skilnad.days} dagar")