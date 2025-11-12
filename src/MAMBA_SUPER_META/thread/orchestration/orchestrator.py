import threading
from queue import Queue

class ThreadManager:
    def __init__(self):
        self.threads = {}
        self.input_queues = {}
        self.output_queues = {}
        self.event_listeners = {}
        self.lock = threading.Lock()

    def start_thread(self, key, target, args=()):
        with self.lock:
            if key in self.threads:
                raise ValueError("Thread with given key already exists")

            input_queue = Queue()
            output_queue = Queue()
            thread = threading.Thread(target=target, args=(input_queue, output_queue) + args)
            self.threads[key] = thread
            self.input_queues[key] = input_queue
            self.output_queues[key] = output_queue
            self.event_listeners[key] = []
            thread.start()


    def stop_thread(self, key):
        with self.lock:
            if key in self.threads:
                self.input_queues[key].put(None)
                self.threads[key].join()
                del self.threads[key]
                del self.input_queues[key]
                del self.output_queues[key]
                del self.event_listeners[key]

    def register(self, key, listener):
        with self.lock:
            if key in self.threads:
                output_queue = Queue()
                self.event_listeners[key].append((listener, output_queue))
                return output_queue
            else:
                raise ValueError("Thread with given key does not exist")


    def poll_queues(self):
        with self.lock:
            for key in self.threads:
                while not self.output_queues[key].empty():
                    event = self.output_queues[key].get()
                    for listener, output_queue in self.event_listeners[key]:
                        output_queue.put(event)


class Orchestrator(ThreadManager, threading.Thread):
    def __init__(self):
        ThreadManager.__init__(self)
        threading.Thread.__init__(self)

    def run(self):
        while True:
            self.poll_queues()

