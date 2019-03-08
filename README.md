# medium-show-and-tell-caption-generator

Code to run inference on a Show And Tell Model.
This model is trained to generate captions given an image.

## Weblinks

A detailed tutorial for the code can be found here:
https://medium.freecodecamp.org/building-an-image-caption-generator-with-deep-learning-in-tensorflow-a142722e9b1f

## Getting started

1. Download Docker image

```bash
$ sudo docker pull colemurray/medium-show-and-tell-caption-generator
```

2. Download model graph and weights

```bash
$ sudo docker run -e PYTHONPATH=$PYTHONPATH:/opt/app -v $PWD:/opt/app \
-it colemurray/medium-show-and-tell-caption-generator \
python3 /opt/app/bin/download_model.py \
--model-dir /opt/app/etc
```

3. Download vocabulary

```bash
$ curl -o etc/word_counts.txt https://raw.githubusercontent
.com/ColeMurray/medium-show-and-tell-caption-generator/master/etc/word_counts.txt
```

4. Add testing images to ```imgs/``` folder

5. Generate captions

```bash
$ sudo docker run -v $PWD:/opt/app \
-e PYTHONPATH=$PYTHONPATH:/opt/app \
-it colemurray/medium-show-and-tell-caption-generator  \
python3 /opt/app/medium_show_and_tell_caption_generator/inference.py \
--model_path /opt/app/etc/show-and-tell.pb \
--vocab_file /opt/app/etc/word_counts.txt \
--input_files /opt/app/imgs/*
```
## Run with conda environment
These steps assume that model and vocabulary are already downloaded.

1. Build and activate conda environment

```bash
$ conda env create -f environment.yml
$ source activate show-and-tell
```

2. Run inference
```bash
$ python -m medium_show_and_tell_caption_generator.inference --model_path='etc/show-and-tell.pb' \
--vocab_file='etc/word_counts.txt' \
--input_files='imgs/*'
```
