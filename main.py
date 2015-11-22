__author__ = "Public Joe62"

import sys
from datetime import datetime

def singleton(class_):
  instances = {}
  def getinstance(*args, **kwargs):
    if class_ not in instances:
        instances[class_] = class_(*args, **kwargs)
    else:
        print "exists"
    return instances[class_]
  return getinstance

@singleton
class LogHelper():
    value = 1

    _isconsole = False
    _isfile = False
    _isfileopened = False
    _filename = ""
    _file = None
    _timestampformat = "%d.%m.%y %H:%M:%S.%f"

    def __init__(self, paramfilename="CONSOLE"):
        print "LogHelper::constructor"

        if paramfilename == "CONSOLE":
            self._isconsole = True
        else:
            # output redirected to file
            #
            self._isfile = True
            self._filename = paramfilename

        return

    def _logopenfile(self):
        if self._isfile:
            self._file = open(self._filename, 'w')
            self._isfileopened = True

        else:
            print "LogHelper::_logopenfile: _isfile=True expected!"
            raise Exception
        return

    def log(self, strMsg):

        # add timestamp to strMsg
        #
        strMsg = datetime.now().strftime(self._timestampformat) + " " + strMsg
        if self._isconsole:
            print strMsg
        elif self._isfile:
            # open file if necessary
            #
            if not self._isfileopened:
                self._logopenfile()
            # write string to file
            #
            self._file.write("%s\r\n" % (strMsg))
        else:
            print "LogHelper::log: self._isconsole or self._isfile expected!"
            raise Exception
        return

    def close(self):
        if self._isfileopened:
            self._file.close()
            self._isfileopened = False

        return

    pass


if __name__ == "__main__":
    print "loghelper.py::main::start"
    m = LogHelper("out2.txt")
    m.log("msg1")
    m.log("msg2")
    m.close()
    print "loghelper.py::main::end"

