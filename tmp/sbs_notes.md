ffmpeg -i udp://239.255.191.255:18212 -c:v copy -c:d copy -map 0:v -map 0:d testCopy.ts

ffmpeg -i testCopy.ts -map 0:d -c copy -f data - | python3 ./klvdata_test.py

ffmpeg -skip_frame nokey -i sbs.ts -map 0:0 -vsync vfr -frame_pts true eo-%02d.jpg
ffmpeg -skip_frame nokey -i sbs.ts -map 0:1 -vsync vfr -frame_pts true ir-%02d.jpg
ffmpeg -skip_frame nokey -i sbs.ts -map 0:2 -vsync vfr -frame_pts true ti-%02d.bin

ffmpeg -skip_frame nokey -i sbs.ts -vsync vfr -frame_pts true -map 0:0 eo-%04d.jpg -map 0:1 -frame_pts true ir-%04d.jpg -map 0:2 -frame_pts true -c copy ti-%04d.jpg

## extract key frame images
ffmpeg -skip_frame nokey -i sbs.ts -vsync vfr -frame_pts true -map 0:0 eo-%04d.jpg -map 0:1 -frame_pts true ir-%04d.jpg

## extract all frame images
ffmpeg -i sbs.ts -map 0:0 eo-%08d.jpg -map 0:1 ir-%08d.jpg -map 0:2 -c copy -f data ti-%08d.bin
