# -*- coding: utf-8 -*-
"""

@author: ayush
"""

import tensorflow as tf

x1 = tf.constant(5)
x2 = tf.constant(6)

result = tf.multiply(x1, x2)

print(result)

# by doing the following, dont have to worry about closing the session
with tf.Session() as sess:
    print(sess.run(result))
