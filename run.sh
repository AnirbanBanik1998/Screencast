mkdir Screenshots
mkdir Videos
python3 screenshot.py
cd Screenshots
ffmpeg -framerate 5 -i Screenshot%01d.png -c:v libx264 -profile:v high -crf 20 -pix_fmt yuv420p output.mp4
cd ..
chmod +x move.sh
./move.sh
