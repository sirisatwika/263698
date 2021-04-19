hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
length = int(input("Event duration (minutes): "))
endhour = hour + (length // 60) 
endminute = mins + (length % 60)
endhour += endminute // 60
endminute = endminute % 60
endhour = endhour % 24 
print('{}:{}'.format(endhour, endminute))

