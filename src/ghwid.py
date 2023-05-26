import subprocess


class HWID:

    @staticmethod
    def grab():

        """
        Retrieves the HWID.
        
        Returns:
            str: HWID.
        """
        
        output = subprocess.check_output('wmic csproduct get uuid').decode('utf-8')
        return output.split('\n')[1].strip()


if __name__ == "__main__":
    main = HWID()
    hwid = main.grab()
    print(hwid)
