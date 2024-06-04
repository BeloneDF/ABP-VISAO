import tensorflow as tf


# Verificar se o TensorFlow detecta a GPU
physical_devices = tf.config.list_physical_devices('GPU')
print("Num GPUs Available: ", len(physical_devices))

# Configurar para limitar a memória da GPU
for gpu in physical_devices:
    tf.config.experimental.set_memory_growth(gpu, True)
