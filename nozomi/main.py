from pathlib import Path, PurePath, PurePosixPath
from nozomi import api
import os
import keyboard

# The tags that the posts retrieved must contain
positive_tags = ['kidmo']

# Gets all posts with the tags 'veigar', 'wallpaper'
downloadNum = 0
downloadLimit = 100
downloadDir="nozomi_Download/"
for i in range(len(positive_tags)):
    if(i>0):
        downloadDir+="_"
    downloadDir+=positive_tags[i]
downloadDir="/"+downloadDir
currentDir=Path(str(Path.cwd())+"/"+downloadDir)
print(currentDir)

if(api.get_post_nums(positive_tags)<downloadLimit):
    downloadLimit=downloadLimit=api.get_post_nums(positive_tags)
for post in api.get_posts(positive_tags):
    downloadNum+=1
    api.download_media(post, currentDir)
    print(f"{downloadNum} files out of {downloadLimit} downloaded")
    if downloadNum==downloadLimit or keyboard.is_pressed('`'):
        break;
