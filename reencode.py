import ffmpeg
import os
import glob
from tqdm import tqdm  # Importa la libreria per la barra di progressione

def reencode_videos():
    videos = glob.glob('./*.*')  # aggiungi i formati video desiderati se necessario
    total_videos = len(videos)
    processed_videos = 0

    for video in tqdm(videos, desc="Ricodifica", ncols=100):
        if not video.endswith('_reencoded.mp4'):
            output_file = video.rsplit('.', 1)[0] + '_reencoded.mp4'
            try:
                ffmpeg.input(video).output(
                    output_file,
                    vcodec='libx264',
                    an=True,  # Questa opzione rimuove l'audio
                    vf='fps=24',  # Cambia il framerate a 24 fps senza modificare la velocità di riproduzione
                    format='mp4',
                    loglevel='error'  # Mostra solo gli errori di ffmpeg
                ).run(overwrite_output=True)
                os.remove(video)  # Rimuovi il file sorgente dopo la ricodifica
                processed_videos += 1

                # Calcola e stampa la percentuale di completamento
                percent_complete = (processed_videos / total_videos) * 100
                remaining_videos = total_videos - processed_videos
                print(f"\r{remaining_videos}/{total_videos} - {percent_complete:.2f}% completato", end="")
            except ffmpeg.Error as e:
                print(f"Errore nella ricodifica del video {video}: {e}")

# Chiamata alla funzione
reencode_videos()
