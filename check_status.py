#!/usr/bin/env python3

#Check for server status

import json

with open("status.json", "r") as f:
    svr = json.load(f)
    print(svr)
    downed_servers = []
    for serv in svr:
        if serv["state"] == "down":
            downed_servers.append(serv)

print(f"The Following is a list of all 'down' servers:{downed_servers}")

with open("downed_servers.txt", "w") as f2:
    spaced_servers = [f"{srv['server']}\n" for srv in downed_servers]
    f2.writelines(spaced_servers)
