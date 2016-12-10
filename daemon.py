import avango
import avango.daemon

host_ips = {
    'arachne':      '141.54.147.27',
    'artemis':      '141.54.147.28',
    'atalante':     '141.54.147.29',
    'athena':       '141.54.147.30',
    'boreas':       '141.54.147.32',
    'charon':       '141.54.147.33',
    'demeter':      '141.54.147.35',
    'eris':         '141.54.147.37',
    'hektor':       '141.54.147.43',
    'minos':        '141.54.147.49',
    'pan':          '141.54.147.52',
    'headcrash':    '141.54.147.63',
    'perseus':      '141.54.147.64',
    'spacemonster': '141.54.147.101',
    'steelyglint':  '141.54.147.102',
    'oelze':        '141.54.172.157',
    'apollo':       '141.54.172.230',
}

device_list = []

def init_hmd_tracking(server_ip, port):
    hmd = avango.daemon.HMDTrack()
    for i in range(7):
        hmd.stations[i] = avango.daemon.Station('hmd-{0}'.format(str(i)))

    hmd.server = server_ip
    hmd.port = port

    device_list.append(hmd)
    print("HMD started!")


if __name__ == '__main__':
    init_hmd_tracking(host_ips["demeter"], "7770")

    avango.daemon.run(device_list)
