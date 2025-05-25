from __future__ import print_function
from tkinter import *
expression = ""
import tkinter
import tkinter.filedialog 
import tkinter.constants
import cv2
import random
import matplotlib, sys
matplotlib.use('TkAgg')

from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy as np
import rasterio
from rasterio.plot import show
from osgeo import gdal
from osgeo import gdal_array
from rasterio.plot import show_hist   
import scipy.misc    


def IMG():
    global file1
    file1 = tkinter.filedialog.askopenfilename(initialdir="/", title="Select file", filetypes=(("jpeg files","*.jpg"),("all files","*.*")))
    print(file1)
    label1= Label(root, text= file1).grid(row=1,column=1)
    
def close_window(): 
    root.destroy()    

def b_h1():
    raster = rasterio.open(file1)
    band1 = raster.read(1)
    fig= show_hist(band1, bins=50, lw=0.0, stacked=False, alpha=0.3, histtype='stepfilled', title="Band 1 Histogram")
    
def b_h2():
    raster = rasterio.open(file1)
    band2 = raster.read(2)
    fig= show_hist(band2, bins=50, lw=0.0, stacked=False, alpha=0.3, histtype='stepfilled', title="Band 2 Histogram")
    
def b_h3():
    raster = rasterio.open(file1)
    band3 = raster.read(3)
    fig= show_hist(band3, bins=50, lw=0.0, stacked=False, alpha=0.3, histtype='stepfilled', title="Band 3 Histogram")
    
def b_h4():
    raster = rasterio.open(file1)
    band4 = raster.read(4)
    fig= show_hist(band4, bins=50, lw=0.0, stacked=False, alpha=0.3, histtype='stepfilled', title="Band 4 Histogram")
    
def b_h5():
    raster = rasterio.open(file1)
    band5 = raster.read(5)
    fig= show_hist(band5, bins=50, lw=0.0, stacked=False, alpha=0.3, histtype='stepfilled', title="Band 5 Histogram")
def b_h6():
    raster = rasterio.open(file1)
    band6 = raster.read(6)
    fig= show_hist(band6, bins=50, lw=0.0, stacked=False, alpha=0.3, histtype='stepfilled', title="Band ratio Histogram")
def b_h7():
    raster = rasterio.open(file1)
    band7 = raster.read(7)
    fig= show_hist(band7, bins=50, lw=0.0, stacked=False, alpha=0.3, histtype='stepfilled', title="Band 7 Histogram")
def b_h8():
    raster = rasterio.open(file1)
    band8 = raster.read(8)
    fig= show_hist(band8, bins=50, lw=0.0, stacked=False, alpha=0.3, histtype='stepfilled', title="Band 8 Histogram")
def b_h9():
    raster = rasterio.open(file1)
    band9 = raster.read(9)
    fig= show_hist(band9, bins=50, lw=0.0, stacked=False, alpha=0.3, histtype='stepfilled', title="Band 9 Histogram")
def b_h10():
    raster = rasterio.open(file1)
    band10 = raster.read(10)
    fig= show_hist(band10, bins=50, lw=0.0, stacked=False, alpha=0.3, histtype='stepfilled', title="Band 10 Histogram")
def b_h11():
    raster = rasterio.open(file1)
    band11 = raster.read(11)
    fig= show_hist(band11, bins=50, lw=0.0, stacked=False, alpha=0.3, histtype='stepfilled', title="Band 11 Histogram")
def b_h12():
    raster = rasterio.open(file1)
    band12 = raster.read(12)
    fig= show_hist(band12, bins=50, lw=0.0, stacked=False, alpha=0.3, histtype='stepfilled', title="Band 12 Histogram")


def b1_img():
    raster = rasterio.open(file1)
    band_img = raster.read(1)
    show(band_img)
    
    scipy.misc.imsave('band_img.tif', ndvi)
    imgFile = cv2.imread('band_img.tif')
    cv2.imshow('dst_rt', imgFile)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
