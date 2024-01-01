# Pdf Similarity
The module provides similarity ratio between pdfs in a given directory.

K-gram fingerprint for each pdf is generated using [Winnowing Algorithm](http://theory.stanford.edu/~aiken/publications/papers/sigmod03.pdf). Then fingerprints are compared using the [levenshtein algorithm](https://en.wikipedia.org/wiki/Levenshtein_distance). This is used to generate levenshtein distance matrix between pdf. This matrix is then normalized for obtain ratios between [0,1], where 0 means exactly same and 1 means completely different pdfs.

## Example 

`./src/example.py`

```python
from PdfSim.pdf_similarity import Pdf_Similarity 
ps = Pdf_Similarity()

# Automatically find pdfs in currenly directory and print ratios
ps.generate()

# relative or absolute path for directory can also be defined
ps.directory("./src")
ps.generate()
```
