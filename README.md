# Arabic-MTL-NMT
A repo for the project "Arabic Multitask Learning Neural Machine Translation"

|      Experiment          |           Discription           |   val bleu    |    test bleu    |
|    -------------         |     -----------------------     |  ------------ | ------------    |
| stanrad translaton [1]   |      6 layers, 50 epochs/70 epochs. [notebook](https://bit.ly/3wxSeRd)        |     30.18/30.32       |   30.56/30.71       |
| stanrad translaton [2]   |      6 layers, 50 epochs. [notebook](https://bit.ly/3wtO7Wo)        |     30.22       |   30.76       |

| mixing with (1,0.3) mixing ratio [1] | 6 layers, 40 epochs + 10 epochs fintuning. [notebook](https://bit.ly/3hzsUGh)   |   30.22/31.06  |   30.44/31.63  |
| mixing with (1,0.3) mixing ratio [2] | 6 layers, 40 epochs + 10 epochs fintuning. [notebook](https://bit.ly/3r44O9D)   |   30.22/31.19  |   30.52/31.49  |

| mixing with (1,0.5) mixing ratio [2]       |     6 layers, 40 epochs + 10 epochs fintuning. |     30.34/31.03 |   30.85/31.55      |
| mixing with (1,0.5) mixing ratio [1] | 6 layers, 40 epochs + 10 epochs fintuning.          |     30.20/30.80     |   30.7/31.70     |

| mixing with (1,0.8) mixing ratio [1]       |     6 layers, 40 epochs + 10 epochs fintuning.           |     29.96/30.48       |   30.45/31.18       |
| mixing with (1,0.8) mixing ratio [2]     |     6 layers, 40 epochs + 10 epochs fintuning.      |     30.02/30.84 |   30.53/31.32|


You can find the notebook for finetuning tasks [here](4/1AX4XfWgPOUr0aO5srLilpLs3Iy7maHTSQZXffUTEt-sRsd2BJuo_cPAAnCY) 




