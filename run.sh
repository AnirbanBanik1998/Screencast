mkdir Screenshots
mkdir Videos
python3 screencast.py
cd Screenshots
ffmpeg -framerate 2 -i Screenshot%01d.png -c:v libx264 -profile:v high -crf 20 -pix_fmt yuv420p output.mp4
cd ..
chmod +x move.sh
./move.sh
