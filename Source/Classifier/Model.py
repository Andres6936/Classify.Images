import numpy as np
import tensorflow as tf
import tensorflow_hub as hub

from typing import AnyStr

from Source.Classifier.LoaderImage import load_image, show_image

model_handle_map = {
    "efficientnetv2-s": "https://tfhub.dev/google/imagenet/efficientnet_v2_imagenet1k_s/classification/2",
    "efficientnetv2-m": "https://tfhub.dev/google/imagenet/efficientnet_v2_imagenet1k_m/classification/2",
    "efficientnetv2-l": "https://tfhub.dev/google/imagenet/efficientnet_v2_imagenet1k_l/classification/2",
    "efficientnetv2-s-21k": "https://tfhub.dev/google/imagenet/efficientnet_v2_imagenet21k_s/classification/2",
    "efficientnetv2-m-21k": "https://tfhub.dev/google/imagenet/efficientnet_v2_imagenet21k_m/classification/2",
    "efficientnetv2-l-21k": "https://tfhub.dev/google/imagenet/efficientnet_v2_imagenet21k_l/classification/2",
    "efficientnetv2-xl-21k": "https://tfhub.dev/google/imagenet/efficientnet_v2_imagenet21k_xl/classification/2",
    "efficientnetv2-b0-21k": "https://tfhub.dev/google/imagenet/efficientnet_v2_imagenet21k_b0/classification/2",
    "efficientnetv2-b1-21k": "https://tfhub.dev/google/imagenet/efficientnet_v2_imagenet21k_b1/classification/2",
    "efficientnetv2-b2-21k": "https://tfhub.dev/google/imagenet/efficientnet_v2_imagenet21k_b2/classification/2",
    "efficientnetv2-b3-21k": "https://tfhub.dev/google/imagenet/efficientnet_v2_imagenet21k_b3/classification/2",
    "efficientnetv2-s-21k-ft1k": "https://tfhub.dev/google/imagenet/efficientnet_v2_imagenet21k_ft1k_s/classification/2",
    "efficientnetv2-m-21k-ft1k": "https://tfhub.dev/google/imagenet/efficientnet_v2_imagenet21k_ft1k_m/classification/2",
    "efficientnetv2-l-21k-ft1k": "https://tfhub.dev/google/imagenet/efficientnet_v2_imagenet21k_ft1k_l/classification/2",
    "efficientnetv2-xl-21k-ft1k": "https://tfhub.dev/google/imagenet/efficientnet_v2_imagenet21k_ft1k_xl/classification/2",
    "efficientnetv2-b0-21k-ft1k": "https://tfhub.dev/google/imagenet/efficientnet_v2_imagenet21k_ft1k_b0/classification/2",
    "efficientnetv2-b1-21k-ft1k": "https://tfhub.dev/google/imagenet/efficientnet_v2_imagenet21k_ft1k_b1/classification/2",
    "efficientnetv2-b2-21k-ft1k": "https://tfhub.dev/google/imagenet/efficientnet_v2_imagenet21k_ft1k_b2/classification/2",
    "efficientnetv2-b3-21k-ft1k": "https://tfhub.dev/google/imagenet/efficientnet_v2_imagenet21k_ft1k_b3/classification/2",
    "efficientnetv2-b0": "https://tfhub.dev/google/imagenet/efficientnet_v2_imagenet1k_b0/classification/2",
    "efficientnetv2-b1": "https://tfhub.dev/google/imagenet/efficientnet_v2_imagenet1k_b1/classification/2",
    "efficientnetv2-b2": "https://tfhub.dev/google/imagenet/efficientnet_v2_imagenet1k_b2/classification/2",
    "efficientnetv2-b3": "https://tfhub.dev/google/imagenet/efficientnet_v2_imagenet1k_b3/classification/2",
    "efficientnet_b0": "https://tfhub.dev/tensorflow/efficientnet/b0/classification/1",
    "efficientnet_b1": "https://tfhub.dev/tensorflow/efficientnet/b1/classification/1",
    "efficientnet_b2": "https://tfhub.dev/tensorflow/efficientnet/b2/classification/1",
    "efficientnet_b3": "https://tfhub.dev/tensorflow/efficientnet/b3/classification/1",
    "efficientnet_b4": "https://tfhub.dev/tensorflow/efficientnet/b4/classification/1",
    "efficientnet_b5": "https://tfhub.dev/tensorflow/efficientnet/b5/classification/1",
    "efficientnet_b6": "https://tfhub.dev/tensorflow/efficientnet/b6/classification/1",
    "efficientnet_b7": "https://tfhub.dev/tensorflow/efficientnet/b7/classification/1",
    "bit_s-r50x1": "https://tfhub.dev/google/bit/s-r50x1/ilsvrc2012_classification/1",
    "inception_v3": "https://tfhub.dev/google/imagenet/inception_v3/classification/4",
    "inception_resnet_v2": "https://tfhub.dev/google/imagenet/inception_resnet_v2/classification/4",
    "resnet_v1_50": "https://tfhub.dev/google/imagenet/resnet_v1_50/classification/4",
    "resnet_v1_101": "https://tfhub.dev/google/imagenet/resnet_v1_101/classification/4",
    "resnet_v1_152": "https://tfhub.dev/google/imagenet/resnet_v1_152/classification/4",
    "resnet_v2_50": "https://tfhub.dev/google/imagenet/resnet_v2_50/classification/4",
    "resnet_v2_101": "https://tfhub.dev/google/imagenet/resnet_v2_101/classification/4",
    "resnet_v2_152": "https://tfhub.dev/google/imagenet/resnet_v2_152/classification/4",
    "nasnet_large": "https://tfhub.dev/google/imagenet/nasnet_large/classification/4",
    "nasnet_mobile": "https://tfhub.dev/google/imagenet/nasnet_mobile/classification/4",
    "pnasnet_large": "https://tfhub.dev/google/imagenet/pnasnet_large/classification/4",
    "mobilenet_v2_100_224": "https://tfhub.dev/google/imagenet/mobilenet_v2_100_224/classification/4",
    "mobilenet_v2_130_224": "https://tfhub.dev/google/imagenet/mobilenet_v2_130_224/classification/4",
    "mobilenet_v2_140_224": "https://tfhub.dev/google/imagenet/mobilenet_v2_140_224/classification/4",
    "mobilenet_v3_small_100_224": "https://tfhub.dev/google/imagenet/mobilenet_v3_small_100_224/classification/5",
    "mobilenet_v3_small_075_224": "https://tfhub.dev/google/imagenet/mobilenet_v3_small_075_224/classification/5",
    "mobilenet_v3_large_100_224": "https://tfhub.dev/google/imagenet/mobilenet_v3_large_100_224/classification/5",
    "mobilenet_v3_large_075_224": "https://tfhub.dev/google/imagenet/mobilenet_v3_large_075_224/classification/5",
}

