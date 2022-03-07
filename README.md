# VplexConfigdump2CSV
Allows to generate Config Detail Data from Dell EMC Vplex configdump.xml file

# Example how to create the file on the Dell EMC Vplex:
VPlexcli:/clusters> configdump --file /var/log/VPlex/cli/config-dump-cluster-1.txt --cluster cluster-1

# How to use the tool
usage: ConfigDump2CSV.py [-h] -f FILE -m {vv,view-init,view-luns,extents,disks,all}

arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  path and filename of configdump file
  -m {vv,view-init,view-luns,extents,disks,all}, --module {vv,view-init,view-luns,extents,disks,all}
                        Requested MODULE for getting detail config. 
                        Possible options are: vv (virtual volumes) | 
                        view-init (view with initiator infos) | 
                        view-luns (view with LUNs infos | 
                        extens | disks | 
                        all (all data)
                        
---
  
Copyright (c) 2022 Dell Technologies

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE

