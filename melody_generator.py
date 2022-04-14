from glob import glob
from re import S
from turtle import color
import tensorflow as tf
from model.generator import define_generator
import argparse
from colored import fg
from datetime import datetime
from utils.image2midi import image2midi
from utils.image2piano import image2piano
import time
from music21 import instrument

parser = argparse.ArgumentParser(description="Arguments for the melody generation")
parser.add_argument('--instrument', metavar='-i', help='Instrument for which audio output will be generated',
                    default='drum')
parser.add_argument("--sequence", metavar='-s', help='Single duration dpicts ~7 second of playtime', default=1,
                    type=int)
args = parser.parse_args()


def instrument_path(argument):
    switcher = {
        '0': 'weights/final_drum_generator_weights.h5',
        '1': 'weights/real_piano_generator.h5'
    }
    try:
        print(switcher)
        return switcher.get(argument, "weights/real_piano_generator.h5")

    except:
        color = fg('red')
        print(color + f'Error with the instrument current available instrument are {switcher}')


playing_instrument_path = instrument_path(args.instrument)
print(args.instrument)
print(playing_instrument_path)
model = None
IMG_SHAPE = (106, 106, 1)
BATCH_SIZE = 64

# Size of the noise vector
noise_dim = 128


def get_model():
    color = fg('blue')
    print(color + f'Loading model')
    global model
    model = define_generator(noise_dim)
    return model


get_model()
model.load_weights(playing_instrument_path)
color = fg('green')
print(color + f'model loaded')
instrument_to_play = None

try:
    color = fg('blue')
    print(color + f'Generating melody')
    seed = tf.random.normal([args.sequence, 128])
    prediction = model(seed, training=False)
    output = []
    for data in prediction:
        data = (data * 127.5) + 127.5
        output.append(data)
    data = tf.concat(output, axis=1)
    img = tf.keras.preprocessing.image.array_to_img(data)
    now = datetime.now()
    img.save(f'audio.png')
    time.sleep(3)
    if args.instrument =='0':
        image2midi(f'audio.png')
    elif args.instrument == '1':
        image2piano(f'audio.png')
    color = fg('green')
    print(color + f'melody generated with name :- {now}.midi')
except Exception as e:
    print(f"error {e}")
