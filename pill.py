import time
from twilio.rest import Client


class Pill:
    def __init__(self, name, amount, times_a_day, times_a_week, time_between_pills, quantity):
        self.name = name
        self.amount = amount
        self.times_a_day = times_a_day
        if int(times_a_week) > 7:
            raise ValueError("You cannot take medicine more than 7 times a week. "
                             "If you are taking this medicine daily, please type 7 for the times a week field")
        elif int(times_a_week) <= 0:
            raise ValueError("You have entered that you will take the medicine 0 times a week or less. "
                             "If it's a mistake, please fix it. If not, please remove the medication.")
        else:
            self.times_a_week = times_a_week
        self.time_between_pills = time_between_pills
        self.quantity = quantity

    def get_name(self):
        return self.name

    def get_amount(self):
        return self.amount

    def get_times_a_day(self):
        return self.times_a_day

    def get_quantity(self):
        return self.quantity

if __name__ == '__main__':

    pillA = Pill("Tylenol", 1, 3, 7, 15, 5)
    pillB = Pill("Ibuprofen", 2, 2, 7, 30, 10)
    # print("Take " + str(pillA.get_amount()) + " " + pillA.get_name() + " " + str(pillA.get_times_a_day()) + " times a day")
    # tm_year=2018, tm_mon=11, tm_mday=3, tm_hour=19, tm_min=41, tm_sec=50, tm_wday=5, tm_yday=307, tm_isdst=1
    # print(time.localtime())

    def check_stock(my_pill, total, times_taken):
        if total <= 1:
            print("Woah there, amount of " + my_pill.get_name() + " is low! Consider restocking your supply of " + my_pill.get_name())
        elif total == 0:
            print("Oops you've ran out of medication")
            times_taken = my_pill.get_times_a_day()

        return times_taken


    def my_pill_schedule_demo(my_pill, interval=""):
        """
        Demo for pill keurig
        :param my_pill: an instance of Pill object
        :param interval: a default value
        :return: keurig will do something
        """
        account = "AC8261256b7360477061624ba55a5d3c77"
        token = "6ffbdb56af556b3ee5185cbfcab4a372"
        client = Client(account, token)
        total = my_pill.get_quantity()
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

        times_taken = 0
        while times_taken < 7:
            if my_pill.get_amount() == 1:
                print(days[times_taken])
            # Say the date after each time
            # In terms of machinery, this would be like keep the servo moving until 1 has been dispensed/beam break triggers
            print("Dispensing " + my_pill.get_name())  # Change code so user gets a text message
            message = client.messages.create(to="+18042008481", from_="+18043312802", body=my_pill.get_name() + " has been dispensed.")
            times_taken += 1

            time.sleep(0.30)

        # Demo test 2: dispense 2 pills 1 time a day
        if my_pill.get_amount() > 1:
            while times_taken < 7:
                # Keep servo dispensing until 2 has been dispensed
                # If possible, incorporate beam break so that we can check that two have been dispensed
                print("Dispensing " + my_pill.get_name())  # Change code so user gets a text message
                times_taken += 1
                total -= 1
                check_stock(my_pill, total, times_taken)
                time.sleep(35)

        # Demo test 3: dispense 1 pill 2 times a day
        elif my_pill.get_times_a_day() == 2:
            while times_taken < my_pill.get_times_a_day():
                print("Dispensing " + my_pill.get_name())  # Change code so user gets a text message
                times_taken += 1
                if interval != "":
                    time.sleep(my_pill.time_between_pills)
                else:
                    time.sleep(30)  # Dispense pill every 30 seconds
                # Possibly, do a beam break
                # While beam_break = is broken:
                    # pause...maybe time.sleep(10)  # Let user know through a text message that pill has been dispensed
                # time.sleep(30) # to indicate the next time frame

    my_pill_schedule_demo(pillA)



# message = client.messages.create(to="+18045022529", from_="+18043312802", body= my_pill.get_name() + " has been dispensed.")
    # fileName = input("Please input the file")
