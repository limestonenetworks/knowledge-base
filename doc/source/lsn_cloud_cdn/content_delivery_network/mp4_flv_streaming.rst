What is MP4/FLV Streaming?
==========================

**Format Recommendation**

Most of the players do not support MPEG-4 encode, you are advised to use h264
videos.

**Start-End Parameter**

By default, videos will play at the beginning and play through till the end,
however, you can customize that through the URL.

MP4 pseudo streaming’s “start” and “end” are in seconds unit. For example, you
could use the URL:

http://example.com/something.mp4?start=12.34&end=55.66 (12.34, 55.66 in
seconds)

FLV pseudo streaming’s “start” is in bytes unit (no “end” for FLV pseudo
streaming). For example:

http://example.com/something.flv?start=1200
