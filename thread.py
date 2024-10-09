import threading
import time

# 定义线程要执行的任务
def task(number):
    print(f"Thread {number} is starting")
    time.sleep(2)  # 模拟任务耗时
    print(f"Thread {number} is finishing")

# 创建并启动 100 个线程
threads = []
for i in range(100):
    thread = threading.Thread(target=task, args=(i,))
    threads.append(thread)
    thread.start()

# 等待所有线程执行完成
for thread in threads:
    thread.join()

print("All threads have finished execution")

