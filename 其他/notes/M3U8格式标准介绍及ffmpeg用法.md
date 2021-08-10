#### 一、M3U8 格式标准介绍

M3U8文件是指UTF-8编码格式的M3U文件。M3U文件是记录了一个索引纯文本文件，打开它时播放软件并不是播放它，而是根据它的索引找到对应的音视频文件的网络地址进行在线播放。

M3U8是一种常见的流媒体格式，主要以文件列表的形式存在，既支持直播又支持点播，尤其在Android、iOS等平台最为常用。

下面是CCTV6直播播放地址：http://ivi.bupt.edu.cn/hls/cctv6hd.m3u8的M3U8的文件列表：

```makefile
#EXTM3U
#EXT-X-VERSION:3
#EXT-X-MEDIA-SEQUENCE:35232
#EXT-X-TARGETDURATION:10
#EXTINF:10.000,
cctv6hd-1549272376000.ts
#EXTINF:10.000,
cctv6hd-1549272386000.ts
#EXTINF:10.000,
cctv6hd-1549272396000.ts
#EXTINF:10.000,
cctv6hd-1549272406000.ts
#EXTINF:10.000,
cctv6hd-1549272416000.ts
#EXTINF:10.000,
cctv6hd-1549272426000.ts
```

相关的几个字段：

- EXTM3U：这个是M3U8文件必须包含的标签，并且必须在文件的第一行，所有的M3U8文件中必须包含这个标签。
- EXT-X-VERSION：M3U8文件的版本，常见的是3（目前最高版本应该是7）。
- EXT-X-TARGETDURATION：该标签指定了媒体文件持续时间的最大值，播放文件列表中的媒体文件在EXTINF标签中定义的持续时间必须小于或者等于该标签指定的持续时间。该标签在播放列表文件中必须出现一次。
- EXT-X-MEDIA-SEQUENCE：M3U8直播是的直播切换序列，当播放打开M3U8时，以这个标签的值作为参考，播放对应的序列号的切片。
- EXTINF：EXTINF为M3U8列表中每一个分片的duration，如上面例子输出信息中的第一片的duration为10秒。在EXTINF标签中，除了duration值，还可以包含可选的描述信息，主要为标注切片信息，使用逗号分隔开。

关于客户端播放M3U8的标准还有更多的讲究，下面我们来介绍一些：

1. 分片必须是动态改变的，序列不能相同，并且序列必须是增序的。
2. 当M3U8没有出现EXT-X-ENDLIST标签时，无论这个M3U8列表中有多少分片，播放分片都是从倒数第三片开始播放，如果不满三片则不应该播放。当然如果有些播放器做了特别定制了，则可以不遵照这个原则。
3. 以播放当前分片的duration时间刷新M3U8列表，然后做对应的加载动作。
4. 前一片分片和后一片分片有不连续的时候，播放可能会出错，那么需要X-DISCONTINUTY标签来解决这个错误。
5. 如果播放列表在刷新之后与之前的列表相同，那么在播放当前分片duration一半的时间内在刷新一次。

在上面，我们提到了，一些上面例子没有出现的一些标签字段，下面我们针对一些额外的标签做一些补充说明：

- EXT-X-ENDLIST：若出现EXT-X-ENDLIST标签，则表明M3U8文件不会再产生更多的切片，可以理解为该M3U8已停止更新，并且播放分片到这个标签后结束。M3U8不仅仅是可以作为直播，也可以作为点播存在，在M3U8文件中保存所有切片信息最后使用EXT-X-ENDLIST结尾，这个M3U8即为点播M3U8。EXT-X-ENDLIST标签可能会出现在播放列表文件的任何地方，但是不能出现两次或以上。
- EXT-X-STREAM-INF：EXT-X-STREAM-INF标签出现在M3U8时，主要是出现在多级M3U8文件中时，例如M3U8中包含子M3U8列表，或者主M3U8中包含多码率M3U8时；该标签后需要跟一些属性，下面就来逐一说明一下这些属性：
  1. BANDWIDTH：BANDWIDTH的值为最高码率值，当播放EXT-X-STREAM-INF下对应的M3U8时占用的最大码率（必要参数）。
  2. AVERAGE-BANDWIDTH：AVERAGE-BANDWIDTH的值为平均码率值，当播放EXT-X-STREAM-INF下对应的M3U8时占用的平均码率。（可选参数）。
  3. CODECS：CODECS的值用于声明EXT-X-STREAM-INF下面对应M3U8里面的音视频编码、视频编码的信息（可选参数）。
  4. RESOLUTION：M3U8中视频的宽高信息描述（可选参数）。
  5. FRAME-RATE：子M3U8中的视频帧率（可选参数）。

#### 二、HLS 与 M3U8 

HLS（全称：Http Live Streaming）是由Apple公司定义的用于实时流传输的协议，HLS基于HTTP协议实现，传输内容包括两部分，一是M3U8描述文件，二是TS媒体文件。

HLS的优势为：自适应码率流播（adaptive streaming）。效果就是客户端会根据网络状况自动选择不同码率的视频流，条件允许的情况下使用高码率，网络繁忙的时候使用低码率，并且能够自动在二者之间随意切换。这对移动设备网络状况不稳定的情况下保障流畅播放非常有帮助。实现方法是服务器端提供多码率视频流，并且在列表文件中注明，播放器根据播放进度和下载速度进行自动调整。

