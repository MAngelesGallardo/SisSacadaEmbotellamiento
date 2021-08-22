#!/usr/bin/env python

#########################################
# Imports
#########################################
# - HMI Windows
import  sys
from gi.repository  import GLib, Gtk, GObject

# - HMI communication
from modbus         import ClientModbus as Client
from modbus	    import ConnectionException 

# - World environement
from world          import *

# "Constants"
HMI_SCREEN_WIDTH = 20
HMI_SLEEP        = 1

class HMIWindow(Gtk.Window):
    def resetLabels(self):
        self.bottlePositionValue.set_markup("<span weight='bold' foreground='gray33'>N/A</span>")
        self.motorStatusValue.set_markup("<span weight='bold' foreground='gray33'>N/A</span>")
        self.levelHitValue.set_markup("<span weight='bold' foreground='gray33'>N/A</span>")
        self.processStatusValue.set_markup("<span weight='bold' foreground='gray33'>N/A</span>")
        self.nozzleStatusValue.set_markup("<span weight='bold' foreground='gray33'>N/A</span>")
        self.connectionStatusValue.set_markup("<span weight='bold' foreground='red'>OFFLINE</span>")

    def __init__(self, address, port):
        Gtk.Window.__init__(self, title="LLenado de botellas")

        self.set_border_width(HMI_SCREEN_WIDTH)
        
        self.client = Client(address, port=port)

        elementIndex = 0

        # Grid
        grid = Gtk.Grid()
        grid.set_row_spacing(15)
        grid.set_column_spacing(10)
        self.add(grid)

        # Main title label
        label = Gtk.Label()
        label.set_markup("<span weight='bold' size='x-large'>Control del sistema de embotellado</span>")
        grid.attach(label, 0, elementIndex, 2, 1)
        elementIndex += 1

        # Bottle in position label
        bottlePositionLabel = Gtk.Label("Botella en posicion")
        bottlePositionValue = Gtk.Label()
        grid.attach(bottlePositionLabel, 0, elementIndex, 1, 1)
        grid.attach(bottlePositionValue, 1, elementIndex, 1, 1)
        elementIndex += 1

        # Nozzle status label
        nozzleStatusLabel = Gtk.Label("Boquilla")
        nozzleStatusValue = Gtk.Label()
        grid.attach(nozzleStatusLabel, 0, elementIndex, 1, 1)
        grid.attach(nozzleStatusValue, 1, elementIndex, 1, 1)
        elementIndex += 1

        # Motor status label
        motorStatusLabel = Gtk.Label("Estado del motor")
        motorStatusValue = Gtk.Label()
        grid.attach(motorStatusLabel, 0, elementIndex, 1, 1)
        grid.attach(motorStatusValue, 1, elementIndex, 1, 1)
        elementIndex += 1

        # Level hit label
        levelHitLabel = Gtk.Label("Etiqueta de nivel")
        levelHitValue = Gtk.Label()
        grid.attach(levelHitLabel, 0, elementIndex, 1, 1)
        grid.attach(levelHitValue, 1, elementIndex, 1, 1)
        elementIndex += 1

        # Process status
        processStatusLabel = Gtk.Label("Estado del proceso")
        processStatusValue = Gtk.Label()
        grid.attach(processStatusLabel, 0, elementIndex, 1, 1)
        grid.attach(processStatusValue, 1, elementIndex, 1, 1)
        elementIndex += 1

        # Connection status
        connectionStatusLabel = Gtk.Label("Estado de la conexion")
        connectionStatusValue = Gtk.Label()
        grid.attach(connectionStatusLabel, 0, elementIndex, 1, 1)
        grid.attach(connectionStatusValue, 1, elementIndex, 1, 1)
        elementIndex += 1

        # Run and Stop buttons
        runButton   = Gtk.Button("Run")
        stopButton  = Gtk.Button("Stop")

        runButton.connect("clicked", self.setProcess, 1)
        stopButton.connect("clicked", self.setProcess, 0)

        grid.attach(runButton, 0, elementIndex, 1, 1)
        grid.attach(stopButton, 1, elementIndex, 1, 1)
        elementIndex += 1

        # VirtuaPlant branding
        virtuaPlant = Gtk.Label()
        grid.attach(virtuaPlant, 0, elementIndex, 2, 1)

        # Attach Value Labels
        self.processStatusValue     = processStatusValue
        self.connectionStatusValue  = connectionStatusValue
        self.levelHitValue          = levelHitValue
        self.motorStatusValue       = motorStatusValue
        self.bottlePositionValue    = bottlePositionValue
        self.nozzleStatusValue      = nozzleStatusValue

        self.resetLabels()
        GObject.timeout_add_seconds(HMI_SLEEP, self.update_status)

    def setProcess(self, widget, data=None):
        try:
            self.client.write(PLC_RW_ADDR + PLC_TAG_RUN, data)
        except:
            pass

    def update_status(self):
        try:
            regs = self.client.readln(PLC_RO_ADDR, 17)

            if regs[PLC_TAG_CONTACT] == 1:
                self.bottlePositionValue.set_markup("<span weight='bold' foreground='green'>Si</span>")
            else:
                self.bottlePositionValue.set_markup("<span weight='bold' foreground='red'>No</span>")

            if regs[PLC_TAG_LEVEL] == 1:
                self.levelHitValue.set_markup("<span weight='bold' foreground='green'>Si</span>")
            else:
                self.levelHitValue.set_markup("<span weight='bold' foreground='red'>No</span>")

            if regs[PLC_TAG_MOTOR] == 1:
                self.motorStatusValue.set_markup("<span weight='bold' foreground='green'>Moviendose</span>")
            else:
                self.motorStatusValue.set_markup("<span weight='bold' foreground='red'>Quieto</span>")

            if regs[PLC_TAG_NOZZLE] == 1:
                    self.nozzleStatusValue.set_markup("<span weight='bold' foreground='green'>Abierto</span>")
            else:
                self.nozzleStatusValue.set_markup("<span weight='bold' foreground='red'>Cerrado</span>")

            regs = self.client.readln(PLC_RW_ADDR, 17)

            if regs[PLC_TAG_RUN] == 1:
                self.processStatusValue.set_markup("<span weight='bold' foreground='green'>Corriendo</span>")
            else:
                self.processStatusValue.set_markup("<span weight='bold' foreground='red'>Detenido</span>")

            self.connectionStatusValue.set_markup("<span weight='bold' foreground='green'>En curso</span>")

        except ConnectionException:
            if not self.client.connect():
                self.resetLabels()
        except:
            raise

        finally:
            return True

def main():
    GObject.threads_init()
    win = HMIWindow(PLC_SERVER_IP, PLC_SERVER_PORT)

    win.connect("delete-event", Gtk.main_quit)
    win.connect("destroy", Gtk.main_quit)

    win.show_all()
    Gtk.main()

if __name__ == "__main__":
    sys.exit(main())
