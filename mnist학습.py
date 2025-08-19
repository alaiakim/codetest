import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

# Load dataset
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

num_classes = 10
#  MNIST: 28x28 흑백 손글씨 숫자 이미지 (0~9)
#  학습 데이터 60,000개, 테스트 데이터 10,000개

# Normalize the images
# Divide every pixel by 255 scaling the range down to [0,1]
x_train = x_train.astype("float32") / 255.0
x_test = x_test.astype("float32") / 255.0

# Add a channel dimension to indicate they are grayscale
# CNN이 요구하는 채널 차원 추가 (흑백이라 채널 1개. RGB 모두 사용하면 채널 3개)
x_train = np.expand_dims(x_train, -1)
x_test = np.expand_dims(x_test, -1)

# One-hot encode the labels
# 정수 라벨 → one-hot 인코딩 
# to_categorical 이라는 함수를 사용. onehot 벡터로 만들기 위함
# 예를들어, 5 -> [0,0,0,0,0,1,0,0,0,0] 0 -> [1,0,0,0,0,0,0,0,0,0]
y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)

# Building the model (Sequential CNN)
model = keras.Sequential([
    keras.Input(shape=(28, 28, 1)),
    keras.layers.Conv2D(32, kernel_size=(3, 3), activation="relu"),     # 3x3 짜리 필터 32개, ReLU로 비선형성 도입(음수는 0으로, 양수는 유지)
    keras.layers.MaxPooling2D(pool_size=(2, 2)),        # 다운샘플링 (2x2 영역에서 가장 큰 값만 남김)
    keras.layers.Conv2D(64, kernel_size=(3, 3), activation="relu"),     # 더 깊고 추상적인 특징 추출 (숫자 형태 구조 등) 
    keras.layers.MaxPooling2D(pool_size=(2, 2)),        # 다운샘플링
    keras.layers.Flatten(),         # 5x5x64의 1D 벡터로 펼침
    keras.layers.Dense(128, activation="relu"),         # 완전 연결 레이어 (fully connected layer), 학습된 특징을 종합해 클래스 구분을 위한 고차원 표현 생성
    keras.layers.Dense(num_classes, activation="softmax")       # 최종 출력층. 10개의 뉴런:각 숫자에 대한 확률분포. softmax:전체 출력이 1로 정규화됨
])

# Compiling the model
model.compile(optimizer='adam',     # 학습률 자동 조정, 모멘텀
              loss='categorical_crossentropy',      # 다중 클래스 분류용 손실 함수
              metrics=['accuracy'])         # 분류 정확도 지표 사용

# Training the model            순전파 역전파 계산을 fit 이 다 해줌
history = model.fit(x_train, y_train, 
                    batch_size=128, 
                    epochs=10, 
                    validation_split=0.1)       # 전체 학습데이터 중 10%는 검증용

# Performance evaluation
score = model.evaluate(x_test, y_test, verbose=0)
print(f"\nTest loss: {score[0]:.4f}")
print(f"Test accuracy: {score[1]:.4f}")


# --- Visualization Code using Matplotlib ---


# Plot training & validation accuracy values
plt.figure(figsize=(12, 4))
plt.subplot(1, 2, 1)
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('Model Accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train', 'Validation'], loc='upper left')

# Plot training & validation loss values
plt.subplot(1, 2, 2)
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Model Loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Validation'], loc='upper left')

# Display the plots
plt.show()
