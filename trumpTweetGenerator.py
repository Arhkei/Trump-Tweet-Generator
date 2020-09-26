import time
import os
from win32com.client import Dispatch
speak = Dispatch("SAPI.SpVoice")
#start_time = time.time()
#import os
#os.environ["KERAS_BACKEND"] = "plaidml.keras.backend"
#import keras
#print("Using " + keras.backend.backend() + " backend")

from textgenrnn import textgenrnn
#t = textgenrnn()
t = textgenrnn(weights_path='trump.hdf5')
#t.train_from_file('tweets.txt', num_epochs=10, batch_size=100)
#print("--- %s seconds ---" % (time.time() - start_time))
tweet = t.generate(5, temperature=0.5, return_as_list=True)
os.system('cls')
for text in range(len(tweet)):
	print(str(text+1) + ": " + tweet[text] + "\n\n")
	#speak.Speak(str(tweet[text]))