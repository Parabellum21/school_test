import states
import time

class Context:
    state: int = states.INIT
    
    wifi: bool = False
    broker: bool = False
    
    mqtt: MQTTClient = None 
    
    temperature: float = None
    humidity: int = None
    light: int = None

if __name__ == "__main__":
    context = Context()
    
    while True:
        if context.state == states.INIT:
            states.init(context)
        elif context.state == states.MEASURE:
            states.measure(context)
        elif context.state == states.UPLOAD:
            states.upload(context)
        elif context.state == states.SLEEP:
            states.sleep_pico(context)
        else:
            print('unknown state')



    
    
    
    
    
