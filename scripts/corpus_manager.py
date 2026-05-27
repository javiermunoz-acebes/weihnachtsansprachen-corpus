#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Corpus Manager for Weihnachtsansprachen Corpus
Migrated from filologia_digital repository
"""

import os
import csv
import re
from pathlib import Path
from collections import Counter

CORPUS_DIR = Path(__file__).parent.parent / 'speeches'
METADATA_FILE = Path(__file__).parent.parent / 'CORPUS_METADATA.csv'


def load_speech(filepath):
    """Load a speech from a text file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()


def tokenize(text):
    """Simple tokenization by splitting on whitespace and removing punctuation."""
    tokens = re.findall(r'\b\w+\b', text.lower())
    return tokens


def compute_ttr(tokens):
    """Compute Type-Token Ratio."""
    if not tokens:
        return 0.0
    types = set(tokens)
    return len(types) / len(tokens)


def get_corpus_stats(corpus_dir=CORPUS_DIR):
    """Get statistics for all speeches in the corpus."""
    stats = []
    for chancellor_dir in sorted(corpus_dir.iterdir()):
        if chancellor_dir.is_dir():
            for speech_file in sorted(chancellor_dir.glob('*.txt')):
                text = load_speech(speech_file)
                tokens = tokenize(text)
                types = set(tokens)
                ttr = compute_ttr(tokens)
                stats.append({
                    'chancellor': chancellor_dir.name,
                    'year': speech_file.stem.split('_')[-1],
                    'filename': speech_file.name,
                    'tokens': len(tokens),
                    'types': len(types),
                    'ttr': round(ttr, 3)
                })
    return stats


def save_metadata(stats, output_file=METADATA_FILE):
    """Save corpus metadata to CSV."""
    fieldnames = ['chancellor', 'year', 'filename', 'tokens', 'types', 'ttr']
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(stats)
    print(f'Metadata saved to {output_file}')


def most_frequent_words(speech_file, n=20):
    """Return the n most frequent words in a speech."""
    text = load_speech(speech_file)
    tokens = tokenize(text)
    counter = Counter(tokens)
    return counter.most_common(n)


if __name__ == '__main__':
    stats = get_corpus_stats()
    for s in stats:
        print(s)
    save_metadata(stats)
