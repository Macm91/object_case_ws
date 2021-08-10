#Generates an alarm 
class alarm_clock:
        def __init__ (self, name, time):
            self.alarm_name = name 
            self.the_current_time = "4:00"
            self.alarm_time = time
            self.toggle_on = True
    #methods to set the alarm
        def set_alarm_time(self):
            self.set_alarm_time = input ("Please enter a time for your alarm.")
            self.alarm_time = self.set_alarm_time
            print ("Alarm time: " + str(self.set_alarm_time))

        def toggle_on_off(self):
            self.toggle_on_off = input ("Please enter 'on' or 'off'.")
            if (self.toggle_on_off == False):
                self.toggle_on_off = "off"
            print ("Alarm is off.")
            
            if (self.toggle_on_off == True):
                self.toggle_on_off = "on"
            print("Alarm is on")

        def list_alarm_info(self):
            print( "Alarm Name: " + str(self.alarm_name))
            print("Alarm Time: " + str(self.alarm_time))
            print ("The alarm is " + str(self.toggle_on))
            print("The current time is: "+ str(self.the_current_time))