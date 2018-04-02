from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import logging
import os


class Vocabulary(object):
    """Vocabulary class for mapping words to ids"""

    def __init__(self,
                 vocab_file_path,
                 start_token="<S>",
                 end_token="</S>",
                 unk_token="<UNK>"):
        """Initializes the vocabulary.
    
        Args:
          vocab_file_path: File containing the vocabulary, where the tokens are the first
            whitespace-separated token on each line (other tokens are ignored) and
            the token ids are the corresponding line numbers.
          start_token: Special token denoting sequence start.
          end_token: Special token denoting sequence end.
          unk_token: Special token denoting unknown tokens.
        """
        self.logger = logging.getLogger(__name__)
        if not os.path.exists(vocab_file_path):
            self.logger.exception("Vocab file %s not found.", vocab_file_path)
            raise RuntimeError
        self.logger.info("Initializing vocabulary from file: %s", vocab_file_path)

        with open(vocab_file_path, mode="r") as f:
            reverse_vocab = list(f.readlines())
        reverse_vocab = [line.split()[0] for line in reverse_vocab]
        assert start_token in reverse_vocab
        assert end_token in reverse_vocab
        if unk_token not in reverse_vocab:
            reverse_vocab.append(unk_token)
        vocab = dict([(x, y) for (y, x) in enumerate(reverse_vocab)])

        self.logger.info("Created vocabulary with %d words" % len(vocab))

        self.vocab = vocab
        self.reverse_vocab = reverse_vocab

        self.start_id = vocab[start_token]
        self.end_id = vocab[end_token]
        self.unk_id = vocab[unk_token]

    def token_to_id(self, token_id):
        if token_id in self.vocab:
            return self.vocab[token_id]
        else:
            return self.unk_id

    def id_to_token(self, token_id):
        if token_id >= len(self.reverse_vocab):
            return self.reverse_vocab[self.unk_id]
        else:
            return self.reverse_vocab[token_id]