为什么要用 TS 而不是 MP4？这是因为两个 TS 片段可以无缝拼接，播放器能连续播放，而 MP4 文件由于编码方式的原因，两段 MP4 不能无缝拼接，播放器连续播放两个 MP4 文件会出现破音和画面间断，影响用户体验。而且如果要在一段长达一小时的视频中跳转，如果使用单个 MP4 格式的视频文件，并且也是用 HTTP 协议，那么需要代理服务器支持 HTTP range request 获取大文件中的一部分。这样的话，对于代理服务器的性能来说要求较高。而 HTTP Live Streaming 则只需要根据列表文件中的时间轴找出对应的 TS 片段下载即可，不需要 range request，对代理服务器的要求小很多。所有代理服务器都支持小文件的高效缓存。



三、ffmpeg 实现m3u8格式互转

```bash
# MP4转m3u8
ffmpeg -re -i test.mp4 -c copy -f hls -hls_list_size 0 -bsf:v h264_mp4toannexb output.m3u8
ffmpeg -re -i test.mp4 -c copy -f hls -start_number 100 -hls_list_size 0 -bsf:v h264_mp4toannexb output.m3u8
# start_number 参数用于设置M3U8列表中的第一片的序列数
# hls_time参数用于设置M3U8列表中切片的duration
# hls_list_size参数用于为M3U8列表中的TS切片的个数。其中设置为0的时候，将包含所有,默认为5个
# hls_base_url 参数用于为M3U8列表的文件路径设置前置基本路径参数，因为在FFmpeg中生成M3U8时写入的TS切片路径默认为M3U8生成的路径相同，但是实际上TS所存储的路径既可以为本地绝对路径，也可以为相对路径，还可以为网络路径，因此使用hls_base_url参数可以达到该效果
ffmpeg -re -i test.mp4 -c copy -f hls -hls_base_url /Users/test/Desktop/test/ -bsf:v h264_mp4toannexb output.m3u8
# ts转MP4
# input.ts为输入TS文件名，output.mp4为输出的MP4文件名
ffmpeg -i input.ts -c copy -map 0:v -map 0:a -bsf:a aac_adtstoasc output.mp4
ffmpeg -i input.ts -c:v copy -c:a libfaac out.mp4
ffmpeg -i input.ts -c:v libx264 -crf 24 -c:a libfaac out.mp4
# 下载m3u8
ffmpeg -i "http://example.com/chunklist.m3u8" -codec copy file.mp4

# 播放
ffplay name.mp4
```

### EDIT 

I try for another `.m3u8` file on the another server with difference URL:

Download and concat together:

```
ffmpeg -i "concat:\
http://184.72.239.149/vod/smil:BigBuckBunny.smil/media_w442897525_b560000_0.ts|\
http://184.72.239.149/vod/smil:BigBuckBunny.smil/media_w442897525_b560000_1.ts|\
http://184.72.239.149/vod/smil:BigBuckBunny.smil/media_w442897525_b560000_2.ts|\
http://184.72.239.149/vod/smil:BigBuckBunny.smil/media_w442897525_b560000_3.ts|\
http://184.72.239.149/vod/smil:BigBuckBunny.smil/media_w442897525_b560000_4.ts|\
http://184.72.239.149/vod/smil:BigBuckBunny.smil/media_w442897525_b560000_5.ts\
" -c copy -y output.ts
```

Another command with `input.txt` URLs file.

```
ffmpeg -f "concat" -i "input.txt" -c copy -y output.ts
```

input.txt file:

```
file 'http://184.72.239.149/vod/smil:BigBuckBunny.smil/media_w442897525_b560000_0.ts'
file 'http://184.72.239.149/vod/smil:BigBuckBunny.smil/media_w442897525_b560000_1.ts'
file 'http://184.72.239.149/vod/smil:BigBuckBunny.smil/media_w442897525_b560000_2.ts'
file 'http://184.72.239.149/vod/smil:BigBuckBunny.smil/media_w442897525_b560000_3.ts'
file 'http://184.72.239.149/vod/smil:BigBuckBunny.smil/media_w442897525_b560000_4.ts'
file 'http://184.72.239.149/vod/smil:BigBuckBunny.smil/media_w442897525_b560000_5.ts'
```

Or this command some time if needed:

```
ffmpeg -f "concat" -safe "0" -protocol_whitelist "file,http,https,tcp,tls" -i "input.txt" -c copy -y output.ts
```

Finally, for that download speed was good

**解密过程：**

1、下载index.m3u8、key.key、视频流

2、首先安装ffmpeg，并且设置好环境变量

3、将index.m3u8、key.key放入视频流所在的目录，将key.key改名为key.m3u8（因为key不是ffmpeg内置格式，使用key.key会报错）

4、在命令行中，进入视频流所在目录，输入以下命令即可完成解密以及合并的工作，最后会在当前目录下生成完整的输出视频out.mp4

```
ffmpeg -i index.m3u8 out.mp4
```

#### 四、参考

- [https://github.com/FFmpeg/FFmpeg](https://github.com/FFmpeg/FFmpeg)
- [https://ffmpeg.org/ffmpeg.html](https://ffmpeg.org/ffmpeg.html)
- [https://ostechnix.com/20-ffmpeg-commands-beginners/](https://ostechnix.com/20-ffmpeg-commands-beginners/)
- [https://www.ruanyifeng.com/blog/2020/01/ffmpeg.html](https://www.ruanyifeng.com/blog/2020/01/ffmpeg.html)
- [https://self-contained.github.io/FFmpeg/FFmpeg.html](https://self-contained.github.io/FFmpeg/FFmpeg.html)
- [https://www.kancloud.cn/zhenhuamcu/ffmpeg/1034137](https://www.kancloud.cn/zhenhuamcu/ffmpeg/1034137)