# **Melody Generator** 
A project indulged with generating ear soothing sounds using artificial neural network.
This project generated sounds on based of user request with various different instrument 
.
## Theory
The model is based on image generation using W-GAN but instead of using real images we use a binary representation of beats, 
and stop duration on an image and use our W-gan to generate that bit image, and then we transfer that image back to original beats, Notes and chords

## How to use it?
1. `pip install -r requirements.txt`
2. once setup is done you need to download models for each instrument and place it under weights folder 
   [DRUM](https://mega.nz/file/7TInBQQD#JpBXmewAPBPe_045azE3F_ekUViVvRzy-a6Kaf-KVxQ) ,[PIANO](https://mega.nz/file/ua4ijLqb#5VcdjS1h3P75RZQvUhov9zGzMLfgx96TgGaERzcrOfU)
3. Currently this script is able to render 2 different instrument i.e. Piano and Drum {0 for drum,1 for piano}
4. Demo command to get user started `python melody_generator.py --instrument 0 --sequence 3`
5. After running the above command you will get two output one bit image and second midi file play it and enjoy <:)

## Update List(13/03/2022):-
Drum model weights updated in drive 
//TODO train model on more instruments
## Update List(14/04/2022):-
Piano model weights updated in drive
//TODO train model on more instruments