def b2_img():
    raster = rasterio.open(file1)
    band_img = raster.read(2)
    show(band_img)
    
    scipy.misc.imsave('band_img.tif', ndvi)
    imgFile = cv2.imread('band_img.tif')
    cv2.imshow('dst_rt', imgFile)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
def b3_img():
    raster = rasterio.open(file1)
    band_img = raster.read(3)
    show(band_img)
    
    scipy.misc.imsave('band_img.tif', ndvi)
    imgFile = cv2.imread('band_img.tif')
    cv2.imshow('dst_rt', imgFile)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def b4_img():
    raster = rasterio.open(file1)
    band_img = raster.read(41)
    show(band_img)
    
    scipy.misc.imsave('band_img.tif', ndvi)
    imgFile = cv2.imread('band_img.tif')
    cv2.imshow('dst_rt', imgFile)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def b5_img():
    raster = rasterio.open(file1)
    band_img = raster.read(5)
    show(band_img)
    
    scipy.misc.imsave('band_img.tif', ndvi)
    imgFile = cv2.imread('band_img.tif')
    cv2.imshow('dst_rt', imgFile)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def b6_img():
    raster = rasterio.open(file1)
    band_img = raster.read(6)
    show(band_img)
    
    scipy.misc.imsave('band_img.tif', ndvi)
    imgFile = cv2.imread('band_img.tif')
    cv2.imshow('dst_rt', imgFile)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def b7_img():
    raster = rasterio.open(file1)
    band_img = raster.read(7)
    show(band_img)
    
    scipy.misc.imsave('band_img.tif', ndvi)
    imgFile = cv2.imread('band_img.tif')
    cv2.imshow('dst_rt', imgFile)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def b8_img():
    raster = rasterio.open(file1)
    band_img = raster.read(8)
    show(band_img)
    
    scipy.misc.imsave('band_img.tif', ndvi)
    imgFile = cv2.imread('band_img.tif')
    cv2.imshow('dst_rt', imgFile)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def b9_img():
    raster = rasterio.open(file1)
    band_img = raster.read(9)
    show(band_img)
    
    scipy.misc.imsave('band_img.tif', ndvi)
    imgFile = cv2.imread('band_img.tif')
    cv2.imshow('dst_rt', imgFile)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
def b10_img():
    raster = rasterio.open(file1)
    band_img = raster.read(10)
    show(band_img)
    
    scipy.misc.imsave('band_img.tif', ndvi)
    imgFile = cv2.imread('band_img.tif')
    cv2.imshow('dst_rt', imgFile)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def b11_img():
    raster = rasterio.open(file1)
    band_img = raster.read(11)
    show(band_img)
    
    scipy.misc.imsave('band_img.tif', ndvi)
    imgFile = cv2.imread('band_img.tif')
    cv2.imshow('dst_rt', imgFile)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def b12_img():
    raster = rasterio.open(file1)
    band_img = raster.read(12)
    show(band_img)
    
    scipy.misc.imsave('band_img.tif', ndvi)
    imgFile = cv2.imread('band_img.tif')
    cv2.imshow('dst_rt', imgFile)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# TO DEFINE AND SET GUI WINDOW    

root = Tk()
root.configure(background="light blue")
root.title("Satellite Image Histogram")
#root.geometry("750x530")
root.iconbitmap(r'C:\Users\User\Desktop\python\d2.ico')
root.state('zoomed')

from PIL import Image, ImageTk
image = Image.open("drone.jpg")
photo = ImageTk.PhotoImage(image)

#canvas_width = 600
#canvas_height = 600
#canvas_widget = Canvas(root, width= canvas_width, height= canvas_height)
#canvas_widget.pack(anchor = sw, row=1,column=5)

menu = Menu(root)
root.config(menu=menu)
subMenu = Menu(menu)
histMenu = Menu(menu)
bimgMenu = Menu(menu)
menu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="Import Image", command= IMG)
subMenu.add_command(label="Exit", command= close_window)

