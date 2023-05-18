IMG_SIZE = 224
BATCH_SIZE = 64

EPOCHS = 20

MAX_SEQ_LENGTH = 20
NUM_FEATURES = 2048

TEST_COUNT = 10

TRAIN_CSV_PATH = "train.csv"
TEST_CSV_PATH = "test.csv"

WEIGHTS_PATH = "tmp/video_classifier"

DATASET_PATH = "UCF11_updated_mpg"
TEST_MULTIPLIER = 5  # every TEST_MULTIPLIER'th row goes to test set, other – to train dataset
