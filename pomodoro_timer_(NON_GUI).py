import os , winsound
import datetime as dt
import tkinter
from tkinter import messagebox

#Initializing Class

class Pomodoro():
    ''' Mimics a Pomodoro timer, a time management tool that breaks work into intervals separated by
        breaks.
    '''
    
    #Class Variables
    pomodoros_completed = 1
    root = tkinter.Tk()
    root.withdraw()

    def __init__(self , task_duration , short_break_duration) -> None:
        self.task_duration = task_duration
        self.short_break_duration = short_break_duration
        self.long_break_duration = 30
    
    #Function to clear screen
    def clear_screen(self):
        os.system('cls')

    #Function to check whether it's time for long break or Not.
    def chech_for_long_break(self):
        return self.pomodoros_completed % 4 == 0


    def start_pomodoro(self):
        self.t_now = dt.datetime.now() + dt.timedelta(seconds=10)
        self.t_fin = self.t_now + dt.timedelta(minutes=self.task_duration)
        return self.t_now , self.t_fin

    def update_timer(self):
        t_now = dt.datetime.now()
        return t_now

    def start_break(self):
        if not self.chech_for_long_break():
            self.t_now = dt.datetime.now() + dt.timedelta(seconds=10)
            self.t_short_break = self.t_now + dt.timedelta(minutes=self.short_break_duration)
            return self.t_now , self.t_short_break , 0
        else:
            self.t_now = dt.datetime.now() + dt.timedelta(seconds=10)
            self.t_long_break = self.t_now + dt.timedelta(minutes=self.long_break_duration)
            return self.t_now , self.t_long_break , 1

    # Function to Initialize Timer
    def initialize_timer(self , t_now , t_fin = None , t_short_break = None , t_long_break = None):
        if t_fin != None:
            while t_now < t_fin:
                t_now = self.update_timer()
                t_cur = t_fin - t_now
                total_seconds = int(t_cur.total_seconds())

                # 3600 seconds in an hour
                hours, remainder = divmod(total_seconds,3600)

                # 60 seconds in a minute  
                minutes, seconds = divmod(remainder,60)
                # print(f'\r{minutes} mins | {seconds} secs remaining' , end=' ')
                print(f'\rWORK TIME | {minutes} mins | {seconds} secs remaining' , end=' ')

        elif t_short_break != None:
             while t_now < t_short_break:
                t_now = self.update_timer()
                t_cur = t_short_break - t_now
                total_seconds = int(t_cur.total_seconds())

                # 3600 seconds in an hour
                hours, remainder = divmod(total_seconds,3600)

                # 60 seconds in a minute
                minutes, seconds = divmod(remainder,60)
                # print(f'\r{minutes} mins | {seconds} secs remaining' , end=' ')
                print(f'\rSHORT BREAK | {minutes} mins | {seconds} secs remaining' , end = ' ')

        else:
            while t_now < t_long_break:
                t_now = self.update_timer()
                t_cur = t_long_break - t_now
                total_seconds = int(t_cur.total_seconds())

                # 3600 seconds in an hour
                hours, remainder = divmod(total_seconds,3600)

                # 60 seconds in a minute
                minutes, seconds = divmod(remainder,60)
                # print(f'\r{minutes} mins | {seconds} secs remaining' , end=' ')
                print (f'\rLONG BREAK | {minutes} mins | {seconds} secs remaining' , end=' ')


#m Main Function

def main():
    task_duration = input('Enter the Interval (Between 25 - 60)) in "MINUTES" in which you want to perform tasks (Press Enter for Default :- 25) :: ') or '25'
    short_break_duration = input('Enter the Break Time (Between 5 - 20)) in "MINUTES" in which yoy want relax (Press Enter for Default :- 5) :: ') or '5'
    pomodoro = Pomodoro(task_duration = int(task_duration) , short_break_duration = int(short_break_duration))
    pomodoro.clear_screen()
    while True:
        t_now  , t_fin = pomodoro.start_pomodoro()
        timenow = t_now.strftime("%H:%M")
        winsound.PlaySound('beep.wav' , winsound.SND_FILENAME)
        messagebox.showinfo(title='Pomodoro Has Started' , message=f'It is now {timenow}\n Timer is set for {task_duration} mins')
        pomodoro.initialize_timer(t_now=t_now , t_fin=t_fin)
        t_now , t_break , t_btype = pomodoro.start_break()
        if t_btype == 0:
            winsound.PlaySound('beep.wav' , winsound.SND_FILENAME)
            pomodoro.initialize_timer(t_now=t_now , t_short_break=t_break)
            winsound.PlaySound('beep.wav' , winsound.SND_FILENAME)
            usr_ans = messagebox.askyesno("Pomodoro Finished!","Would you like to start another pomodoro?")
            if usr_ans == True:
            # user wants another pomodoro! Update values to indicate new timeset.
                pomodoro.pomodoros_completed += 1
                continue
            elif usr_ans == False:
                # Show a final message)
                messagebox.showinfo("Pomodoro Finished!", "\nIt is now "+timenow+
                "\nYou completed "+str(pomodoro.pomodoros_completed)+" pomodoros today!")
                pomodoro.clear_screen()
                break
        else:
            winsound.PlaySound('beep.wav' , winsound.SND_FILENAME)
            pomodoro.initialize_timer(t_now=t_now , t_long_break=t_break)
            winsound.PlaySound('beep.wav' , winsound.SND_FILENAME)
            usr_ans = messagebox.askyesno("Pomodoro Finished!","Would you like to start another pomodoro?")
            if usr_ans == True:
            # user wants another pomodoro! Update values to indicate new timeset.
                pomodoro.pomodoros_completed += 1
                continue
            elif usr_ans == False:
                # Show a final message)
                messagebox.showinfo("Pomodoro Finished!", "\nIt is now "+timenow+
                "\nYou completed "+str(pomodoro.pomodoros_completed)+" pomodoros today!")
                pomodoro.clear_screen()
                break
        

if __name__ == "__main__":
    main()