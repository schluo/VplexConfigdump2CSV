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
