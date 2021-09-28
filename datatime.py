#labb 1
# from datetime import datetime, timedelta
# nu_tid= datetime.now()
# tid_secoder= nu_tid.strftime("%Y-%m-%d-%X")
# tid_useconder=nu_tid.strftime("%Y-%m-%d")
# print(tid_secoder)
# print(tid_useconder)

# labb2
# from datetime import datetime
# komp_tid=datetime (2016,8,16,3,57,32,11)
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

#labb4
from datetime import datetime, timedelta
till_40dagar= datetime.now()
org_tid= till_40dagar.strftime("%Y-%m-%d-%X")
weekDays = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
dag_efter40= till_40dagar+timedelta(days=40)
print(f"idag{till_40dagar}")
print(weekDays[dag_efter40.weekday()])
