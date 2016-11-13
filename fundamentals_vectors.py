import tensorflow as tf

a = tf.constant([5, 3], name='input_a')
b = tf.reduce_prod(a, name='prod_b')
c = tf.reduce_sum(a, name='sum_c')
d = tf.add(b, c, name='add_d')

sess = tf.Session()
output = sess.run(d)
print(output)
write = tf.train.SummaryWriter('graph', sess.graph)
write.close()

sess.close()
