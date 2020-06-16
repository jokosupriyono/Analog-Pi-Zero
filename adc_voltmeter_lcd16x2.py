#!/usr/bin/python3
from time import sleep
from gpiozero import MCP3008
import lcddriver
vref = 3.296
adc_list = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
conversion_factors = [3.080,4.668,6.43,1,1,1,1,1]
toggle = 0
counter = 0
lcd = lcddriver.lcd()    # create object for lcd control
lcd.lcd_clear()          # clear LCD ready for start

def update():
    lcd.lcd_display_string('{:^16}'.format(row_one), 1)
    lcd.lcd_display_string('{:^16}'.format(row_two), 2)

# display an intro message
row_one = "Hi 16x2 RasPiO"
row_two = "Analog Zero"
update()
sleep(2)

while True:
    for x in range(3):
        adc = MCP3008(channel=x)
        readings = 0.0
        repetitions = 200            # how many times we sample
        for y in range(repetitions):
            readings += adc.value
        average = readings / repetitions
        volts = '{:6.3f}'.format(vref * average * conversion_factors[x])
        print("channel " + str(x) + ":", volts,"Volts")
        adc_list[x] = volts
        if x == 2:
            row_one   = str("10V:"+adc_list[0])+"V"
            row_two   = str("15V:"+adc_list[1])+"V"
            row_three = str("20V:"+adc_list[2])+"V"
            row_four  = str("RasPiO Voltmeter")
            if counter % 7 == 0:       # change to tweak alternation
                if toggle == 0:
                    toggle = 1
                elif toggle == 1:
                    toggle = 0
            if toggle:
                row_one = row_three
                row_two = row_four
            update()
        sleep(0.05)
        counter += 1

# Kalibrasi
# Voltmeter akan lebih atau kurang akurat (~ 5%) apa adanya, tetapi
# jika Anda ingin hasil yang akurat, ukur garis 3V3 Pi Anda dengan
# Voltmeter yang akurat dan sesuaikan nilai vref pada baris 5
# Kemudian atur conversion_factors = [1,1,1,1,1,1,1,1] pada baris 7
# Kemudian jalankan skrip dan hubungkan masing-masing 
Saluran # 10V (ch0), 15V (ch1) dan 20V (ch2) ke Pi's 3V3
# faktor konversi Anda adalah ...
# vref / nilai yang diukur 
# lalu edit konversi_faktor untuk memasukkan nilai Anda ke 3 dp
