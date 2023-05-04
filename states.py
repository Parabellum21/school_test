import ntptime
import utime
import _thread
import json
import settings
from dht import DHT11
from machine import Pin, ADC, deepsleep, RTC, WDT
import helper
from time import sleep


INIT = 1
MEASURE = 2
UPLOAD = 3
SLEEP = 4


pin_dht = DHT11(Pin(settings.DHT_PIN))
pin_svetla = ADC(Pin(settings.LIGHT_PIN))
pin_led = Pin(settings.LED_PIN, Pin.OUT)


#basic function
def init(context):
    context.state = MEASURE

def measure(context):
    context.state = UPLOAD

def upload(context):
    context.state = SLEEP
    
def sleep_pico(context):
    context.state = INIT
    
    
    
    
    
    
    
    