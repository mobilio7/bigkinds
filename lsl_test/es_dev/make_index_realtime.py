# import os
# import time
# from watchdog.observers import Observer
# from watchdog.events import FileSystemEventHandler

# class Target:
#     watchDir = os.getcwd()
#     # watchDir = os.chdir('../data')
#     #watchDir에 감시하려는 디렉토리를 명시한다.

#     def __init__(self):
#         self.observer = Observer()   #observer객체를 만듦

#     def run(self):
#         event_handler = Handler()
#         self.observer.schedule(event_handler, self.watchDir, 
#                                                        recursive=True)
#         self.observer.start()
#         try:
#             while True:
#                 time.sleep(1)
#         except:
#             self.observer.stop()
#             print("Error")
#             self.observer.join()

# class Handler(FileSystemEventHandler):
# #FileSystemEventHandler 클래스를 상속받음.
# #아래 핸들러들을 오버라이드 함

#     #파일, 디렉터리가 move 되거나 rename 되면 실행
#     def on_moved(self, event):
#         print(event)

#     def on_created(self, event): #파일, 디렉터리가 생성되면 실행
#         print(event)

#     def on_deleted(self, event): #파일, 디렉터리가 삭제되면 실행
#         print(event)

#     def on_modified(self, event): #파일, 디렉터리가 수정되면 실행
#         print(event)

# if __name__ == '__main__': #본 파일에서 실행될 때만 실행되도록 함
#     w = Target()
#     w.run()


#--------------------------------------
import time
import os

try:
    from watchdog.observers import Observer
    from watchdog.events import FileSystemEventHandler
except ModuleNotFoundError as e:
    print (e)
    os.system("pip install watchdog")

# ------------------------------------------------
class Handler(FileSystemEventHandler):
    def on_created(self, event): # 파일 생성시
        print (f'event type : {event.event_type}\n'

               f'event src_path : {event.src_path}')
        if event.is_directory:
            print ("디렉토리 생성")
        else: # not event.is_directory
            """
            Fname : 파일 이름
            Extension : 파일 확장자 
            """
            Fname, Extension = os.path.splitext(os.path.basename(event.src_path))
            '''
             1. zip 파일
             2. exe 파일
             3. lnk 파일
            '''
            if Extension == '.zip':
                print (".zip 압축 파일 입니다.")
            elif Extension == '.exe':
                print (".exe 실행 파일 입니다.")
                os.remove(Fname + Extension)   # _파일 삭제 event 발생
            elif Extension == '.lnk':
                print (".lnk 링크 파일 입니다.")

    def on_deleted(self, event):
        print ("삭제 이벤트 발생")

    def on_moved(self, event): # 파일 이동시
        print (f'event type : {event.event_type}\n')

class Watcher:
    # 생성자
    def __init__(self, path):
        print ("감시 중 ...")
        self.event_handler = None      # Handler
        self.observer = Observer()     # Observer 객체 생성
        self.target_directory = path   # 감시대상 경로
        self.currentDirectorySetting() # instance method 호출 func(1)

    # func (1) 현재 작업 디렉토리
    def currentDirectorySetting(self):
        print ("====================================")
        print ("현재 작업 디렉토리:  ", end=" ")
        os.chdir(self.target_directory)
        print ("{cwd}".format(cwd = os.getcwd()))
        print ("====================================")

    # func (2)
    def run(self):
        self.event_handler = Handler() # 이벤트 핸들러 객체 생성
        self.observer.schedule(
            self.event_handler,
            self.target_directory,
            recursive=False
        )

        self.observer.start() # 감시 시작
        try:
            while True: # 무한 루프
                time.sleep(5) # 1초 마다 대상 디렉토리 감시
        except KeyboardInterrupt as e: # 사용자에 의해 "ctrl + z" 발생시
            print ("감시 중지...")
            self.observer.stop() # 감시 중단

myWatcher = Watcher("../data")
myWatcher.run()