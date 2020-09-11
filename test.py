from sshtunnel import SSHTunnelForwarder

server = SSHTunnelForwarder(
    "newton3.bair.berkeley.edu",
    ssh_username="justinvyu",
    ssh_pkey="~/.ssh/id_rsa",
    remote_bind_address=("127.0.0.1", 5001)
)

server.start()

print(server.local_bind_port)  # show assigned local port

