#pip install pytube
import pytube

link = input("Entrer l'URL de la video Youtube : ")
yt = pytube.YouTube(link)
#yt.streams.first().download()
yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
print(link, 'telecharger avec succes !!!')