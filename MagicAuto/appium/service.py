#!/usr/bin/env python

import http.client
import os
import subprocess
import time
from multiprocessing import Process
import threading
from MagicAuto.appium.common.common import common as cm
from MagicAuto.common.operateYaml import getyaml

def poll_url(host, port, path, timeout_ms):
    time_started_sec = time.time()
    while time.time() < time_started_sec + timeout_ms / 1000.0:
        try:
            conn = http.client.HTTPConnection(host=host, port=port, timeout=1.0)
            conn.request('HEAD', path)
            if conn.getresponse().status < 400:
                return True
        except Exception:
            pass
        time.sleep(1.0)
    return False


class AppiumServiceError(RuntimeError):
    pass


class AppiumService(object):
    def __init__(self, l_devices):
        self._devices = l_devices

    def start(self, **kwargs):
        """
        Starts Appium service with given arguments.
        """
        self.stop()
        for i in range(0,len(self._devices["appium"])):
            t1 = runServer(self._devices["appium"][i]["cmd"])
            p = Process(target=t1.start())
            p.start()


    def stop(self):
        """
        Stops Appium service if it is running.
        The call will be ignored if the service is not running
        or has been already stopped.

        :return:
        `True` if the service was running before being stopped
        """
        is_terminated = False
        if self.is_running:
            os.system('taskkill /f /im  node.exe')
            is_terminated = True
        return is_terminated

    @property
    def is_running(self):
        """
        Check if the service is running.

        :return:
        `True` or `False`
        """


        for i in range(0, len(self._devices["appium"])):
            if not poll_url(cm.DEFAULT_HOST,str(self._devices["appium"][i]["port"]),cm.STATUS_URL,1000):
                return False
        return True


class runServer(threading.Thread):
    def __init__(self, cmd):
        threading.Thread.__init__(self)
        self.cmd = cmd
    def run(self):
        os.system(self.cmd)
        error_msg = None

        # if  not poll_url(cm.DEFAULT_HOST, cm.DEFAULT_PORT, cm.STATUS_URL, cm.STARTUP_TIMEOUT_MS):
        #     error_msg = 'Appium has failed to start on {}:{} within {}ms timeout' \
        #         .format(cm.DEFAULT_HOST, cm.DEFAULT_PORT, cm.STATUS_URL, cm.STARTUP_TIMEOUT_MS)
        #
        #     raise AppiumServiceError(error_msg)


if __name__ == '__main__':
   devices = getyaml(r"D:\AutoEnvironment\MagicAuto\devices\devices.yaml")
   os.system("appium  -a 127.0.0.1 -p 4723 -bp 4733")
   # server = AppiumService(devices)
   # server.start()
   # server.stop()