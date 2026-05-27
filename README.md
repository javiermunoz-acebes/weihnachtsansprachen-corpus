# Weihnachtsansprachen-Korpus

A plain-text corpus of German federal Christmas addresses (*Weihnachtsansprachen*), compiled for digital philological and computational text analysis research. The corpus is designed for incremental expansion across speakers and periods.

## Current coverage

| Speaker | Period | Speeches |
|---------|--------|----------|
| Konrad Adenauer | 1949–1962 | 14 |

## Repository structure

```
weihnachtsansprachen-corpus/
├── CITATION.cff
├── CORPUS_METADATA.csv
├── README.MD
├── scripts/
│   └── corpus_manager.py
└── speeches/
    └── Adenauer/
        ├── Adenauer_Weihnachtsanprache_1949.txt
        ├── ...
        └── Adenauer_Weihnachtsanprache_1962.txt
```

## License

This corpus is released under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Please cite according to `CITATION.cff`.
