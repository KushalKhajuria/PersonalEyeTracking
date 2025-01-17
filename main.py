import os
import django
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'django_files')))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eyetracking.settings')
django.setup()

from backend.video import Video

def main():
    # pass
    vid = Video()
    vid.runVideo()

if __name__ == "__main__":
    main()
