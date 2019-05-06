# -*- coding: utf-8 -*-
import os
import subprocess
import signal
import sys


class MockLogger(object):
    """
    the log module
    """

    def __init__(self):
        self.info = self.error = self.critical = self.debug

    def debug(self, msg):
        print("LOGGER:" + msg)


class cmd(object):
    """
        Encapsulating CMD command execution
    """


    def __init__(self, cmdStr):
        self.cmdStr = cmdStr
        self.ret_code = None
        self.ret_info = None
        self.err_info = None
        self.logger = MockLogger()

    def run(self):
        self.logger.debug("run %s" % self.cmdStr)
        self._process = subprocess.Popen(self.cmdStr, shell=True,
                                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self.wait()

    def wait(self):
        self.logger.debug("waiting %s" % self.cmdStr)
        self.ret_info, self.err_info = self._process.communicate()
        self.ret_code = self._process.returncode
        self.logger.debug("waiting %s done. return code is %d" % (self.cmdStr,
                                                                  self.ret_code))

    def get_status(self):
        retcode = self._process.poll()
        if retcode == None:
            status = "RUNNING"
        else:
            status = "FINISHED"
        self.logger.debug("%s status is %s" % (self.cmdStr, status))
        return status


    def close(self, sig):
        self.logger.debug("send signal %s to %s" % (sig, self.cmdStr))
        os.kill(self._process.pid, sig)

