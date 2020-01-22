#!/bin/bash

cd /work/scratch/zhou1/pytorch-CycleGAN-and-pix2pix


#set -ex
/home/students/zhou1/miniconda3/envs/myenv/bin/python /work/scratch/zhou1/pytorch-CycleGAN-and-pix2pix/test.py --dataroot ./datasets/maps --name maps_cyclegan --model cycle_gan --phase test --no_dropout
