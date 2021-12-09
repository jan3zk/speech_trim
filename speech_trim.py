# -*- coding: utf-8 -*-
print('Nalaganje programskih knjižnic ...')
from glob import glob
import os
import argparse
import soundfile as sf
import numpy as np
from pydub import AudioSegment,silence
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


ap = argparse.ArgumentParser(description = 
'Skripta za prirez začetnih in končnih premorov v govornih datotekah tipa WAW.')
ap._action_groups.pop()
required = ap.add_argument_group('required arguments')
optional = ap.add_argument_group('optional arguments')
required.add_argument('-i',
  type = str,
  help = 'Vhodna datoteka ali direktorij s posnetki WAV.')
required.add_argument('-o',
  type = str,
  help = 'Izhodna datoteka ali direktorij s posnetki WAV.')
optional.add_argument('-v', 
  action='store_true',
  help = 'Argument s katerim vključimo izpis na konzolo.')
optional.add_argument('-p', 
  type=float,
  default=0.8,
  help = 'Dolžina premora v sekundah.')
optional.add_argument('-t', 
  type=int,
  default=-34,
  help = 'Prag tišine v dbFS.')
optional.add_argument('-c', 
  type=int,
  default=75,
  help = 'Odsek procesiranja v ms.')
args = ap.parse_args()

if os.path.isfile(args.i):
  in_wavs = [args.i]
else:
  in_wavs = glob(os.path.join(args.i, '*.wav'))

print('\nPrirez zvočnih posnetkov:\n')
for wav in in_wavs:
  print('\nVhodni posnetek: %s'%wav)

  speech = AudioSegment.from_file(wav)
  t_ini_v = silence.detect_leading_silence(speech, silence_threshold=args.t, chunk_size=args.c)
  t_ini = t_ini_v/1000
  t_fin_v = silence.detect_leading_silence(speech.reverse(), silence_threshold=args.t, chunk_size=args.c)
  t_fin = t_fin_v/1000

  if os.path.isfile(args.o):
    out_path = args.o
  else:
    out_path = os.path.join(args.o,os.path.basename(wav))
  print('Prirezani posnetek: %s'%out_path)
  
  data, rate = sf.read(wav)
  t_end = len(data)/rate
  leading_trim = t_ini-args.p if t_ini-args.p > 0 else 0
  trailing_trim = t_fin-args.p if t_fin-args.p > 0 else 0
  sf.write(out_path, data[int((leading_trim)*rate):int((t_end-trailing_trim)*rate)], rate)
  
  print('Ocenjen začetni premor: %.1f'%t_ini)
  print('Ocenjen končni premor: %.1f'%t_fin)
  print('Dolžina začetnega obreza: %.1f s'%leading_trim)
  print('Dolžina končnega obreza: %.1f s'%trailing_trim)
  if t_ini < 0.5: print('\tPOZOR: Premajhen začetni premor.')
  if t_fin < 0.5: print('\tPOZOR: Premajhen končni premor.')
  
  if args.v:
    fig, ax = plt.subplots()
    plt.plot( np.linspace(0,t_ini,len(data[:int(t_ini*rate)])),
      data[:int(t_ini*rate)], 'r')
    plt.plot( np.linspace(t_ini,t_end-t_fin,
      len(data[int(t_ini*rate):int((t_end-t_fin)*rate)])),
      data[int(t_ini*rate):int((t_end-t_fin)*rate)], 'g')
    plt.plot( np.linspace(t_end-t_fin,t_end,
      len(data[int((t_end-t_fin)*rate):])),
      data[int((t_end-t_fin)*rate):], 'r')
    plt.axvspan(0, .5, facecolor='r', alpha=.3)
    plt.axvspan(t_end, t_end-.5, facecolor='r', alpha=.3)
    plt.axvspan(1, t_end-1, facecolor='g', alpha=.3)
    plt.axhline(y=.5, color='k', linestyle='--')
    plt.axhline(y=-.5, color='k', linestyle='--')
    plt.ylim([-1, 1])
    plt.xlim(0,t_end)
    plt.xlabel('Čas [s]')
    plt.ylabel('Amplituda')
    ax.set_title('Začetni premor: %.2f s, končni premor: %.2f s'%(t_ini, t_fin))
    plt.show()
 
