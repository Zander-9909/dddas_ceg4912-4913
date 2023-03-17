
import ffmpeg
import os
#stream = ffmpeg.input('test.mp4',r=1)
#stream = ffmpeg.filter(stream, 'fps',fps='1/60')
#stream = ffmpeg.output(stream, './frames/test-%d.jpg',start_number=0)
#stream = ffmpeg.overwrite_output(stream)
#ffmpeg.run(stream)

#try:
#    (ffmpeg.input('test.mp4', r=1)
#        .filter('fps', fps=1)
#        .output('frames/%d.png',
#        start_number=0)
#        .run(capture_stdout=True, capture_stderr=True))
#except ffmpeg.Error as e:
#    print('stdout:', e.stdout.decode('utf8'))
#    print('stderr:', e.stderr.decode('utf8'))

input_file = 'C:/Users/Megan-2/Desktop/inputFolder/input.mp4'
output_dir = 'C:/Users/Megan-2/Desktop/inputFolder/out'

os.makedirs(output_dir, exist_ok=True)

# Set the output image file name format
output_file_format = output_dir + '/%d.png'

# Open the input video file
input_video = ffmpeg.input(input_file)

# Extract one image per second
(
    input_video
    .filter('fps', fps=1)
    .output(output_file_format, format='image2', vcodec='png')
    .run()
)