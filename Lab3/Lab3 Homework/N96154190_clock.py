import time
from tm1637 import TM1637

# 請根據你實際插的 BCM GPIO 腳位進行調整
CLK = 23  # 例如 BCM 23 (實體腳位 16)
DIO = 24  # 例如 BCM 24 (實體腳位 18)

class Clock:
    def __init__(self, tm_instance):
        self.tm = tm_instance
        self.show_colon = False

    def run(self):
        print("時鐘啟動中... (按 Ctrl+C 退出)")
        while True:
            # 取得目前的本地時間
            t = time.localtime()
            
            # 每次迴圈切換冒號狀態：True 與 False 交替，達成一秒閃爍一次
            self.show_colon = not self.show_colon
            
            # tm.numbers(小時, 分鐘, 冒號開關)
            self.tm.numbers(t.tm_hour, t.tm_min, self.show_colon)
            
            # 暫停 1 秒
            time.sleep(1)

if __name__ == '__main__':
    # 初始化 TM1637
    tm = TM1637(clk=CLK, dio=DIO)
    tm.brightness(2)  # 設定亮度 (0~7)
    
    clock = Clock(tm)
    try:
        clock.run()
    except KeyboardInterrupt:
        # 退出時將螢幕熄滅清除
        tm.write([0, 0, 0, 0])
        print("\n時鐘已停止")