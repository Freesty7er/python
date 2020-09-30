int_time_in_sec = int(input("input time in sec"))

hours = int_time_in_sec // (60*60)

int_time_in_sec = int_time_in_sec - hours*60*60
minutes = int_time_in_sec // 60

int_time_in_sec = int_time_in_sec - minutes*60
seconds = int_time_in_sec

print("%d:%d:%d"%(hours, minutes,seconds))