# import time module, Observer, FileSystemEventHandler 
import time 
from watchdog.observers import Observer 
from watchdog.events import FileSystemEventHandler 
import ntpath
import os
import shutil


watchDirectory = input("the full path to the file that you wanna arrange: ")
destination=input("the destination where the files should be arranged: ")
video=destination+'/video'
os.mkdir(video)
pdf=destination+'/pdf'
os.mkdir(pdf)
images=destination+'/images'
os.mkdir(images)
app=destination+'/app'
os.mkdir(app)
zipfile=destination+'/zip'
os.mkdir(zipfile)

class OnMyWatch: 
	watchDirectory=watchDirectory
	

	def __init__(self): 
		self.observer = Observer() 

	def run(self): 
		event_handler = Handler() 
		self.observer.schedule(event_handler, self.watchDirectory, recursive = True) 
		self.observer.start() 
		try: 
			while True: 
				time.sleep(5) 
		except: 
			self.observer.stop() 
			print("Observer Stopped") 

		self.observer.join() 

class Handler(FileSystemEventHandler):
	def on_any_event(self,event):
		if event.is_directory:
			return None
		elif event.event_type == 'created':
			file_path=event.src_path
			file_name=ntpath.basename(file_path)
			split=os.path.splitext(file_name)
			if split[1]=='.pdf':
    				shutil.move(file_path,pdf)
			if split[1]=='.mp4' or split[1]=='.avi' or split[1]=='.mov' or split[1]=='.flv' or split[1]=='.mkv' or split[1]=='.ts':
    				shutil.move(file_path,video)
			if split[1]=='.zip':
    				shutil.move(file_path,zipfile)
			if split[1]=='.jpeg' or split[1]=='.gif' or split[1]=='.png' or split[1]=='.svg':
    				shutil.move(file_path,images)
			if split[1]=='.exe':
    				shutil.move(file_path,app)



    				
    				
		
			
		
    			

if __name__=='__main__':
	watch=OnMyWatch()
	watch.run()


						 

				

