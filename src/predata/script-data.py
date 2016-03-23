import re


def get_line_content(line):
    "deal with per line"
    return line.split(",")[-3]


def get_join_line_content(line):
    "deal with per line"
    return line.split(",")[-4] + line.split(",")[-3]


def get_line_digit(line):
    return line.split(",")[-5]


def get_line_time(line):
    return line.split(",")[1]


roamd_file = open('result/romanfile.csv', 'w+a')  # open for output (creates)
offline_file = open('result/offline.csv', 'w+a')  # open for output (creates)
join_file = open('result/join.csv', 'w+a')  # open for output (creates)


def deal_roamd_content(content):
    data = ""
    action_user = content[content.find("Client") + 7:content.find("roamed from") - 1]
    roman_from = content[content.find("from BSSID") + 11:content.find("of AC") - 1]
    roman_to = content[content.find("to BSSID") + 9:content.find("to BSSID") + 23]

    data = data + time + "," + action_user + "," + roman_from + "," + roman_to + "\n";
    roamd_file.write(data)


def deal_off_content(content):
    data = ""
    action_user = content[content.find("Client") + 7:content.find("disconnected") - 1]
    data = data + time + "," + action_user + "\n"
    offline_file.write(data)


def deal_join_content(content):
    data = ""
    action_user = content[content.find("Client") + 7:content.find("successfully") - 1]
    join_on = content[content.find("with BSSID") + 11:content.find("with BSSID") + 25]
    data = data + time + "," + action_user + "," + join_on+"\n"
    join_file.write(data)


if __name__ == '__main__':
    data_file="data.csv"
    filedata = open(data_file)
    for line in filedata:
        content = get_line_content(line)
        time = get_line_time(line)
        if re.match(".*WMAC_CLIENT_JOIN_WLAN", line) is not None:
            content = get_join_line_content(line)
            print(content)
            deal_join_content(content)

        if re.match(".*WMAC_CLIENT_GOES_OFFLINE", line) is not None:
            deal_off_content(content)

        if re.match(".*WROAM_ROAM_HAPPEN", line) is not None:
            deal_roamd_content(content)

