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


