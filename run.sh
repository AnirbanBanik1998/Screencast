if ! [ -d Screenshots ]
then
	mkdir Screenshots
fi
if ! [ -d Videos ]
then
	mkdir Videos
fi
python3 screenshot.py $1
cd Screenshots
rate=$(ls -1 | wc -l)
ffmpeg -framerate $rate/$1 -i Screenshot%01d.png -c:v libx264 -profile:v high -crf 20 -pix_fmt yuv420p output.mp4
cd ..
chmod +x move.sh
./move.sh