menu.add_cascade(label="Histogram", menu=histMenu)
histMenu.add_command(label="Bandwise Histograms")
histMenu.add_command(label="Band1 Histogram", command= b_h1)
histMenu.add_command(label="Band2 Histogram", command= b_h2)
histMenu.add_command(label="Band3 Histogram", command= b_h3)
histMenu.add_command(label="Band4 Histogram", command= b_h4)
histMenu.add_command(label="Band5 Histogram", command= b_h5)
histMenu.add_command(label="Band Ratio Histogram", command= b_h6)
histMenu.add_command(label="Band7 Histogram", command= b_h7)
histMenu.add_command(label="Band8 Histogram", command= b_h8)
histMenu.add_command(label="Band9 Histogram", command= b_h9)
histMenu.add_command(label="Band10 Histogram", command= b_h10)
histMenu.add_command(label="Band11 Histogram", command= b_h11) 
histMenu.add_command(label="Band12 Histogram", command= b_h12)

menu.add_cascade(label="Band Image", menu= bimgMenu)
bimgMenu.add_command(label="Band Image")
bimgMenu.add_command(label="Band 1 Image", command= b1_img)
bimgMenu.add_command(label="Band 2 Image", command= b2_img)
bimgMenu.add_command(label="Band 3 Image", command= b3_img)
bimgMenu.add_command(label="Band 4 Image", command= b4_img)
bimgMenu.add_command(label="Band 5 Image", command= b5_img)
bimgMenu.add_command(label="Band 6 Image", command= b6_img)
bimgMenu.add_command(label="Band 7 Image", command= b7_img)
bimgMenu.add_command(label="Band 8 Image", command= b8_img)
bimgMenu.add_command(label="Band 9 Image", command= b9_img)
bimgMenu.add_command(label="Band 10 Image", command= b10_img)
bimgMenu.add_command(label="Band 11 Image", command= b11_img)
bimgMenu.add_command(label="Band 12 Image", command= b12_img)


#C = Canvas(root, bg="blue", height=250, width=300)
#filename = PhotoImage(file = "C:\\Users\\Pranjal\\Desktop\\Python\\ass.gif")
#background_label = Label(root, image=filename)
#background_label.place(x=0, y=0, relwidth=1, relheight=1)
#C.pack()

def no_bands():
    raster = rasterio.open(file1)
    c= raster.count
    label2= Label(root, text= c, padx=2, pady=2).grid(row=2,column=1)

def dimensions():
    raster = rasterio.open(file1)
    a= raster.width 
    b= raster.height
    label3= Label(root, text= b, padx=2, pady=2).grid(row=3,column=1)
    label4= Label(root, text= a, padx=2, pady=2).grid(row=3,column=2)

# FOR BAND-WISE HISTOGRAM DISPLAY USING RASTERIO
def call():
    raster = rasterio.open(file1)
    fig= show_hist(raster, bins=50, lw=0.0, stacked=False, alpha=0.3, histtype='stepfilled', title="Histogram")


# FUNCTION TO EXECUTE NDVI USING RASTERIO
def NDVI():
    # Open a GDAL dataset
    #dataset = rasterio.open(file1)
    dataset = gdal.Open(file1 , gdal.GA_ReadOnly)

    # Allocate our array using the first band's datatype
    image_datatype = dataset.GetRasterBand(1).DataType

    image = np.zeros((dataset.RasterYSize, dataset.RasterXSize, dataset.RasterCount),
                 dtype=gdal_array.GDALTypeCodeToNumericTypeCode(image_datatype))

    # Loop over all bands in dataset
    for b in range(dataset.RasterCount):
    # Remember, GDAL index is on 1, but Python is on 0 -- so we add 1 for our GDAL calls
        band = dataset.GetRasterBand(b + 1)
    
    # Read in the band's data into the third dimension of our array
        image[:, :, b] = band.ReadAsArray()
    
    print('Red band mean: {r}'.format(r=image[:, :, 2].mean()))
    print('NIR band mean: {nir}'.format(nir=image[:, :, 3].mean()))
    b_red = 2
    b_nir = 3
    ndvi = (image[:, :, 3].mean() - image[:, :, 2].mean()) / (image[:, :, 3].mean() + image[:, :, 2].mean())
    print(ndvi)
    label6= Label(root, text= ndvi, padx=2, pady=2).grid(row=5,column=1)

