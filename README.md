# **TeraBoxUtility**

## Overview 

>TeraBoxUtility is a tool to quickly upload data to TeraBox. Store large amounts of information securely. 

## Requirement
> TeraBoxUtility use python 9 and chrome driver.
Need to have google chrome to use.



## Usage


```python
from terabox_utility.util.tera import TeraBox

# Set path to folder
# Example D:\test1
a = ['nguyenthanhdungktum@gmail.com']
account = 'email:password:backup_email'
key = 'ZmDfcTF7_60GrrY167zsiPd67pEvs0aGOv2oasOM1Pg='
upload_path = 'D:\\profiles'
download_path = 'D:\\test1\\'
download_location = 'C:\\Users\\Admin\\Downloads'
tera = TeraBox(a, account, key, upload_path, download_path, download_location)
#Upload
tera.upload()
#Download
tera.download()
```

## Credit


## License
Copyright © 2022 moligroup