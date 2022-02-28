import subprocess
import platform
from chardet import detect

# args = ['ping', 'yandex.ru']
# subproc_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
# for line in subproc_ping.stdout:
#     ping_results += line.decode('cp866')
#
# args = ['ping', 'youtube.com']
# subproc_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
# for line in subproc_ping.stdout:
#     ping_results += line.decode('cp866')
#
# print(ping_results.encode('utf-8').decode('utf-8'))

urls=['yandex.ru','youtube.com']
code='-n' if platform.system().lower() == 'windows' else '-c'

for url in urls:
    args=['ping', code, '4', url]
    ping_results=subproc_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
    for line in ping_results.stdout:
        result=detect(line)
        print(result)
        line=line.decode(result['encoding']).encode('utf-8')
        print(line.decode('utf-8'))