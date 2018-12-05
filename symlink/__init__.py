# coding: utf8
from __future__ import unicode_literals

from pathlib import Path
from spacy.util import load_model_from_init_py, get_model_meta
from en_coref_md.neuralcoref import NeuralCoref

__version__ = get_model_meta(Path(__file__).parent)['version']


def load(**overrides):
    disable = overrides.get('disable', [])
    overrides['disable'] = disable + ['neuralcoref']
    nlp = load_model_from_init_py(__file__, **overrides)
    coref = NeuralCoref(nlp.vocab)
    coref.from_disk(nlp.path / 'neuralcoref')
    nlp.add_pipe(coref, name='neuralcoref')
    return nlp