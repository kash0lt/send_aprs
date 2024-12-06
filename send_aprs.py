import socket
from aprs_secinfo import aprs_secinfo

# Configuration
APRS_SERVER = "rotate.aprs2.net"  # APRS-IS server
APRS_PORT = 14580                # APRS-IS port
aprssec = aprs_secinfo()

CALLSIGN = aprssec.CALLSIGN       # Replace with your callsign
PASSCODE = aprssec.PASSCODE      # Replace with your APRS passcode
LATITUDE = aprssec.LATITUDE            # Replace with your latitude
LONGITUDE = aprssec.LONGITUDE          # Replace with your longitude
COMMENT = aprssec.COMMENT            # Optional status comment
SYMBOL_CODE = aprssec.SYMBOL_CODE

# Construct the APRS packet
aprs_packet = f"{CALLSIGN}>APRS,TCPIP*:!{LATITUDE}/{LONGITUDE}{SYMBOL_CODE} {COMMENT}"

def send_aprs_packet(server, port, callsign, passcode, packet):
    try:
        # Connect to the APRS-IS server
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((server, port))
            print(f"Connected to {server}:{port}")

            # Authenticate with the server
            auth_message = f"user {callsign} pass {passcode} vers PYTHON-APRS 1.0\n"
            s.send(auth_message.encode())
            print("Authentication sent.")

            # Send the APRS packet
            s.send((packet + "\n").encode())
            print(f"Packet sent: {packet}")

            # Read and print server response
            response = s.recv(1024).decode()
            print(f"Server response: {response}")

    except Exception as e:
        print(f"Error: {e}")

# Call the function to send the APRS packet
send_aprs_packet(APRS_SERVER, APRS_PORT, CALLSIGN, PASSCODE, aprs_packet)
