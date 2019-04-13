import os, time, pickle, argparse, networks, utils
import torch
import torch.nn as nn
import torch.optim as optim
import matplotlib.pyplot as plt
from torchvision import transforms
import tkinter
from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk
import numpy
import shutil
from shutil import copyfile


parser = argparse.ArgumentParser()
parser.add_argument('--name', required=False, default='project_name',  help='')
parser.add_argument('--src_data', required=False, default='src_data_path',  help='sec data path')
parser.add_argument('--tgt_data', required=False, default='tgt_data_path',  help='tgt data path')
parser.add_argument('--vgg_model', required=False, default='pre_trained_VGG19_model_path/vgg19.pth', help='pre-trained VGG19 model path')
parser.add_argument('--in_ngc', type=int, default=3, help='input channel for generator')
parser.add_argument('--out_ngc', type=int, default=3, help='output channel for generator')
parser.add_argument('--in_ndc', type=int, default=3, help='input channel for discriminator')
parser.add_argument('--out_ndc', type=int, default=1, help='output channel for discriminator')
parser.add_argument('--batch_size', type=int, default=8, help='batch size')
parser.add_argument('--ngf', type=int, default=64)
parser.add_argument('--ndf', type=int, default=32)
parser.add_argument('--nb', type=int, default=8, help='the number of resnet block layer for generator')
parser.add_argument('--input_size', type=int, default=256, help='input size')
parser.add_argument('--train_epoch', type=int, default=100)
parser.add_argument('--pre_train_epoch', type=int, default=10)
parser.add_argument('--lrD', type=float, default=0.0002, help='learning rate, default=0.0002')
parser.add_argument('--lrG', type=float, default=0.0002, help='learning rate, default=0.0002')
parser.add_argument('--con_lambda', type=float, default=10, help='lambda for content loss')
parser.add_argument('--beta1', type=float, default=0.5, help='beta1 for Adam optimizer')
parser.add_argument('--beta2', type=float, default=0.999, help='beta2 for Adam optimizer')
parser.add_argument('--pre_trained_model', required=True, default='generator_latest.pkl', help='pre_trained cartoongan model path')
parser.add_argument('--image_dir', required=True, default='image_dir', help='test image path')
parser.add_argument('--output_image_dir', required=True, default='result', help='output test image path')
args = parser.parse_args()

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
if torch.backends.cudnn.enabled:
    torch.backends.cudnn.benchmark = True

G = networks.generator(args.in_ngc, args.out_ngc, args.ngf, args.nb)
if torch.cuda.is_available():
    G.load_state_dict(torch.load(args.pre_trained_model))
else:
    # cpu mode
    G.load_state_dict(torch.load(args.pre_trained_model, map_location=lambda storage, loc: storage))
G.to(device)

src_transform = transforms.Compose([
        transforms.Resize((args.input_size, args.input_size)),
        transforms.ToTensor(),
        transforms.Normalize(mean=(0.5, 0.5, 0.5), std=(0.5, 0.5, 0.5))
])

top = Tk()
top.title = 'Cartoon Style Transfer'
top.geometry('650x360')
canvas = Canvas(top, width=256,height=256, bd=0, bg='white')
canvas.grid(row=1, column=0)
canvas2 = Canvas(top, width=256,height=256, bd=0, bg='white')
canvas2.grid(row=1, column=1)


def showImg():
    File = askopenfilename(title='Open Image')
    e.set(File)

    shutil.copy(File, r"C:\Users\LQF\Desktop\moTest\image_dir\test2")
    
    load = Image.open(e.get())
    w, h = load.size
    imgfile = ImageTk.PhotoImage(load)
    
    canvas.image = imgfile  # <--- keep reference of your image
    canvas.create_image(2,2,anchor='nw',image=imgfile)

e = StringVar()

submit_button = Button(top, text ='Open', command = showImg)
submit_button.grid(row=0, column=0)

def Transfer():

    image_src = utils.data_load(os.path.join(args.image_dir), 'test2', src_transform, 1, shuffle=True, drop_last=True)

    with torch.no_grad():
        G.eval()
        for n, (x, _) in enumerate(image_src):
            x = x.to(device)
            G_recon = G(x)
            #result = torch.cat((x[0], G_recon[0]), 2)
            result = G_recon[0]
            path = os.path.join(args.output_image_dir, str(n + 1) + '.png')
            plt.imsave(path, (result.cpu().numpy().transpose(1, 2, 0) + 1) / 2)

    load = Image.open(r"C:\Users\LQF\Desktop\moTest\result"+"\\"+str(1)+".png")
    imgfile = ImageTk.PhotoImage(load)   
    canvas2.image = imgfile  # <--- keep reference of your image
    canvas2.create_image(2,2,anchor='nw',image=imgfile)

    os.remove(r"C:\Users\LQF\Desktop\moTest\result"+"\\"+str(1)+".png")
    for i in os.listdir(r"C:\Users\LQF\Desktop\moTest\image_dir\test2"):
        path_file = os.path.join(r"C:\Users\LQF\Desktop\moTest\image_dir\test2",i)
        if os.path.isfile(path_file):
            os.remove(path_file)

    
submit_button = Button(top, text ='Transfer', command = Transfer)
submit_button.grid(row=0, column=1)

l1=Label(top,text='Please <Open> a real world image, then press <Transfer>')
l1.grid(row=2)


top.mainloop()

