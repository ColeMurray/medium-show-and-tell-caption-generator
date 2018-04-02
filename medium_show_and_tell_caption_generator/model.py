import logging
import os

import tensorflow as tf


class ShowAndTellModel(object):
    def __init__(self, model_path):
        self._model_path = model_path
        self.logger = logging.getLogger(__name__)

        self._load_model(model_path)
        self._sess = tf.Session(graph=tf.get_default_graph())

    def _load_model(self, frozen_graph_path):
        """
        Loads a frozen graph
        :param frozen_graph_path: path to .pb graph
        :type frozen_graph_path: str
        """

        model_exp = os.path.expanduser(frozen_graph_path)
        if os.path.isfile(model_exp):
            self.logger.info('Loading model filename: %s' % model_exp)
            with tf.gfile.FastGFile(model_exp, 'rb') as f:
                graph_def = tf.GraphDef()
                graph_def.ParseFromString(f.read())
                tf.import_graph_def(graph_def, name='')
        else:
            raise RuntimeError("Missing model file at path: {}".format(frozen_graph_path))

    def feed_image(self, encoded_image):
        initial_state = self._sess.run(fetches="lstm/initial_state:0",
                                       feed_dict={"image_feed:0": encoded_image})
        return initial_state

    def inference_step(self, input_feed, state_feed):
        softmax_output, state_output = self._sess.run(
            fetches=["softmax:0", "lstm/state:0"],
            feed_dict={
                "input_feed:0": input_feed,
                "lstm/state_feed:0": state_feed,
            })
        return softmax_output, state_output, None
