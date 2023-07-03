```python
import os
import subprocess
from modeltrackr.models import Recording

class RecordingService:
    def __init__(self, db):
        self.db = db

    def start_recording(self, model):
        recording = Recording(model_id=model.id, status='recording')
        self.db.session.add(recording)
        self.db.session.commit()

        # Start recording process
        subprocess.Popen(['ffmpeg', '-i', model.stream_url, '-c', 'copy', os.path.join('recordings', f'{recording.id}.mp4')])

        return recording

    def end_recording(self, recording):
        recording.status = 'ended'
        self.db.session.commit()

        # End recording process
        subprocess.Popen(['killall', 'ffmpeg'])

    def get_recordings(self, user):
        return Recording.query.filter_by(user_id=user.id).all()
```