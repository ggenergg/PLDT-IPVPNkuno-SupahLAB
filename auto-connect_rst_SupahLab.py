
rst_ip = crt.Dialog.Prompt("What is your RST SupahLAB IPv4 Address? ")

connections = [
	"/TELNET " + rst_ip + " 2018",
	"/TELNET " + rst_ip + " 2019",
	"/TELNET " + rst_ip + " 2027",
	"/TELNET " + rst_ip + " 2026",
	"/TELNET " + rst_ip + " 2025",
	"/TELNET " + rst_ip + " 2028",
	"/TELNET " + rst_ip + " 2023",
	"/TELNET " + rst_ip + " 2022",
]

crt.Screen.Synchronous = True

for connection in connections:
	crt.Session.ConnectInTab(connection)

crt.Screen.Synchronous = False