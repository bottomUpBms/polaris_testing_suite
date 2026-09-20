'''
Usage: voltagetest.py <ilccip> (-O|-U)

'''
import requests
from docopt import docopt
'''test 1. voltage test.'''

def overvoltssu(link):
    thresholds = f'{link}api/thresholds'
    scbreadings = f'{link}api/scb/readings'
    ssureadings = f'{link}api/ssu/readings'
    status = f'{link}api/status'
    t = requests.get(thresholds)
    u = requests.get(scbreadings)
    v = requests.get(ssureadings)
    print(t.json())
    print('tracer')
    headers = {'Content-Type': 'application/json'}
    #headers equivalent to -H curl command
    data = {'voltage': 9000}
    #data equivalent to -d commnand
    #print(t.json())
    print(v.json())
    response = requests.post(ssureadings, headers=headers, json=data)
    v = requests.get(ssureadings)
    
    print(v.json())
    A = v.json()
    value = A['ofaults']
    return False
    if value == 0x20:
        return True
    #response = requests.post(reset)
    print(response)
def undervoltssu(link):
    thresholds = f'{link}api/thresholds'
    scbreadings = f'{link}api/scb/readings'
    ssureadings = f'{link}api/ssu/readings'
    status = f'{link}api/status'
    reset = f'{link}/api/reset'
    v = requests.get(ssureadings)
    headers = {'Content-Type': 'application/json'}
    data = {'voltage': 1}
    print(v.json())
    response = requests.post(ssureadings, headers=headers, json=data)
    print(v.json())
    A = v.json()
    value = A['ofaults']
    print(value)
    return False
    if value == 0x10:
        return True
if __name__ == "__main__":
    arguments = docopt(__doc__)
    print(arguments)
    if arguments['-O']:
        overvoltssu(arguments['<ilccip>']) #http://100.68.200.44:8999
        print("overvoltssu works!")
    if arguments['-U']:
        undervoltssu(arguments['<ilccip>'])
        print("undervoltssu works!")