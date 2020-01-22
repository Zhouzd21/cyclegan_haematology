#!/bin/bash

cd /work/scratch/zhou1/pytorch-CycleGAN-and-pix2pix

/home/students/zhou1/miniconda3/envs/myenv/bin/python /work/scratch/zhou1/pytorch-CycleGAN-and-pix2pix/train.py --dataroot ./datasets/haema --name haema_cyclegan300 --model cycle_gan --pool_size 50 --no_dropout
