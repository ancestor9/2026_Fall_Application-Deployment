import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from tensorflow import keras
from tensorflow.keras import layers

# 공통 컬러맵 정의
CMAP = LinearSegmentedColormap.from_list("tf_playground", ["#f59322", "#ffffff", "#0877bd"])

def _create_grid_and_features():
    """2차원 좌표 평면과 7가지 입력 특성을 생성하는 내부 함수"""
    grid = np.linspace(-6, 6, 300)
    X1, X2 = np.meshgrid(grid, grid)
    
    features_list = [
        (r"$X_1$",       X1,         6),
        (r"$X_2$",       X2,         6),
        (r"$X_1^2$",     X1**2,      36),
        (r"$X_2^2$",     X2**2,      36),
        (r"$X_1 X_2$",   X1 * X2,    36),
        (r"$\sin(X_1)$", np.sin(X1), 1),
        (r"$\sin(X_2)$", np.sin(X2), 1)
    ]
    
    features_grid = np.stack([item[1] for item in features_list], axis=-1)
    return features_list, features_grid

def plot_inputs():
    """첫 번째 코드: 7가지 입력 특성 시각화"""
    inputs, _ = _create_grid_and_features()
    
    fig, axes = plt.subplots(1, len(inputs), figsize=(14, 2.5))
    for ax, (label, data, v_limit) in zip(axes, inputs):
        ax.imshow(data, cmap=CMAP, origin='lower', vmin=-v_limit, vmax=v_limit)
        ax.set_title(label, fontsize=13, pad=10)
        ax.set_xticks([])
        ax.set_yticks([])
        for spine in ax.spines.values():
            spine.set_edgecolor('black')
            spine.set_linewidth(1.8)
            
    plt.tight_layout()
    plt.show()

def plot_hidden_layers():
    """두 번째 코드: Keras 모델의 은닉층 1, 2 출력 시각화"""
    _, features_grid = _create_grid_and_features()
    X_input = features_grid.reshape(-1, 7)

    # Keras 모델 정의
    inputs = keras.Input(shape=(7,), name="input_features")
    hidden1 = layers.Dense(1, activation="tanh", name="hidden_layer_1")(inputs)
    hidden2 = layers.Dense(1, activation="tanh", name="hidden_layer_2")(hidden1)
    model = keras.Model(inputs=inputs, outputs=hidden2)

    # 가중치 및 편향 설정
    w1 = np.array([[0.8], [-0.3], [0.1], [-0.2], [-0.7], [0.3], [0.2]])
    b1 = np.array([0.1])
    model.get_layer("hidden_layer_1").set_weights([w1, b1])

    w2 = np.array([[0.3]])
    b2 = np.array([0.0])
    model.get_layer("hidden_layer_2").set_weights([w2, b2])

    # 중간층 출력 추출 및 예측
    activation_model = keras.Model(
        inputs=model.input,
        outputs=[
            model.get_layer("hidden_layer_1").output,
            model.get_layer("hidden_layer_2").output
        ]
    )
    h1_out, h2_out = activation_model.predict(X_input, verbose=0)
    h1_img = h1_out.reshape(300, 300)
    h2_img = h2_out.reshape(300, 300)

    # 시각화
    visuals = [
        ("Hidden Layer 1\n(1 Neuron)", h1_img),
        ("Hidden Layer 2\n(1 Neuron)", h2_img)
    ]

    fig, axes = plt.subplots(1, 2, figsize=(6, 3))
    for ax, (title, img) in zip(axes, visuals):
        ax.imshow(img, cmap=CMAP, origin="lower", vmin=-1, vmax=1)
        ax.set_title(title, fontsize=12, pad=10)
        ax.set_xticks([])
        ax.set_yticks([])
        for spine in ax.spines.values():
            spine.set_edgecolor("black")
            spine.set_linewidth(1.8)

    plt.tight_layout()
    plt.show()
