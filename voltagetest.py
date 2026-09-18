import requests
'''test 1. voltage test.'''

def voltagetest(link):
    #payload = 
    thresholds = f'{link}api/thresholds'
    scbreadings = f'{link}api/scb/readings'
    ssureadings = f'{link}api/ssu/readings'
    status = f'{link}api/status'
    t = requests.get(thresholds)
    u = requests.get(scbreadings)
    v = requests.get(ssureadings)
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
    if value == 32:
        return True
if __name__ == "__main__":
    ilccip = input()
    if voltagetest('http://100.68.200.44:8999/'):
        print("overvolt works!")
