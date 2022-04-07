from tabulate import tabulate

from task2 import host_range_ping


def host_range_ping_tab(host_range: str):
    hosts = host_range_ping(host_range, need_print=False)
    results = {'Reachable': [], 'Unreachable': []}
    for host in hosts:
        if host[1]:
            results['Reachable'].append(host[0])
        else:
            results['Unreachable'].append(host[0])
    print(tabulate(results, headers='keys', tablefmt='simple'))


if __name__ == '__main__':
    host_range = '192.168.178.0/29'
    host_range_ping_tab(host_range)