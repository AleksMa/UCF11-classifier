### UCF11 video classification

#### Prepare data

Download and unpack dataset:  
https://www.crcv.ucf.edu/data/UCF11_updated_mpg.rar

Prepare train and test lists:
```
python3 preprocess.py
```

#### Train and evaluating

```
python3 pip install -r requirements.txt  # change 'tensorflow-macos' and 'tensorflow-metal' to 'tensorflow' on Linux/Windows
python3 main.py
```

#### Results

```
Accuracy: 64.44%

Tests:
– Test video path: UCF11_updated_mpg/walking/v_walk_dog_15/v_walk_dog_15_03.mpg
        walking: 44.42%
        horse_riding:  8.53%
        basketball:  8.31%
        biking:  7.93%
        tennis_swing:  6.48%
        diving:  6.28%
        trampoline_jumping:  5.34%
        volleyball_spiking:  4.63%
        golf_swing: 3.76%
        swing: 2.97%
        soccer_juggling: 1.35%
– Test video path: UCF11_updated_mpg/biking/v_biking_20/v_biking_20_07.mpg
        biking:  47.39%
        golf_swing:  8.43%
        tennis_swing:  7.91%
        diving:  6.27%
        basketball:  5.88%
        soccer_juggling: 4.96%
        volleyball_spiking:  4.05%
        trampoline_jumping:  3.73%
        horse_riding: 3.16%
        walking: 3.00%
        swing: 2.24%
```
