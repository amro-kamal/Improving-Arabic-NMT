# Arabic-MTL-NMT
### A repo for the project "Arabic Multitask Learning Neural Machine Translation"
The results after 40 epochs with the mixed data and  of fine tuning on the original data

|      Experiment          |           Discription           |   val     |    test     |
|    -------------         |     -----------------------     |  ------------ | ------------    |
| stanrad (baseline) translaton (seed=42)  |      6 layers, 50 epochs. [notebook](https://bit.ly/3wtO7Wo)    |    30.22   |   30.76         |
| mixing with (1,0.3) mixing ratio (seed=42) |  6 layers, 40 epochs / 10 epochs finetuning. [notebook](https://bit.ly/3hzsUGh)  |  30.22/31.06 |  30.44/31.63  | 
| mixing with (1,0.5) mixing ratio (seed=42) |  6 layers, 40 epochs / 10 epochs finetuning.      |     30.34/31.03 |   30.85/31.55      |
| mixing with (1,0.8) mixing ratio (seed=42) |  6 layers, 40 epochs / 10 epochs finetuning.      |     30.02/30.84 |   30.53/31.32    |
| mixing with (1,1) mixing ratio (seed=42)   |  6 layers, 40 epochs / 10 epochs finetuning.      |     30.11/30.74  |    31.35/31.44   |

The results after 70 epochs with the mixed data and 10 epochs of fine tuning on the original data. We can see that the baseline model doesn't benifit from long training in contrast to training with mixed data. 

|      Experiment          |           Discription           |      val        |      test       |
|    -------------         |     -----------------------     |  ------------   |   ------------  |
| stanrad (baseline) translaton (seed=42)  |    6 layers, 70 epochs. [notebook](https://bit.ly/3wxSeRd)   |    30.32    |    30.71    |
| stanrad (baseline) translaton (seed=22)  |    6 layers, 70 epochs. [notebook](https://bit.ly/3mWOjwm)   |    30.42    |    31.02    |
| mixing with (1,0.3) mixing ratio (seed=42) |  6 layers, 70 epochs / 10 epochs finetuning. [notebook](https://bit.ly/3mW5KwH)  |  31.51/32.00 |  32.43/32.76  |
| [1]mixing with (1,0.5) mixing ratio [seed=42] |  6 layers, 70 epochs / 10 epochs finetuning. [notebook](https://bit.ly/3gLWsj3)  |     32.05/32.47  |    32.33/32.96    |
| [2]mixing with (1,0.5) mixing ratio [seed=42] |  6 layers, 70 epochs / 10 epochs finetuning. [notebook](??)  |     31.27/31.55  |    31.62/32.25   |
| mixing with (1,0.8) mixing ratio [seed=42] |  6 layers, 70 epochs / 10 epochs finetuning.      |     31.01/31.47     |    31.68/31.98     |
| mixing with (1,1) mixing ratio (seed=42)   |  6 layers, 70 epochs / 10 epochs finetuning. [notebook](https://bit.ly/3zCUIQN)  |  31.87/32.00 | 32.08/32.85   |
| mixing with (1,1.2) mixing ratio (seed=42)   |  6 layers, 70 epochs / 10 epochs finetuning. [notebook](https://bit.ly/3zJi8nA)|    31.68/32.00 | 32.18/32.69    |


You can find the notebook for finetuning tasks [here](https://colab.research.google.com/drive/1C0xC56U1VmDhcE02rGbGb4b2SvypGZmS?usp=sharing) 

  

<!-- # Arabic-MTL-NMT
### A repo for the project "Arabic Multitask Learning Neural Machine Translation"
The results after 40 epochs with the mixed data and  of fine tuning on the original data

|      Experiment          |           Discription           |   val     |    test     |
|    -------------         |     -----------------------     |  ------------ | ------------    |
| stanrad (baseline) translaton (seed=42)  |      6 layers, 50 epochs. [notebook](https://bit.ly/3wtO7Wo)    |    30.22   |   30.76         |
| mixing with (1,0.3) mixing ratio (seed=42) |  6 layers, 40 epochs / 10 epochs finetuning. [notebook](https://bit.ly/3hzsUGh)  |  30.22/31.06 |  30.44/31.63  | 
| mixing with (1,0.3) mixing ratio (seed=42) |  6 layers, 40 epochs / 10 epochs finetuning. [notebook](https://bit.ly/3r44O9D)  |  30.22/31.19 |  30.52/31.49  |
| mixing with (1,0.5) mixing ratio (seed=42) |  6 layers, 40 epochs / 10 epochs finetuning.      |     30.20/30.80     |   30.7/31.70   |
| mixing with (1,0.5) mixing ratio (seed=42) |  6 layers, 40 epochs / 10 epochs finetuning.      |     30.34/31.03 |   30.85/31.55      |
| mixing with (1,0.8) mixing ratio (seed=42) |  6 layers, 40 epochs / 10 epochs finetuning.      |     29.96/30.48       |   30.45/31.18  |
| mixing with (1,0.8) mixing ratio (seed=42) |  6 layers, 40 epochs / 10 epochs finetuning.      |     30.02/30.84 |   30.53/31.32    |

The results after 70 epochs with the mixed data and 10 epochs of fine tuning on the original data. We can see that the baseline model doesn't benifit from long training in contrast to training with mixed data. 

|      Experiment          |           Discription           |   val     |    test     |
|    -------------         |     -----------------------     |  ------------ | ------------    |
| stanrad (baseline) translaton (seed=42)  |      6 layers, 50 epochs/70 epochs. [notebook](https://bit.ly/3wxSeRd)      |   30.18/30.32   |    30.56/30.71   |
| stanrad (baseline) translaton (seed=22)  |      6 layers, 70 epochs. [notebook](https://bit.ly/3mWOjwm)   |    30.42   |   31.02   |
| mixing with (1,0.3) mixing ratio (seed=42) |  6 layers, 70 epochs / 10 epochs finetuning. [notebook](https://bit.ly/3mW5KwH)  |  31.51/32.00 |  32.43/32.76  |
| mixing with (1,0.5) mixing ratio [seed=42] |  6 layers, 70 epochs / 10 epochs finetuning. [notebook](https://bit.ly/3gLWsj3)      |     32.05/?   |    32.33/?  |
| mixing with (1,1) mixing ratio (seed=42)   |  6 layers, 70 epochs / 10 epochs finetuning. [notebook](https://bit.ly/3zCUIQN)  |  31.87/32.00 | 32.08/32.85 |
| mixing with (1,1) mixing ratio (seed=22)   |  6 layers, 70 epochs / 10 epochs finetuning.      |    ?????      |   ???????    |








You can find the notebook for finetuning tasks [here](https://colab.research.google.com/drive/1C0xC56U1VmDhcE02rGbGb4b2SvypGZmS?usp=sharing) 
 -->
  