model_image_size_map = {
    "efficientnetv2-s": 384,
    "efficientnetv2-m": 480,
    "efficientnetv2-l": 480,
    "efficientnetv2-b0": 224,
    "efficientnetv2-b1": 240,
    "efficientnetv2-b2": 260,
    "efficientnetv2-b3": 300,
    "efficientnetv2-s-21k": 384,
    "efficientnetv2-m-21k": 480,
    "efficientnetv2-l-21k": 480,
    "efficientnetv2-xl-21k": 512,
    "efficientnetv2-b0-21k": 224,
    "efficientnetv2-b1-21k": 240,
    "efficientnetv2-b2-21k": 260,
    "efficientnetv2-b3-21k": 300,
    "efficientnetv2-s-21k-ft1k": 384,
    "efficientnetv2-m-21k-ft1k": 480,
    "efficientnetv2-l-21k-ft1k": 480,
    "efficientnetv2-xl-21k-ft1k": 512,
    "efficientnetv2-b0-21k-ft1k": 224,
    "efficientnetv2-b1-21k-ft1k": 240,
    "efficientnetv2-b2-21k-ft1k": 260,
    "efficientnetv2-b3-21k-ft1k": 300,
    "efficientnet_b0": 224,
    "efficientnet_b1": 240,
    "efficientnet_b2": 260,
    "efficientnet_b3": 300,
    "efficientnet_b4": 380,
    "efficientnet_b5": 456,
    "efficientnet_b6": 528,
    "efficientnet_b7": 600,
    "inception_v3": 299,
    "inception_resnet_v2": 299,
    "mobilenet_v2_100_224": 224,
    "mobilenet_v2_130_224": 224,
    "mobilenet_v2_140_224": 224,
    "nasnet_large": 331,
    "nasnet_mobile": 224,
    "pnasnet_large": 331,
    "resnet_v1_50": 224,
    "resnet_v1_101": 224,
    "resnet_v1_152": 224,
    "resnet_v2_50": 224,
    "resnet_v2_101": 224,
    "resnet_v2_152": 224,
    "mobilenet_v3_small_100_224": 224,
    "mobilenet_v3_small_075_224": 224,
    "mobilenet_v3_large_100_224": 224,
    "mobilenet_v3_large_075_224": 224,
}


