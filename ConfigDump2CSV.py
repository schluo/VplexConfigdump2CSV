# encoding: utf-8

__author__    = "Oliver Schlueter"
__copyright__ = "Copyright 2021, Dell Technologies"
__license__   = "GPL"
__version__   = "1.0.2"
__email__     = "oliver.schlueter@dell.com"
__status__    = "Production"

""""
###########################################################################################################

  DELL EMC VPLEX config reader


  Permission is hereby granted, free of charge, to any person obtaining a copy of this software 
  and associated documentation files (the "Software"), to deal in the Software without restriction, 
  including without limitation the rights to use, copy, modify, merge, publish, distribute, 
  sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is 
  furnished to do so, subject to the following conditions:
  The above copyright notice and this permission notice shall be included in all copies or substantial 
  portions of the Software.
  
  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT 
  LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. 
  IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, 
  WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE 
  SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

###########################################################################################################

#import modules"""
import argparse
import sys
import xmltodict
import datetime


###########################################
#        VARIABLE
###########################################
DEBUG = False

###########################################
#    Methods
###########################################

def escape_ansi(line):
        ansi_escape = re.compile(r'(\x9B|\x1B\[)[0-?]*[ -/]*[@-~]')
        return ansi_escape.sub('', str(line))

def get_argument():
    global file, module
    try:
        # Setup argument parser
        parser = argparse.ArgumentParser()
        parser.add_argument('-f', '--file', type=str, help='path and filename of configdump file', required=True)
        parser.add_argument('-m', '--module',
                    type=str,
                    choices=['vv',
                             'view-init',
                             'view-luns',
                             'extents',
                             'disks',
                             'all'],
                    help='Requested MODULE for getting detail config. \
                            Possible options are: vv (virtual volumes)  | \
                            view-init (view with initiator infos) | \
                            view-luns (view with LUNs infos | \
                            extens | \
                            disks | \
                            all (all data) ',
                    dest='module', required=True)      
        
        args = parser.parse_args()

    except KeyboardInterrupt:
        # handle keyboard interrupt #
        return 0

    file = args.file
    module = args.module
  


###########################################
#    CLASS
###########################################

class Vplex():
    # This class permit to connect of the vplex's API

    def __init__(self):
        self.file = file

    def read_configdump(self):
        # send a request and get the result as dict
        global configDump


        # Request metrics of local cluster
        try:
            with open(file) as fd:
               configDump = xmltodict.parse(fd.read())["configDump"]
        except Exception as err:
            print(timestamp + ": Not able to read file: " + str(err))
            exit(1)

    def process_configdump(self):

        # initiate  output
        try:
            print("Config Data successful loaded at " + timestamp )

            if module=="vv" or module=="all":
                # Virtual Volumes            
                print("virtual-volume,size, locality")
                for vv in configDump["virtual-volumes"]["volume"]:
                    print(vv["@name"] + "," + vv["@size"] + "," + vv["@locality"])
                 

            if module=="view-init" or module=="all":
                # Views Initiator
                print("view name, view initiators")
                for view in configDump["views"]["view"]:
                   listOfInitiators = ""
                   for initiator in view["viewInitiators"]["viewInitiator"]:
                      listOfInitiators = listOfInitiators + initiator["@id"] + ";"
                   print(view["@name"] + "," + listOfInitiators )

            if module=="view-luns" or module=="all":
                # Views LUNs
                print("view name, view volumes")
                for view in configDump["views"]["view"]:
                    listOfLUNs = ""
                    volumes=view["viewVolumes"]["viewVolume"]
                    if "@id" in volumes:
                        listOfLUNs = listOfLUNs + volumes["@id"] + "|" + volumes["@lun"] + ";"
                    else:
                       for volume in volumes:
                          listOfLUNs = listOfLUNs + volume["@id"] + "|" + volume["@lun"] + ";"
                    print(view["@name"] + "," + listOfLUNs)
                    
                    
            if module=="extents" or module=="all":
                # extents
                print("extent name, extens size, used by")
                for extent in configDump["extents"]["extent"]:
                    print(extent["@name"] + "," + extent["@size"] + "," + extent["@used-by"] + ",")
                    
                    
            if module=="disks" or module=="all":
                # disks
                print("disk name, extens size, used")
                for disk in configDump["disks"]["disk"]:
                    print(disk["@name"] + "," + disk["@size"] + "," + disk["@use"] + ",")
                

        except Exception as err:
            print(timestamp + ": Error while generating result output: " + str(err))
            exit(1)

        sys.exit(0)


def main(argv=None):
    # get and test arguments
    get_argument()

    # store timestamp
    global timestamp
    timestamp = datetime.datetime.now().strftime("%d-%b-%Y (%H:%M:%S)")

    # display arguments if DEBUG enabled
    if DEBUG:
        print("file: " + file)
    else:
        sys.tracebacklimit = 0

    myvplex = Vplex()

    myvplex.read_configdump()
    myvplex.process_configdump()


if __name__ == '__main__':
    main()
    sys.exit(3)
