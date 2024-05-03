speed_user = float(input())

if speed_user <= 10:
    print("slow")
elif 10 < speed_user <= 50:
    print("average")
elif 50 < speed_user <= 150:
    print("fast")
elif 150 < speed_user <= 1000:
    print("ultra fast")
else:
    print("extremely fast")