"""
训练模型5
BY 李说啥都对
2018.3
"""
import tensorflow as tf
from cfg_5 import MAX_CAPTCHA, CHAR_SET_LEN, save_model, tb_log_path, rand
from cnn_sys_5 import crack_captcha_cnn, Y, keep_prob, X
from data_iter_5 import get_next_batch


def train_crack_captcha_cnn():
    """
    训练模型
    :return:
    """
    output = crack_captcha_cnn()
    with tf.name_scope('Monitor'):
        loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=output, labels=Y))
        # loss = tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(logits=output, labels=Y))
    tf.summary.scalar('Loss', loss)
    # global_step = tf.placeholder(tf.float32)

    global_step = tf.Variable(0, name="global_step")
    learning_rate = tf.train.exponential_decay(0.0001, global_step, 500000, 0.96, staircase=True)  # 生成学习率
    optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate, name="optimizer").minimize(loss, global_step=global_step)

    predict = tf.reshape(output, [-1, MAX_CAPTCHA, CHAR_SET_LEN], name="output")

    max_idx_p = tf.argmax(predict, 2)
    max_idx_l = tf.argmax(tf.reshape(Y, [-1, MAX_CAPTCHA, CHAR_SET_LEN]), 2)
    correct_pred = tf.equal(max_idx_p, max_idx_l)

    with tf.name_scope('Monitor'):
        accuracy = tf.reduce_mean(tf.cast(correct_pred, tf.float32))
    tf.summary.scalar('Accuracy', accuracy)

    saver = tf.train.Saver(max_to_keep=0)

    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        merged = tf.summary.merge_all()
        writer = tf.summary.FileWriter(tb_log_path, sess.graph)

        step = 0

        for epoch in range(6):
            cnt = 0
            while True:
                if cnt == 2264:
                    saver.save(sess, save_model, global_step=step)
                    break
                batch_x, batch_y = get_next_batch(128, rand[cnt])
                for j in range(50):
                    _, lossSize = sess.run([optimizer, loss], feed_dict={X: batch_x, Y: batch_y, keep_prob: 0.8})

                    if step % 10 == 0:
                        lr = sess.run(learning_rate)
                        print("learning_rate: ", lr)
                        print("epoch: " + str(epoch) + "\tcnt: " + str(cnt) + "\tstep: " + str(step) + "\tloss: " + str(lossSize))
                        batch_x_test, batch_y_test = get_next_batch(128, rand[cnt+1])
                        acc = sess.run(accuracy, feed_dict={X: batch_x_test, Y: batch_y_test, keep_prob: 1.})
                        print("Accuracy: " + str(acc))

                        constant_graph = tf.graph_util.convert_variables_to_constants(sess, sess.graph_def, ["output"])
                        with tf.gfile.FastGFile("E:/Users/Dell/PycharmProjects/freeze/out.pb", mode='wb') as f:
                            f.write(constant_graph.SerializeToString())

                        if step % 5000 == 0:
                            saver.save(sess, save_model, global_step=step)
                        if step % 1000 == 0:
                            summary = sess.run(merged, feed_dict={X: batch_x_test, Y: batch_y_test, keep_prob: 1.})
                            writer.add_summary(summary, step)
                    step += 1
                cnt += 1


if __name__ == '__main__':
    train_crack_captcha_cnn()
    print('end')