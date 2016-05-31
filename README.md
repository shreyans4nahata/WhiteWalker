# WhiteWalker
Repository for youtube song listing and  downloading!!
#  Usage:

  1) Terminal Download:
    <br>
    ```
    cd WhiteWalker/
    ```
    <br>
    ```
    pip3 install -r requirements.txt
    ```
    <br>
    ```
    python3 audio_dwnld.py
    ```
    <br>
    Enter the song name. The file downloads in the current working directory.
    <br>
  2) Deploy Server: 
     <br>
    ``` cd WhiteWalker/mytest/```
    <br>
    ```    python3 manage.py runserver 0.0.0.0:3000```
    <br>
    The Server is started on port 3000.
    <br>
  3) Use Extension:
    <br>
    For Chrome( Similar for others ):
    <br>
    -> Open the extensions control from settings menu.
    <br>
    -> Click on the 'Load Unpacked Extensions...' button.
    <br>
    -> Choose the chrome-ext folder.
    <br>
    It adds the song-dl extension. Use it to download your audio files. 
    <br>
    <b>Currently the extension requires local server to be deployed first.</b>
    
# Features:
  1. Listing of billboard UK top 40  songs.
  2. Download of the Audio or Video of any song or video on youtube.
  3. Chrome extension for downloading audio.
  4. Download from terminal using the script.
