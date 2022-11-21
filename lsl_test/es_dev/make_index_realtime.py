import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from newsml_to_json import make_json
from elasticsearch import Elasticsearch

# es = Elasticsearch('http://10.37.30.125:9199')
es = Elasticsearch('http://localhost:9199')

mapping = {
    "settings" : {
        "number_of_shards": 6,
        "number_of_replicas": 1
    }
}

class Target:

    def __init__(self, path):
        #watchDir에 감시하려는 디렉토리를 명시한다.
        os.chdir(path)
        self.watchDir = os.getcwd()

        self.observer = Observer()   #observer객체를 만듦

    def run(self):
        event_handler = Handler()
        # schedule 실행
        self.observer.schedule(event_handler, self.watchDir, 
                                                       recursive=True)
        self.observer.start()
        try:
            while True:
                # 60초마다 실행
                time.sleep(60)
        except:
            self.observer.stop()
            print("Error")
            self.observer.join()

class Handler(FileSystemEventHandler):
#FileSystemEventHandler 클래스를 상속받음.
#아래 핸들러들을 오버라이드 함

    #파일, 디렉터리가 move 되거나 rename 되면 실행
    def on_moved(self, event):
        print('move')
        print(event)

    def on_created(self, event): #파일, 디렉터리가 생성되면 실행
        print('create')
        if event.is_directory :
            print('----------------- new directory -----------------')
            print(event.src_path)
        else :
            print('----------------- index 추가 -----------------')
            Fname, Extension = os.path.splitext(os.path.basename(event.src_path))
            if Extension == '.xml':
                #json 변환
                json_dict = make_json(event.src_path)
                print(json_dict)
                date = "kpf_bigkindslab_v1.1_" + json_dict['NewsEnvelope']['DateAndTime'][:4]
                print(date)
                # index가 존재하는 지 확인
                # index 없을 경우 index 생성 후 doc 추가
                # if es.indices.exists(index=date)==False:
                #     es.indices.create(index=date, body=mapping)
                #     print('index create : '+date)

                # result = es.index(index=date, doc_type="_doc", body=json_dict, id=Fname)
                # print(result)


    def on_deleted(self, event): #파일, 디렉터리가 삭제되면 실행
        print('delete')
        print(event)

    def on_modified(self, event): #파일, 디렉터리가 수정되면 실행
        print('modified')
        print(event.src_path)

if __name__ == '__main__': #본 파일에서 실행될 때만 실행되도록 함
    # 실제 디렉토리 경로
    # w = Target('/hadoop/newsml/data')
    w = Target('../data')
    w.run()