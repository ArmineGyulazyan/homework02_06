while True:
	
	hour = int(input("Enter hour: "))
	if hour in range(1,13):
		day_night = int(input("am(1) or pm(2)? "))
		ahead_h = int(input("How many hours ahead? "))
		new_hour = hour + ahead_h
		
		if day_night == 1:
			if new_hour >= 12:
				new_hour -= 12
				day_night = 2	
		elif day_night == 2:
			if new_hour >= 12:					
				new_hour -= 12
				day_night = 1
			
		if new_hour >= 12:
			new_hour -= 12
			day_night = 2

			
		print(new_hour if new_hour != 0 else 12, "am" if day_night == 1 else "pm")
		break	

	else:
		print("Hour should be between 1 and 12 ")
			
