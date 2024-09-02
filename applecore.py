import pickle
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np
import pandas as pd
from dataset import dataset
import tensorflow as tf
import actions

ds = pd.DataFrame(dataset)

text = ""

with open("build.log") as log:
    text = log.read()

with open('tokenizer.pkl', 'rb') as file:
    tokenizer = pickle.load(file)
model = tf.keras.models.load_model('applecore.h5')
log_sequences = tokenizer.texts_to_sequences([text])
action_ = ds.loc[np.argmax(model.predict(pad_sequences(log_sequences, maxlen=1000, padding="post")))]["resolution"]
# ends here

action = getattr(actions, action_)
print(action(text))