import os
import os.path
from tkinter import Label, Tk

# pip install 'pyserial' to import serial
# The script below adds pyserial to your python modules if it's not installed
try:
    import os

    import serial
    import serial.tools.list_ports
except:
    os.system('pip install pyserial')
    import serial
    import serial.tools.list_ports

root = Tk()

# Add Icon to window Titlebar
if os.name == 'nt':
    homepath = os.path.expanduser('~')
    tempFile = '%s\Caveman Software\%s' % (homepath, 'Icon\icon.ico')

    if (os.path.exists(tempFile) == True):
        root.wm_iconbitmap(default=tempFile)

    else:
        import create_icon
        print('File Created')
        root.wm_iconbitmap(default=tempFile)

title = (os.path.basename(__file__)[0:-3])
root.title(title.title())
root.geometry('400x200')


# get a list of ports being used as Arduinos
ports = list(serial.tools.list_ports.comports())
for p in ports:
    if "Arduino" in p.description:
        myport = str(p)[0: 5: 1]
        nextrow = myport[3:]
        print('Arduino found on : ' + myport+'\nUsing '+myport)
        from tkinter import Label
        lblmyport = Label(root, text='Arduino found on ' + myport)
        lblmyport.grid(column=0, row=nextrow)
    else:
        myport = str(p)[0: 5: 1]
        nextrow = myport[3:]
        lbl2 = Label(root, text='Found open port ' +
                     myport+' but No Arduino Found')
        lbl2.grid(column=0, row=nextrow)
        print('Found open port ' + myport+' but No Arduino Found')

root.mainloop()
