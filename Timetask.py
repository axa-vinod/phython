from datetime import datetime
current_time=(datetime.now())
print(current_time)
format1=current_time.strftime("%Y-%m-%d %H:%M:%S")
print(format1)
format2=current_time.strftime("%m/%d/%Y")
print(format2)
format3=current_time.strftime("%A,%B %d,%Y")
print(format3)
formate4=current_time.strftime("%A,%B %d,%Y %H:%M,%S %p")
print(formate4)
format5=current_time.strftime("%a-%b-%d %H:%m:%S IST %Y")
print(format5)
format6=current_time.strftime("%d")
print(format6)
format7=current_time.strftime("%H:%m:%S")
print(format7)
format8=current_time.isoformat()
print(format8)
format9=current_time.strftime("%m")
print(format9)
format10=current_time.strftime("%Y")
print(format10)