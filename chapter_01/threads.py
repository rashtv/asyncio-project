import threading


def hello_from_thread():
    print(f'Hello from thread {threading.current_thread()}')


hello_thread = threading.Thread(target=hello_from_thread)
hello_thread.start()

total_threads = threading.active_count()
thread_name = threading.current_thread().name

print(f'Active threads: {total_threads}')
print(f'Thread name: {thread_name}')
hello_thread.join()
