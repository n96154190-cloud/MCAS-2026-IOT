import RPi.GPIO as GPIO
import time

# 腳位設定（使用 BOARD 實體腳位模式）
LED_PIN = 18     # 實體腳位 11
BUZZER_PIN = 11  # 實體腳位 12
FREQ = 523       # 蜂鳴器頻率 (523Hz 約為 C5 音高)

# 摩斯密碼時間單位 (秒)
UNIT = 0.2
DOT_TIME = UNIT       # 短音 (1 個單位)
DASH_TIME = UNIT * 3  # 長音 (3 個單位)
GAP_TIME = UNIT       # 同一字母內點與線之間的間隔
LETTER_GAP = UNIT * 3 # 字母與字母之間的間隔
WORD_GAP = UNIT * 7   # 整個單字播放完後的間隔

# 初始化 GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

# 設定蜂鳴器 PWM 控制
buzzer = GPIO.PWM(BUZZER_PIN, FREQ)

def play_signal(duration):
    """同時點亮 LED 並讓蜂鳴器發聲"""
    GPIO.output(LED_PIN, True)
    buzzer.start(50)  # 占空比 50% 發聲
    time.sleep(duration)
    
    # 關閉並間隔
    GPIO.output(LED_PIN, False)
    buzzer.stop()
    time.sleep(GAP_TIME)

def dot():
    """發出短信號 (·)"""
    play_signal(DOT_TIME)

def dash():
    """發出長信號 (—)"""
    play_signal(DASH_TIME)

def play_s():
    dot()
    dot()
    dot()

def play_o():
    dash()
    dash()
    dash()

try:
    print("開始以摩斯密碼播放 SOS... (按 Ctrl+C 結束)")
    while True:
        # S (3 短)
        play_s()
        time.sleep(LETTER_GAP - GAP_TIME)

        # O (3 長)
        play_o()
        time.sleep(LETTER_GAP - GAP_TIME)

        # S (3 短)
        play_s()

        # 循環休息
        time.sleep(WORD_GAP)

except KeyboardInterrupt:
    print("\n程式已中斷退出")
finally:
    buzzer.stop()
    GPIO.cleanup()