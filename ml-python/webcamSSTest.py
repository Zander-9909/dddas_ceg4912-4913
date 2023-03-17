import ffmpeg


stream = ffmpeg.input('Integrated Webcam', framerate=30,ss = 0, r = 0.5)
stream = ffmpeg.filter(stream,'fps', fps = '1/30')
#stream = ffmpeg.output(stream,'testSS-%d.jpg',start_number=0)
ffmpeg.run(stream)