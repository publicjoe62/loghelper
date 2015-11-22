# LogHelper

The class LogHelper is used to output logging information.

## Methods
Nachfolgend die Liste der öffentlichen Methoden von LogHelper().

### Constructor
* __LogHelper()__ 
    
    Ein Konstruktoraufruf ohne Parameter lenkt die Ausgaben auf die Konsole um und als Log-Level wird "ALL" 
    angewendet. Als Zeitstempel wird das Format "dd.mm.yy hh:mm:ss.msec" verwendet.


* LogHelper(outputfilename)


### log(message)
Ausgabe einer Log Meldung

### close()
Falls die Ausgabe in eine Datei umgelenkt wurde, wird die Datei geschlossen.



