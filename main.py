from flask import Flask, render_template, request, redirect
import json
import os
from utils import db
import random



print("Current Path: " + os.getcwd())
save_path = os.getcwd() + "\static\clips"
print("Saving Path: " + save_path)


app = Flask(__name__)

@app.route('/')
def index():
    data = db.Db.get_data(self=True)
    videos = []
    if data: 
        for video_id, video_data in data.items():
            videos.append({
                'id': video_id,
                'time': video_data.get('time', ''),
                'title': video_data.get('title', ''),
                'uploader': video_data.get('uploader', ''),
                'url': video_data.get('url', '')
            })
    return render_template('index.html', videos=videos)


@app.route('/upload')
def upload():
    return render_template('upload.html')


@app.route('/submit_clip', methods=['POST'])
def submit_clip():
    # Get data from the POST request
    username = request.form['username']
    title = request.form['title']
    time = request.form['time']
    clip = request.files['clip']

    clip_filename = username + "_" + str(random.randint(1000000, 9000000)) + ".mp4"
    clip.save(clip_filename)

    dbagent = db.Db(uploader=username, title=title, time=time)
    
    
    dbagent.store_vid(vid_path=clip_filename)

    dbagent.uploader()

    return redirect('/')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
 

