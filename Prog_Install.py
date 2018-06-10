# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 18:27:40 2018

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