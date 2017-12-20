#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
from tensorflow.contrib.learn.python.learn.metric_spec import MetricSpec

learn = tf.contrib.learn
slim = tf.contrib.slim


def cnn(x, y):
    x = tf.reshape(x, [-1, 28, 28, 1])
    y = slim.one_hot_encoding(y, 10)

    net = slim.conv2d(x, 48, [5, 5], scope='conv1')
    net = slim.max_pool2d(net, [2, 2], scope='pool1')
    net = slim.conv2d(net, 96, [5, 5], scope='conv2')
    net = slim.max_pool2d(net, [2, 2], scope='pool2')
    net = slim.flatten(net, scope='flatten')
    net = slim.fully_connected(net, 512, scope='fully_connected1')
    logits = slim.fully_connected(
            net, 10, activation_fn=None, scope='fully_connected2'
    )

    prob = slim.softmax(logits)
    loss = slim.losses.softmax_cross_entropy(logits, y)
    train_op = slim.optimize_loss(loss,
                                  slim.get_global_step(),
                                  learning_rate=0.001,
                                  optimizer='Adam')

    return {'class': tf.argmax(prob, 1), 'prob': prob}, \
            loss, train_op


if __name__ == '__main__':
    mnist = input_data.read_data_sets('/tmp/minst', one_hot=False)
    train_x = mnist.train.images
    train_y = mnist.train.labels
    test_x = mnist.validation.images
    test_y = mnist.validation.labels

    tf.logging.set_verbosity(tf.logging.INFO)

    validation_metrics = {
            'Accuracy' : MetricSpec(
                metric_fn=tf.contrib.metrics.streaming_accuracy,
                prediction_key='class'
            )
    }

    validation_monitor = learn.monitors.ValidationMonitor(
            test_x,
            test_y,
            metrics=validation_metrics,
            every_n_steps=100
    )

    classfier = learn.Estimator(
            model_fn=cnn,
            model_dir='/tmp/cnn_log',
            config=learn.RunConfig(save_checkpoints_secs=10)
    )

    classfier.fit(x=train_x,
                  y=train_y,
                  steps=3200,
                  batch_size=64,
                  monitors=[validation_monitor]
    )
