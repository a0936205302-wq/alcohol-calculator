SHOW_DETAILS=False
SHOW_ADVANCED_INPUT=False
# 中文漢化版酒精計算機 ver1.1
print("有夠好用酒精計算機")
drink_list=[]
METABOLISM_RATE=10
while True:
    print("1. 事前預估模式")
    print("2. 事後回推模式")
    print("3. 已知開車時間，反推可喝量模式")

    mode=input("選擇模式:")
    
    if mode =="1":
        print("你選擇了事前預估模式:")
        if SHOW_ADVANCED_INPUT:
          weight=float(input("Enter weight:"))
          sex=input("Enter sex:")
          empty_stomach=input("Are you empty stomach? (y/n)")
        
        age=int(input("年齡:"))
        print("新增酒類")
        drink_name=input("酒類名稱:")
        volume=float(input("容量(ml):"))
        abv=float(input("酒精含量(%):"))
        count=float(input("數量:"))
        start_time=input("開始時間(HH:MM):")
        hour,minute=start_time.split(":")
        hour=int(hour)
        minute=int(minute)
        start_minutes=hour*60+minute
        drinking_duration=float(input("預估喝多久(小時):"))
        drinking_minutes=int(drinking_duration*60)
        finish_time_minutes=start_minutes+drinking_minutes
        finish_hour=finish_time_minutes//60
        finish_minutes=finish_time_minutes%60
        print(f"結束時間: {finish_hour:02d}:{finish_minutes:02d}")
        total_alcohol=volume*(abv/100)*0.789*count
        metabolism_hours=total_alcohol/METABOLISM_RATE
        metabolism_minutes=metabolism_hours*60
        earliest_drive_minutes=int(finish_time_minutes+metabolism_minutes)
        earliest_drive_minutes = earliest_drive_minutes%(24*60)
        earliest_drive_hours=earliest_drive_minutes//60
        earliest_drive_minute=earliest_drive_minutes%60
        print("總酒精量:",total_alcohol,"克")
        print(f"你可以在 {earliest_drive_hours:02d}:{earliest_drive_minute:02d} 之後開車")
        if age>51:
          print("年齡超過51歲,請多抓更多緩衝時間。")
          
        elif age>31:
          print("年齡超過31歲,請多抓緩衝時間。")
        if SHOW_DETAILS:
          print("Total alcohol:",total_alcohol)
          print("Metabolism hours:",metabolism_hours)
          
        break
        
    elif mode =="2":
        print("你選擇了事後回推模式")
        if SHOW_ADVANCED_INPUT:
          weight=float(input("Enter weight:"))
          sex=input("Enter sex:")
          empty_stomach=input("Are you empty stomach? (y/n)")
        
        age=int(input("年齡:"))
        print("新增酒類")
        drink_name=input("酒類名稱:")
        volume=float(input("容量(ml):"))
        abv=float(input("酒精含量(%):"))
        count=float(input("數量:"))
        current_time=input("現在時間(HH:MM):")
        hour,minute=current_time.split(":")
        hour=int(hour)
        minute=int(minute)
        current_minutes=hour*60+minute
        drinking_duration=float(input("已經喝了多久 (小時):"))
        drinking_minutes=int(drinking_duration*60)
        start_time_minutes=current_minutes-drinking_minutes
        start_time_minutes=start_time_minutes%(24*60)
        start_hour=start_time_minutes//60
        start_minutes=start_time_minutes%60
        print(f"從: {start_hour:02d}:{start_minutes:02d} 開始喝")
        print("喝到:",current_time)
        total_alcohol=volume*(abv/100)*0.789*count
        metabolism_hours=total_alcohol/METABOLISM_RATE
        metabolism_minutes=metabolism_hours*60
        earliest_drive_minutes=int(current_minutes+metabolism_minutes)
        earliest_drive_minutes = earliest_drive_minutes%(24*60)
        earliest_drive_hours=earliest_drive_minutes//60
        earliest_drive_minute=earliest_drive_minutes%60
        print("總酒精量:",total_alcohol,"克")
        print(f"你可以在 {earliest_drive_hours:02d}:{earliest_drive_minute:02d} 之後開車")
        if age>51:
          print("年齡超過51歲,請多抓更多緩衝時間。")
          
        elif age>31:
          print("年齡超過31歲,請多抓緩衝時間。")
        if SHOW_DETAILS:
          print("Total alcohol:",total_alcohol)
          print("Metabolism hours:",metabolism_hours)
          
        break
          
    elif mode =="3":
        print("你選擇了已知開車時間，反推可喝量模式")
        if SHOW_ADVANCED_INPUT:
          weight=float(input("Enter weight:"))
          sex=input("Enter sex:")
          empty_stomach=input("Are you empty stomach? (y/n)")
        
        age=int(input("年齡:"))
        print("新增酒類")
        drink_name=input("酒類名稱:")
        volume=float(input("容量(ml):"))
        abv=float(input("酒精含量(%):"))
        current_time=input("輸入現在時間 (HH:MM):")
        hour,minute=current_time.split(":")
        hour=int(hour)
        minute=int(minute)
        current_minutes=hour*60+minute
        drive_time=input("預計開始開車時間 (HH:MM):")
        hour,minute=drive_time.split(":")
        hour=int(hour)
        minute=int(minute)
        drive_minutes=hour*60+minute
        available_minutes=drive_minutes-current_minutes
        if available_minutes<0:
           available_minutes=available_minutes+24*60
        available_hours=available_minutes/60
        print(f"可用時間: {available_hours:.1f} 小時")
        max_alcohol=available_hours*METABOLISM_RATE
        single_alcohol=volume*(abv/100)*0.789
        max_count=max_alcohol/single_alcohol
        print(f"可代謝酒精上限: {max_alcohol:.1f} 克")
        print(f"最大可飲酒量: {max_count:.1f}")
        safe_count=int(max_count)
        print("最大可飲酒罐數:",safe_count)
        if age>51:
          print("年齡超過51歲,請多抓更多緩衝罐數。")
          
        elif age>31:
          print("年齡超過31歲,請多抓緩衝罐數。")
        break
          
    else:
        print("輸入錯誤")
        print("重新選擇啦白癡= =")