def GNDVI():
    # Open a GDAL dataset
    #raster = rasterio.open(file1)
    dataset = gdal.Open(file1 , gdal.GA_ReadOnly)

    # Allocate our array using the first band's datatype
    image_datatype = dataset.GetRasterBand(1).DataType

    image = np.zeros((dataset.RasterYSize, dataset.RasterXSize, dataset.RasterCount),
                 dtype=gdal_array.GDALTypeCodeToNumericTypeCode(image_datatype))

    # Loop over all bands in dataset
    for b in range(dataset.RasterCount):
    # Remember, GDAL index is on 1, but Python is on 0 -- so we add 1 for our GDAL calls
        band = dataset.GetRasterBand(b + 1)
    
    # Read in the band's data into the third dimension of our array
        image[:, :, b] = band.ReadAsArray()
    
    b_green = 1
    b_nir = 3
    gndvi = (image[:, :, 3].mean() - image[:, :, 1].mean()) / (image[:, :, 3].mean() + image[:, :, 1].mean())
    print(gndvi)
    label15= Label(root, text= gndvi, padx=2, pady=2).grid(row=15,column=1)
    
def ndvi_img():
    raster = rasterio.open(file1)
    red = raster.read(4)
    nir = raster.read(5)
    red   
    nir
    type(nir)
    red = red.astype(float)
    nir = nir.astype(float)
    nir
    np.seterr(divide='ignore', invalid='ignore')
    check = np.logical_or ( red > 0, nir > 0 )
    ndvi = (nir.astype(float) - red.astype(float)) / (nir + red)   
    # Set spatial characteristics of the output object to mirror the input
    kwargs = raster.meta
    kwargs.update(
        dtype=rasterio.float32,
        count = 1)

    # Create the file
    with rasterio.open('ndvi.tif', 'w', **kwargs) as dst:
            dst.write_band(1, ndvi.astype(rasterio.float32))
    #scipy.misc.imsave('ndvi.tif',ndvi)
            ''''imgFile = cv2.imread('ndvi.tif',0)
            cv2.imshow('dst_rt', imgFile)
            cv2.waitKey(0)
            cv2.destroyAllWindows()'''
            img=cv2.imread('ndvi.tif',10)
            cv2.imshow('image',img)
            cv2.waitKey(0)
            cv2.destroyallwindows()
    

def ndvi_hist():
    raster = rasterio.open(file1)
    red = raster.read(4)
    nir = raster.read(5)
    red   
    nir
    type(nir)
    red = red.astype(float)
    nir = nir.astype(float)
    nir
    np.seterr(divide='ignore', invalid='ignore')
    check = np.logical_or ( red > 0, nir > 0 )
    ndvi = (nir.astype(float) - red.astype(float)) / (nir + red)
    ndvi
    fig=show_hist(ndvi, bins=50, lw=0.0, stacked=False,histtype='barstacked',alpha=0.3, title="Histogram")
    # Set spatial characteristics of the output object to mirror the input
    kwargs = src.meta
    kwargs.update(
        dtype=rasterio.float32,
        count = 1)

    # Create the file
    with rasterio.open('ndvi.tif', 'w', **kwargs) as dst:
            dst.write_band(1, ndvi.astype(rasterio.float32))
    label7= Label(root, image= show_hist, padx=2, pady=2).grid(row=8,column=1)

