"""
训练模型3
BY 李说啥都对
2018.3
"""
import tensorflow as tf
from cfg_3 import MAX_CAPTCHA, CHAR_SET_LEN, tb_log_path, save_model, rand
from cnn_sys_3 import crack_captcha_cnn, Y, keep_prob, X
from data_iter_3 import get_next_batch


def train_crack_captcha_cnn():
    """
    训练模型
    :return:
    """
    output = crack_captcha_cnn()
    with tf.name_scope('Monitor'):
        # loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=output, labels=Y))
        loss = tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(logits=output, labels=Y))
    tf.summary.scalar('Loss', loss)
    # optimizer 为了加快训练 learning_rate应该开始大，然后慢慢衰
    optimizer = tf.train.AdamOptimizer(learning_rate=0.001).minimize(loss)

    predict = tf.reshape(output, [-1, MAX_CAPTCHA, CHAR_SET_LEN])

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
        for epoch in range(3):
            cnt = 0
            while True:
                if cnt == 125:
                    saver.save(sess, save_model, global_step=step)
                    break
                batch_x, batch_y = get_next_batch(128, rand[cnt])
                for j in range(100):
                    _, lossSize = sess.run([optimizer, loss], feed_dict={X: batch_x, Y: batch_y, keep_prob: 0.8})

                    if step % 5 == 0:
                        print("epoch: " + str(epoch) + "\tcnt: " + str(cnt) + "\tstep: " + str(step) + "\tloss: " + str(lossSize))
                        batch_x_test, batch_y_test = batch_x, batch_y
                        acc = sess.run(accuracy, feed_dict={X: batch_x_test, Y: batch_y_test, keep_prob: 1.0})
                        print("Accuracy: " + str(acc))
                    if step % 2000 == 0:
                        saver.save(sess, save_model, global_step=step)
                    if step % 100 == 0:
                        summary = sess.run(merged, feed_dict={X: batch_x_test, Y: batch_y_test, keep_prob: 1.})
                        writer.add_summary(summary, step)
                    step += 1
                cnt += 1


if __name__ == '__main__':
    train_crack_captcha_cnn()
    print('end')
    pass