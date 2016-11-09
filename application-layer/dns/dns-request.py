import socket
import struct
import binascii

#qid = '0x62cd'
#flags = '0x0100'
#qd = '0x0001'
#an = '0x0000'
#ns = '0x0000'
#ar = '0x0000'

# www.nasa.gov
#q = '03777777046e61736103676f7600'
#dnstype = '0x0001'
#dnsclass = '0x0001'

def main():
    query = ( 0x62, 0xcd, 0x01, 0x00,
              0x00, 0x01, 0x00, 0x00,
              0x00, 0x00, 0x00, 0x00,
              0x03, 0x77, 0x77, 0x77,
              0x04, 0x6e, 0x61, 0x73,
              0x61, 0x03, 0x67, 0x6f,
              0x76, 0x00, 0x00, 0x01,
              0x00, 0x01 )

    sd = struct.Struct('30B')
    message = sd.pack(*query)
    print("Sending request:\n%s" % ( binascii.hexlify(message) ))

    server = '8.8.8.8'  # google dns
    port = 53

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.sendto(message, (server, port))

    s2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s2.bind(( '', 5300 ))
    while True:
        data, addr = s.recvfrom(512)
        print("Recieved message: %s" % (data))

    s.close()

if __name__ == "__main__":
    main()
