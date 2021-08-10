1. `iOS` 用到的`ideviceinstaller`，类似于`Android`的`adb`
   
   安装：`brew install libimobiledevice`
   
2. 安装应用：`ideviceinstaller -i xxx.ipa`
   
3. 卸载应用：`ideviceinstaller -U <bundleId>`
   
4. 查看应用列表：`ideviceinstaller [-u <device-udid>] -l`
   
5. 查看系统日志：`idevicesyslog [-u <device-udid>]`
   
6. 查看当前设备列表：`instruments -s devices`  
   注意：这里列出的设备包括模拟器及 mac 电脑本身
   
7. 查看当前已连接的设备的UUID：`idevice_id --list`
   
8.  截图：`idevicescreenshot`
   
9.  查看设备信息：`ideviceinfo`

10. [参考](https://github.com/libimobiledevice/libimobiledevice/)