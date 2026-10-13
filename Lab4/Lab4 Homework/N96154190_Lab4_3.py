import time
import serial

# 設定 UART 連接埠與參數（預設使用樹莓派 /dev/serial0）
# 硬體腳位對應：GPIO14 (Pin 8, TXD) 與 GPIO15 (Pin 10, RXD)
ser = serial.Serial(
    port='/dev/serial0',  # 樹莓派主要 UART 設備節點
    baudrate=9600,        # 傳輸速率
    timeout=1             # 讀取逾時時間（秒）
)

# 傳送資料函式
def send_data(data):
    if ser.is_open:
        ser.write(data.encode('utf-8'))
        print(f"[Tx] Sent : {data.strip()}")

# 接收資料函式
def receive_data():
    if ser.is_open:
        incoming = ser.readline().decode('utf-8', errors='ignore').strip()
        if incoming:
            print(f"[Rx]Recieve: {incoming}")
        return incoming

# 主程式
try:
    
    counter = 1

    while True:
        # 發揮傳輸內容：包含遞增數字 (counter) 與輪替字元 (A-Z)
        char_data = chr(65 + ((counter - 1) % 26))
        message = f"Num:{counter}, Char:{char_data}\n"

        # 傳送資料
        send_data(message)
        time.sleep(0.5)

        # 接收並顯示資料
        receive_data()
        time.sleep(1.0)

        counter += 1

except KeyboardInterrupt:
    print("\n程式中斷")

finally:
    if ser.is_open:
        ser.close()
        print("串列埠已關閉")