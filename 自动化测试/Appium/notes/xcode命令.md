
1. 截图：
   `xcrun simctl io booted screenshot /pictures/test.png`

2. 录屏命令：
   `xcrun simctl io booted recordVideo /videos/test.mp4`

   在终端按Ctrl+C来停止录屏.

3. 查看已安装的设备：
   `xcrun simctl list`

   列出安装的可用的模拟器：`xcrun instruments -s`

   查看已安装的模拟器： `ios-sim showdevicetypes`

4. 启动模拟器： 
   `xcrun simctl boot $UUID`

   `xcrun instruments -w "iPhone 8(11.2)"`

   用来启动模拟器，其中的UUID参数就是之前列表中的UUID。
   
5. 关闭模拟器： 
   `xcrun simctl shutdown $UUID`

6. 重置模拟器： 
   `xcrun simctl erase $UUID`

7. 清理不可用的模拟器： 
   `xcrun simctl delete unavailable`

   当Mac空间不够用时，这条命令或许可以帮你重获不是磁盘空间。

8. 安装指定app：
   `xcrun simctl install booted <app路径>`

   多设备时：
   `xcrun simctl install <device> <app路径> `

   安装指定app: `ios-sim launch /Users/nali/Desktop/ting.app --devicetypeid iPhone-X, 11.2`

9. 运行指定的app：
   `xcrun simctl launch booted <bundle identifier>`

   多设备时：
   `xcrun simctl launch <device> <bundle identifier>`

10. 关闭已经打开的应用：
    `xcrun simctl terminate booted <bundle identifer>`

    多设备时：
    `xcrun simctl terminate <device> <bundle identifier>`

11. 卸载指定应用：
    `xcrun simctl uninstall booted <bundle identifer>`

    多设备时：
    `xcrun simctl uninstall <device> <bundle identifier>`
    
12. 在模拟器与Mac设备之间进行复制&粘贴pbcopy & pbpaste
	`pbcopy`复制内容到Mac设备的剪贴板

	`pbpaste` 将 Mac设备的剪贴板的内容进行粘贴

	`xcrun simctl pbcopy booted`  将Mac设备中剪贴板上的内容复制到模拟器上的剪贴板上；方向：Mac->模拟器
   
	`xcrun simctl pbpaste booted` 将模拟器中剪贴板上的内容复制到Mac设备上的剪贴板上：方向：模拟器->Mac
	`xcrun simctl pbsync sourceDevice` destDevice 将source设备中剪贴板上的内容同步到dest设备上的剪贴板上；方向：source<->dest,其中可以用 host 表示Mac设备

13. 查看更多功能：
   `xcrun simctl -h`
