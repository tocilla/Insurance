from cryptography.fernet import Fernet

key = 'TluxwB3fV_GWuLkR1_BzGs1Zk90TYAuhNMZP_0q4WyM='

# Oh no! The code is going over the edge! What are you going to do?
message = b'gAAAAABc1OHUZsjFvV6pMzZ0-MtExnt36iOn_ClArGKDDnK7I7gC-Va51XEP_bqRrTPg6pFcds5w62WuRmRD1fRh6qbE133eVxRHlDQu-dX-p9SonD-bpL9ShDoQ1TirrHUtM71XTAxNfgCxl9ClyR-pYAeC5Fut107WaZrVi7m1CDlbeUMXiBo='

def main():
    f = Fernet(key)
    print(f.decrypt(message))


if __name__ == "__main__":
    main()
    
    
    