# FUNCTION TO EXECUTE BAND RATIO USING RASTERIO
def Band():
    # Open a GDAL dataset
    #raster = rasterio.open(file1)
    dataset = gdal.Open(file1 , gdal.GA_ReadOnly)
    # Allocate our array using the first band's datatype
    
    image_datatype = dataset.GetRasterBand(1).DataType

    image = np.zeros((dataset.RasterYSize, dataset.RasterXSize, dataset.RasterCount),
                 dtype=gdal_array.GDALTypeCodeToNumericTypeCode(image_datatype))

    # Loop over all bands in dataset
    for b in range(dataset.RasterCount):
    # Remember, GDAL index is on 1, but Python is on 0 -- so we add 1 for our GDAL calls
       band = dataset.GetRasterBand(b + 1)
    
    # Read in the band's data into the third dimension of our array
       image[:, :, b] = band.ReadAsArray()
    

    #print('Red band mean: {r}'.format(r=image[:, :, 2].mean()))
    #print('NIR band mean: {nir}'.format(nir=image[:, :, 3].mean()))
    b_red = 2
    b_nir = 3

    band_ratio = (image[:, :, 3].mean()/image[:, :, 2].mean())
    print(band_ratio)
    label8= Label(root, text= band_ratio, padx=2, pady=2).grid(row=8,column=1)

def band_hist():
    raster = rasterio.open(file1)
    s = range(0,13)
    s = e.get()
    band = raster.read(s)
    band
    show_hist(band, bins=50, lw=0.0, stacked=False, alpha=0.3, histtype='stepfilled', title="Histogram")
label9 = Label(root, text ="Enter Band Value for histogram:", padx=2, pady=2).grid(row= 10, column = 0, ipady=2, ipadx = 8)
global v
v= int()
v = range(0, 13)
e = Entry(root, textvariable=v)
e.grid(row = 10, column = 1)
e.bind('<Return>', band_hist)
#e.focus_set() 
#photo = PhotoImage(file = "ccc.gif")
#w = Label(root, image=photo)
#w.pack()


def BR_hist():
    raster = rasterio.open(file1)
    red = raster.read(4)
    nir = raster.read(5)
    type(nir)
    red = red.astype(float)
    nir = nir.astype(float)
    np.seterr(divide='ignore', invalid='ignore')
    check = np.logical_or ( red > 0, nir > 0 )
    BR = (nir.astype(float)/red.astype(float))
    
    scipy.misc.imsave('BR.tif',BR)
    imgFile = cv2.imread('BR.tif')
    cv2.imshow('dst_rt', imgFile)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    label10= Label(root, image= show_hist, padx=2, pady=2).grid(row=11,column=1)

def gndvi_hist():
    raster = rasterio.open(file1)
    green = raster.read(3)
    nir = raster.read(5)
    green   
    nir
    type(nir)
    green = green.astype(float)
    nir = nir.astype(float)
    nir
    np.seterr(divide='ignore', invalid='ignore')
    check = np.logical_or ( green > 0, nir > 0 )
    gndvi = (nir.astype(float) - green.astype(float)) / (nir + green)
    gndvi
    fig=show_hist(gndvi, bins=50, lw=0.0, stacked=False,histtype='barstacked',alpha=0.3, title="Histogram")

    # Set spatial characteristics of the output object to mirror the input
    kwargs = raster.meta
    kwargs.update(
        dtype=rasterio.float32,
        count = 1)
    

def savi_img():
    raster = rasterio.open(file1)
    red = raster.read(4)
    nir = raster.read(5)
    red   
    nir
    type(nir)
    red = red.astype(float)
    nir = nir.astype(float)
    nir
    np.seterr(divide='ignore', invalid='ignore')
    check = np.logical_or ( red > 0, nir > 0 )
    l= int()
    l = es.get()
    savi = (1+l)*(nir.astype(float) - red.astype(float)) / (nir + red+l)
    savi
    # Set spatial characteristics of the output object to mirror the input
    kwargs = src.meta
    kwargs.update(
        dtype=rasterio.float32,
        count = 1)

    # Create the file
    with rasterio.open('savi.tif', 'w', **kwargs) as dst:
            dst.wr.ite_band(1, savi.astype(rasterio.float32))
    #label11= Label(root, image= show_hist).grid(row=12,column=1)
l = range(0,1)    
es = Entry(root, textvariable= l)
es.grid(row = 14, column = 1)
es.bind('<Return>', savi_img)
#e.focus_set() 

