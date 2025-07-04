from geopy.distance import geodesic
import json
import os
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

with open('formulas.json') as f:
    data = json.load(f)
with open('wikidata.json') as f:
    metadata = json.load(f)

def centralize(c1, c2):

    midpoint = ((c1[0] + c2[0]) / 2, (c1[1] + c2[1]) / 2)
    translation = (-midpoint[0], -midpoint[1])

    return [
        [ c1[0] + translation[0], c1[1] + translation[1] ],
        [ c2[0] + translation[0], c2[1] + translation[1] ],
    ]


def centralize2(c1, c2):

    return [
        [ 0, 0 ],
        [ c2[0] - c1[0], c2[1] - c1[1] ],
    ]


coords = dict()
for lang in data:
    if lang not in ('cs', 'en', 'fr', 'ru', 'de', 'sl'):
        continue
    coords[lang] = list()
    for poem_id in data[lang]:
        for formula in data[lang][poem_id]:
            c1 = metadata[formula[0]]['lon'], metadata[formula[0]]['lat']
            c2 = metadata[formula[1]]['lon'], metadata[formula[1]]['lat']
            #print(x1, y1, x2, y2)
            c1, c2 = centralize2(c1, c2)
            #print(x1, y1, x2, y2);input()

            coords[lang].append({
                'x': [c1[0], c2[0]],
                'y': [c1[1], c2[1]],
            })


fig, axes = plt.subplots(3, 2, figsize=(10, 8), sharex=True, sharey=True)
axes = axes.flatten()
for i, lang in enumerate(sorted(coords)):
    for c in coords[lang]:
        axes[i].plot(c['x'], c['y'], c='b', alpha=0.2)
    axes[i].set_title(lang)

plt.tight_layout()
plt.show()