class Classifier:
    def __init__(self):
        labels_file = "https://storage.googleapis.com/bit_models/imagenet21k_wordnet_lemmas.txt"
        # download labels and creates a maps
        self.downloaded_file = tf.keras.utils.get_file("labels.txt", origin=labels_file)
        self.classes = []

        with open(self.downloaded_file) as file:
            labels = file.readlines()
            self.classes = [line.strip() for line in labels]

        self.image_size = 224
        self.dynamic_size = False

        model_name = "efficientnetv2-l-21k"  # @param ['efficientnetv2-s', 'efficientnetv2-m', 'efficientnetv2-l', 'efficientnetv2-s-21k', 'efficientnetv2-m-21k', 'efficientnetv2-l-21k', 'efficientnetv2-xl-21k', 'efficientnetv2-b0-21k', 'efficientnetv2-b1-21k', 'efficientnetv2-b2-21k', 'efficientnetv2-b3-21k', 'efficientnetv2-s-21k-ft1k', 'efficientnetv2-m-21k-ft1k', 'efficientnetv2-l-21k-ft1k', 'efficientnetv2-xl-21k-ft1k', 'efficientnetv2-b0-21k-ft1k', 'efficientnetv2-b1-21k-ft1k', 'efficientnetv2-b2-21k-ft1k', 'efficientnetv2-b3-21k-ft1k', 'efficientnetv2-b0', 'efficientnetv2-b1', 'efficientnetv2-b2', 'efficientnetv2-b3', 'efficientnet_b0', 'efficientnet_b1', 'efficientnet_b2', 'efficientnet_b3', 'efficientnet_b4', 'efficientnet_b5', 'efficientnet_b6', 'efficientnet_b7', 'bit_s-r50x1', 'inception_v3', 'inception_resnet_v2', 'resnet_v1_50', 'resnet_v1_101', 'resnet_v1_152', 'resnet_v2_50', 'resnet_v2_101', 'resnet_v2_152', 'nasnet_large', 'nasnet_mobile', 'pnasnet_large', 'mobilenet_v2_100_224', 'mobilenet_v2_130_224', 'mobilenet_v2_140_224', 'mobilenet_v3_small_100_224', 'mobilenet_v3_small_075_224', 'mobilenet_v3_large_100_224', 'mobilenet_v3_large_075_224']
        model_handle = model_handle_map[model_name]

        self.max_dynamic_size = 512
        if model_name in model_image_size_map:
            self.image_size = model_image_size_map[model_name]
            self.dynamic_size = False
            print(f"Images will be converted to {self.image_size}x{self.image_size}")
        else:
            self.dynamic_size = True
            print(f"Images will be capped to a max size of {self.max_dynamic_size}x{self.max_dynamic_size}")

        self.classifier = hub.load(model_handle)

    def ClassifyImage(self, pathImage: AnyStr) -> dict[AnyStr, float]:
        image, original_image = load_image(pathImage, self.image_size, self.dynamic_size, self.max_dynamic_size)
        # Run model on image
        probabilities = tf.nn.softmax(self.classifier(image)).numpy()
        top_5 = tf.argsort(probabilities, axis=-1, direction="DESCENDING")[0][:5].numpy()

        for i, item in enumerate(top_5):
            class_index = item
            return {'Label': self.classes[class_index], 'Probability': probabilities[0][top_5][i]}
