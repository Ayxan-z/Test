import threading, queue

q = queue.Queue()

liste = ['Ankara','İstanbul','Kayseri']

def islem(threadName,q):
    global liste
    while not q.empty():
        item = q.get()
        print(f"{threadName} Çıkarılacak eleman: {item}")        
        q.task_done()

for i in liste:
    q.put(i)

for i in range(2):
    worker = threading.Thread(target=islem, args=(f"Thread-{i}",q), daemon=True)
    worker.start()

q.join()