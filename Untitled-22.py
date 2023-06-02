class Time:
    def __int__(self, h ,m,s):
        self.h = h
        self.m = m
        self.s = s

        def show(self):
            print(self.h,":",self.m,":",self.s)

        #def sum(self, t):
            #result = Time(None, None, None)
            #result.h = self.h + t.h
            #result.m = self.m + t.m
            #result.s = self.s + self.s
            #return result
        
    def time_to_sec(self):
        self.m=self.h*60+self.m
        self.s=self.m*60+self.s
        print(self.s,"seconds")
    def sec_to_time(self):
        if self.s>=60:
            s=self.s % 60
            self.m=int(self.s/60)
        if self.m>=60:
            self.m=self.m%60
            self.h = int(self.m//60)
        print(self.h,":",self.m,":",s)
while True:
    r=Time(0,0,0)
    op=input("for (time to sec) Enter 1 and for (sec to time) Enter 2 , e to exit:")
    if op=="e":
        break
    if op=="1":
        r.h=int(input("Enter the hours:"))
        r.m=int(input("Enter the minutes:"))
        r.s=int(input("Enter the seconds:"))
        r.time_to_sec()
    elif op=="2":
        r.s=int(input("Enter the seconds:"))
        r.sec_to_time()
    else:
        print("Please select from the specified items")
#time2 = Time()
#time1 = Time()
#s = time1.sum(time2)
#s.show()