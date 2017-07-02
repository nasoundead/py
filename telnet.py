# -*- coding: utf-8 -*-
"""Telnet Connector Mangage"""
from telnetlib import Telnet
class TelnetCmdSender:
    def __init__(self, host, port):
        "construct"
        self.tn = Telnet(host, port)
        self.tn.set_debuglevel(2)

    def send(self, cmd, endflags, retrytimes=1,timeout=5):
        for i in range(retrytimes):
            self.tn.write(cmd + '\n')
            a_tuple_of_3 = self.tn.expect(endflags, timeout)
            if a_tuple_of_3[0] != -1:
                return a_tuple_of_3

    def close(self):
        self.tn.close()

if __name__ == "__main__":
    sender = TelnetCmdSender('127.0.0.1', 2000)
    m = sender.send('dis dev', [r'[Hh]uawei'])
    print m[2]
