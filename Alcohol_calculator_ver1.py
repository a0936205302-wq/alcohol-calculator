SHOW_DETAILS=False
SHOW_ADVANCED_INPUT=False
# AC ver1.1

print("Alcohol Calculator")
drink_list=[]
METABOLISM_RATE=10
while True:
    print("1. Estimate before drinking")
    print("2. Calculate after drinking")
    print("3. Max drink before driving")

    mode=input("Choose mode:")
    
    if mode =="1":
        print("You choose Estimate before drinking")
        if SHOW_ADVANCED_INPUT:
          weight=float(input("Enter weight:"))
          sex=input("Enter sex:")
          empty_stomach=input("Are you empty stomach? (y/n)")
        
        age=int(input("Enter age:"))
        print("Add drink")
        drink_name=input("Enter drink name:")
        volume=float(input("Enter volume(ml):"))
        abv=float(input("Enter ABV(%):"))
        count=float(input("Enter count:"))
        start_time=input("Enter start drinking time (hh:mm):")
        hour,minute=start_time.split(":")
        hour=int(hour)
        minute=int(minute)
        start_minutes=hour*60+minute
        drinking_duration=float(input("Enter drinking duration (hours):"))
        drinking_minutes=int(drinking_duration*60)
        finish_time_minutes=start_minutes+drinking_minutes
        finish_hour=finish_time_minutes//60
        finish_minutes=finish_time_minutes%60
        print(f"Finish drinking time: {finish_hour:02d}:{finish_minutes:02d}")
        total_alcohol=volume*(abv/100)*0.789*count
        metabolism_hours=total_alcohol/METABOLISM_RATE
        metabolism_minutes=metabolism_hours*60
        earliest_drive_minutes=int(finish_time_minutes+metabolism_minutes)
        earliest_drive_minutes = earliest_drive_minutes%(24*60)
        earliest_drive_hours=earliest_drive_minutes//60
        earliest_drive_minute=earliest_drive_minutes%60
        print("Total alcohol:",total_alcohol,"g")
        print(f"You can drive at {earliest_drive_hours:02d}:{earliest_drive_minute:02d}")
        if age>51:
          print("Age over 51: Please allow extra safety time before driving.")
          
        elif age>31:
          print("Age over 31: Consider adding extra safety time before driving.")
        if SHOW_DETAILS:
          print("Total alcohol:",total_alcohol)
          print("Metabolism hours:",metabolism_hours)
          
        break
        
    elif mode =="2":
        print("You choose Calculate after drinking")
        if SHOW_ADVANCED_INPUT:
          weight=float(input("Enter weight:"))
          sex=input("Enter sex:")
          empty_stomach=input("Are you empty stomach? (y/n)")
        
        age=int(input("Enter age:"))
        print("Add drink")
        drink_name=input("Enter drink name:")
        volume=float(input("Enter volume(ml):"))
        abv=float(input("Enter ABV(%):"))
        count=float(input("Enter count:"))
        current_time=input("Enter current time(hh:mm):")
        hour,minute=current_time.split(":")
        hour=int(hour)
        minute=int(minute)
        current_minutes=hour*60+minute
        drinking_duration=float(input("Enter drinking duration (hours):"))
        drinking_minutes=int(drinking_duration*60)
        start_time_minutes=current_minutes-drinking_minutes
        start_time_minutes=start_time_minutes%(24*60)
        start_hour=start_time_minutes//60
        start_minutes=start_time_minutes%60
        print(f"Start drinking time: {start_hour:02d}:{start_minutes:02d}")
        print("Finish drinking time:",current_time)
        total_alcohol=volume*(abv/100)*0.789*count
        metabolism_hours=total_alcohol/METABOLISM_RATE
        metabolism_minutes=metabolism_hours*60
        earliest_drive_minutes=int(current_minutes+metabolism_minutes)
        earliest_drive_minutes = earliest_drive_minutes%(24*60)
        earliest_drive_hours=earliest_drive_minutes//60
        earliest_drive_minute=earliest_drive_minutes%60
        print("Total alcohol:",total_alcohol,"g")
        print(f"You can drive at {earliest_drive_hours:02d}:{earliest_drive_minute:02d}")
        if age>51:
          print("Age over 51: Please allow extra safety time before driving.")
          
        elif age>31:
          print("Age over 31: Consider adding extra safety time before driving.")
        if SHOW_DETAILS:
          print("Total alcohol:",total_alcohol)
          print("Metabolism hours:",metabolism_hours)
          
        break
          
    elif mode =="3":
        print("You choose Max drink before driving")
        if SHOW_ADVANCED_INPUT:
          weight=float(input("Enter weight:"))
          sex=input("Enter sex:")
          empty_stomach=input("Are you empty stomach? (y/n)")
        
        age=int(input("Enter age:"))
        print("Add drink")
        drink_name=input("Enter drink name:")
        volume=float(input("Enter volume(ml):"))
        abv=float(input("Enter ABV(%):"))
        current_time=input("Enter current time (hh:mm):")
        hour,minute=current_time.split(":")
        hour=int(hour)
        minute=int(minute)
        current_minutes=hour*60+minute
        drive_time=input("Enter drive time (hh:mm):")
        hour,minute=drive_time.split(":")
        hour=int(hour)
        minute=int(minute)
        drive_minutes=hour*60+minute
        available_minutes=drive_minutes-current_minutes
        if available_minutes<0:
           available_minutes=available_minutes+24*60
        available_hours=available_minutes/60
        print(f"Available time: {available_hours:.1f} hours")
        max_alcohol=available_hours*METABOLISM_RATE
        single_alcohol=volume*(abv/100)*0.789
        max_count=max_alcohol/single_alcohol
        print("Theoretical alcohol limit:",max_alcohol,"g")
        print("Theoretical max count:",max_count)
        safe_count=int(max_count)
        print("Recommended max drinks:",safe_count)
        break
          
    else:
        print("Invalid mode")
        print("Please choose again idiot= =")