def gndvi_img():
    raster = rasterio.open(file1)
    green = raster.read(3)
    nir = raster.read(5)
    green   
    nir
    type(nir)
    green = green.astype(float)
    nir = nir.astype(float)
    nir
    np.seterr(divide='ignore', invalid='ignore')
    check = np.logical_or ( green > 0, nir > 0 )
    gndvi = (nir.astype(float) - green.astype(float)) / (nir + green)
    gndvi
    
    # Set spatial characteristics of the output object to mirror the input
    kwargs = raster.meta
    kwargs.update(
        dtype=rasterio.float32,
        count = 1)

    # Create the file
    with rasterio.open('gndvi.tif', 'w', **kwargs) as dst:
            dst.write_band(1, gndvi.astype(rasterio.float32))
            
            
            
def br_hist():
    raster = rasterio.open(file1)
    red = raster.read(4)
    nir = raster.read(5)
    red   
    nir
    type(nir)
    red = red.astype(float)
    nir = nir.astype(float)
    nir
    np.seterr(divide='ignore', invalid='ignore')
    check = np.logical_or ( red > 0, nir > 0 )
    br = (nir.astype(float) / red.astype(float))
    br
    fig=show_hist(br, bins=50, lw=0.0, stacked=False,histtype='barstacked',alpha=0.3, title="Histogram")
    # Set spatial characteristics of the output object to mirror the input
    kwargs = src.meta
    kwargs.update(
        dtype=rasterio.float32,
        count = 1)

    # Create the file
    with rasterio.open('ndvi.tif', 'w', **kwargs) as dst:
            dst.write_band(1, ndvi.astype(rasterio.float32))
    label7= Label(root, image= show_hist, padx=2, pady=2).grid(row=15,column=1)

            

button_1 = Button(root, text="Enter your image!!", command=IMG , height=1, width=26, padx=2, pady=2 )
button_1.grid(row=1, sticky=W)


button2= Button(root, text="No. of Bands", command= no_bands, height=1, width=26, padx=2, pady=2)
button2.grid(row=2,)

button3= Button(root, text="Raster Dimensions: Height, Width", command= dimensions, height=1, width=26, padx=2, pady=2)
button3.grid(row=3,)

button4= Button(root, text="Band-wise Histogram", command=call, height=1, width=26, padx=2, pady=2)
button4.grid(row=4,sticky=W)

button5= Button(root, text="NDVI Mean Value", command= NDVI,  height=1, width=26, padx=2, pady=2)
button5.grid(row=5,sticky=W)

button15= Button(root, text="GNDVI Mean Value", command= GNDVI,  height=1, width=26, padx=2, pady=2)
button15.grid(row=15,sticky=W)

button6= Button(root, text="Show NDVI Image", command=ndvi_img , height=1, width=26, padx=2, pady=2)
button6.grid(row=6, sticky=W)
    
button7= Button(root, text="Show NVDi Image Histogram", command= ndvi_hist , height=1, width=26, padx=2, pady=2)
button7.grid(row=7, sticky=W)

button8= Button(root, text="Calculate Band ratio", command=Band, height=1, width=26, padx=2, pady=2)
button8.grid(row=8 ,sticky=W)

button9= Button(root, text="Get band histogram", command=band_hist , height=1, width=26, padx=2, pady=2)
button9.grid(row=11 ,sticky=W)

button10= Button(root, text="Band ratio image", command=BR_hist, height=1, width=26, padx=2, pady=2)
button10.grid(row=12 ,sticky=W)

button11= Button(root, text="GNDVI Histogram", command=gndvi_hist, height=1, width=26, padx=2, pady=2)
button11.grid(row=13 ,sticky=W)

button12= Button(root, text="SAVI Histogram", command=savi_img, height=1, width=26, padx=2, pady=2)
button12.grid(row=14 ,sticky=W)
#label10= Label(root, image= show_hist).grid(row=11,column=1)
button13= Button(root, text="GNDVI Image", command=gndvi_img, height=1, width=26, padx=2, pady=2)
button13.grid(row=15 ,sticky=W)
button14= Button(root, text="Band Ratio Histogram", command=br_hist, height=1, width=26, padx=2, pady=2)
button14.grid(row=16 ,sticky=W)





root.mainloop()
