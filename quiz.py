from cryptography.fernet import Fernet

key = 'TluxwB3fV_GWuLkR1_BzGs1Zk90TYAuhNMZP_0q4WyM='

# Oh no! The code is going over the edge! What are you going to do?
message = b'gAAAAABcXLCk3u8odZY-1SxIWs7o_Ny-tp5K9N3uCj86VO64VU0ui7JnqTxZvPjDUuDFw0q07I4XDSF4O1HY1SlWDucZ8XJzWZH7SLLfOr1lUmlszC7UqZP5RHbQoJUaoWUsm6pxDE3bLxTCCSfmZsw1cb_GiZtEUY5vhiMmmZo9gaq3Ue8hxYI='

def main():
    f = Fernet(key)
    print(f.decrypt(message))


if __name__ == "__main__":
    main()
