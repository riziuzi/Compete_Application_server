import socket

def get_ip_address():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip_address = s.getsockname()[0]
        s.close()

        return ip_address
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def updateEnv():
    ip_address_str = str(get_ip_address())

    # os.environ["HOST"] = ip_address_str
    # os.environ["PORT"] = "8088"

    with open(".env", "w") as env_file:
        env_file.write(f"REACT_APP_HOST={ip_address_str}\n")
        env_file.write("REACT_APP_PORT=8055\n")

    print(f"HOST value updated to: {ip_address_str}")
    print("PORT value updated to: 8055")
    
if __name__ == "__main__":
    updateEnv()