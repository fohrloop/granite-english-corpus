# Granite English Ngrams

This repository contains the character-based ngrams (unigrams, bigrams, trigrams) used for the development of the [Granite Layout](https://github.com/fohrloop/granite-layout) which are compatible with the [Keyboard Layout Optimizer](https://github.com/dariogoetz/keyboard_layout_optimizer) by Dario Götz. The corpus was cleaned from untypical characters before creating the ngrams (see below for details).

The used  corpus is a mixture of two dataset with following weights

- 40% Leipzig (10% News, 10% Web-public com, 10% Web-public UK & 10% Wikipedia, 463 MB cleaned)
- 60% Reddit TLDR17 (5.6 GB cleaned)

Other related repos: [granite-code-ngrams](https://github.com/fohrloop/granite-code-ngrams) and [granite-finnish-ngrams](https://github.com/fohrloop/granite-finnish-ngrams).

# Most common ngrams

Most common trigrams using the `ngram_show` tool from [granite-tools](https://github.com/fohrloop/granite-tools), case ignored (unit: percents)
<details>
<summary>Most common unigrams (Granite English)</summary>

```
──────────────────── english ─────────────────────
   1: ␣ ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 17.74
   2: e ▇▇▇▇▇▇▇▇▇▇▇▇ 9.40
   3: t ▇▇▇▇▇▇▇▇▇ 7.27
   4: a ▇▇▇▇▇▇▇▇ 6.39
   5: o ▇▇▇▇▇▇▇▇ 6.01
   6: i ▇▇▇▇▇▇▇▇ 5.82
   7: n ▇▇▇▇▇▇▇ 5.42
   8: s ▇▇▇▇▇▇▇ 5.04
   9: r ▇▇▇▇▇▇ 4.50
  10: h ▇▇▇▇▇ 3.91
  11: l ▇▇▇▇ 3.28
  12: d ▇▇▇▇ 3.01
  13: u ▇▇▇ 2.28
  14: c ▇▇▇ 2.20
  15: m ▇▇▇ 2.09
  16: g ▇▇ 1.75
  17: y ▇▇ 1.66
  18: f ▇▇ 1.65
  19: w ▇▇ 1.61
  20: p ▇▇ 1.57
  21: b ▇▇ 1.25
  22: . ▇ 0.99
  23: v ▇ 0.85
  24: , ▇ 0.81
  25: k ▇ 0.73
  26: ⏎ ▇ 0.53
  27: ' ▇ 0.40
  28: x  0.16
  29: "  0.16
  30: -  0.16
  31: j  0.15
  32: 0  0.14
  33: 1  0.12
  34: (  0.10
  35: )  0.09
  36: 2  0.09
  37: q  0.07
  38: z  0.07
  39: 3  0.05
  40: 5  0.05
```
</details>

<details>
<summary>Most common bigrams (Granite English)</summary>

```
──────────────────── english ─────────────────────
   1: e␣ ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 2.94
   2: ␣t ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 2.47
   3: ␣a ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 2.02
   4: th ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 2.01
   5: s␣ ▇▇▇▇▇▇▇▇▇▇▇▇▇ 1.77
   6: t␣ ▇▇▇▇▇▇▇▇▇▇▇▇▇ 1.74
   7: he ▇▇▇▇▇▇▇▇▇▇▇▇ 1.66
   8: in ▇▇▇▇▇▇▇▇▇▇▇ 1.53
   9: d␣ ▇▇▇▇▇▇▇▇▇▇▇ 1.52
  10: ␣i ▇▇▇▇▇▇▇▇▇▇▇ 1.45
  11: an ▇▇▇▇▇▇▇▇▇ 1.21
  12: er ▇▇▇▇▇▇▇▇▇ 1.18
  13: ␣s ▇▇▇▇▇▇▇▇▇ 1.18
  14: n␣ ▇▇▇▇▇▇▇▇ 1.12
  15: ␣w ▇▇▇▇▇▇▇▇ 1.09
  16: re ▇▇▇▇▇▇▇▇ 1.07
  17: ␣o ▇▇▇▇▇▇▇ 0.99
  18: y␣ ▇▇▇▇▇▇▇ 0.97
  19: on ▇▇▇▇▇▇▇ 0.93
  20: r␣ ▇▇▇▇▇▇▇ 0.91
  21: nd ▇▇▇▇▇▇ 0.85
  22: o␣ ▇▇▇▇▇▇ 0.85
  23: at ▇▇▇▇▇▇ 0.83
  24: ␣h ▇▇▇▇▇▇ 0.81
  25: ␣b ▇▇▇▇▇▇ 0.80
  26: ,␣ ▇▇▇▇▇▇ 0.79
  27: ng ▇▇▇▇▇▇ 0.78
  28: en ▇▇▇▇▇▇ 0.78
  29: ␣m ▇▇▇▇▇▇ 0.77
  30: to ▇▇▇▇▇▇ 0.77
  31: ␣c ▇▇▇▇▇▇ 0.75
  32: ou ▇▇▇▇▇▇ 0.75
  33: or ▇▇▇▇▇ 0.73
  34: it ▇▇▇▇▇ 0.73
  35: ha ▇▇▇▇▇ 0.70
  36: ␣f ▇▇▇▇▇ 0.69
  37: st ▇▇▇▇▇ 0.67
  38: es ▇▇▇▇▇ 0.67
  39: te ▇▇▇▇▇ 0.64
  40: ed ▇▇▇▇▇ 0.64

```
</details>

<details>
<summary>Most common trigrams (Granite English)</summary>

```
──────────────────── english ─────────────────────
   1: ␣th ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 1.49
   2: the ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 1.17
   3: he␣ ▇▇▇▇▇▇▇▇▇▇▇▇▇ 0.97
   4: ing ▇▇▇▇▇▇▇▇▇ 0.67
   5: ␣an ▇▇▇▇▇▇▇▇▇ 0.66
   6: nd␣ ▇▇▇▇▇▇▇▇▇ 0.64
   7: ␣to ▇▇▇▇▇▇▇▇ 0.62
   8: and ▇▇▇▇▇▇▇▇ 0.59
   9: ng␣ ▇▇▇▇▇▇▇▇ 0.59
  10: to␣ ▇▇▇▇▇▇▇▇ 0.56
  11: ed␣ ▇▇▇▇▇▇▇ 0.50
  12: ␣in ▇▇▇▇▇▇ 0.44
  13: er␣ ▇▇▇▇▇▇ 0.42
  14: ␣of ▇▇▇▇▇▇ 0.42
  15: ␣a␣ ▇▇▇▇▇▇ 0.42
  16: of␣ ▇▇▇▇▇ 0.38
  17: ␣i␣ ▇▇▇▇▇ 0.37
  18: at␣ ▇▇▇▇▇ 0.36
  19: is␣ ▇▇▇▇▇ 0.36
  20: e␣t ▇▇▇▇▇ 0.35
  21: re␣ ▇▇▇▇▇ 0.34
  22: in␣ ▇▇▇▇ 0.33
  23: ␣be ▇▇▇▇ 0.32
  24: ␣co ▇▇▇▇ 0.31
  25: as␣ ▇▇▇▇ 0.31
  26: on␣ ▇▇▇▇ 0.30
  27: e␣a ▇▇▇▇ 0.30
  28: s␣a ▇▇▇▇ 0.30
  29: ␣ha ▇▇▇▇ 0.29
  30: hat ▇▇▇▇ 0.29
  31: or␣ ▇▇▇▇ 0.29
  32: her ▇▇▇▇ 0.28
  33: ly␣ ▇▇▇▇ 0.27
  34: ␣re ▇▇▇▇ 0.27
  35: t␣t ▇▇▇▇ 0.27
  36: d␣t ▇▇▇▇ 0.27
  37: ion ▇▇▇▇ 0.26
  38: ␣wa ▇▇▇▇ 0.26
  39: tha ▇▇▇ 0.26
  40: for ▇▇▇ 0.26
```

</details>


<details>
<summary>Most common unigrams, whitespace ignored (Granite English)</summary>

```
──────────────────── english ─────────────────────
   1: e ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 11.50
   2: t ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 8.89
   3: a ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 7.82
   4: o ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 7.36
   5: i ▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 7.13
   6: n ▇▇▇▇▇▇▇▇▇▇▇▇▇ 6.63
   7: s ▇▇▇▇▇▇▇▇▇▇▇▇ 6.17
   8: r ▇▇▇▇▇▇▇▇▇▇▇ 5.51
   9: h ▇▇▇▇▇▇▇▇▇▇ 4.79
  10: l ▇▇▇▇▇▇▇▇ 4.02
  11: d ▇▇▇▇▇▇▇ 3.68
  12: u ▇▇▇▇▇▇ 2.79
  13: c ▇▇▇▇▇ 2.69
  14: m ▇▇▇▇▇ 2.56
  15: g ▇▇▇▇ 2.15
  16: y ▇▇▇▇ 2.03
  17: f ▇▇▇▇ 2.02
  18: w ▇▇▇▇ 1.97
  19: p ▇▇▇▇ 1.92
  20: b ▇▇▇ 1.53
  21: . ▇▇ 1.22
  22: v ▇▇ 1.04
  23: , ▇▇ 0.99
  24: k ▇▇ 0.89
  25: ' ▇ 0.49
  26: x  0.20
  27: "  0.20
  28: -  0.19
  29: j  0.19
  30: 0  0.17
  31: 1  0.14
  32: (  0.12
  33: )  0.11
  34: 2  0.11
  35: q  0.09
  36: z  0.08
  37: 3  0.06
  38: 5  0.06
  39: ?  0.06
  40: :  0.05
```
</details>

<details>
<summary>Most common bigrams, whitespace ignored (Granite English)</summary>

```
──────────────────── english ─────────────────────
   1: th ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 3.14
   2: he ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 2.60
   3: in ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 2.39
   4: an ▇▇▇▇▇▇▇▇▇▇▇▇▇ 1.90
   5: er ▇▇▇▇▇▇▇▇▇▇▇▇▇ 1.84
   6: re ▇▇▇▇▇▇▇▇▇▇▇▇ 1.67
   7: on ▇▇▇▇▇▇▇▇▇▇ 1.46
   8: nd ▇▇▇▇▇▇▇▇▇ 1.33
   9: at ▇▇▇▇▇▇▇▇▇ 1.30
  10: ng ▇▇▇▇▇▇▇▇▇ 1.23
  11: en ▇▇▇▇▇▇▇▇▇ 1.22
  12: to ▇▇▇▇▇▇▇▇ 1.21
  13: ou ▇▇▇▇▇▇▇▇ 1.17
  14: or ▇▇▇▇▇▇▇▇ 1.15
  15: it ▇▇▇▇▇▇▇▇ 1.14
  16: ha ▇▇▇▇▇▇▇▇ 1.10
  17: st ▇▇▇▇▇▇▇ 1.05
  18: es ▇▇▇▇▇▇▇ 1.04
  19: te ▇▇▇▇▇▇▇ 1.00
  20: ed ▇▇▇▇▇▇▇ 1.00
  21: ar ▇▇▇▇▇▇▇ 0.98
  22: al ▇▇▇▇▇▇▇ 0.97
  23: ti ▇▇▇▇▇▇▇ 0.96
  24: is ▇▇▇▇▇▇▇ 0.95
  25: ve ▇▇▇▇▇▇▇ 0.93
  26: me ▇▇▇▇▇▇ 0.89
  27: as ▇▇▇▇▇▇ 0.87
  28: nt ▇▇▇▇▇▇ 0.85
  29: hi ▇▇▇▇▇▇ 0.81
  30: se ▇▇▇▇▇▇ 0.81
  31: le ▇▇▇▇▇▇ 0.78
  32: ea ▇▇▇▇▇ 0.75
  33: ll ▇▇▇▇▇ 0.72
  34: of ▇▇▇▇▇ 0.69
  35: ne ▇▇▇▇▇ 0.67
  36: co ▇▇▇▇ 0.63
  37: ro ▇▇▇▇ 0.62
  38: de ▇▇▇▇ 0.60
  39: be ▇▇▇▇ 0.59
  40: ri ▇▇▇▇ 0.58
```
</details>


<details>
<summary>Most common trigrams, whitespace ignored (Granite English)</summary>

```
──────────────────── english ─────────────────────
   1: the ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 2.49
   2: ing ▇▇▇▇▇▇▇▇▇▇▇ 1.43
   3: and ▇▇▇▇▇▇▇▇▇▇ 1.26
   4: hat ▇▇▇▇▇ 0.61
   5: her ▇▇▇▇▇ 0.60
   6: ion ▇▇▇▇▇ 0.56
   7: tha ▇▇▇▇ 0.55
   8: for ▇▇▇▇ 0.55
   9: ent ▇▇▇▇ 0.53
  10: thi ▇▇▇▇ 0.50
  11: all ▇▇▇▇ 0.47
  12: tio ▇▇▇▇ 0.45
  13: ver ▇▇▇ 0.42
  14: you ▇▇▇ 0.42
  15: ter ▇▇▇ 0.40
  16: ere ▇▇▇ 0.38
  17: his ▇▇▇ 0.38
  18: ith ▇▇▇ 0.36
  19: wit ▇▇▇ 0.35
  20: was ▇▇▇ 0.33
  21: eve ▇▇▇ 0.33
  22: ati ▇▇▇ 0.33
  23: out ▇▇▇ 0.33
  24: rea ▇▇▇ 0.32
  25: ate ▇▇▇ 0.32
  26: are ▇▇▇ 0.31
  27: ome ▇▇ 0.29
  28: hin ▇▇ 0.29
  29: ave ▇▇ 0.28
  30: ers ▇▇ 0.28
  31: one ▇▇ 0.28
  32: our ▇▇ 0.27
  33: ted ▇▇ 0.26
  34: hav ▇▇ 0.25
  35: not ▇▇ 0.25
  36: com ▇▇ 0.25
  37: con ▇▇ 0.25
  38: but ▇▇ 0.24
  39: sta ▇▇ 0.24
  40: n't ▇▇ 0.24
```
</details>

<details>
<summary>Most common unigrams in the leipzig and tldr17 datasets</summary>

This compares `leipzig` to `tldr17` dataset.

```
─────────────────────leipzig────────────────────── ──────────────────────tldr17──────────────────────
 1: ␣ ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 15.84                1 ( +0): ␣ ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 19.00
 2: e ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 9.67                           2 ( +0): e ▇▇▇▇▇▇▇▇▇▇▇▇ 9.23
 3: t ▇▇▇▇▇▇▇▇▇▇▇ 7.15                               3 ( +0): t ▇▇▇▇▇▇▇▇▇▇ 7.35
 4: a ▇▇▇▇▇▇▇▇▇▇ 6.63                                4 ( +0): a ▇▇▇▇▇▇▇▇ 6.23
 5: o ▇▇▇▇▇▇▇▇▇▇ 6.06                                5 ( +0): o ▇▇▇▇▇▇▇▇ 5.99
 6: i ▇▇▇▇▇▇▇▇▇ 5.93                                 6 ( +0): i ▇▇▇▇▇▇▇▇ 5.75
 7: n ▇▇▇▇▇▇▇▇▇ 5.69                                 7 ( +0): n ▇▇▇▇▇▇▇ 5.24
 8: s ▇▇▇▇▇▇▇▇ 5.33                                  8 ( +0): s ▇▇▇▇▇▇ 4.85
 9: r ▇▇▇▇▇▇▇▇ 5.12                                  9 ( +0): r ▇▇▇▇▇ 4.09
10: h ▇▇▇▇▇▇ 3.66                                   10 ( +0): h ▇▇▇▇▇ 4.08
11: l ▇▇▇▇▇ 3.35                                    11 ( +0): l ▇▇▇▇ 3.23
12: d ▇▇▇▇▇ 3.02                                    12 ( +0): d ▇▇▇▇ 3.00
13: c ▇▇▇▇ 2.65                                     13 ( +1): u ▇▇▇ 2.29
14: u ▇▇▇▇ 2.26                                     14 ( +1): m ▇▇▇ 2.16
15: m ▇▇▇ 1.99                                      15 ( -2): c ▇▇ 1.89
16: p ▇▇▇ 1.75                                      16 ( +2): g ▇▇ 1.83
17: f ▇▇▇ 1.75                                      17 ( +2): y ▇▇ 1.82
18: g ▇▇▇ 1.64                                      18 ( +2): w ▇▇ 1.75
19: y ▇▇ 1.43                                       19 ( -2): f ▇▇ 1.59
20: w ▇▇ 1.41                                       20 ( -4): p ▇▇ 1.45
21: b ▇▇ 1.22                                       21 ( +0): b ▇▇ 1.27
22: . ▇ 0.92                                        22 ( +0): . ▇ 1.05
23: v ▇ 0.90                                        23 ( +0): v ▇ 0.82
24: ⏎ ▇ 0.86                                        24 ( +2): k ▇ 0.82
25: , ▇ 0.81                                        25 ( +0): , ▇ 0.80
26: k ▇ 0.60                                        26 ( +1): ' ▇ 0.49
27: '  0.26                                         27 ( -3): ⏎  0.31
28: -  0.23                                         28 ( +5): j  0.16
29: 0  0.20                                         29 ( +3): x  0.16
30: "  0.19                                         30 ( +0): "  0.14
31: 1  0.18                                         31 ( +7): (  0.11
32: x  0.17                                         32 ( -4): -  0.11
33: j  0.14                                         33 ( +6): )  0.11
34: 2  0.13                                         34 ( -5): 0  0.09
35: q  0.09                                         35 ( -4): 1  0.07
36: z  0.08                                         36 (+11): ?  0.07
37: 9  0.08                                         37 ( -3): 2  0.06
38: (  0.07                                         38 ( -2): z  0.06
39: )  0.07                                         39 ( -4): q  0.06
40: 3  0.06                                         40 (+10): /  0.05
47: ?  0.03                                         42 ( -2): 3  0.04
50: /  0.02                                         48 (-11): 9  0.02
```
</details>

# Comparison to other corpora

## granite-english vs colemak-iweb

Download link: [iweb-corpus-samples-cleaned.txt.xz](https://colemak.com/pub/corpus/iweb-corpus-samples-cleaned.txt.xz). This is the same as the `ngrams/shai_english` in the Keyboard Layout Optimizer[^shai], named after Shai Coleman, the creator of Colemak layout. It is unclear if the corpus has been superceded by larger corpora later, as the current version of [Colemak Design](https://colemak.com/Design) page refers to [English Letter Frequency Counts: Mayzner Revisited or ETAOIN SRHLDCU](https://norvig.com/mayzner.html)

There is a claim that P is slightly more common than G in English (See e.g. [comment here](https://forum.colemak.com/topic/362-dear-shai-g-is-more-frequent-than-p/#p2357) and [Colemak FAQ](https://colemak.com/Design_FAQ)). However, the Granite English dataset does not seem to agree with it. The reason is that while the Leipzig dataset has more common P than G (1.75% vs 1.64%), more weight is given to the Reddit 2017 dataset, which has the opposite (P: 1.45%, G: 1.83%).

<details>
<summary>iweb vs Granite English: unigrams</summary>

```
───────────────────────iweb─────────────────────── ─────────────────────english──────────────────────
 1: ␣  ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 16.84                1 (+0): ␣   ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 17.74
 2: e  ▇▇▇▇▇▇▇▇▇▇▇▇▇ 9.59                           2 (+0): e   ▇▇▇▇▇▇▇▇▇▇▇▇▇ 9.40
 3: t  ▇▇▇▇▇▇▇▇▇▇ 7.28                              3 (+0): t   ▇▇▇▇▇▇▇▇▇▇ 7.27
 4: a  ▇▇▇▇▇▇▇▇▇ 6.50                               4 (+0): a   ▇▇▇▇▇▇▇▇▇ 6.39
 5: o  ▇▇▇▇▇▇▇▇ 6.22                                5 (+0): o   ▇▇▇▇▇▇▇▇ 6.01
 6: i  ▇▇▇▇▇▇▇▇ 5.81                                6 (+0): i   ▇▇▇▇▇▇▇▇ 5.82
 7: n  ▇▇▇▇▇▇▇▇ 5.54                                7 (+0): n   ▇▇▇▇▇▇▇ 5.42
 8: s  ▇▇▇▇▇▇▇ 5.24                                 8 (+0): s   ▇▇▇▇▇▇▇ 5.04
 9: r  ▇▇▇▇▇▇▇ 4.93                                 9 (+0): r   ▇▇▇▇▇▇ 4.50
10: h  ▇▇▇▇▇ 3.73                                  10 (+0): h   ▇▇▇▇▇ 3.91
11: l  ▇▇▇▇▇ 3.38                                  11 (+0): l   ▇▇▇▇ 3.28
12: d  ▇▇▇▇ 2.96                                   12 (+0): d   ▇▇▇▇ 3.01
13: c  ▇▇▇ 2.53                                    13 (+1): u   ▇▇▇ 2.28
14: u  ▇▇▇ 2.36                                    14 (-1): c   ▇▇▇ 2.20
15: m  ▇▇▇ 1.98                                    15 (+0): m   ▇▇▇ 2.09
16: f  ▇▇ 1.74                                     16 (+2): g   ▇▇ 1.75
17: p  ▇▇ 1.71                                     17 (+2): y   ▇▇ 1.66
18: g  ▇▇ 1.67                                     18 (-2): f   ▇▇ 1.65
19: y  ▇▇ 1.57                                     19 (+1): w   ▇▇ 1.61
20: w  ▇▇ 1.47                                     20 (-3): p   ▇▇ 1.57
21: b  ▇▇ 1.22                                     21 (+0): b   ▇▇ 1.25
22: .  ▇ 0.89                                      22 (+0): .   ▇ 0.99
23: v  ▇ 0.87                                      23 (+0): v   ▇ 0.85
24: ,  ▇ 0.82                                      24 (+0): ,   ▇ 0.81
25: k  ▇ 0.65                                      25 (+0): k   ▇ 0.73
26: ⏎   0.35                                       26 (+0): ⏎   ▇ 0.53
27: -   0.21                                       27 (+1): '   ▇ 0.40
28: '   0.21                                       28 (+1): x    0.16
29: x   0.18                                       29 (+1): "    0.16
30: "   0.15                                       30 (-3): -    0.16
31: 0   0.15                                       31 (+1): j    0.15
32: j   0.14                                       32 (-1): 0    0.14
33: 1   0.13                                       33 (+0): 1    0.12
34: 2   0.10                                       34 (+4): (    0.10
35: q   0.08                                       35 (+2): )    0.09
36: z   0.08                                       36 (-2): 2    0.09
37: )   0.08                                       37 (-2): q    0.07
38: (   0.08                                       38 (-2): z    0.07
39: :   0.06                                       39 (+2): 3    0.05
40: 5   0.05                                       40 (+0): 5    0.05
41: 3   0.05                                       41 (+2): ?    0.05
42: 9   0.04                                       42 (-3): :    0.04
43: ?   0.04                                       43 (-1): 9    0.04
44: 4   0.04                                       44 (+0): 4    0.04
45: !   0.04                                       45 (+4): /    0.04
46: 6   0.04                                       46 (+0): 6    0.03
47: 8   0.03                                       47 (+0): 8    0.03
48: 7   0.03                                       48 (+0): 7    0.03
49: /   0.02                                       49 (-4): !    0.03
50: ;   0.02                                       50 (+0): ;    0.01
51: $   0.01                                       51 (+0): $    0.01
52: %   0.01                                       52 (+0): %    0.01
53: &   0.01                                       53 (???): ]   0.01
54: +   0.01                                       54 (???): [   0.01
55: *   0.00                                       55 (+1): >    0.01
56: >   0.00                                       56 (-3): &    0.01
57: =   0.00                                       57 (-3): +    0.00
58: #   0.00                                       58 (-3): *    0.00
59: @   0.00                                       59 (-2): =    0.00
60: <   0.00                                       60 (???): ^   0.00
61:     0.00                                       61 (???): ~   0.00
62: ’   0.00                                       62 (???): _   0.00
63: ”   0.00                                       63 (-5): #    0.00
64: “   0.00                                       64 (???): €   0.00
65: —   0.00                                       65 (???): |   0.00
66: ü   0.00                                       66 (-6): <    0.00
67: –   0.00                                       67 (-8): @    0.00
68: •   0.00                                       68 (???): \   0.00
69: ¢   0.00                                       69 (???): {   0.00
70: ´   0.00                                       70 (???): }   0.00
71: é   0.00                                       71 (???): `   0.00
72: ʼ   0.00                                       ??? (???): и  0.00
73: ®   0.00                                       ??? (???): ⅔  0.00
74: ¤   0.00                                       ??? (???): ¢  0.00
75: ‐   0.00                                       ??? (???): ä  0.00
76: §   0.00                                       ??? (???): ⅓  0.00
77: ä   0.00                                       ??? (???): ®  0.00
78: ⅓   0.00                                       ??? (???): ʼ  0.00
79: ′   0.00                                       ??? (???): ´  0.00
80: ć   0.00                                       ??? (???): §  0.00
81: →   0.00                                       ??? (???): ­  0.00
82: и   0.00                                       ??? (???): —  0.00
83: ⅔   0.00                                       ??? (???):    0.00
84: ⅜   0.00                                       ??? (???): ′  0.00
85: ¬   0.00                                       ??? (???): ‐  0.00
86: ­   0.00                                       ??? (???): ·  0.00
87: ›   0.00                                       ??? (???): ”  0.00
88: ö   0.00                                       ??? (???): ⅛  0.00
89: ☺   0.00                                       ??? (???): •  0.00
90: ·   0.00                                       ??? (???): â  0.00
91: °   0.00                                       ??? (???): ÷  0.00
92: ÷   0.00                                       ??? (???): ö  0.00
93: â   0.00                                       ??? (???): “  0.00
94: ⅛   0.00                                       ??? (???): ü  0.00
???: [  0.00                                       ??? (???): ⅜  0.00
???: ^  0.00                                       ??? (???): é  0.00
???: ]  0.00                                       ??? (???): ć  0.00
???: ~  0.00                                       ??? (???): →  0.00
???: {  0.00                                       ??? (???): ›  0.00
???: €  0.00                                       ??? (???): ¬  0.00
???: \  0.00                                       ??? (???): ☺  0.00
???: `  0.00                                       ??? (???): °  0.00
???: _  0.00                                       ??? (???): –  0.00
???: }  0.00                                       ??? (???): ¤  0.00
???: |  0.00                                       ??? (???): ’  0.00
```
</details>

<details>
<summary>iweb vs Granite English: bigrams</summary>

```
───────────────────────iweb─────────────────────── ─────────────────────english──────────────────────
 1: e␣ ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 2.94                 1 ( +0): e␣ ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 2.94
 2: ␣t ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 2.50                     2 ( +0): ␣t ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 2.47
 3: th ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 2.03                        3 ( +1): ␣a ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 2.02
 4: ␣a ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 1.99                         4 ( -1): th ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 2.01
 5: s␣ ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 1.84                          5 ( +0): s␣ ▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 1.77
 6: he ▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 1.66                           6 ( +2): t␣ ▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 1.74
 7: in ▇▇▇▇▇▇▇▇▇▇▇▇▇ 1.55                            7 ( -1): he ▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 1.66
 8: t␣ ▇▇▇▇▇▇▇▇▇▇▇▇ 1.49                             8 ( -1): in ▇▇▇▇▇▇▇▇▇▇▇▇ 1.53
 9: d␣ ▇▇▇▇▇▇▇▇▇▇▇ 1.40                              9 ( +0): d␣ ▇▇▇▇▇▇▇▇▇▇▇▇ 1.52
10: an ▇▇▇▇▇▇▇▇▇▇ 1.25                              10 ( +3): ␣i ▇▇▇▇▇▇▇▇▇▇▇▇ 1.45
11: er ▇▇▇▇▇▇▇▇▇▇ 1.21                              11 ( -1): an ▇▇▇▇▇▇▇▇▇▇ 1.21
12: n␣ ▇▇▇▇▇▇▇▇▇▇ 1.20                              12 ( -1): er ▇▇▇▇▇▇▇▇▇▇ 1.18
13: ␣i ▇▇▇▇▇▇▇▇▇▇ 1.20                              13 ( +2): ␣s ▇▇▇▇▇▇▇▇▇▇ 1.18
14: re ▇▇▇▇▇▇▇▇▇ 1.14                               14 ( -2): n␣ ▇▇▇▇▇▇▇▇▇ 1.12
15: ␣s ▇▇▇▇▇▇▇▇▇ 1.12                               15 ( +4): ␣w ▇▇▇▇▇▇▇▇▇ 1.09
16: ␣o ▇▇▇▇▇▇▇▇▇ 1.06                               16 ( -2): re ▇▇▇▇▇▇▇▇▇ 1.07
17: on ▇▇▇▇▇▇▇▇ 0.99                                17 ( -1): ␣o ▇▇▇▇▇▇▇▇ 0.99
18: r␣ ▇▇▇▇▇▇▇▇ 0.97                                18 ( +4): y␣ ▇▇▇▇▇▇▇▇ 0.97
19: ␣w ▇▇▇▇▇▇▇▇ 0.95                                19 ( -2): on ▇▇▇▇▇▇▇▇ 0.93
20: ␣c ▇▇▇▇▇▇▇ 0.86                                 20 ( -2): r␣ ▇▇▇▇▇▇▇ 0.91
21: at ▇▇▇▇▇▇▇ 0.86                                 21 ( +3): nd ▇▇▇▇▇▇▇ 0.85
22: y␣ ▇▇▇▇▇▇▇ 0.84                                 22 ( +6): o␣ ▇▇▇▇▇▇▇ 0.85
23: or ▇▇▇▇▇▇▇ 0.83                                 23 ( -2): at ▇▇▇▇▇▇▇ 0.83
24: nd ▇▇▇▇▇▇▇ 0.83                                 24 (+17): ␣h ▇▇▇▇▇▇▇ 0.81
25: en ▇▇▇▇▇▇▇ 0.80                                 25 ( +6): ␣b ▇▇▇▇▇▇▇ 0.80
26: ,␣ ▇▇▇▇▇▇ 0.79                                  26 ( +0): ,␣ ▇▇▇▇▇▇ 0.79
27: es ▇▇▇▇▇▇ 0.79                                  27 ( +5): ng ▇▇▇▇▇▇ 0.78
28: o␣ ▇▇▇▇▇▇ 0.77                                  28 ( -3): en ▇▇▇▇▇▇ 0.78
29: to ▇▇▇▇▇▇ 0.76                                  29 (+11): ␣m ▇▇▇▇▇▇ 0.77
30: ou ▇▇▇▇▇▇ 0.76                                  30 ( -1): to ▇▇▇▇▇▇ 0.77
31: ␣b ▇▇▇▇▇▇ 0.75                                  31 (-11): ␣c ▇▇▇▇▇▇ 0.75
32: ng ▇▇▇▇▇▇ 0.73                                  32 ( -2): ou ▇▇▇▇▇▇ 0.75
33: it ▇▇▇▇▇▇ 0.72                                  33 (-10): or ▇▇▇▇▇▇ 0.73
34: te ▇▇▇▇▇▇ 0.70                                  34 ( -1): it ▇▇▇▇▇▇ 0.73
35: ␣f ▇▇▇▇▇▇ 0.70                                  35 (+10): ha ▇▇▇▇▇▇ 0.70
36: ti ▇▇▇▇▇▇ 0.69                                  36 ( -1): ␣f ▇▇▇▇▇▇ 0.69
37: st ▇▇▇▇▇▇ 0.69                                  37 ( +0): st ▇▇▇▇▇ 0.67
38: ar ▇▇▇▇▇▇ 0.68                                  38 (-11): es ▇▇▇▇▇ 0.67
39: ␣p ▇▇▇▇▇ 0.67                                   39 ( -5): te ▇▇▇▇▇ 0.64
40: ␣m ▇▇▇▇▇ 0.64                                   40 ( +4): ed ▇▇▇▇▇ 0.64
41: ␣h ▇▇▇▇▇ 0.64                                   41 ( -3): ar ▇▇▇▇▇ 0.62
44: ed ▇▇▇▇▇ 0.63                                   43 ( -7): ti ▇▇▇▇▇ 0.61
45: ha ▇▇▇▇▇ 0.61                                   46 ( -7): ␣p ▇▇▇▇▇ 0.61
```
</details>

<details>
<summary>iweb vs Granite English: bigrams (ignore whitespace)</summary>

```
───────────────────────iweb─────────────────────── ─────────────────────english──────────────────────
 1: th ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 3.10                1 (+0): th ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 3.14
 2: he ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 2.53                    2 (+0): he ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 2.60
 3: in ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 2.36                      3 (+0): in ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 2.39
 4: an ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 1.90                         4 (+0): an ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 1.90
 5: er ▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 1.85                          5 (+0): er ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 1.84
 6: re ▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 1.74                          6 (+0): re ▇▇▇▇▇▇▇▇▇▇▇▇▇ 1.67
 7: on ▇▇▇▇▇▇▇▇▇▇▇▇ 1.51                            7 (+0): on ▇▇▇▇▇▇▇▇▇▇▇▇ 1.46
 8: at ▇▇▇▇▇▇▇▇▇▇ 1.31                              8 (+2): nd ▇▇▇▇▇▇▇▇▇▇▇ 1.33
 9: or ▇▇▇▇▇▇▇▇▇▇ 1.27                              9 (-1): at ▇▇▇▇▇▇▇▇▇▇ 1.30
10: nd ▇▇▇▇▇▇▇▇▇▇ 1.27                             10 (+5): ng ▇▇▇▇▇▇▇▇▇▇ 1.23
11: en ▇▇▇▇▇▇▇▇▇ 1.22                              11 (+0): en ▇▇▇▇▇▇▇▇▇▇ 1.22
12: es ▇▇▇▇▇▇▇▇▇ 1.20                              12 (+1): to ▇▇▇▇▇▇▇▇▇▇ 1.21
13: to ▇▇▇▇▇▇▇▇▇ 1.16                              13 (+1): ou ▇▇▇▇▇▇▇▇▇ 1.17
14: ou ▇▇▇▇▇▇▇▇▇ 1.16                              14 (-5): or ▇▇▇▇▇▇▇▇▇ 1.15
15: ng ▇▇▇▇▇▇▇▇▇ 1.11                              15 (+1): it ▇▇▇▇▇▇▇▇▇ 1.14
16: it ▇▇▇▇▇▇▇▇ 1.09                               16 (+8): ha ▇▇▇▇▇▇▇▇▇ 1.10
17: te ▇▇▇▇▇▇▇▇ 1.07                               17 (+2): st ▇▇▇▇▇▇▇▇ 1.05
18: ti ▇▇▇▇▇▇▇▇ 1.06                               18 (-6): es ▇▇▇▇▇▇▇▇ 1.04
19: st ▇▇▇▇▇▇▇▇ 1.05                               19 (-2): te ▇▇▇▇▇▇▇▇ 1.00
20: ar ▇▇▇▇▇▇▇▇ 1.03                               20 (+3): ed ▇▇▇▇▇▇▇▇ 1.00
21: al ▇▇▇▇▇▇▇ 0.97                                21 (-1): ar ▇▇▇▇▇▇▇▇ 0.98
22: is ▇▇▇▇▇▇▇ 0.96                                22 (-1): al ▇▇▇▇▇▇▇▇ 0.97
23: ed ▇▇▇▇▇▇▇ 0.96                                23 (-5): ti ▇▇▇▇▇▇▇▇ 0.96
24: ha ▇▇▇▇▇▇▇ 0.93                                24 (-2): is ▇▇▇▇▇▇▇▇ 0.95
25: nt ▇▇▇▇▇▇▇ 0.90                                25 (+1): ve ▇▇▇▇▇▇▇ 0.93
26: ve ▇▇▇▇▇▇▇ 0.86                                26 (+6): me ▇▇▇▇▇▇▇ 0.89
27: le ▇▇▇▇▇▇ 0.84                                 27 (+2): as ▇▇▇▇▇▇▇ 0.87
28: se ▇▇▇▇▇▇ 0.84                                 28 (-3): nt ▇▇▇▇▇▇▇ 0.85
29: as ▇▇▇▇▇▇ 0.79                                 29 (+9): hi ▇▇▇▇▇▇ 0.81
30: ea ▇▇▇▇▇▇ 0.77                                 30 (-2): se ▇▇▇▇▇▇ 0.81
31: of ▇▇▇▇▇▇ 0.76                                 31 (-4): le ▇▇▇▇▇▇ 0.78
32: me ▇▇▇▇▇▇ 0.76                                 32 (-2): ea ▇▇▇▇▇▇ 0.75
33: co ▇▇▇▇▇▇ 0.71                                 33 (+1): ll ▇▇▇▇▇▇ 0.72
34: ll ▇▇▇▇▇ 0.70                                  34 (-3): of ▇▇▇▇▇ 0.69
35: ro ▇▇▇▇▇ 0.69                                  35 (+1): ne ▇▇▇▇▇ 0.67
36: ne ▇▇▇▇▇ 0.69                                  36 (-3): co ▇▇▇▇▇ 0.63
37: de ▇▇▇▇▇ 0.67                                  37 (-2): ro ▇▇▇▇▇ 0.62
38: hi ▇▇▇▇▇ 0.66                                  38 (-1): de ▇▇▇▇▇ 0.60
39: ri ▇▇▇▇▇ 0.62                                  39 (+9): be ▇▇▇▇▇ 0.59
40: li ▇▇▇▇▇ 0.60                                  40 (-1): ri ▇▇▇▇▇ 0.58
48: be ▇▇▇▇ 0.54                                   41 (-1): li ▇▇▇▇▇ 0.58
```
</details>

<details>
<summary>iweb vs Granite English: trigrams</summary>

```
───────────────────────iweb─────────────────────── ─────────────────────english──────────────────────
 1: ␣th  ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 1.57                   1 (  +0): ␣th ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 1.49
 2: the  ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 1.29                       2 (  +0): the ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 1.17
 3: he␣  ▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 1.03                          3 (  +0): he␣ ▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 0.97
 4: ␣an  ▇▇▇▇▇▇▇▇ 0.63                                4 (  +1): ing ▇▇▇▇▇▇▇▇▇ 0.67
 5: ing  ▇▇▇▇▇▇▇▇ 0.61                                5 (  -1): ␣an ▇▇▇▇▇▇▇▇▇ 0.66
 6: nd␣  ▇▇▇▇▇▇▇▇ 0.61                                6 (  +0): nd␣ ▇▇▇▇▇▇▇▇▇ 0.64
 7: and  ▇▇▇▇▇▇▇▇ 0.59                                7 (  +1): ␣to ▇▇▇▇▇▇▇▇▇ 0.62
 8: ␣to  ▇▇▇▇▇▇▇▇ 0.58                                8 (  -1): and ▇▇▇▇▇▇▇▇ 0.59
 9: ng␣  ▇▇▇▇▇▇▇ 0.54                                 9 (  +0): ng␣ ▇▇▇▇▇▇▇▇ 0.59
10: to␣  ▇▇▇▇▇▇▇ 0.53                                10 (  +0): to␣ ▇▇▇▇▇▇▇▇ 0.56
11: ␣in  ▇▇▇▇▇▇▇ 0.50                                11 (  +1): ed␣ ▇▇▇▇▇▇▇ 0.50
12: ed␣  ▇▇▇▇▇▇ 0.48                                 12 (  -1): ␣in ▇▇▇▇▇▇ 0.44
13: ␣of  ▇▇▇▇▇▇ 0.47                                 13 (  +3): er␣ ▇▇▇▇▇▇ 0.42
14: of␣  ▇▇▇▇▇▇ 0.43                                 14 (  -1): ␣of ▇▇▇▇▇▇ 0.42
15: ␣a␣  ▇▇▇▇▇ 0.40                                  15 (  +0): ␣a␣ ▇▇▇▇▇▇ 0.42
16: er␣  ▇▇▇▇▇ 0.40                                  16 (  -2): of␣ ▇▇▇▇▇ 0.38
17: is␣  ▇▇▇▇▇ 0.36                                  17 (+105): ␣i␣ ▇▇▇▇▇ 0.37
18: in␣  ▇▇▇▇▇ 0.35                                  18 (  +7): at␣ ▇▇▇▇▇ 0.36
19: ␣co  ▇▇▇▇▇ 0.35                                  19 (  -2): is␣ ▇▇▇▇▇ 0.36
20: re␣  ▇▇▇▇▇ 0.35                                  20 (  +2): e␣t ▇▇▇▇▇ 0.35
21: on␣  ▇▇▇▇▇ 0.35                                  21 (  -1): re␣ ▇▇▇▇▇ 0.34
22: e␣t  ▇▇▇▇▇ 0.34                                  22 (  -4): in␣ ▇▇▇▇▇ 0.33
23: s␣a  ▇▇▇▇ 0.33                                   23 (  +8): ␣be ▇▇▇▇ 0.32
24: ion  ▇▇▇▇ 0.33                                   24 (  -5): ␣co ▇▇▇▇ 0.31
25: at␣  ▇▇▇▇ 0.32                                   25 ( +12): as␣ ▇▇▇▇ 0.31
26: or␣  ▇▇▇▇ 0.32                                   26 (  -5): on␣ ▇▇▇▇ 0.30
27: es␣  ▇▇▇▇ 0.30                                   27 (  +1): e␣a ▇▇▇▇ 0.30
28: e␣a  ▇▇▇▇ 0.30                                   28 (  -5): s␣a ▇▇▇▇ 0.30
29: ent  ▇▇▇▇ 0.29                                   29 ( +15): ␣ha ▇▇▇▇ 0.29
30: ␣re  ▇▇▇▇ 0.29                                   30 ( +13): hat ▇▇▇▇ 0.29
31: ␣be  ▇▇▇▇ 0.29                                   31 (  -5): or␣ ▇▇▇▇ 0.29
32: for  ▇▇▇▇ 0.28                                   32 ( +18): her ▇▇▇▇ 0.28
33: you  ▇▇▇▇ 0.27                                   33 ( +18): ly␣ ▇▇▇▇ 0.27
34: ␣fo  ▇▇▇▇ 0.27                                   34 (  -4): ␣re ▇▇▇▇ 0.27
35: ␣yo  ▇▇▇▇ 0.27                                   35 (  +7): t␣t ▇▇▇▇ 0.27
36: tio  ▇▇▇▇ 0.26                                   36 (  +5): d␣t ▇▇▇▇ 0.27
37: as␣  ▇▇▇ 0.26                                    37 ( -13): ion ▇▇▇▇ 0.26
38: ␣wi  ▇▇▇ 0.26                                    38 ( +32): ␣wa ▇▇▇▇ 0.26
39: n␣t  ▇▇▇ 0.25                                    39 (  +7): tha ▇▇▇▇ 0.26
40: s␣t  ▇▇▇ 0.25                                    40 (  -8): for ▇▇▇▇ 0.26
41: d␣t  ▇▇▇ 0.25                                    41 ( -14): es␣ ▇▇▇▇ 0.26
42: t␣t  ▇▇▇ 0.24                                    42 ( -13): ent ▇▇▇ 0.25
43: hat  ▇▇▇ 0.23                                    44 ( -10): ␣fo ▇▇▇ 0.24
44: ␣ha  ▇▇▇ 0.23                                    47 (  -9): ␣wi ▇▇▇ 0.23
46: tha  ▇▇▇ 0.23                                    51 ( -12): n␣t ▇▇▇ 0.23
50: her  ▇▇▇ 0.22                                    54 ( -14): s␣t ▇▇▇ 0.22
51: ly␣  ▇▇▇ 0.22                                    60 ( -24): tio ▇▇▇ 0.21
70: ␣wa  ▇▇ 0.18                                     67 ( -34): you ▇▇▇ 0.20
122: ␣i␣ ▇▇ 0.13                                     72 ( -37): ␣yo ▇▇▇ 0.19
```
</details>

<details>
<summary>iweb vs Granite English: trigrams (ignore whitespace)</summary>

```
───────────────────────iweb─────────────────────── ─────────────────────english──────────────────────
 1: the  ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 2.63                   1 (  +0): the ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 2.49
 2: ing  ▇▇▇▇▇▇▇▇▇▇ 1.25                              2 (  +0): ing ▇▇▇▇▇▇▇▇▇▇▇▇ 1.43
 3: and  ▇▇▇▇▇▇▇▇▇▇ 1.19                              3 (  +0): and ▇▇▇▇▇▇▇▇▇▇▇ 1.26
 4: ion  ▇▇▇▇▇ 0.67                                   4 (  +5): hat ▇▇▇▇▇ 0.61
 5: ent  ▇▇▇▇▇ 0.59                                   5 (  +6): her ▇▇▇▇▇ 0.60
 6: for  ▇▇▇▇▇ 0.57                                   6 (  -2): ion ▇▇▇▇▇ 0.56
 7: you  ▇▇▇▇ 0.55                                    7 (  +3): tha ▇▇▇▇▇ 0.55
 8: tio  ▇▇▇▇ 0.53                                    8 (  -2): for ▇▇▇▇▇ 0.55
 9: hat  ▇▇▇▇ 0.48                                    9 (  -4): ent ▇▇▇▇ 0.53
10: tha  ▇▇▇▇ 0.46                                   10 (  +5): thi ▇▇▇▇ 0.50
11: her  ▇▇▇▇ 0.45                                   11 (  +2): all ▇▇▇▇ 0.47
12: ter  ▇▇▇ 0.41                                    12 (  -4): tio ▇▇▇▇ 0.45
13: all  ▇▇▇ 0.39                                    13 (  +3): ver ▇▇▇▇ 0.42
14: ati  ▇▇▇ 0.38                                    14 (  -7): you ▇▇▇ 0.42
15: thi  ▇▇▇ 0.36                                    15 (  -3): ter ▇▇▇ 0.40
16: ver  ▇▇▇ 0.36                                    16 (  +4): ere ▇▇▇ 0.38
17: ate  ▇▇▇ 0.36                                    17 (  +7): his ▇▇▇ 0.38
18: our  ▇▇▇ 0.36                                    18 (  +3): ith ▇▇▇ 0.36
19: are  ▇▇▇ 0.34                                    19 (  +3): wit ▇▇▇ 0.35
20: ere  ▇▇▇ 0.34                                    20 ( +32): was ▇▇▇ 0.33
21: ith  ▇▇▇ 0.34                                    21 (  +7): eve ▇▇▇ 0.33
22: wit  ▇▇▇ 0.33                                    22 (  -8): ati ▇▇▇ 0.33
23: ers  ▇▇▇ 0.33                                    23 ( +10): out ▇▇▇ 0.33
24: his  ▇▇▇ 0.32                                    24 (  +2): rea ▇▇▇ 0.32
25: pro  ▇▇ 0.30                                     25 (  -8): ate ▇▇▇ 0.32
26: rea  ▇▇ 0.29                                     26 (  -7): are ▇▇▇ 0.31
27: res  ▇▇ 0.27                                     27 (  +8): ome ▇▇ 0.29
28: eve  ▇▇ 0.27                                     28 ( +26): hin ▇▇ 0.29
29: con  ▇▇ 0.27                                     29 (  +9): ave ▇▇ 0.28
30: com  ▇▇ 0.27                                     30 (  -7): ers ▇▇ 0.28
31: ill  ▇▇ 0.26                                     31 ( +14): one ▇▇ 0.28
32: ive  ▇▇ 0.24                                     32 ( -14): our ▇▇ 0.27
33: out  ▇▇ 0.24                                     33 (  +4): ted ▇▇ 0.26
34: ess  ▇▇ 0.24                                     34 ( +17): hav ▇▇ 0.25
35: ome  ▇▇ 0.24                                     35 ( +15): not ▇▇ 0.25
36: ons  ▇▇ 0.24                                     36 (  -6): com ▇▇ 0.25
37: ted  ▇▇ 0.24                                     37 (  -8): con ▇▇ 0.25
38: ave  ▇▇ 0.24                                     38 ( +30): but ▇▇ 0.24
39: nce  ▇▇ 0.24                                     39 (  +4): sta ▇▇ 0.24
40: men  ▇▇ 0.24                                     40 (+131): n't ▇▇ 0.24
43: sta  ▇▇ 0.23                                     41 ( -14): res ▇▇ 0.24
45: one  ▇▇ 0.23                                     44 (  -5): nce ▇▇ 0.23
50: not  ▇▇ 0.20                                     45 ( -14): ill ▇▇ 0.23
51: hav  ▇▇ 0.20                                     46 ( -21): pro ▇▇ 0.23
52: was  ▇▇ 0.20                                     47 ( -15): ive ▇▇ 0.22
54: hin  ▇▇ 0.19                                     49 ( -13): ons ▇▇ 0.22
68: but  ▇ 0.17                                      54 ( -20): ess ▇▇ 0.21
171: n't ▇ 0.11                                      58 ( -18): men ▇▇ 0.20
```
</details>

# How the corpus was created

## The Granite Leipzig dataset
The Granite English corpus (`ngrams/english`) is a mixture of following from the [Leipzig Corpora Collection](https://wortschatz.uni-leipzig.de/en/download)[^leipzig]:

- News 2023 1M dataset (`eng_news_2023_1M.tar.gz`)
- Web-public com 1M dataset (`eng-com_web-public_2018_1M.tar.gz`)
- Web public United Kingdow 1M dataset (`eng-uk_web-public_2018_1M.tar.gz`)
- Wikipedia 2016 1M dataset (`eng_wikipedia_2016_1M.tar.gz`)

The Granite Eglish Leipzig dataset uses only the `*-sentences.txt` file from each, containing 4M English sentences in total. The sentence numbering and the tab was removed, and all the data from the four `*-sentences.txt` was merged into one. After cleaning the data, the `ngrams` binary from the [Keyboard Layout Optimizer](https://github.com/dariogoetz/keyboard_layout_optimizer) was used to form the Granite Leipzig ngrams (`ngrams/leipzig`).


<details>
<summary>Script used to create `combined-leipzig.txt`</summary>

```python
from pathlib import Path

folder = Path(__file__).parent / "raw" / "leipzig"
outfile = Path(__file__).parent / "corpus-not-clean" / "combined-leipzig.txt"
outfile.parent.mkdir(exist_ok=True)


def process_files():
    with open(outfile, "w") as out:
        for file in folder.glob("*.txt"):
            process_file(file, out)


def process_file(filename: Path, outfile):
    print(f"Processing {filename}")
    with open(filename, "r") as file:
        for line in file:
            linedata = line.split("\t", maxsplit=1)[-1]
            print(linedata, file=outfile, end="")


if __name__ == "__main__":
    process_files()
```

</details>

## The Granite Reddit TLDR17 dataset

IThe `tldr17` dataset was created from the [Webis-TLDR-17 Corpus](https://zenodo.org/records/1043504)[^tldr17]. The corpus was created by extracting the "content" field from each of the rows, stripping whitespace from the beginning and end of each, adding single space between contents, and combining all of that into a single 5.6GB text file (`tldr17.txt`).


<details>
<summary>Script used to create `tldr17.txt`</summary>

```python
import json
from pathlib import Path

infile = Path(__file__).parent / "raw" / "corpus-webis-tldr-17.json"
outfile = Path(__file__).parent / "corpus-not-clean"  / "tldr17.txt"
outfile.parent.mkdir(exist_ok=True)


def process_file():
    with open(infile, "r") as indata, open(outfile, "w") as out:
        for line in indata:
            data = json.loads(line)
            content = data["content"].strip()
            print(content, file=out, end=" ")


if __name__ == "__main__":
    process_file()
```

</details>

## The Granite English dataset

The Granite English ngrams were created from the  `leipzig` and the `tldr17` by first normalizing the ngram files using the `normalize.py` script from the [Keyboard Layout Optimizer](https://github.com/dariogoetz/keyboard_layout_optimizer)

```
python ./scripts/ngrams/normalize.py /somepath/ngrams/<corpusname>
```

and then merging the ngram files with weighting using the `ngram_merge` binary from the Keyboard Layout Optimizer:

```
❯ ./target/release/ngram_merge english/ngrams/english english/ngrams/leipzig:0.4 english/ngrams/tldr17:0.6
```

The used version of the Keyboard Layout Optimizer is specified by commit [f93bd06](https://github.com/dariogoetz/keyboard_layout_optimizer/commit/f93bd06820790ae746fbe66445bdf4427260fd31).

## Cleaning the datasets

Before creating the ngrams, only following ASCII alphanumerics (62 characters):
```
qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890
```

and following punctuation and special characters (33 characters):

```
,.!?;:_'"^~#%&/\()[]{}<>=+-*`@$€|
```

were accepted to the ngrams. The conversion script below was used to either remove or replace characters which belong to the following set:

```
¡£¤§«­®°²³´¶·¹»½¾¿ÁÃÅÆÉÌÓ×ØßàáâãåæçèéêëìíîïðñòóôõøúûüýāăćčīłŋōŠšūŽžə͜͡αβεηικλμνοπρςστυАЩавдеиклмнорстأابةتخدرسعقلمنهويนรลอาเ​‒–—―‘’“”•…₹™→−─│┆┌┐└┘┬┴═╞╡╪♪♫月语𞤫
```


<details>
<summary>Corpora cleanup script</summary>

This is the cleanup script which was used to clean the English, Code and Finnish corpora. 

```python
from pathlib import Path

root = Path(__file__).parent.parent


TYPABLE_CHARS = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890"
TYPABLE_CHARS += r""",.!?;:_'"^~#%&/\()[]{}<>=+-*`@$€|"""
TYPABLE_CHARS += " \t\n"
ALLOWED_CHARACTERS = set(TYPABLE_CHARS)
ALLOWED_CHARACTERS_FINNISH = ALLOWED_CHARACTERS | set("äöÄÖ")

replacements_finnish = {
    "¹": "1",
    "²": "2",
    "³": "3",
    "½": "1/2",
    "¾": "3/4",
    "Á": "A",
    "Ã": "A",
    "Å": "A",
    "Æ": "AE",
    "É": "E",
    "Ì": "I",
    "Ó": "O",
    "×": "x",
    "Ø": "Ö",
    "ß": "ss",
    "à": "a",
    "á": "a",
    "â": "a",
    "ã": "a",
    "å": "a",
    "æ": "ae",
    "ç": "c",
    "è": "e",
    "é": "e",
    "ê": "e",
    "ë": "e",
    "ì": "i",
    "í": "i",
    "î": "i",
    "ï": "i",
    "ð": "d",
    "ñ": "n",
    "ò": "o",
    "ó": "o",
    "ô": "o",
    "õ": "o",
    "ø": "ö",
    "ú": "u",
    "û": "u",
    "ü": "u",
    "ý": "y",
    "ā": "a",
    "ă": "a",
    "ć": "c",
    "č": "c",
    "ī": "i",
    "ł": "l",
    "ŋ": "NG",
    "ō": "o",
    "Š": "S",
    "š": "s",
    "ū": "u",
    "Ž": "Z",
    "ž": "z",
    "α": "a",
    "β": "b",
    "ε": "e",
    "η": "e",
    "ι": "i",
    "κ": "k",
    "λ": "l",
    "μ": "m",
    "ν": "n",
    "ο": "o",
    "π": "p",
    "ρ": "r",
    "ς": "s",
    "σ": "s",
    "τ": "t",
    "υ": "u",
    "А": "A",
    "Щ": "Shch",
    "а": "a",
    "в": "v",
    "д": "d",
    "е": "e",
    "и": "i",
    "к": "k",
    "л": "l",
    "м": "m",
    "н": "n",
    "о": "o",
    "р": "r",
    "с": "s",
    "т": "t",
    "‒": "-",
    "–": "-",
    "—": "--",
    "―": "--",
    "−": "-",
    "─": "-",
    "‘": "'",
    "’": "'",
    "´": "'",
    "“": '"',
    "”": '"',
    "«": '"',
    "»": '"',
    "•": "*",
    "·": "*",
    "…": "...",
    "™": "(tm)",
    "­®": "(r)",
}
replacements = replacements_finnish.copy()
replacements["Ø"] = "O"
replacements["ø"] = "o"


def process_file(input_path, output_path, replacements, allowed_chars):
    chunk_size = 50 * 1024 * 1024  # 50 MB chunk size
    with open(input_path, "r", encoding="utf-8") as infile, open(
        output_path, "w", encoding="utf-8"
    ) as outfile:
        while True:
            chunk = infile.read(chunk_size)
            if not chunk:
                break  # End of file

            for old_str, new_str in replacements.items():
                chunk = chunk.replace(old_str, new_str)
            chunk = "".join(char for char in chunk if char in allowed_chars)
            outfile.write(chunk)


def cleanup_folder(
    folder: Path,
    folder_out: Path,
    allowed_characters: set[str],
    used_replacements: dict[str, str],
):
    folder_out.mkdir(exist_ok=True)
    for file in folder.glob("*.txt"):
        file_out = folder_out / file.name
        print(f"Processing {file} -> {file_out}")
        process_file(file, file_out, used_replacements, allowed_characters)


if __name__ == "__main__":
    import time

    start = time.time()
    for lang in ("english", "code", "finnish"):
        langfolder = root / lang
        allowed_characters = (
            ALLOWED_CHARACTERS_FINNISH if lang == "finnish" else ALLOWED_CHARACTERS
        )
        used_replacements = replacements_finnish if lang == "finnish" else replacements
        cleanup_folder(
            langfolder / "corpus-not-clean",
            langfolder / "corpus-clean",
            allowed_characters,
            used_replacements,
        )
    print("Done in", time.time() - start, "seconds")
```
</details>



[^leipzig]: D. Goldhahn, T. Eckart & U. Quasthoff: Building Large Monolingual Dictionaries at the Leipzig Corpora Collection: From 100 to 200 Languages. In: Proceedings of the 8th International Language Resources and Evaluation (LREC'12), 2012
[^tldr17]: Syed, S., Voelske, M., Potthast, M., & Stein, B. (2017). Webis-TLDR-17 Corpus [Data set]. EMNLP 2017 Workshop on New Frontiers in Summarization (EMNLP 2017). Zenodo. https://doi.org/10.5281/zenodo.1043504
[^shai]: See: [dariogoetz/keyboard_layout_optimizer/discussions/78](https://github.com/dariogoetz/keyboard_layout_optimizer/discussions/78#discussioncomment-10866520)