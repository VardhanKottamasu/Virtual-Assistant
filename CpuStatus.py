import psutil
import Main

def cpu():
    usage = str(psutil.cpu_percent())
    Main.speak('CPU is at'+usage)
    print('CPU is at '+str(usage)+' percent usage')
    
def battery_status():
    battery=psutil.sensors_battery()
    Main.speak('Battery is at '+str(battery.percent)+ 'percentage')
    print('Battery is at '+str(battery.percent)+ ' percentage')