import tensorflow as tf

a = tf.constant(5, name='input_a')
b = tf.constant(3, name='input_b')
c = tf.add(a, b)

sess = tf.Session()
output = sess.run(c)

print(output)

writer = tf.train.SummaryWriter('graph', sess.graph)
writer.close()
sess.close()
