# Objects used in financal aspects of the game
import capitalist_business
import capitalist_math
class loan:
    year = 1982
    month = 6
    # day = 4
    borrower = capitalist_business.business()
    giver = capitalist_business.business()
    sum = 0.00 #Value in Currency units
    rate = 0.00 #Value in Currency units per month
    intrest = 0.0000 #Value in Percent
    duration = 0 #Value in rate time units (months)
    def request(self,borrower,giver,sum,intrest,rate=None,duration=None):
        pass
    def offer(self,borrower,giver,sum,intrest,rate=None,duration=None):
        pass
    def take(self,borrower,giver,sum,intrest,rate=None,duration=None):
        self.giver = giver
        self.sum = sum
        self.intrest = intrest
        #Rework: borth missing
        if rate == None:
            self.rate = capitalist_math.calculate_rate(sum=sum,intrest=intrest,duration=duration)
        else:
            self.rate = rate
        if duration == None:
            self.duration = capitalist_math.calculate_duration(sum=sum,intrest=intrest,rate=rate)
        else:
            self.duration = duration
            borrower.loans.add(self)
    def give(self):
        pass
    def do_pay_rate(self):
        pass
    def refuse_to_pay_rate(self):
        pass
