#!/usr/bin/python3

import netifaces
import socket

def hostname_f():
    """Obtain hostname of machine"""
    return socket.gethostname()

def interface_f():
    """Pull all interfaces for networking"""
    return netifaces.interfaces()

def ip_function_f(x):
    """IP for given interface"""
    return netifaces.ifaddresses(x)[2][0]['addr']

def all_interf_ip_f():
    """Iterate through interfaces and IP"""
    print(hostname_f())
    for i in interface_f():
        try:
            print("%s: %s" % (i, ip_function_f(i)))
        except:
            pass



if __name__ == '__main__':
    all_interf_ip_f()
