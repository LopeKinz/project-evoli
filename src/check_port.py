import socket


class PortChecker:
    
    @staticmethod
    def is_open(ip:str, port:str) -> None:
        
        """
        Checks if a port is open on an IP.

        Args:
            ip (str): The IP address to check.
            port (int): The port number to check.

        Returns:
            bool: True if the port is open, False otherwise.
        """
        
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((ip, int(port)))
            s.shutdown(2)
            return True
        except:
            return False


# test case 

if __name__ == "__main__":
    ip_address = "127.0.0.1"
    port_number = 80
    result = PortChecker.is_open(ip_address, port_number)
    print(result)
