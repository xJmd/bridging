import firebase_admin
from firebase_admin import db,credentials
from firebase_admin import storage
import random

cred = credentials.Certificate('bridgify-2b152-firebase-adminsdk-gym6u-cc34e5430e.json')
firebase_admin.initialize_app(cred, {'databaseURL': 'https://bridgify-2b152-default-rtdb.europe-west1.firebasedatabase.app/','storageBucket': 'bridgify-2b152.appspot.com'})



class Db():


    def __init__(self, uploader, time, title):
    
        self.data_to_push = {
            "title": title,
            "uploader": uploader,
            "time": time
        }
    
    
    def uploader(self):

        dirpath = "/" + str(random.randint(100000000, 900000000))
        new_data_path = db.reference(dirpath)
        new_data_path.set(self.data_to_push)


    def store_vid(self, vid_path):

        bucket = storage.bucket()       
        local_file_path = f"{vid_path}"
        destination_blob_name = f'videos/{vid_path}'
        blob = bucket.blob(destination_blob_name)
        blob.upload_from_filename(local_file_path)
        blob.make_public()      
        # Generate public URL for the video
        self.data_to_push["url"] = blob.public_url        


    def get_data(self):
        ref = db.reference('/')

        return ref.get()