def get_cmds()-> list:
	cmds = ["touch sshworked.txt", "touch create.txt", "touch file3.txt", "ls"]
	my_cmds []
	while True:
		print(f"Commands to Run: {my_cmds}")
                        cmd = int(input(f'Select one of the following commands:\n1: {}\n2: {}\n3: {}\n4: {}\nPress 5 to exit\n'.format(*cmds)))
	if cmd == 5
		break
		my_cmds.append(cmds[cmd-1])
		return my_cmds
