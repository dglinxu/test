import time
import schedule 
def do_sth():
    print('测试事件！')
    time.sleep(5)
schedule.every(5).seconds.do(do_sth)

while True:
      schedule.run_pending()

