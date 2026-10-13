import time
import board
import adafruit_dht

# 初始化 DHT11 感測器，接在 GPIO4 (BCM 模式，Pin 7)
dht_device = adafruit_dht.DHT11(board.D4)

print("程式啟動，開始讀取 DHT11 溫溼度（按 Ctrl+C 可停止）...")

try:
    while True:
        try:
            # 讀取攝氏溫度與濕度
            temperature_c = dht_device.temperature
            temperature_f = temperature_c * (9 / 5) + 32
            humidity = dht_device.humidity

            # 依投影片格式要求持續輸出數值與單位
            print("Temp:{:.1f} C / {:.1f} F    Humidity: {}%".format(temperature_c, temperature_f, humidity))

        except RuntimeError as err:
            # DHT11 為單線協議，通訊校驗偶爾失敗屬正常現象，印出錯誤訊息後持續重試
            print(err.args[0])

        except Exception as error:
            dht_device.exit()
            raise error

        # DHT11 取樣頻率建議至少間隔 2 秒
        time.sleep(2.0)

except KeyboardInterrupt:
    print("\n程式已手動中斷。")

finally:
    # 確保釋放 GPIO 資源
    dht_device.exit()
    print("DHT11 資源已釋放，程式結束。")