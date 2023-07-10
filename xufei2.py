import time

def pomodoro_timer(focus_time=25, break_time=5, cycles=4):
    for cycle in range(cycles):
        print(f"开始专注 {focus_time} 分钟")
        time.sleep(focus_time * 60)
        print(f"休息 {break_time} 分钟")
        time.sleep(break_time * 60)
    print("专注时钟结束")

pomodoro_timer()
