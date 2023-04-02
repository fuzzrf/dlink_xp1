D-Link Dir-2150 xupnpd remote exploit 

This router has usb media support. When USB storage is in use, it is also possible to enable xupnpd service.

There are several xupnpd plugins which are enabled by default, let's take a look at Dreambox plugin.

```
plugins/xupnpd_dreambox.lua

function dreambox_updatefeed(feed,friendly_name)
    local rc=false
    local feedspath=cfg.feeds_path
    if not friendly_name then
        friendly_name=feed
    end
    local wget="wget -q -O- "
[1]    local dreambox_url='http://'..feed..'/web/'
    local bouquets={}
    print(wget..dreambox_url.."getservices")
[2]    local xmlbouquetsfile=io.popen(wget..dreambox_url.."getservices")
    bouquets=xml_to_tables(xmlbouquetsfile,"e2servicelist")
</code>
```

The variable 'feed' on line #1 comes from HTTP request, it is not sanitized.

It is used on line #2 via io.popen, thus it is possible to execute arbitrary commands.

```
$ cat /VERSION 
NAME:           DIR_2150_MT7621D
VERSION:        4.0.0
DATAMODEL:      2.40.0
SYSBUILDTIME:   Fri Jun  5 18:21:26 MSK 2020
VENDOR:         D-Link Russia
BUGS:           <support@dlink.ru>
SUMMARY:        Root filesystem image for DIR_2150_MT7621D

```

How to use:
```
$ ./t1.py 
```

File /tmp/hello.txt should be created on a device.

