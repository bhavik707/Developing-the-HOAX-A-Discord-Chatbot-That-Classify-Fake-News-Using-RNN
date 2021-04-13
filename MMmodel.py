import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing.text import Tokenizer

def preprocessing(Fake, True_):
    fake_df = pd.read_csv(Fake)
    real_df = pd.read_csv(True_)
    fake_df.isnull().sum()
    real_df.isnull().sum()
    fake_df.subject.unique()
    real_df.subject.unique()
    fake_df.drop(['date', 'subject'], axis=1, inplace=True)
    real_df.drop(['date', 'subject'], axis=1, inplace=True)
    fake_df['class'] = 0
    real_df['class'] = 1
    print('Difference in news articles:', len(fake_df) - len(real_df))
    news_df = pd.concat([fake_df, real_df], ignore_index=True, sort=False)
    news_df['text'] = news_df['title'] + news_df['text']
    features = news_df['title']
    targets = news_df['class']
    return features, targets

def RNN(max_vocab):
    inputs = tf.keras.Input(name='inputs',shape=[150])
    layer = tf.keras.layers.Embedding(max_vocab,50)(inputs)
    layer = tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(64))(layer)
    layer = tf.keras.layers.Dense(256,name='FC1')(layer)
    layer = tf.keras.layers.Activation('relu')(layer)
    layer = tf.keras.layers.Dropout(0.5)(layer)
    layer = tf.keras.layers.Dense(1)(layer)
    layer = tf.keras.layers.Activation('sigmoid')(layer)
    model = tf.keras.Model(inputs=inputs,outputs=layer)
    return model

def modeling(features, targets):
    X_train, X_test, y_train, y_test = train_test_split(features, targets, test_size=0.2)
    max_vocab = 1000
    tokenizer = Tokenizer(num_words=max_vocab)
    tokenizer.fit_on_texts(X_train)
    X_train = tokenizer.texts_to_sequences(X_train)
    X_test = tokenizer.texts_to_sequences(X_test)
    X_train = tf.keras.preprocessing.sequence.pad_sequences(X_train, maxlen=150)
    X_test = tf.keras.preprocessing.sequence.pad_sequences(X_test, maxlen=150)
    model = RNN(max_vocab)
    model.summary()
    early_stop = tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience=2, restore_best_weights=True)
    model.compile(loss=tf.keras.losses.BinaryCrossentropy(),
                  optimizer=tf.keras.optimizers.Adam(1e-4),
                  metrics=['accuracy'])
    model.fit(X_train, y_train, epochs=10, validation_split=0.1, batch_size=16, shuffle=True,
                        callbacks=[early_stop])
    return model, tokenizer

def input_(model, val, tokenizer):
    text = pd.Series([val])
    text_sequence = tokenizer.texts_to_sequences(text)
    text_sequence_matrix = tf.keras.preprocessing.sequence.pad_sequences(text_sequence, maxlen=150)
    pred = model.predict(text_sequence_matrix)[0][0]
    return pred