__Author__ = "lee"
#! -*- coding:utf-8 -*-
from MagicAuto.wrapper.common import paramCheck
def top(param):
    """
    Assemble the command
    :param:
        -H      Show threads
        -k      Fallback sort FIELDS (default -S,-%CPU,-ETIME,-PID)
        -o      Show FIELDS (def PID,USER,PR,NI,VIRT,RES,SHR,S,%CPU,%MEM,TIME+,CMDLINE)
        -O      Add FIELDS (replacing PR,NI,VIRT,RES,SHR,S from default)
        -s      Sort by field number (1-X, default 9)
        -b      Batch mode (no tty)
        -d      Delay SECONDS between each cycle (default 3)
        -m      Maximum number of tasks to show
        -n      Exit after NUMBER iterations
        -p      Show these PIDs
        -u      Show these USERs
        -q      Quiet (no header lines)
        Cursor LEFT/RIGHT to change sort, UP/DOWN move list, space to force
        update, R to reverse sort, Q to exit.

    :return:
         the assembled command string

    """
    paramStand = {"H":"optional",
                  "k":"optional",
                  "o":"optional",
                  "O":"optional",
                  "s":"optional",
                  "b":"optional",
                  "d":"optional",
                  "m":"optional",
                  "n":"optional",
                  "p":"optional",
                  "u":"optional",
                  "q":"optional"
    }
    paramCheck(paramStand,param)
    cmd = "top"
    for key in param:
        cmd = cmd + " -%s"%key
        if param[key] is not "":
            cmd = cmd + " %s"%param[key]
        else:
            pass
    return cmd




