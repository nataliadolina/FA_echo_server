import csv


def read_hosts_passwords(filename="saved_hosts.csv"):
    b = {}
    with open('txt/' + filename) as file:
        reader = csv.DictReader(file, delimiter=',')
        for line in reader:
            host = line["host"]
            password = line["password"]
            nick = line["nickname"]
            b[host] = [password, nick]

    return b


def write_host_password(data, filename="saved_hosts.csv"):
    with open('txt/' + filename, 'a+', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(data)


def get_saved_hosts():
    return list(read_hosts_passwords("saved_hosts.csv").keys())


def get_password(host):
    return read_hosts_passwords("saved_hosts.csv")[host][0]


def get_nickname(host):
    return read_hosts_passwords("saved_hosts.csv")[host][1]
