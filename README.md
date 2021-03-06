# CartoonGAN
* Pytorch implementation of CartoonGAN(Shinkai Style) 
* The code is based on [CartoonGAN-Pytorch](https://github.com/znxlwm/pytorch-CartoonGAN) with some changes
* The pytorchCart folder contains all the code for training and the moTest contains all the code for test.
* Build a simple GUI based on Tkinker
* I do not attach any dataset here.
* As for video demo, you can check it here: https://youtu.be/0rBYc4kZztU
 
### 1.Download model
* [VGG19](https://download.pytorch.org/models/vgg19-dcbb9e9d.pth)

### 2.Train
```
python CartoonGAN.py --name cartoonShinkaiStyle --src_data src_data --tgt_data tgt_data --vgg_model vgg19.pth
```
### 3.Test
```
python test2.py --pre_trained_model generator_latest.pkl --image_dir image_dir --output_image_dir result
```

### 4.Result
#### CartoonGAN
<table align='center'>
<tr align='center'>
<td> Input - Output </td>
</tr>
<tr>
<td><img src = 'https://github.com/LiEAEX/CSCE636Project/blob/master/result/5.png'>
</tr>
<tr>
<td><img src = 'https://github.com/LiEAEX/CSCE636Project/blob/master/result/11.png'>
</tr>
<tr>
<td><img src = 'https://github.com/LiEAEX/CSCE636Project/blob/master/result/13.png'>
</tr>
<tr>
<td><img src = 'https://github.com/LiEAEX/CSCE636Project/blob/master/result/14.png'>
</tr>
</table>


## Development Environment

* NVIDIA GTX 1070
* python 3.6.4
* pytorch 0.4.1
* cuda 10.0
* cudatoolkit 10.0.130
* hdf5 1.10.1
* torchvision 0.2.2
* opencv 3.3.1

## Reference
Chen, Yang, Yu-Kun Lai, and Yong-Jin Liu. "CartoonGAN: Generative Adversarial Networks for Photo Cartoonization." Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition. 2018.
