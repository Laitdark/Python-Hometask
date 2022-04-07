from ipaddress import ip_address
from socket import gethostbyname
from subprocess import Popen, PIPE
import platform
import chardet


def host_ping(hosts_lst: list, need_print: bool = True) -> list:

    checked_hosts = []
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    for host in hosts_lst:
        if type(host) is not str:
            raise ValueError(f'The passed object in the list must be of a str type. {type(host)} was given.')
        process = Popen(['ping', '-t2', param, '1', host], stdout=PIPE, stderr=PIPE)
        data, err = process.communicate()
        result = chardet.detect(data)
        result_decoded = data.decode(result['encoding'])
        is_reachable = False if "unreachable" in result_decoded else True
        ip = ip_address(gethostbyname(host))
        checked_hosts.append((ip, is_reachable))
        ip_str = str(ip)
        if need_print:
            print(f'Host {host if host == ip_str else (host + " (" + ip_str + ")")} is '
                  f'{"" if is_reachable else "un"}reachable')
    return checked_hosts


if __name__ == '__main__':
    hosts = ['google.com', 'susu.ru', 'tum.de', '192.168.178.30', '192.168.178.233']
    host_ping(hosts)