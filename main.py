__author__ = "Johannes Velmans"

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
class MyClass():
    value = 1

    def getValue(self):
        return self.value

    def setValue(self, xvalue):
        self.value = xvalue
        return

    pass

class LogHelper:

    def __init__(self):
        return


if __name__ == "__main__":
    print "loghelper.py::main::start"
    m = MyClass()
    print "wert 1 = %d" % m.getValue()
    m.setValue(3)
    n = MyClass()
    print "wert 2 = %d" % n.getValue()

    print "loghelper.py::main::end"

