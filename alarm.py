import datetime
import time
from pytube import YouTube
import ssl
import os
import glob
import subprocess
import youtube_dl

ssl._create_default_https_context = ssl._create_unverified_context


# Replace "video.mp4" with the path to your downloaded video file
#import webbrowser

# Make a class for a clock
"""
1. Make a class
2. Have a function to set whether it is a 24 hour clock or a 12 hour clock
3. Have a method to get the current time
4. Have a method to get the time difference
5. Have a method to start the countdown.
6. Have a method to play the video at the end"""
class Clock:
        def __init__(self):
                self.__clock_type = None
                self.__current_time = None
                self.__alarm_time = None
                self.__time_diff = None
                self.__AMPM = None
                self.__alarm_list = None
        def set_clock_type(self):
                valid_clock = True
                while valid_clock:
                        clock_type = input("Do you want a 12 hour clock or a 24 hour clock? ")
                        if "12" in clock_type:
                                self.__clock_type = "12"
                                valid_clock = False
                        elif "24" in clock_type:
                                self.__clock_type = "24"
                                valid_clock = False
                        else:
                                print("Please enter a valid clock type.")
        def set_alarm(self):
                alarm = input("Enter the desired time for the alarm to go off: ")
                if self.__clock_type == "12":
                        #AMPM = input("AM or PM? ")
                        #if "AM" not in AMPM.upper() or "PM" not in AMPM.upper():
                                #raise Exception("Enter a proper AM or PM")
                        #else:
                                #self.__AMPM = AMPM
                        alarmTime = [int(n) for n in alarm.split(":")]
                        if alarmTime[0] > 12 or alarmTime[0] < 0:
                                raise Exception("Invalid hour.")
                        elif alarmTime[1] >= 60 or alarmTime[1] < 0:
                                raise Exception("Invalid minutes")
                elif self.__clock_type == "24":
                        alarmTime = [int(n) for n in alarm.split(":")]
                        if alarmTime[0] >= 24 or alarmTime[0] < 0:
                                raise Exception("Invalid hour.")
                        elif alarmTime[1] >= 60 or alarmTime[1] < 0:
                                raise Exception("Invalid minutes.")
                self.__alarm_list = alarmTime
        
        def set_current_time(self):
                seconds_hms = [3600, 60, 1]   # Seconds per hour, minute, second
                now = datetime.datetime.now()
                current_time_in_sec = sum([b*c for b,c in zip(seconds_hms, [now.hour, now.minute, now.second])])
                self.__current_time = current_time_in_sec
                pass
        def set_alarm_time(self):
                seconds_hms = [3600, 60, 1]   # Seconds per hour, minute, second
                alarmSeconds = sum([a*b for a,b in zip(seconds_hms[:len(self.__alarm_list)], self.__alarm_list)])   # Find out what the zip function does. 
                self.__alarm_time = alarmSeconds
                pass
        def set_time_diff(self):
                time_diff = self.__alarm_time - self.__current_time
                if self.__clock_type == "12":
                        if time_diff < 0:
                                self.__time_diff = time_diff + 86400
                        elif time_diff == 0:
                                self.__time_diff = 86400
                        else:
                                self.__time_diff = time_diff
                elif self.__clock_type == "24":
                        if time_diff < 0:
                                self.__time_diff = time_diff + 86400  
                        else:
                                self.__time_diff = time_diff
        def get_time_diff(self):
                return self.__time_diff

#from moviepy.editor import VideoFileClip
#import os
"""
1. Get a function to accept url
2. Get a function to actually download the video associated with the url
3. Get a function to play the video.
"""

#class Downloader:
        #def __init__(self):
                #self.__url = None
                #self.__yt = None
                #pass
        #def set_url(self):
                #keep_asking = True
                #while keep_asking:
                        #try:
                                #url = input("Enter the URL of the video: ")
                                #yt = YouTube(url)
                                #self.__url = url
                                #self.__yt = yt
                                #print(self.__yt.vid_info)
                                #keep_asking = False
                        #except Exception as e:
                                #print(e)
        #def download_video(self):
                #stream = self.__yt.streams.filter(file_extension='mp4').first()
                ##stream = self.__yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
                #stream.download()  
                #print("Downloaded")                
        #def play_video(self):
                #video_extension = "*.mp4"  # replace with your video file extension
                
                ## Set the search directory to the current working directory
                #search_dir = os.getcwd()
                
                ## Construct the pattern to search for
                #search_pattern = os.path.join(search_dir, video_extension)
                
                ## Use glob to search for video files that match the pattern
                #video_files = glob.glob(search_pattern)
                
                ## Print the list of video files found
                
                
                #for file in video_files:
                        #subprocess.call(["open", "-a", "QuickTime Player",file])
                        ## Simulate a space key press to start playing the video
                        #osascript = 'tell application "System Events" to keystroke space'
                        #subprocess.call(['osascript', '-e', osascript])  
                        #os.remove(file)                

invalid = True


## Create a YouTube object
#downloader = Downloader()
#downloader.set_url()
#downloader.download_video()
def Download(link):
        youtubeObject = YouTube(link)
        youtubeObject.streams
        youtubeObject = youtubeObject.streams.get_highest_resolution()
        try:
                youtubeObject.download()
        except:
                print("An error has occurred")
        print("Download is completed successfully")




#keep_asking = True
#while keep_asking:
        #try:
                #link = input("Enter the URL of the video: ")
                ##yt = YouTube(url)
                #keep_asking = False
        #except Exception as e:
                #print(e)

# Get the highest resolution stream
#stream = yt.streams.filter(file_extension='mp4').first()
#stream.download()  
# Create the options object with desired options
  
# link of the video to be downloaded 
  

#Download(link)

#output_path = os.getcwd()
#print(output_path)
## Change the permissions of the current directory to writable
#os.chmod('.', 0o777)

## Download the video using youtube-dl and redirect the output to a file
#with open('youtube-dl.log', 'w') as log_file:
        #subprocess.run(['youtube-dl', '--no-check-certificate', '-f', 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best', '-o', '.', url], stdout=log_file, stderr=log_file)

#subprocess.run(['youtube-dl', '--no-check-certificate', '-f', 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best', '-o', f'{output_path}', f'{url}'])
#print("Downloaded")
clock = Clock()
clock.set_clock_type()
        
        
        
while invalid:
        try:
                clock.set_alarm()
                invalid = False
        except Exception as e:
                print(e)

clock.set_alarm_time()
clock.set_current_time()
clock.set_time_diff()


print(f"Alarm is set!\nIt will ring in {datetime.timedelta(seconds=clock.get_time_diff())}")
time_diff = clock.get_time_diff()

for i in range(time_diff):
        time.sleep(1)
        time_diff -= 1
        print(datetime.timedelta(seconds=time_diff))
    
##time.sleep(clock.get_time_diff())
# Set the file extension to search for (e.g., ".mp4")
video_extension = "*.mp4"  # replace with your video file extension

## Set the search directory to the current working directory
search_dir = os.getcwd()

## Construct the pattern to search for
search_pattern = os.path.join(search_dir, video_extension)

## Use glob to search for video files that match the pattern
video_files = glob.glob(search_pattern)

## Print the list of video files found


for file in video_files:
        subprocess.run(['open', '-a', 'QuickTime Player', f'{search_dir}'])
        # Simulate a space key press to start playing the video
        osascript = 'tell application "System Events" to keystroke space'
        subprocess.call(['osascript', '-e', osascript])  
        
#downloader.play_video()

        

print("WAKE UP!")    # How can I add sound?
