
from tensorflow.keras.applications import VGG16
from tensorflow.keras.layers import Input, Conv2D, MaxPooling2D, UpSampling2D, concatenate
from tensorflow.keras.models import Model

def unet_vgg16(input_shape=(256, 256, 3)):
    vgg16 = VGG16(include_top=False, weights='imagenet', input_shape=input_shape)

    for layer in vgg16.layers:
        layer.trainable = False

    inputs = Input(shape=input_shape)

    c1 = vgg16.get_layer('block1_conv2').output
    p1 = vgg16.get_layer('block1_pool').output

    c2 = vgg16.get_layer('block2_conv2').output
    p2 = vgg16.get_layer('block2_pool').output

    c3 = vgg16.get_layer('block3_conv3').output
    p3 = vgg16.get_layer('block3_pool').output

    c4 = vgg16.get_layer('block4_conv3').output
    p4 = vgg16.get_layer('block4_pool').output

    c5 = vgg16.get_layer('block5_conv3').output

    u6 = UpSampling2D()(c5)
    u6 = concatenate([u6, c4])
    c6 = Conv2D(512, (3, 3), activation='relu', padding='same')(u6)

    u7 = UpSampling2D()(c6)
    u7 = concatenate([u7, c3])
    c7 = Conv2D(256, (3, 3), activation='relu', padding='same')(u7)

    u8 = UpSampling2D()(c7)
    u8 = concatenate([u8, c2])
    c8 = Conv2D(128, (3, 3), activation='relu', padding='same')(u8)

    u9 = UpSampling2D()(c8)
    u9 = concatenate([u9, c1])
    c9 = Conv2D(64, (3, 3), activation='relu', padding='same')(u9)

    outputs = Conv2D(1, (1, 1), activation='sigmoid')(c9)

    model = Model(inputs=vgg16.input, outputs=outputs)

    return model

if __name__ == "__main__":
    model = unet_vgg16()
    model.summary()
