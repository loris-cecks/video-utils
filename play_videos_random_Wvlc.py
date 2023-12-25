import os
import random
import subprocess
import threading
import shutil
import sys

def create_playlist(video_files):
    playlist_file_path = 'playlist.m3u'
    with open(playlist_file_path, 'w', encoding='utf-8') as file:
        for video_file in video_files:
            # Converte i percorsi relativi in percorsi assoluti
            absolute_path = os.path.abspath(video_file)
            file.write(absolute_path + '\n')
    return playlist_file_path

def create_exe():
    # Costruisci il comando per PyInstaller solo se lo script è eseguito come script e non come .exe
    script_name = os.path.basename(sys.argv[0])  # Usa sys.argv[0] invece di __file__
    if script_name.endswith('.py'):  # Controlla se lo script è eseguito come script Python
        command = f"pyinstaller --onefile --distpath . {script_name}"
        # Esegui PyInstaller
        subprocess.run(command, shell=True)
    
    # Elimina la cartella build e il file .spec
    shutil.rmtree('build', ignore_errors=True)
    spec_file = os.path.splitext(script_name)[0] + '.spec'  # Usa script_name invece di __file__
    if os.path.exists(spec_file):
        os.remove(spec_file)

    # Chiudi la finestra del terminale
    exit()

def main():
    pass  # La funzione main è ora vuota

if __name__ == "__main__":
    # Questo codice verrà eseguito ogni volta che esegui il file .exe
    current_dir = os.getcwd()  # Ottiene la directory corrente
    video_files = []
    for root_dir, sub_dirs, files in os.walk(current_dir):
        for file in files:
            if file.endswith(('.mp4', '.avi', '.mkv', '.mov')):  # Aggiungi altri formati video se necessario
                video_files.append(os.path.join(root_dir, file))
    random.shuffle(video_files)  # Mescola l'ordine dei video in modo casuale
    playlist_file_path = create_playlist(video_files)
    
    # Apri VLC con la nuova playlist in modalità schermo intero e volume al minimo
    subprocess.Popen(['C:\\Program Files (x86)\\VideoLAN\\VLC\\vlc.exe', playlist_file_path, '--fullscreen', '--volume', '0'])

    # Avvia un nuovo thread per creare l'eseguibile mentre VLC è in esecuzione
    exe_thread = threading.Thread(target=create_exe)
    exe_thread.start()
