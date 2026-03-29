

# 文件: tutorial/avframe_ocv/README.md

---

# avframe_ocv例程

### 1.说明

实现avframe到cv::Mat的转换过程，本例程支持在1684&X的SoC和PCIE上使用，1688和CV186H暂不支持，原因是ffmpeg版本更新，一些接口发生变化，具体信息可参考[FFmpeg接口改动](https://doc.sophgo.com/bm1688_sdk-docs/v1.7/docs_latest_release/docs/BM1688_CV186AH_SophonSDK_doc/appendix/4_compatibility_doc.html#ffmpeg)

### 2.样例测试

- [C++例程](./cpp)


# 文件: tutorial/avframe_ocv/cpp/README.md

---

# C++例程

## 目录

* [1. 环境准备](#1-环境准备)
    * [1.1 x86/arm PCIe平台](#11-x86arm-pcie平台)
    * [1.2 SoC平台](#12-soc平台)
* [2. 程序编译](#2-程序编译)
    * [2.1 x86/arm PCIe平台](#21-x86arm-pcie平台)
    * [2.2 SoC平台](#22-soc平台)
* [3. 推理测试](#3-推理测试)
    * [3.1 参数说明](#31-参数说明)
    * [3.2 测试图片](#32-测试图片)

cpp目录下提供了C++例程以供参考使用，具体情况如下：
| 序号  | C++例程      | 说明                                 |
| ---- | ------------- | -----------------------------------  |
| 1    | avframe_ocv | avframe到cv::Mat转换的例程 |

## 1. 环境准备
### 1.1 x86/arm PCIe平台
如果您在x86/arm平台安装了PCIe加速卡（如SC系列加速卡），可以直接使用它作为开发环境和运行环境。您需要安装libsophon、sophon-opencv和sophon-ffmpeg，具体步骤可参考[x86-pcie平台的开发和运行环境搭建](../../../docs/Environment_Install_Guide.md#3-x86-pcie平台的开发和运行环境搭建)或[arm-pcie平台的开发和运行环境搭建](../../../docs/Environment_Install_Guide.md#5-arm-pcie平台的开发和运行环境搭建)。

### 1.2 SoC平台
如果您使用SoC平台（如SE、SM系列边缘设备），刷机后在`/opt/sophon/`下已经预装了相应的libsophon、sophon-opencv和sophon-ffmpeg运行库包，可直接使用它作为运行环境。通常还需要一台x86主机作为开发环境，用于交叉编译C++程序。


## 2. 程序编译
C++程序运行前需要编译可执行文件。
### 2.1 x86/arm PCIe平台
可以直接在PCIe平台上编译程序：
```bash
mkdir build && cd build
cmake .. 
make
cd ..
```
编译完成后，会在当前目录下生成avframe_ocv.pcie。

### 2.2 SoC平台
通常在x86主机上交叉编译程序，您需要在x86主机上使用SOPHON SDK搭建交叉编译环境，将程序所依赖的头文件和库文件打包至soc-sdk目录中，具体请参考[交叉编译环境搭建](../../../docs/Environment_Install_Guide.md#41-交叉编译环境搭建)。本例程主要依赖libsophon、sophon-opencv和sophon-ffmpeg运行库包。

交叉编译环境搭建好后，使用交叉编译工具链编译生成可执行文件：
```bash
mkdir build && cd build
#请根据实际情况修改-DSDK的路径，需使用绝对路径。
cmake -DTARGET_ARCH=soc -DSDK=/path_to_sdk/soc-sdk ..  
make
```
编译完成后，会在当前目录下生成avframe_ocv.soc。

## 3. 测试
对于PCIe平台，可以直接在PCIe平台上测试；对于SoC平台，需将交叉编译生成的可执行文件及所需的模型、测试数据拷贝到SoC平台中测试。测试的参数及运行方式是一致的，下面主要以PCIe模式进行介绍。

### 3.1 参数说明
可执行程序默认有一套参数，请注意根据实际情况进行传参，`avframe_ocv.pcie与avframe_ocv.soc参数相同。`以avframe_ocv.pcie为例，具体参数说明如下：
```bash
usage:
        ./avframe_ocv.pcie <input_video> [dev_id] 
params:
        input_video: video for decode to get avframe
        dev_id:  using device id, default 0
```
### 3.2 测试视频
测试实例如下
```bash
./avframe_ocv.pcie test_car_person_1080P.mp4 0
```
测试结束后，会将avframe转换后的mat保存到当前文件夹下。

### 3.3 程序说明
本例程通过ffmpeg解码视频得到avframe。

yuv mat是sophon-opencv中mat的扩展数据结构，一般由avframe生成。yuv mat可以通过mat.u->frame得到其中的avframe。

从avframe到普通cv::mat的流程是，从avframe构造yuv mat，yuv mat 通过tomat方法得到普通cv::mat，然后释放yuv mat/avframe。

例程中两个函数是avframe转换到普通cv::mat的不同情况：

avframe_to_cvmat1中，根据avframe生成的yuv mat可以同时管理其中的avframe的释放，当yuv mat调用release的时候，其中的avframe也会自动释放。

avframe_to_cvmat2中，avframe和其生成的yuv mat的释放是相互独立的。此时需要通过调用av_frame_free手动释放avframe，否则会有内存泄漏。


# 文件: tutorial/blend/cpp/blend_bmcv/README.md

---


# C++例程

## 目录

* [1. 环境准备](#1-环境准备)
    * [1.1 SoC平台](#12-soc平台)
* [2. 程序编译](#2-程序编译)
    * [2.1 SoC平台](#21-soc平台)
* [3. 推理测试](#3-推理测试)
    * [3.1 参数说明](#31-参数说明)
    * [3.2 测试图片](#32-测试图片)

cpp目录下提供了C++例程以供参考使用，具体情况如下：
| 序号  | C++例程      | 说明                                 |
| ---- | ------------- | -----------------------------------  |
| 1    | [blend_bmcv](./blend_bmcv) | 使用BMCV接口做融合拼接 |

## 1. 环境准备
### 1.1 SoC平台
如果您使用SoC平台（如SE、SM系列边缘设备），刷机后在`/opt/sophon/`下已经预装了相应的libsophon、sophon-opencv和sophon-ffmpeg运行库包，可直接使用它作为运行环境。通常还需要一台x86主机作为开发环境，用于交叉编译C++程序。

## 2. 程序编译
C++程序运行前需要编译可执行文件，目前该功能只支持在BM1688/CV186X(SoC)上使用。

### 2.1 SoC平台
通常在x86主机上交叉编译程序，您需要在x86主机上使用SOPHON SDK搭建交叉编译环境，将程序所依赖的头文件和库文件打包至soc-sdk目录中，具体请参考[交叉编译环境搭建](../../../docs/Environment_Install_Guide.md#41-交叉编译环境搭建)。本例程主要依赖libsophon、sophon-opencv和sophon-ffmpeg运行库包。

交叉编译环境搭建好后，使用交叉编译工具链编译生成可执行文件：
#### 2.1.1 bmcv
```bash
cd cpp/blend_bmcv
mkdir build && cd build
#请根据实际情况修改-DSDK的路径，需使用绝对路径。
cmake -DTARGET_ARCH=soc -DSDK=/path_to_sdk/soc-sdk ..  
make
```
编译完成后，会在blend_bmcv目录下生成bmcv_blend.soc。


## 3. 测试
对于PCIe平台，可以直接在PCIe平台上测试；对于SoC平台，需将交叉编译生成的可执行文件及所需的模型、测试数据拷贝到SoC平台中测试。测试的参数及运行方式是一致的，下面主要以PCIe模式进行介绍。首先，下载测试包：
```bash
python3 -m dfss --url=open@sophgo.com:sophon-demo/tutorial/bmcv_blend/data.tar.gz
tar -xvf data.tar.gz
```

### 3.1 参数说明
可执行程序默认有一套参数，请注意根据实际情况进行传参。`bmcv_blend.pcie为例，具体参数说明如下：
```bash
Usage: 
./bmcv_blend.pcie <left image_path> <right image_path> <left wgt> <right wgt>
```
### 3.2 测试图片
图片测试实例如下。
```bash
./bmcv_blend.soc ./data/left.jpg ./data/right.jpg ./data/c01_alpha12_444p_m2__0_288x2304.bin ./data/c01_beta12_444p_m2__0_288x2304.bin
```
测试结束后，会将缩放后的图片保存为当前文件夹下blend_image.jpg。


## 4. 权重生成方法
### 4.1 工具准备

```bash
pip3 install dfss -i https://pypi.tuna.tsinghua.edu.cn/simple --upgrade
python3 -m dfss --url=open@sophgo.com:sophon-demo/tutorial/bmcv_blend/blend_2im_v20240508.zip
```

### 4.2 权重生成
具体方法暂时先参照：blend_2im_v20240508.zip文件中的广角拼接调试指南.docx



# 文件: tutorial/bm1688_2core2task_yolov5/README.md

---

# bm1688_2core2task_yolov5例程

### 1.说明

这是一个在BM1688上运行双核双任务的例子，BM1688的TPU有两个npu core，“双核双任务”的意思就是在这两个npu core上分别跑一个bmodel。
该例程的重点在于指导用户如何使用BM1688的双核推理功能，没有后处理加速、前后处理/推理并行功能，如果您需要其他版本的教程，可以参考[YOLOv5例程](../../sample/YOLOv5/README.md#22-算法特性).

### 2.准备数据

可以通过如下命令下载测试视频和模型：
```bash
mkdir -p datasets
mkdir -p models/BM1688
pip3 install dfss --upgrade
python3 -m dfss --url=open@sophgo.com:sophon-demo/common/test_car_person_1080P.mp4
python3 -m dfss --url=open@sophgo.com:sophon-demo/tutorials/bm1688_2core2task_yolov5/yolov5s_v6.1_3output_int8_4b.bmodel
python3 -m dfss --url=open@sophgo.com:sophon-demo/common/coco.names
mv test_car_person_1080P.mp4 datasets/
mv yolov5s_v6.1_3output_int8_4b.bmodel models/BM1688
mv coco.names datasets/
```
模型来源：[YOLOv5例程](../../sample/YOLOv5/README.md#3-准备模型与数据)

### 3.样例测试

- [C++例程](./cpp/README.md)
- [Python例程](./python/README.md)

# 文件: tutorial/bm1688_2core2task_yolov5/cpp/README.md

---

# C++例程

## 目录

* [1. 环境准备](#1-环境准备)
    * [1.1 x86/arm PCIe平台](#11-x86arm-pcie平台)
    * [1.2 SoC平台](#12-soc平台)
* [2. 程序编译](#2-程序编译)
    * [2.1 x86/arm PCIe平台](#21-x86arm-pcie平台)
    * [2.2 SoC平台](#22-soc平台)
* [3. 推理测试](#3-推理测试)
    * [3.1 参数说明](#31-参数说明)
    * [3.2 测试视频](#32-测试视频)

cpp目录下提供了C++例程以供参考使用，具体情况如下：
| 序号  | C++例程      | 说明                                 |
| ---- | ------------- | -----------------------------------  |
| 1    | yolov5_bmcv | 一个调用sophon-openCV解码、BMCV前处理、BMRT推理的多路YOLOv5检测例程，第N路视频流会在第N%2个npu core做推理 |

## 1. 环境准备
### 1.1 x86/arm PCIe平台
BM1688暂不支持x86/arm PCIe平台。

### 1.2 SoC平台
如果您使用SoC平台（如SE、SM系列边缘设备），刷机后在`/opt/sophon/`下已经预装了相应的libsophon、sophon-opencv和sophon-ffmpeg运行库包，可直接使用它作为运行环境。通常还需要一台x86主机作为开发环境，用于交叉编译C++程序。


## 2. 程序编译
C++程序运行前需要编译可执行文件。
### 2.1 x86/arm PCIe平台
BM1688暂不支持x86/arm PCIe平台。

### 2.2 SoC平台
通常在x86主机上交叉编译程序，您需要在x86主机上使用SOPHON SDK搭建交叉编译环境，将程序所依赖的头文件和库文件打包至soc-sdk目录中，具体请参考[交叉编译环境搭建](../../../docs/Environment_Install_Guide.md#41-交叉编译环境搭建)。本例程主要依赖libsophon、sophon-opencv和sophon-ffmpeg运行库包。

交叉编译环境搭建好后，使用交叉编译工具链编译生成可执行文件：
```bash
mkdir build && cd build
#请根据实际情况修改-DSDK的路径，需使用绝对路径。
cmake -DTARGET_ARCH=soc -DSDK=/path_to_sdk/soc-sdk ..  
make
```
编译完成后，会在当前目录下生成yolov5_bmcv.soc。

## 3. 推理测试
对于SoC平台，需将交叉编译生成的可执行文件及所需的模型、测试数据拷贝到SoC平台中测试。

### 3.1 参数说明
可执行程序默认有一套参数，请注意根据实际情况进行传参，以yolov5_bmcv.soc为例，具体参数说明如下：
```bash
Usage: yolov5_bmcv.soc [params]

        --bmodel (value:../../models/BM1688/yolov5s_v6.1_3output_int8_4b.bmodel)
                bmodel file path
        --chan_num (value:2)
                copy the input video into chan_num copies
        --classnames (value:../../datasets/coco.names)
                class names file path
        --conf_thresh (value:0.5)
                confidence threshold for filter boxes
        --dev_id (value:0)
                TPU device id
        --help (value:true)
                print help information.
        --input (value:../../datasets/test_car_person_1080P.mp4)
                input video file path
        --nms_thresh (value:0.5)
                iou threshold for nms
```
### 3.2 测试视频
2路测试实例如下：
```bash
./yolov5_bmcv.soc --chan_num=2
```
测试结束后，会将视频中的帧以jpg图片的形式保存在`results/images_chan_N`中，N表示第N路。

测试过程中，您可以通过如下命令查看BM1688两个npu core的占用情况：
```bash
cat /sys/class/bm-tpu/bm-tpu0/device/npu_usage
```

# 文件: tutorial/bm1688_2core2task_yolov5/python/README.md

---

# Python例程

## 目录

- [Python例程](#python例程)
  - [目录](#目录)
  - [1. 环境准备](#1-环境准备)
    - [1.1 x86/arm PCIe平台](#11-x86arm-pcie平台)
    - [1.2 SoC平台](#12-soc平台)
  - [2. 推理测试](#2-推理测试)
    - [2.1 参数说明](#21-参数说明)
    - [2.2 测试视频](#22-测试视频)

python目录下提供了python例程以供参考使用，具体情况如下：
| 序号  |   Python例程     |                                           说明                                                       |
| ---- | ---------------- | --------------------------------------------------------------------------------------------------- |
| 1    | yolov5_bmcv.py   |      一个调用SAIL解码、BMCV前处理、SAIL推理的多路YOLOv5检测例程，第N路视频流会在第N%2个npu core做推理          |

## 1. 环境准备
### 1.1 x86/arm PCIe平台
BM1688暂不支持x86/arm PCIe平台。

### 1.2 SoC平台
如果您使用SoC平台（如SE、SM系列边缘设备），并使用它测试本例程，刷机后在`/opt/sophon/`下已经预装了相应的libsophon、sophon-opencv和sophon-ffmpeg运行库包，可直接使用它作为运行环境。

此外，您还需要安装其他第三方库：
```bash
pip3 install opencv-python opencv-python-headless
```
由于本例程需要的sophon-sail版本较新，这里提供一个可用的sophon-sail whl包，SoC环境下可用以下命令下载和安装：
```bash
pip3 install dfss --upgrade
python3 -m dfss --url=open@sophgo.com:sophon-demo/ChatGLM3/sail/soc/SE9/sophon-3.8.0-py3-none-any.whl #arm soc, py38, for SE9
pip3 install sophon-3.8.0-py3-none-any.whl
```
如果您需要其他python版本的sophon-sail，可以参考[SoC平台交叉编译安装sophon-sail](../../../docs/Environment_Install_Guide.md#42-交叉编译安装sophon-sail)，到官网下载sophon-sail (sail的版本>=v3.8.0,对应BM1684&BM1684X SDK>=V24.04.01, BM1688&CV186AH SDK>=V1.6.0)自己编译。

## 2. 推理测试
python例程不需要编译，可以直接运行。
### 2.1 参数说明
可执行程序默认有一套参数，请注意根据实际情况进行传参，以yolov5_bmcv.py为例，具体参数说明如下：
```bash
Usage: yolov5_bmcv.py [params]

        --bmodel (value:../models/BM1688/yolov5s_v6.1_3output_int8_4b.bmodel)
                bmodel file path
        --chan_num (value:2)
                copy the input video into chan_num copies
        --classnames (value:../datasets/coco.names)
                class names file path
        --conf_thresh (value:0.5)
                confidence threshold for filter boxes
        --dev_id (value:0)
                TPU device id
        --input (value:../datasets/test_car_person_1080P.mp4)
                input video file path
        --nms_thresh (value:0.5)
                iou threshold for nms
```
### 2.2 测试视频
2路测试实例如下：
```bash
python3 yolov5_bmcv.py --chan_num=2
```
测试结束后，会将视频中的帧以jpg图片的形式保存在`results/images_chan_N`中，N表示第N路。

测试过程中，您可以通过如下命令查看BM1688两个npu core的占用情况：
```bash
cat /sys/class/bm-tpu/bm-tpu0/device/npu_usage
```

# 文件: tutorial/crop_and_resize_padding/README.md

---

# crop_and_resize_padding例程

### 1.说明

实现将图片指定位置指定大小部分图片抠出，缩放后填充到大图中，空余部分填充指定像素数值的功能，支持在 BM1688、CV186H、BM1684X 以及 BM1684 的 SoC 和 PCIE 模式下使用。

### 2.样例测试

- [C++例程](./cpp)
- [Python例程](./python)

# 文件: tutorial/crop_and_resize_padding/cpp/README.md

---

# C++例程

## 目录

* [1. 环境准备](#1-环境准备)
    * [1.1 x86/arm PCIe平台](#11-x86arm-pcie平台)
    * [1.2 SoC平台](#12-soc平台)
* [2. 程序编译](#2-程序编译)
    * [2.1 x86/arm PCIe平台](#21-x86arm-pcie平台)
    * [2.2 SoC平台](#22-soc平台)
* [3. 推理测试](#3-推理测试)
    * [3.1 参数说明](#31-参数说明)
    * [3.2 测试图片](#32-测试图片)

cpp目录下提供了C++例程以供参考使用，具体情况如下：
| 序号  | C++例程      | 说明                                 |
| ---- | ------------- | -----------------------------------  |
| 1    | [crop_and_resize_padding_bmcv](./crop_and_resize_padding_bmcv) | 使用BMC接口做裁剪 |
| 2    | [crop_and_resize_padding_sail](./crop_and_resize_padding_bmcv) | 使用SAIL接口做裁剪 |

## 1. 环境准备
### 1.1 x86/arm PCIe平台
如果您在x86/arm平台安装了PCIe加速卡（如SC系列加速卡），可以直接使用它作为开发环境和运行环境。您需要安装libsophon、sophon-opencv和sophon-ffmpeg，具体步骤可参考[x86-pcie平台的开发和运行环境搭建](../../../docs/Environment_Install_Guide.md#3-x86-pcie平台的开发和运行环境搭建)或[arm-pcie平台的开发和运行环境搭建](../../../docs/Environment_Install_Guide.md#5-arm-pcie平台的开发和运行环境搭建)。

### 1.2 SoC平台
如果您使用SoC平台（如SE、SM系列边缘设备），刷机后在`/opt/sophon/`下已经预装了相应的libsophon、sophon-opencv和sophon-ffmpeg运行库包，可直接使用它作为运行环境。通常还需要一台x86主机作为开发环境，用于交叉编译C++程序。


## 2. 程序编译
C++程序运行前需要编译可执行文件。
### 2.1 x86/arm PCIe平台
可以直接在PCIe平台上编译程序：
#### 2.1.1 bmcv
```bash
cd cpp/crop_and_resize_padding_bmcv
mkdir build && cd build
cmake .. 
make
cd ..
```
编译完成后，会在crop_and_resize_padding_bmcv目录下生成crop_and_resize_padding_bmcv.pcie。

#### 2.1.2 sail
如果您使用sophon-sail接口，需要[编译安装sophon-sail](../../../docs/Environment_Install_Guide.md#33-编译安装sophon-sail)，然后进行如下步骤。
```bash
cd cpp/crop_and_resize_padding_sail
mkdir build && cd build
cmake ..
make
cd ..
```
编译完成后，会在crop_and_resize_padding_sail目录下生成crop_and_resize_padding_sail.pcie。

### 2.2 SoC平台
通常在x86主机上交叉编译程序，您需要在x86主机上使用SOPHON SDK搭建交叉编译环境，将程序所依赖的头文件和库文件打包至soc-sdk目录中，具体请参考[交叉编译环境搭建](../../../docs/Environment_Install_Guide.md#41-交叉编译环境搭建)。本例程主要依赖libsophon、sophon-opencv和sophon-ffmpeg运行库包。

交叉编译环境搭建好后，使用交叉编译工具链编译生成可执行文件：
#### 2.2.1 bmcv
```bash
cd cpp/crop_and_resize_padding_bmcv
mkdir build && cd build
#请根据实际情况修改-DSDK的路径，需使用绝对路径。
cmake -DTARGET_ARCH=soc -DSDK=/path_to_sdk/soc-sdk ..  
make
```
编译完成后，会在crop_and_resize_padding_bmcv目录下生成crop_and_resize_padding_bmcv.soc。

#### 2.2.2 sail
如果您使用sophon-sail接口，需要参考[交叉编译安装sophon-sail](../../../docs/Environment_Install_Guide.md#42-交叉编译安装sophon-sail)，给soc环境配置sophon-sail，然后进行如下步骤。
```bash
cd cpp/crop_and_resize_padding_sail
mkdir build && cd build
#请根据实际情况修改-DSDK和-DSAIL_PATH的路径，需使用绝对路径。
cmake -DTARGET_ARCH=soc -DSDK=/path_to_sdk/soc-sdk -DSAIL_PATH=/path_to_sail/sophon-sail/build_soc/sophon-sail ..
make
```
编译完成后，会在crop_and_resize_padding_sail目录下生成crop_and_resize_padding_sail.soc。

## 3. 测试
对于PCIe平台，可以直接在PCIe平台上测试；对于SoC平台，需将交叉编译生成的可执行文件及所需的模型、测试数据拷贝到SoC平台中测试。测试的参数及运行方式是一致的，下面主要以PCIe模式进行介绍。

### 3.1 参数说明
可执行程序默认有一套参数，请注意根据实际情况进行传参，`resize_bmcv.pcie与resize_sail.pcie参数相同。`以crop_and_resize_padding_bmcv.pcie为例，具体参数说明如下：
```bash
Usage: 
./crop_and_resize_padding_bmcv.pcie <image path>
```
### 3.2 测试图片
图片测试实例如下
```bash
./crop_and_resize_padding_bmcv.pcie ../../datasets/test/zidane.jpg
```
测试结束后，会将处理后的图片保存为当前文件夹下crop_and_resize_padding.jpg。


# 文件: tutorial/crop_and_resize_padding/python/README.md

---

# Python例程

## 目录

* [1. 环境准备](#1-环境准备)
    * [1.1 x86/arm PCIe平台](#11-x86arm-pcie平台)
    * [1.2 SoC平台](#12-soc平台)
* [2. 推理测试](#2-推理测试)
    * [2.1 参数说明](#21-参数说明)
    * [2.2 测试图片](#22-测试图片)
    * [2.3 测试视频](#23-测试视频)

python目录下提供了一系列Python例程，具体情况如下：

| 序号 |  Python例程      | 说明                                |
| ---- | ---------------- | -----------------------------------  |
| 1    | [crop_and_resize_padding.py](./crop_and_resize_padding.py) | 使用SAIL将图片指定位置指定大小部分图片抠出，缩放后填充到大图中，空余部分填充指定像素数值 |

## 1. 环境准备
### 1.1 x86/arm PCIe平台

如果您在x86/arm平台安装了PCIe加速卡（如SC系列加速卡），并使用它测试本例程，您需要安装libsophon、sophon-opencv、sophon-ffmpeg和sophon-sail，具体请参考[x86-pcie平台的开发和运行环境搭建](../../../docs/Environment_Install_Guide.md#3-x86-pcie平台的开发和运行环境搭建)或[arm-pcie平台的开发和运行环境搭建](../../../docs/Environment_Install_Guide.md#5-arm-pcie平台的开发和运行环境搭建)。

### 1.2 SoC平台

如果您使用SoC平台（如SE、SM系列边缘设备），并使用它测试本例程，刷机后在`/opt/sophon/`下已经预装了相应的libsophon、sophon-opencv和sophon-ffmpeg运行库包。您还需要交叉编译安装sophon-sail，具体可参考[交叉编译安装sophon-sail](../../../docs/Environment_Install_Guide.md#42-交叉编译安装sophon-sail)。

## 2. 测试
python例程不需要编译，可以直接运行，PCIe平台和SoC平台的测试参数和运行方式是相同的。
### 2.1 参数说明
```bash
usage: crop_and_resize_padding.py [-h] [--image_path IMAGE_PATH]

optional arguments:
  -h, --help            show this help message and exit
  --image_path IMAGE_PATH
                        input image path
```

### 2.2 测试图片
图片测试实例如下
```bash
python3 python/crop.py --image_path ../datasets/test/zidane.jpg
```
测试结束后，会将处理后的图片保存为当前文件夹下crop_and_resize_padding.jpg。


# 文件: tutorial/crop/cpp/README.md

---

# C++例程

## 目录

* [1. 环境准备](#1-环境准备)
    * [1.1 x86/arm PCIe平台](#11-x86arm-pcie平台)
    * [1.2 SoC平台](#12-soc平台)
* [2. 程序编译](#2-程序编译)
    * [2.1 x86/arm PCIe平台](#21-x86arm-pcie平台)
    * [2.2 SoC平台](#22-soc平台)
* [3. 推理测试](#3-推理测试)
    * [3.1 参数说明](#31-参数说明)
    * [3.2 测试图片](#32-测试图片)

cpp目录下提供了C++例程以供参考使用，具体情况如下：
| 序号  | C++例程      | 说明                                 |
| ---- | ------------- | -----------------------------------  |
| 1    | [crop_bmcv](./crop_bmcv) | 使用BMC接口做裁剪 |
| 2    | [crop_sail](./crop_sail) | 使用SAIL接口做裁剪 |

## 1. 环境准备
### 1.1 x86/arm PCIe平台
如果您在x86/arm平台安装了PCIe加速卡（如SC系列加速卡），可以直接使用它作为开发环境和运行环境。您需要安装libsophon、sophon-opencv和sophon-ffmpeg，具体步骤可参考[x86-pcie平台的开发和运行环境搭建](../../../docs/Environment_Install_Guide.md#3-x86-pcie平台的开发和运行环境搭建)或[arm-pcie平台的开发和运行环境搭建](../../../docs/Environment_Install_Guide.md#5-arm-pcie平台的开发和运行环境搭建)。

### 1.2 SoC平台
如果您使用SoC平台（如SE、SM系列边缘设备），刷机后在`/opt/sophon/`下已经预装了相应的libsophon、sophon-opencv和sophon-ffmpeg运行库包，可直接使用它作为运行环境。通常还需要一台x86主机作为开发环境，用于交叉编译C++程序。


## 2. 程序编译
C++程序运行前需要编译可执行文件。
### 2.1 x86/arm PCIe平台
可以直接在PCIe平台上编译程序：
#### 2.1.1 bmcv
```bash
cd cpp/crop_bmcv
mkdir build && cd build
cmake .. 
make
cd ..
```
编译完成后，会在crop_bmcv目录下生成crop_bmcv.pcie。

#### 2.1.2 sail
如果您使用sophon-sail接口，需要[编译安装sophon-sail](../../../docs/Environment_Install_Guide.md#33-编译安装sophon-sail)，然后进行如下步骤。
```bash
cd cpp/crop_sail
mkdir build && cd build
cmake ..
make
cd ..
```
编译完成后，会在crop_sail目录下生成crop_sail.pcie。

### 2.2 SoC平台
通常在x86主机上交叉编译程序，您需要在x86主机上使用SOPHON SDK搭建交叉编译环境，将程序所依赖的头文件和库文件打包至soc-sdk目录中，具体请参考[交叉编译环境搭建](../../../docs/Environment_Install_Guide.md#41-交叉编译环境搭建)。本例程主要依赖libsophon、sophon-opencv和sophon-ffmpeg运行库包。

交叉编译环境搭建好后，使用交叉编译工具链编译生成可执行文件：
#### 2.2.1 bmcv
```bash
cd cpp/crop_bmcv
mkdir build && cd build
#请根据实际情况修改-DSDK的路径，需使用绝对路径。
cmake -DTARGET_ARCH=soc -DSDK=/path_to_sdk/soc-sdk ..  
make
```
编译完成后，会在crop_bmcv目录下生成crop_bmcv.soc。

#### 2.2.2 sail
如果您使用sophon-sail接口，需要参考[交叉编译安装sophon-sail](../../../docs/Environment_Install_Guide.md#42-交叉编译安装sophon-sail)，给soc环境配置sophon-sail，然后进行如下步骤。
```bash
cd cpp/crop_sail
mkdir build && cd build
#请根据实际情况修改-DSDK和-DSAIL_PATH的路径，需使用绝对路径。
cmake -DTARGET_ARCH=soc -DSDK=/path_to_sdk/soc-sdk -DSAIL_PATH=/path_to_sail/sophon-sail/build_soc/sophon-sail ..
make
```
编译完成后，会在crop_sail目录下生成crop_sail.soc。

## 3. 测试
对于PCIe平台，可以直接在PCIe平台上测试；对于SoC平台，需将交叉编译生成的可执行文件及所需的模型、测试数据拷贝到SoC平台中测试。测试的参数及运行方式是一致的，下面主要以PCIe模式进行介绍。

### 3.1 参数说明
可执行程序默认有一套参数，请注意根据实际情况进行传参，`crop_bmcv.pcie与crop_sail.pcie参数相同。`以crop_bmcv.pcie为例，具体参数说明如下：
```bash
Usage: 
./crop_bmcv.pcie <image path>
```
### 3.2 测试图片
图片测试实例如下
```bash
./crop_bmcv.pcie ../../datasets/test/zidane.jpg
```
测试结束后，会将裁剪后的图片保存为当前文件夹下crop.jpg。


# 文件: tutorial/crop/python/README.md

---

# Python例程

## 目录

* [1. 环境准备](#1-环境准备)
    * [1.1 x86/arm PCIe平台](#11-x86arm-pcie平台)
    * [1.2 SoC平台](#12-soc平台)
* [2. 推理测试](#2-推理测试)
    * [2.1 参数说明](#21-参数说明)
    * [2.2 测试图片](#22-测试图片)
    * [2.3 测试视频](#23-测试视频)

python目录下提供了一系列Python例程，具体情况如下：

| 序号 |  Python例程      | 说明                                |
| ---- | ---------------- | -----------------------------------  |
| 1    | [crop.py](./crop.py) | 使用SAIL做裁剪 |

## 1. 环境准备
### 1.1 x86/arm PCIe平台

如果您在x86/arm平台安装了PCIe加速卡（如SC系列加速卡），并使用它测试本例程，您需要安装libsophon、sophon-opencv、sophon-ffmpeg和sophon-sail，具体请参考[x86-pcie平台的开发和运行环境搭建](../../../docs/Environment_Install_Guide.md#3-x86-pcie平台的开发和运行环境搭建)或[arm-pcie平台的开发和运行环境搭建](../../../docs/Environment_Install_Guide.md#5-arm-pcie平台的开发和运行环境搭建)。

### 1.2 SoC平台

如果您使用SoC平台（如SE、SM系列边缘设备），并使用它测试本例程，刷机后在`/opt/sophon/`下已经预装了相应的libsophon、sophon-opencv和sophon-ffmpeg运行库包。您还需要交叉编译安装sophon-sail，具体可参考[交叉编译安装sophon-sail](../../../docs/Environment_Install_Guide.md#42-交叉编译安装sophon-sail)。

## 2. 测试
python例程不需要编译，可以直接运行，PCIe平台和SoC平台的测试参数和运行方式是相同的。
### 2.1 参数说明
```bash
usage: crop.py [-h] [--image_path IMAGE_PATH]

optional arguments:
  -h, --help            show this help message and exit
  --image_path IMAGE_PATH
                        input image path
```

### 2.2 测试图片
图片测试实例如下
```bash
python3 python/crop.py --image_path ../datasets/test/zidane.jpg
```
测试结束后，会将裁剪后的图片保存为当前文件夹下crop.jpg。


# 文件: tutorial/DPU/README.md

---

[简体中文](./README.md) | [English](./README_EN.md)

# DPU例程

## 目录

- [DPU例程](#dpu例程)
  - [目录](#目录)
  - [1. 简介](#1-简介)
  - [2. 交叉编译及准备数据集](#2-交叉编译及准备数据集)
    - [2.1 程序编译](#21-程序编译)
    - [2.2 准备数据集](#22-准备数据集)
  - [3. 推理测试](#3-推理测试)
    - [3.1 参数说明](#31-参数说明)
    - [3.2 测试图片](#32-测试图片)
    - [3.3 DPU参数配置](#33-dpu参数配置)

## 1. 简介
本例程是双目深度的DPU实现。支持在BM1688/CV186X上测试。
DPU（Depth Process Unit）是BM1688/CV186X的深度处理单元：利用双目校正后的左、右图，计算出图像的视差/深度信息。具有如下两种功能。
- SGBM(Semi-Global Block Matching) :半全局块匹配算法，计算视差图。
- FGS（Fast Global Smooth）:快速全局平滑滤波，平滑视差图。视差转深度功能包含在FGS模块里。
当前支持两种处理模式： SGBM和Online(SGBM+FGS).

## 2. 交叉编译及准备数据集

### 2.1 程序编译
如果您使用SoC平台（如SE、SM系列边缘设备），刷机后在`/opt/sophon/`下已经预装了相应的libsophon、sophon-opencv和sophon-ffmpeg运行库包，可直接使用它作为运行环境。还需要一台x86主机作为开发环境，用于交叉编译C++程序。


C++程序运行前需要编译可执行文件。在x86主机上交叉编译程序，您需要在x86主机上使用SOPHON SDK搭建交叉编译环境，将程序所依赖的头文件和库文件打包至soc-sdk目录中，具体请参考[交叉编译环境搭建](../../../docs/Environment_Install_Guide.md#41-交叉编译环境搭建)。本例程主要依赖libsophon、sophon-opencv和sophon-ffmpeg运行库包。

交叉编译环境搭建好后，使用交叉编译工具链编译生成可执行文件：
```bash
cd cpp/dpu_bmcv
mkdir build && cd build
# 请根据实际情况修改-DSDK的路径，需使用绝对路径。
cmake -DTARGET_ARCH=soc -DSDK=/path_to_sdk/soc-sdk ..  
make
```
编译完成后，会在dpu_bmcv目录下生成dpu_bmcv.soc。

### 2.2 准备数据集

```bash
pip3 install dfss -i https://pypi.tuna.tsinghua.edu.cn/simple --upgrade
python3 -m dfss --url=open@sophgo.com:sophon-demo/LightStereo/KITTI12.tar.gz
tar xvf KITTI12.tar.gz && rm KITTI12.tar.gz
```

## 3. 推理测试
### 3.1 参数说明
可执行程序默认有一套参数，请注意根据实际情况进行传参，具体参数说明如下：
```bash
Usage:  dpu_demo.soc [params] 

        --dev_id (value:0)
                TPU device id
        --help (value:true)
                print help information.
        --mode (value:0)
                0: SGBM, 1: Online(SGBM+FGS)
        --input (value:KITTI12/kitti12_train194.txt)
                input path
        --output (value: results/images)
                output path
        --debug (value:0)
                0:do not save debug image, 1: save debug image
```

**注意：** CPP传参与python不同，需要用等于号，例如`./dpu_demo.soc --mode=xxx`。

### 3.2 测试图片

图片测试实例如下：
```bash
# 测试整个文件夹  
./dpu_demo.soc --input=../../KITTI12/kitti12_train194.txt
```
测试结束后，会将预测结果保存在`results/images`下，同时会打印推理时间等信息。


### 3.3 DPU参数配置

DPU支持以下参数配置，接口详情请参考算能官网--技术资料--BMCV文档。

1. SGBM参数：
```cpp
bmcv_dpu_sgbm_attrs sgbm_params;
sgbm_params.bfw_mode_en = DPU_BFW_MODE_5x5;        // 块匹配窗口大小
sgbm_params.disp_range_en = BMCV_DPU_DISP_RANGE_128; // 视差范围
sgbm_params.disp_start_pos = 0;                     // 视差起始位置
sgbm_params.dcc_dir_en = BMCV_DPU_DCC_DIR_A13;     // DCC方向
sgbm_params.dpu_census_shift = 1;                   // Census变换移位
sgbm_params.dpu_rshift1 = 0;                        // 右移1参数
sgbm_params.dpu_rshift2 = 2;                        // 右移2参数
sgbm_params.dpu_ca_p1 = 2880;                       // 代价聚合P1参数
sgbm_params.dpu_ca_p2 = 14400;                      // 代价聚合P2参数
sgbm_params.dpu_uniq_ratio = 0;                     // 唯一性比率
sgbm_params.dpu_disp_shift = 4;                     // 视差移位

dpu.setSGBMParams(sgbm_params);
```

2. FGS参数：
```cpp
bmcv_dpu_fgs_attrs fgs_params;
fgs_params.depth_unit_en = BMCV_DPU_DEPTH_UNIT_MM; // 深度单位
fgs_params.fgs_max_count = 19;                      // 最大迭代次数
fgs_params.fgs_max_t = 3;                           // 最大阈值
fgs_params.fxbase_line = 864000;                    // 基线参数

dpu.setFGSParams(fgs_params);
```



# 文件: tutorial/DWA/README.md

---

# DWA 例程


- [DWA 例程](#dwa-例程)
  - [1. 说明](#1-说明)
  - [2. 相机标定，数据准备](#2-相机标定数据准备)
  - [3. 样例测试](#3-样例测试)


## 1. 说明

DWA 是算能BM1688/CV186AH上的硬件去畸变仿射模块；具有几何畸变校正功能，通过校正镜头引起的图像畸变（针对桶形畸变 (Barrel Distortion) 及枕形畸变 (Pincushion Distortion) ），使图像中的直线变得更加准确和几何正确，提高图像的质量和可视化效果。

本例程是调用 bmcv_dwa_gdc 接口的示例，接口的具体表述请参考算能官网--技术资料--BM1688/CV186AH的BMCV手册。

## 2. 相机标定，数据准备
相机标定可以参考 https://github.com/sophgo/sophon-stream/blob/master/samples/dwa_dpu_encode/Calibration.md.

本demo也提供了标定测试图片及标定后的参数文件:

```bash
# 下载文件
pip3 install dfss -i https://pypi.tuna.tsinghua.edu.cn/simple --upgrade
python3 -m dfss --url=open@sophgo.com:/sophon-demo/DWA/data.zip

# 安装unzip，若已安装请跳过，非ubuntu系统视情况使用yum或其他方式安装
sudo apt-get install unzip
# 解压文件
unzip data.zip
```

`data`目录如下。

.
├── left            # 测试组1 
│   ├── left.jpg
│   └── LL.dat
└── right           # 测试组2
    ├── right.jpg
    └── RR.dat

## 3. 样例测试

- [C++例程](./cpp/README.md)



# 文件: tutorial/DWA/cpp/README.md

---

# DWA C++例程

## 目录

- [DWA C++例程](#dwa-c例程)
  - [目录](#目录)
  - [1. 环境准备](#1-环境准备)
  - [2. 程序编译](#2-程序编译)
  - [3. 测试](#3-测试)
    - [3.1 参数说明](#31-参数说明)
    - [3.2 测试图片](#32-测试图片)

提供了C++例程以供参考使用，具体情况如下：
| 序号  | C++例程      | 说明                                 |
| ---- | ------------- | -----------------------------------  |
| 1    | [dwa_bmcv](./dwa_bmcv) | 使用BMCV接口做图像矫正 |

## 1. 环境准备

SoC平台（如SE、SM系列边缘设备），刷机后在`/opt/sophon/`下已经预装了相应的libsophon、sophon-opencv和sophon-ffmpeg运行库包，可直接使用它作为运行环境。通常还需要一台x86主机作为开发环境，用于交叉编译C++程序。

## 2. 程序编译
C++程序运行前需要编译可执行文件，目前该功能只支持在BM1688/CV186X上使用。

通常在x86主机上交叉编译程序，您需要在x86主机上使用SOPHON SDK搭建交叉编译环境，将程序所依赖的头文件和库文件打包至soc-sdk目录中，具体请参考[交叉编译环境搭建](../../../docs/Environment_Install_Guide.md#41-交叉编译环境搭建)。本例程主要依赖libsophon、sophon-opencv和sophon-ffmpeg运行库包。

交叉编译环境搭建好后，使用交叉编译工具链编译生成可执行文件：

```bash
cd cpp/dwa_bmcv
mkdir build && cd build
#请根据实际情况修改-DSDK的路径，需使用绝对路径。
cmake -DTARGET_ARCH=soc -DSDK=/path_to_sdk/soc-sdk ..  
make
```
编译完成后，会在dwa_bmcv目录下生成dwa_bmcv.soc.


## 3. 测试
对于SoC平台，需将交叉编译生成的可执行文件及所需的模型、测试数据拷贝到SoC平台中测试。测试的参数及运行方式是一致的，下面主要以PCIe模式进行介绍。

### 3.1 参数说明
可执行程序默认有一套参数，请注意根据实际情况进行传参。
```bash
Usage: 
./dwa_bmcv.soc <input_grid_path> <input_image_path> <if_resize> <resize_h> <resize_w> <debug>
``` 
注意：
1. <resize>参数是指在dwa之前对图片缩放，是否resize需要根据相机标定时是否缩放确定，即配合参数<input_grid_path>确认。
2. <debug>参数是指是否保存dwa的输入输出图像。


### 3.2 测试图片
图片测试实例如下
```bash
./dwa_bmcv.soc 
```

```bash
./dwa_bmcv.soc 
    --input_grid_path=/data/images/left/LL.dat
    --input_image_path=/data/images/left/left.jpg
    --if_resize=true
    --resize_h=1080
    --resize_w=1920
    --debug=true
```
测试结束后，会将缩放后的图片保存为当前文件夹下dwa_image.bmp。

# 文件: tutorial/mmap/README.md

---

# mmap例程

### 1.说明

mmap功能，当使用FPGA或者网络通信时，直接传输裸图像数据，可以通过mmap的方法，直接将数据写入TPU memory,可有效降低数据搬运时间，仅限SOC模式，支持BM1688、CV186H及BM1684X。

### 2.样例测试

- [C++例程](./cpp)


# 文件: tutorial/mmap/cpp/README.md

---

# C++例程

## 目录

- [C++例程](#c例程)
  - [目录](#目录)
  - [1. 环境准备](#1-环境准备)
  - [2. 程序编译](#2-程序编译)
  - [3. 测试](#3-测试)
    - [3.1 参数说明](#31-参数说明)
    - [3.2 测试图片](#32-测试图片)

cpp目录下提供了C++例程以供参考使用，具体情况如下：
| 序号  | C++例程      | 说明                                 |
| ---- | ------------- | -----------------------------------  |
| 1    | [mmap_bmcv](./mmap_bmcv.soc) | mmap直接在TPU写入数据，并使用bmcv库进行了处理 |


## 1. 环境准备
mmap仅适用于SOC平台，刷机后在`/opt/sophon/`下已经预装了相应的libsophon、sophon-opencv和sophon-ffmpeg运行库包，可直接使用它作为运行环境。通常还需要一台x86主机作为开发环境，用于交叉编译C++程序。


## 2. 程序编译
C++程序运行前需要编译可执行文件，SOC平台通常在x86主机上交叉编译程序，您需要在x86主机上使用SOPHON SDK搭建交叉编译环境，将程序所依赖的头文件和库文件打包至soc-sdk目录中，具体请参考[交叉编译环境搭建](../../../docs/Environment_Install_Guide.md#41-交叉编译环境搭建)。本例程主要依赖libsophon、sophon-opencv和sophon-ffmpeg运行库包。

交叉编译环境搭建好后，使用交叉编译工具链编译生成可执行文件：
```bash
cd cpp
mkdir build && cd build
#请根据实际情况修改-DSDK的路径，需使用绝对路径。
cmake -DTARGET_ARCH=soc -DSDK=/path_to_sdk/soc-sdk ..  
make
```
编译完成后，会在mmap_bmcv目录下生成mmap_bmcv.soc。

## 3. 测试
对于SoC平台，需将交叉编译生成的可执行文件及所需的模型、测试数据拷贝到SoC平台中测试。

### 3.1 参数说明
可执行程序默认有一套参数，请注意根据实际情况进行传参，具体参数说明如下：
```bash
Usage: 
./mmap_bmcv.soc <image path>
```

### 3.2 测试图片
图片测试实例如下
```bash
./mmap_bmcv.soc ../../datasets/test/zidane.jpg
```
测试结束后，会将经过处理后的图片保存为当前文件夹下debug.bmp。


# 文件: tutorial/ocv_avframe/cpp/README.md

---

# C++例程

## 目录

* [1. 环境准备](#1-环境准备)
    * [1.1 x86/arm PCIe平台](#11-x86arm-pcie平台)
    * [1.2 SoC平台](#12-soc平台)
* [2. 程序编译](#2-程序编译)
    * [2.1 x86/arm PCIe平台](#21-x86arm-pcie平台)
    * [2.2 SoC平台](#22-soc平台)
* [3. 推理测试](#3-推理测试)
    * [3.1 参数说明](#31-参数说明)
    * [3.2 测试图片](#32-测试图片)

cpp目录下提供了C++例程以供参考使用，具体情况如下：
| 序号  | C++例程      | 说明                                 |
| ---- | ------------- | -----------------------------------  |
| 1    | ocv_avframe | bgr mat到avframe转换的例程 |

## 1. 环境准备
### 1.1 x86/arm PCIe平台
如果您在x86/arm平台安装了PCIe加速卡（如SC系列加速卡），可以直接使用它作为开发环境和运行环境。您需要安装libsophon、sophon-opencv和sophon-ffmpeg，具体步骤可参考[x86-pcie平台的开发和运行环境搭建](../../../docs/Environment_Install_Guide.md#3-x86-pcie平台的开发和运行环境搭建)或[arm-pcie平台的开发和运行环境搭建](../../../docs/Environment_Install_Guide.md#5-arm-pcie平台的开发和运行环境搭建)。

### 1.2 SoC平台
如果您使用SoC平台（如SE、SM系列边缘设备），刷机后在`/opt/sophon/`下已经预装了相应的libsophon、sophon-opencv和sophon-ffmpeg运行库包，可直接使用它作为运行环境。通常还需要一台x86主机作为开发环境，用于交叉编译C++程序。


## 2. 程序编译
C++程序运行前需要编译可执行文件。
### 2.1 x86/arm PCIe平台
可以直接在PCIe平台上编译程序：
```bash
mkdir build && cd build
cmake .. 
make
cd ..
```
编译完成后，会在当前目录下生成ocv_avframe.pcie。

### 2.2 SoC平台
通常在x86主机上交叉编译程序，您需要在x86主机上使用SOPHON SDK搭建交叉编译环境，将程序所依赖的头文件和库文件打包至soc-sdk目录中，具体请参考[交叉编译环境搭建](../../../docs/Environment_Install_Guide.md#41-交叉编译环境搭建)。本例程主要依赖libsophon、sophon-opencv和sophon-ffmpeg运行库包。

交叉编译环境搭建好后，使用交叉编译工具链编译生成可执行文件：
```bash
mkdir build && cd build
#请根据实际情况修改-DSDK的路径，需使用绝对路径。
cmake -DTARGET_ARCH=soc -DSDK=/path_to_sdk/soc-sdk ..  
make
```
编译完成后，会在当前目录下生成ocv_avframe.soc。

## 3. 测试
对于PCIe平台，可以直接在PCIe平台上测试；对于SoC平台，需将交叉编译生成的可执行文件及所需的模型、测试数据拷贝到SoC平台中测试。测试的参数及运行方式是一致的，下面主要以PCIe模式进行介绍。

### 3.1 参数说明
可执行程序默认有一套参数，请注意根据实际情况进行传参，`ocv_avframe.pcie与ocv_avframe.soc参数相同。`以ocv_avframe.pcie为例，具体参数说明如下：
```bash
usage:
        ./ocv_avframe.pcie <input_pic> [dev_id]
params:
        input_pic: picture for decode to get bgr mat
        dev_id:  using device id
```
### 3.2 测试视频
测试实例如下
```bash
./ocv_avframe.pcie zidane.jpg 0
```
测试结束后，会将读取的bgr mat格式的图片转换成yuv420p的数据，保存到当前文件夹下，命名为output.yuv。

### 3.3 程序说明
本例程通过opencv解码图片获得bgr mat，然后将bgr mat转为avframe进行编码操作。

yuv mat是sophon-opencv中mat的扩展数据结构，一般由avframe生成。yuv mat可以通过mat.u->frame得到其中的avframe。

bgr mat不能直接转换为avframe，一种比较推荐的做法是先将bgr mat转换为yuv mat，然后取yuv mat中的avframe进行后续操作，此时取得的avframe内容即为对应的bgr mat的内容。



# 文件: tutorial/ocv_jpubasic/cpp/README.md

---

# C++例程

## 目录

* [1. 环境准备](#1-环境准备)
    * [1.1 x86/arm PCIe平台](#11-x86arm-pcie平台)
    * [1.2 SoC平台](#12-soc平台)
* [2. 程序编译](#2-程序编译)
    * [2.1 x86/arm PCIe平台](#21-x86arm-pcie平台)
    * [2.2 SoC平台](#22-soc平台)
* [3. 推理测试](#3-推理测试)
    * [3.1 参数说明](#31-参数说明)
    * [3.2 测试图片](#32-测试图片)

cpp目录下提供了C++例程以供参考使用，具体情况如下：
| 序号  | C++例程      | 说明                                 |
| ---- | ------------- | -----------------------------------  |
| 1    | ocv_jpubasic | 使用sophon-opencv硬件加速实现图片编解码 |

## 1. 环境准备
### 1.1 x86/arm PCIe平台
如果您在x86/arm平台安装了PCIe加速卡（如SC系列加速卡），可以直接使用它作为开发环境和运行环境。您需要安装libsophon、sophon-opencv和sophon-ffmpeg，具体步骤可参考[x86-pcie平台的开发和运行环境搭建](../../../docs/Environment_Install_Guide.md#3-x86-pcie平台的开发和运行环境搭建)或[arm-pcie平台的开发和运行环境搭建](../../../docs/Environment_Install_Guide.md#5-arm-pcie平台的开发和运行环境搭建)。

### 1.2 SoC平台
如果您使用SoC平台（如SE、SM系列边缘设备），刷机后在`/opt/sophon/`下已经预装了相应的libsophon、sophon-opencv和sophon-ffmpeg运行库包，可直接使用它作为运行环境。通常还需要一台x86主机作为开发环境，用于交叉编译C++程序。


## 2. 程序编译
C++程序运行前需要编译可执行文件。
### 2.1 x86/arm PCIe平台
可以直接在PCIe平台上编译程序：
```bash
mkdir build && cd build
cmake .. 
make
cd ..
```
编译完成后，会在当前目录下生成ocv_jpubasic.pcie。

### 2.2 SoC平台
通常在x86主机上交叉编译程序，您需要在x86主机上使用SOPHON SDK搭建交叉编译环境，将程序所依赖的头文件和库文件打包至soc-sdk目录中，具体请参考[交叉编译环境搭建](../../../docs/Environment_Install_Guide.md#41-交叉编译环境搭建)。本例程主要依赖libsophon、sophon-opencv和sophon-ffmpeg运行库包。

交叉编译环境搭建好后，使用交叉编译工具链编译生成可执行文件：
```bash
mkdir build && cd build
#请根据实际情况修改-DSDK的路径，需使用绝对路径。
cmake -DTARGET_ARCH=soc -DSDK=/path_to_sdk/soc-sdk ..  
make
```
编译完成后，会在当前目录下生成ocv_jpubasic.soc。

## 3. 测试
对于PCIe平台，可以直接在PCIe平台上测试；对于SoC平台，需将交叉编译生成的可执行文件及所需的模型、测试数据拷贝到SoC平台中测试。测试的参数及运行方式是一致的，下面主要以PCIe模式进行介绍。

### 3.1 参数说明
可执行程序默认有一套参数，请注意根据实际情况进行传参，`ocv_jpubasic.pcie与ocv_jpubasic.pcie参数相同。`以jpubasic.pcie为例，具体参数说明如下：
```bash
usage:
        ./ocv_jpubasic.pcie <file> <loop> <yuv_enable> <dump_enable> [card]
params:
        <yuv_enable>: 0 decode output BGR; 1 decode output YUV.
        <dump_enable>: 0 no dump file; 1 output dump file.
```
### 3.2 测试图片
图片测试实例如下
```bash
./ocv_jpubasic.pcie zidane.jpg 1 1 0 0
```
测试结束后，会将图片解码后再编码保存到当前文件夹下。


# 文件: tutorial/ocv_jpubasic/python/README.md

---

# Python例程

## 目录

* [1. 环境准备](#1-环境准备)
    * [1.1 x86/arm PCIe平台](#11-x86arm-pcie平台)
    * [1.2 SoC平台](#12-soc平台)
* [2. 推理测试](#2-推理测试)
    * [2.1 参数说明](#21-参数说明)
    * [2.2 测试图片](#22-测试图片)
    * [2.3 测试视频](#23-测试视频)

python目录下提供了一系列Python例程，具体情况如下：

| 序号 |  Python例程      | 说明                                |
| ---- | ---------------- | -----------------------------------  |
| 1    | [ocv_jpubasic.py](./ocv_jpubasic.py) | 使用sophon-opencv硬件加速实现图片编解码 |

## 1. 环境准备
### 1.1 x86/arm PCIe平台

如果您在x86/arm平台安装了PCIe加速卡（如SC系列加速卡），并使用它测试本例程，您需要安装libsophon、sophon-opencv和sophon-ffmpeg，具体请参考[x86-pcie平台的开发和运行环境搭建](../../../docs/Environment_Install_Guide.md#3-x86-pcie平台的开发和运行环境搭建)或[arm-pcie平台的开发和运行环境搭建](../../../docs/Environment_Install_Guide.md#5-arm-pcie平台的开发和运行环境搭建)。

### 1.2 SoC平台

如果您使用SoC平台（如SE、SM系列边缘设备），并使用它测试本例程，刷机后在`/opt/sophon/`下已经预装了相应的libsophon、sophon-opencv和sophon-ffmpeg运行库包。

## 2. 测试
python例程不需要编译，只需要手动设置环境变量，导入sophon-opencv的python接口就可以直接运行，PCIe平台和SoC平台的测试参数和运行方式是相同的。
### 2.1 参数说明
```bash
usage: ocv_jpubasic.py [-h] [--image_path IMAGE_PATH] [--device_id DEVICE_ID]

optional arguments:
  -h, --help            show this help message and exit
  --image_path IMAGE_PATH
                        input image path
  --device_id DEVICE_ID
                        device id
```

### 2.2 测试图片
图片测试实例如下
```bash
# 手动设置环境变量，使用sophon-opencv的python接口
export PYTHONPATH=$PYTHONPATH:/opt/sophon/sophon-opencv-latest/opencv-python

python3 python/ocv_jpubasic.py --image_path zidane.jpg --device_id 0
```
测试结束后，会将图片解码后再编码保存到当前文件夹下。

**注意，使用sophon-opencv需要保证python版本小于等于3.8。**

# 文件: tutorial/ocv_vidbasic/cpp/README.md

---

# C++例程

## 目录

* [1. 环境准备](#1-环境准备)
    * [1.1 x86/arm PCIe平台](#11-x86arm-pcie平台)
    * [1.2 SoC平台](#12-soc平台)
* [2. 程序编译](#2-程序编译)
    * [2.1 x86/arm PCIe平台](#21-x86arm-pcie平台)
    * [2.2 SoC平台](#22-soc平台)
* [3. 推理测试](#3-推理测试)
    * [3.1 参数说明](#31-参数说明)
    * [3.2 测试图片](#32-测试图片)

cpp目录下提供了C++例程以供参考使用，具体情况如下：
| 序号  | C++例程      | 说明                                 |
| ---- | ------------- | -----------------------------------  |
| 1    | [ocv_vidbasic.cpp](./ocv_vidbasic.cpp) | 使用sophon-opencv硬件加速实现视频解码，并将视频记录为png或jpg格式 |

## 1. 环境准备
### 1.1 x86/arm PCIe平台
如果您在x86/arm平台安装了PCIe加速卡（如SC系列加速卡），可以直接使用它作为开发环境和运行环境。您需要安装libsophon、sophon-opencv和sophon-ffmpeg，具体步骤可参考[x86-pcie平台的开发和运行环境搭建](../../../docs/Environment_Install_Guide.md#3-x86-pcie平台的开发和运行环境搭建)或[arm-pcie平台的开发和运行环境搭建](../../../docs/Environment_Install_Guide.md#5-arm-pcie平台的开发和运行环境搭建)。

### 1.2 SoC平台
如果您使用SoC平台（如SE、SM系列边缘设备），刷机后在`/opt/sophon/`下已经预装了相应的libsophon、sophon-opencv和sophon-ffmpeg运行库包，可直接使用它作为运行环境。通常还需要一台x86主机作为开发环境，用于交叉编译C++程序。


## 2. 程序编译
C++程序运行前需要编译可执行文件。
### 2.1 x86/arm PCIe平台
可以直接在PCIe平台上编译程序：
```bash
mkdir build && cd build
cmake .. 
make
cd ..
```
编译完成后，会在当前目录下生成ocv_vidbasic.pcie。

### 2.2 SoC平台
通常在x86主机上交叉编译程序，您需要在x86主机上使用SOPHON SDK搭建交叉编译环境，将程序所依赖的头文件和库文件打包至soc-sdk目录中，具体请参考[交叉编译环境搭建](../../../docs/Environment_Install_Guide.md#41-交叉编译环境搭建)。本例程主要依赖libsophon、sophon-opencv和sophon-ffmpeg运行库包。

交叉编译环境搭建好后，使用交叉编译工具链编译生成可执行文件：
```bash
mkdir build && cd build
#请根据实际情况修改-DSDK的路径，需使用绝对路径。
cmake -DTARGET_ARCH=soc -DSDK=/path_to_sdk/soc-sdk ..  
make
```
编译完成后，会在当前目录下生成ocv_vidbasic.soc。

## 3. 测试
对于PCIe平台，可以直接在PCIe平台上测试；对于SoC平台，需将交叉编译生成的可执行文件及所需的模型、测试数据拷贝到SoC平台中测试。测试的参数及运行方式是一致的，下面主要以PCIe模式进行介绍。

### 3.1 参数说明
可执行程序默认有一套参数，请注意根据实际情况进行传参，`ocv_vidbasic.pcie与ocv_vidbasic.pcie参数相同。`以ocv_vidbasic.pcie为例，具体参数说明如下：
```bash
usage:
        ./ocv_vidbasic.pcie <input_video> <output_name> <frame_num> <yuv_enable> [card] [WxH] [dump.BGR or dump.YUV]
        --> test video record as png or jpg(enable yuv). And dump BGR or YUV raw data if you enable the dump.
params:
        <input_video>:           input video path.
        <output_name>:           output image name.
        <frame_num>:             the number of frames that need to be decoded.
        <yuv_enable>:            0 decode output BGR; 1 decode output YUV.
        <card>:                  device id.
        <WxH>:                   decoded image width and height.
        <dump.BGR or dump.YUV>:  dump.BGR dump BGR file; dump.BGR dump YUV file, this parameter is optional.
```
注意：如果是SoC平台，忽略[card]参数。

### 3.2 测试实例

```bash
./ocv_vidbasic.pcie road.mp4 out 300 0 0 1920x1080 dump.BGR
```
测试结束后，会将视频解码后再记录为jpg或png格式，保存到当前文件夹下。


# 文件: tutorial/ocv_vidbasic/python/README.md

---

# Python例程

## 目录

* [1. 环境准备](#1-环境准备)
    * [1.1 x86/arm PCIe平台](#11-x86arm-pcie平台)
    * [1.2 SoC平台](#12-soc平台)
* [2. 推理测试](#2-推理测试)
    * [2.1 参数说明](#21-参数说明)
    * [2.2 测试图片](#22-测试图片)
    * [2.3 测试视频](#23-测试视频)

python目录下提供了一系列Python例程，具体情况如下：

| 序号 |  Python例程      | 说明                                |
| ---- | ---------------- | -----------------------------------  |
| 1    | [ocv_vidbasic.py](./ocv_vidbasic.py) | 使用sophon-opencv硬件加速实现视频解码，并将视频记录为png或jpg格式 |

## 1. 环境准备
### 1.1 x86/arm PCIe平台

如果您在x86/arm平台安装了PCIe加速卡（如SC系列加速卡），并使用它测试本例程，您需要安装libsophon、sophon-opencv和sophon-ffmpeg，具体请参考[x86-pcie平台的开发和运行环境搭建](../../../docs/Environment_Install_Guide.md#3-x86-pcie平台的开发和运行环境搭建)或[arm-pcie平台的开发和运行环境搭建](../../../docs/Environment_Install_Guide.md#5-arm-pcie平台的开发和运行环境搭建)。

### 1.2 SoC平台

如果您使用SoC平台（如SE、SM系列边缘设备），并使用它测试本例程，刷机后在`/opt/sophon/`下已经预装了相应的libsophon、sophon-opencv和sophon-ffmpeg运行库包。

## 2. 测试
python例程不需要编译，只需要导入sophon-opencv的python接口，手动设置环境变量后就可以直接运行，PCIe平台和SoC平台的测试参数和运行方式是相同的。
### 2.1 参数说明
```bash
usage: ocv_vidbasic.py [-h] [--video_path VIDEO_PATH] [--device_id DEVICE_ID] [--frame_num FRAME_NUM] [--width WIDTH]
                       [--height HEIGHT] [--output_name OUTPUT_NAME]

optional arguments:
  -h, --help            show this help message and exit
  --video_path VIDEO_PATH
                        input video path
  --device_id DEVICE_ID
                        device id
  --frame_num FRAME_NUM
                        encode and decode frame number
  --width WIDTH         width of sampler
  --height HEIGHT       height of sampler
  --output_name OUTPUT_NAME
                        output name of frame
```

### 2.2 测试图片
图片测试实例如下
```bash
# 手动设置环境变量，使用sophon-opencv的python接口
export PYTHONPATH=$PYTHONPATH:/opt/sophon/sophon-opencv-latest/opencv-python

python3 ocv_vidbasic.py --video_path road.mp4 --frame_num 300 --device_id 0 --output_name out
```
测试结束后，会将视频解码后再记录为jpg格式，保存到当前文件夹下。

**注意，若使用sophon-opencv需要保证python版本小于等于3.8。**

# 文件: tutorial/resize/cpp/README.md

---

# C++例程

## 目录

* [1. 环境准备](#1-环境准备)
    * [1.1 x86/arm PCIe平台](#11-x86arm-pcie平台)
    * [1.2 SoC平台](#12-soc平台)
* [2. 程序编译](#2-程序编译)
    * [2.1 x86/arm PCIe平台](#21-x86arm-pcie平台)
    * [2.2 SoC平台](#22-soc平台)
* [3. 推理测试](#3-推理测试)
    * [3.1 参数说明](#31-参数说明)
    * [3.2 测试图片](#32-测试图片)

cpp目录下提供了C++例程以供参考使用，具体情况如下：
| 序号  | C++例程      | 说明                                 |
| ---- | ------------- | -----------------------------------  |
| 1    | [resize_bmcv](./resize_bmcv) | 使用BMC接口做缩放 |
| 2    | [resize_sail](./resize_sail) | 使用SAIL接口做缩放 |

## 1. 环境准备
### 1.1 x86/arm PCIe平台
如果您在x86/arm平台安装了PCIe加速卡（如SC系列加速卡），可以直接使用它作为开发环境和运行环境。您需要安装libsophon、sophon-opencv和sophon-ffmpeg，具体步骤可参考[x86-pcie平台的开发和运行环境搭建](../../../docs/Environment_Install_Guide.md#3-x86-pcie平台的开发和运行环境搭建)或[arm-pcie平台的开发和运行环境搭建](../../../docs/Environment_Install_Guide.md#5-arm-pcie平台的开发和运行环境搭建)。

### 1.2 SoC平台
如果您使用SoC平台（如SE、SM系列边缘设备），刷机后在`/opt/sophon/`下已经预装了相应的libsophon、sophon-opencv和sophon-ffmpeg运行库包，可直接使用它作为运行环境。通常还需要一台x86主机作为开发环境，用于交叉编译C++程序。


## 2. 程序编译
C++程序运行前需要编译可执行文件。
### 2.1 x86/arm PCIe平台
可以直接在PCIe平台上编译程序：
#### 2.1.1 bmcv
```bash
cd cpp/resize_bmcv
mkdir build && cd build
cmake .. 
make
cd ..
```
编译完成后，会在resize_bmcv目录下生成resize_bmcv.pcie。

#### 2.1.2 sail
如果您使用sophon-sail接口，需要[编译安装sophon-sail](../../../docs/Environment_Install_Guide.md#33-编译安装sophon-sail)，然后进行如下步骤。
```bash
cd cpp/resize_sail
mkdir build && cd build
cmake ..
make
cd ..
```
编译完成后，会在resize_sail目录下生成resize_sail.pcie。

### 2.2 SoC平台
通常在x86主机上交叉编译程序，您需要在x86主机上使用SOPHON SDK搭建交叉编译环境，将程序所依赖的头文件和库文件打包至soc-sdk目录中，具体请参考[交叉编译环境搭建](../../../docs/Environment_Install_Guide.md#41-交叉编译环境搭建)。本例程主要依赖libsophon、sophon-opencv和sophon-ffmpeg运行库包。

交叉编译环境搭建好后，使用交叉编译工具链编译生成可执行文件：
#### 2.2.1 bmcv
```bash
cd cpp/resize_bmcv
mkdir build && cd build
#请根据实际情况修改-DSDK的路径，需使用绝对路径。
cmake -DTARGET_ARCH=soc -DSDK=/path_to_sdk/soc-sdk ..  
make
```
编译完成后，会在resize_bmcv目录下生成resize_bmcv.soc。

#### 2.2.2 sail
如果您使用sophon-sail接口，需要参考[交叉编译安装sophon-sail](../../../docs/Environment_Install_Guide.md#42-交叉编译安装sophon-sail)，给soc环境配置sophon-sail，然后进行如下步骤。
```bash
cd cpp/resize_sail
mkdir build && cd build
#请根据实际情况修改-DSDK和-DSAIL_PATH的路径，需使用绝对路径。
cmake -DTARGET_ARCH=soc -DSDK=/path_to_sdk/soc-sdk -DSAIL_PATH=/path_to_sail/sophon-sail/build_soc/sophon-sail ..
make
```
编译完成后，会在resize_sail目录下生成resize_sail.soc。

## 3. 测试
对于PCIe平台，可以直接在PCIe平台上测试；对于SoC平台，需将交叉编译生成的可执行文件及所需的模型、测试数据拷贝到SoC平台中测试。测试的参数及运行方式是一致的，下面主要以PCIe模式进行介绍。

### 3.1 参数说明
可执行程序默认有一套参数，请注意根据实际情况进行传参，`resize_bmcv.pcie与resize_sail.pcie参数相同。`以resize_bmcv.pcie为例，具体参数说明如下：
```bash
Usage: 
./resize_bmcv.pcie <image path>
```
### 3.2 测试图片
图片测试实例如下。
```bash
./resize_bmcv.pcie ../../datasets/test/zidane.jpg
```
测试结束后，会将缩放后的图片保存为当前文件夹下resized.jpg。


# 文件: tutorial/resize/python/README.md

---

# Python例程

## 目录

* [1. 环境准备](#1-环境准备)
    * [1.1 x86/arm PCIe平台](#11-x86arm-pcie平台)
    * [1.2 SoC平台](#12-soc平台)
* [2. 推理测试](#2-推理测试)
    * [2.1 参数说明](#21-参数说明)
    * [2.2 测试图片](#22-测试图片)
    * [2.3 测试视频](#23-测试视频)

python目录下提供了一系列Python例程，具体情况如下：

| 序号 |  Python例程      | 说明                                |
| ---- | ---------------- | -----------------------------------  |
| 1    | [resize.py](./resize.py) | 使用SAIL做缩放 |

## 1. 环境准备
### 1.1 x86/arm PCIe平台

如果您在x86/arm平台安装了PCIe加速卡（如SC系列加速卡），并使用它测试本例程，您需要安装libsophon、sophon-opencv、sophon-ffmpeg和sophon-sail，具体请参考[x86-pcie平台的开发和运行环境搭建](../../../docs/Environment_Install_Guide.md#3-x86-pcie平台的开发和运行环境搭建)或[arm-pcie平台的开发和运行环境搭建](../../../docs/Environment_Install_Guide.md#5-arm-pcie平台的开发和运行环境搭建)。

### 1.2 SoC平台

如果您使用SoC平台（如SE、SM系列边缘设备），并使用它测试本例程，刷机后在`/opt/sophon/`下已经预装了相应的libsophon、sophon-opencv和sophon-ffmpeg运行库包。您还需要交叉编译安装sophon-sail，具体可参考[交叉编译安装sophon-sail](../../../docs/Environment_Install_Guide.md#42-交叉编译安装sophon-sail)。

## 2. 测试
python例程不需要编译，可以直接运行，PCIe平台和SoC平台的测试参数和运行方式是相同的。
### 2.1 参数说明
```bash
usage: resize.py [-h] [--image_path IMAGE_PATH]

optional arguments:
  -h, --help            show this help message and exit
  --image_path IMAGE_PATH
                        input image path
```

### 2.2 测试图片
图片测试实例如下，支持对整个图片文件夹进行测试。
```bash
python3 python/resize.py --image_path ../datasets/test/zidane.jpg
```
测试结束后，会将缩放后的图片保存为当前文件夹下resized.jpg。


# 文件: tutorial/stitch/cpp/stitch_bmcv/README.md

---


# C++例程

## 目录

* [1. 环境准备](#1-环境准备)
    * [1.1 x86/arm PCIe平台](#11-x86arm-pcie平台)
    * [1.2 SoC平台](#12-soc平台)
* [2. 程序编译](#2-程序编译)
    * [2.1 x86/arm PCIe平台](#21-x86arm-pcie平台)
    * [2.2 SoC平台](#22-soc平台)
* [3. 推理测试](#3-推理测试)
    * [3.1 参数说明](#31-参数说明)
    * [3.2 测试图片](#32-测试图片)

cpp目录下提供了C++例程以供参考使用，具体情况如下：
| 序号  | C++例程      | 说明                                 |
| ---- | ------------- | -----------------------------------  |
| 1    | [stitch_bmcv](./stitch_bmcv) | 使用BMCV接口做拼接 |

## 1. 环境准备
### 1.1 x86/arm PCIe平台
如果您在x86/arm平台安装了PCIe加速卡（如SC系列加速卡），可以直接使用它作为开发环境和运行环境。您需要安装libsophon、sophon-opencv和sophon-ffmpeg，具体步骤可参考[x86-pcie平台的开发和运行环境搭建](../../../docs/Environment_Install_Guide.md#3-x86-pcie平台的开发和运行环境搭建)或[arm-pcie平台的开发和运行环境搭建](../../../docs/Environment_Install_Guide.md#5-arm-pcie平台的开发和运行环境搭建)。

### 1.2 SoC平台
如果您使用SoC平台（如SE、SM系列边缘设备），刷机后在`/opt/sophon/`下已经预装了相应的libsophon、sophon-opencv和sophon-ffmpeg运行库包，可直接使用它作为运行环境。通常还需要一台x86主机作为开发环境，用于交叉编译C++程序。


## 2. 程序编译
C++程序运行前需要编译可执行文件。
### 2.1 x86/arm PCIe平台
可以直接在PCIe平台上编译程序：
#### 2.1.1 bmcv
```bash
cd cpp/stitch_bmcv
mkdir build && cd build
cmake .. 
make
cd ..
```
编译完成后，会在stitch_bmcv目录下生成stitch_bmcv.pcie。


### 2.2 SoC平台
通常在x86主机上交叉编译程序，您需要在x86主机上使用SOPHON SDK搭建交叉编译环境，将程序所依赖的头文件和库文件打包至soc-sdk目录中，具体请参考[交叉编译环境搭建](../../../docs/Environment_Install_Guide.md#41-交叉编译环境搭建)。本例程主要依赖libsophon、sophon-opencv和sophon-ffmpeg运行库包。

交叉编译环境搭建好后，使用交叉编译工具链编译生成可执行文件：
#### 2.2.1 bmcv
```bash
cd cpp/stitch_bmcv
mkdir build && cd build
#请根据实际情况修改-DSDK的路径，需使用绝对路径。
cmake -DTARGET_ARCH=soc -DSDK=/path_to_sdk/soc-sdk ..  
make
```
编译完成后，会在stitch_bmcv目录下生成stitch_bmcv.soc。


## 3. 测试
对于PCIe平台，可以直接在PCIe平台上测试；对于SoC平台，需将交叉编译生成的可执行文件及所需的模型、测试数据拷贝到SoC平台中测试。测试的参数及运行方式是一致的，下面主要以PCIe模式进行介绍。首先，下载测试包：
```bash
python3 -m dfss --url=open@sophgo.com:sophon-demo/tutorial/bmcv_stitch/data.tar.gz
tar -xvf data.tar.gz
mv data datasets
```

### 3.1 参数说明
可执行程序默认有一套参数，请注意根据实际情况进行传参。`以stitch_bmcv.pcie为例，具体参数说明如下：
```bash
Usage: 
./stitch_bmcv.pcie <left image_path> <right image_path>
```
### 3.2 测试图片
图片测试实例如下。
```bash
./stitch_bmcv.pcie ./datasets/1920_1088.jpg ./datasets/1920_1088.jpg
```
测试结束后，会将缩放后的图片保存为当前文件夹下stitch_image.jpg。



# 文件: tutorial/video_encode/README.md

---

# encode例程

### 1.说明

实现将视频解码后推流出去。在运行推流程序之前，需要先启动一个流媒体服务器，[例如mediamtx，用于接收流媒体数据。](https://github.com/bluenviron/mediamtx)。本实例支持在 BM1688、CV186H、BM1684X 以及 BM1684 的 SoC 和 PCIE 模式下使用。

### 2.样例测试

- [C++例程](./cpp)
- [Python例程](./python)

# 文件: tutorial/video_encode/cpp/README.md

---

# C++例程

## 目录

- [C++例程](#c例程)
  - [目录](#目录)
  - [1. 环境准备](#1-环境准备)
    - [1.1 x86/arm PCIe平台](#11-x86arm-pcie平台)
    - [1.2 SoC平台](#12-soc平台)
  - [2. 程序编译](#2-程序编译)
    - [2.1 x86/arm PCIe平台](#21-x86arm-pcie平台)
      - [2.1.1 bmcv](#211-bmcv)
      - [2.1.2 sail](#212-sail)
    - [2.2 SoC平台](#22-soc平台)
      - [2.2.1 bmcv](#221-bmcv)
      - [2.2.2 sail](#222-sail)
  - [3. 测试](#3-测试)
    - [3.1 参数说明](#31-参数说明)
    - [3.2 测试视频](#32-测试视频)

cpp目录下提供了C++例程以供参考使用，具体情况如下：
| 序号  | C++例程      | 说明                                 |
| ---- | ------------- | -----------------------------------  |
| 1    | [encode_bmcv](./encode_bmcv) | 使用bmcv做编码 |
| 2    | [encode_sail](./encode_sail) | 使用SAIL接口做编码 |

## 1. 环境准备
### 1.1 x86/arm PCIe平台
如果您在x86/arm平台安装了PCIe加速卡（如SC系列加速卡），可以直接使用它作为开发环境和运行环境。您需要安装libsophon、sophon-opencv和sophon-ffmpeg，具体步骤可参考[x86-pcie平台的开发和运行环境搭建](../../../docs/Environment_Install_Guide.md#3-x86-pcie平台的开发和运行环境搭建)或[arm-pcie平台的开发和运行环境搭建](../../../docs/Environment_Install_Guide.md#5-arm-pcie平台的开发和运行环境搭建)。

### 1.2 SoC平台
如果您使用SoC平台（如SE、SM系列边缘设备），刷机后在`/opt/sophon/`下已经预装了相应的libsophon、sophon-opencv和sophon-ffmpeg运行库包，可直接使用它作为运行环境。通常还需要一台x86主机作为开发环境，用于交叉编译C++程序。


## 2. 程序编译
C++程序运行前需要编译可执行文件。
### 2.1 x86/arm PCIe平台
可以直接在PCIe平台上编译程序：
#### 2.1.1 bmcv
```bash
cd cpp/encode_bmcv
mkdir build && cd build
cmake .. 
make
cd ..
```
编译完成后，会在encode_bmcv目录下生成encode_bmcv.pcie。

#### 2.1.2 sail
如果您使用sophon-sail接口，需要[编译安装sophon-sail](../../../docs/Environment_Install_Guide.md#33-编译安装sophon-sail)，然后进行如下步骤。
```bash
cd cpp/encode_sail
mkdir build && cd build
cmake ..
make
cd ..
```
编译完成后，会在encode_sail目录下生成encode_sail.pcie。

### 2.2 SoC平台
通常在x86主机上交叉编译程序，您需要在x86主机上使用SOPHON SDK搭建交叉编译环境，将程序所依赖的头文件和库文件打包至soc-sdk目录中，具体请参考[交叉编译环境搭建](../../../docs/Environment_Install_Guide.md#41-交叉编译环境搭建)。本例程主要依赖libsophon、sophon-opencv和sophon-ffmpeg运行库包。

交叉编译环境搭建好后，使用交叉编译工具链编译生成可执行文件：
#### 2.2.1 bmcv
```bash
cd cpp/encode_bmcv
mkdir build && cd build
#请根据实际情况修改-DSDK的路径，需使用绝对路径。
cmake -DTARGET_ARCH=soc -DSDK=/path_to_sdk/soc-sdk ..  
make
```
编译完成后，会在encode_bmcv目录下生成encode_bmcv.soc。

#### 2.2.2 sail
如果您使用sophon-sail接口，需要参考[交叉编译安装sophon-sail](../../../docs/Environment_Install_Guide.md#42-交叉编译安装sophon-sail)，给soc环境配置sophon-sail，然后进行如下步骤。
```bash
cd cpp/encode_sail
mkdir build && cd build
#请根据实际情况修改-DSDK和-DSAIL_PATH的路径，需使用绝对路径。
cmake -DTARGET_ARCH=soc -DSDK=/path_to_sdk/soc-sdk -DSAIL_PATH=/path_to_sail/sophon-sail/build_soc/sophon-sail ..
make
```
编译完成后，会在encode_sail目录下生成encode_sail.soc。

## 3. 测试
对于PCIe平台，可以直接在PCIe平台上测试；对于SoC平台，需将交叉编译生成的可执行文件及所需的模型、测试数据拷贝到SoC平台中测试。测试的参数及运行方式是一致的，下面主要以PCIe模式进行介绍。

### 3.1 参数说明
可执行程序默认有一套参数，请注意根据实际情况进行传参，`encode_bmcv.pcie与encode_sail.pcie参数相同。`以encode_bmcv.pcie为例，具体参数说明如下：
```bash
Usage: encode_bmcv.pcie [params]

        --bitrate (value:2000)
                encoded bitrate
        --compressed_nv12 (value:true)
                Whether the format of decoded output is compressed NV12.
        --dev_id (value:0)
                Device id
        --enc_fmt (value:h264_bm)
                encoded video format, h264_bm/hevc_bm
        --framerate (value:25)
                encode frame rate
        --gop (value:32)
                gop size
        --gop_preset (value:2)
                gop_preset
        --height (value:1080)
                The height of the encoded video
        --help (value:true)
                print help information.
        --input_path (value:../datasets/test_car_person_1080P.mp4)
                Path or rtsp url to the video/image file.
        --output_path (value:output.mp4)
                Local file path or stream url
        --pix_fmt (value:NV12)
                encoded pixel format
        --width (value:1920)
                The width of the encoded video

```
### 3.2 测试视频
视频测试实例1如下：
```bash
./encode_bmcv.pcie --input_path=rtsp://127.0.0.1:8554/0 --output_path=test.mp4
```
测试完成后，会将接受的rtsp流保存为test.mp4文件。

视频测试实例2如下：
```bash
./encode_bmcv.pcie --input_path=rtsp://127.0.0.1:8554/0 --output_path=rtsp://127.0.0.1:8554/1
```
测试开始后，会将接受的rtsp流转发到rtsp://127.0.0.1:8554/1。


# 文件: tutorial/video_encode/python/README.md

---

# Python例程

## 目录

- [Python例程](#python例程)
  - [目录](#目录)
  - [1. 环境准备](#1-环境准备)
    - [1.1 x86/arm PCIe平台](#11-x86arm-pcie平台)
    - [1.2 SoC平台](#12-soc平台)
  - [2. 测试](#2-测试)
    - [2.1 参数说明](#21-参数说明)
    - [2.2 测试视频：](#22-测试视频)

python目录下提供了一系列Python例程，具体情况如下：

| 序号 |  Python例程      | 说明                                |
| ---- | ---------------- | -----------------------------------  |
| 1    | [encode_sail.py](./encode_sail.py) | 使用SAIL将输入视频、图片、rtsp流保存为视频、图片，或转发为rtsp流 |

## 1. 环境准备
### 1.1 x86/arm PCIe平台

如果您在x86/arm平台安装了PCIe加速卡（如SC系列加速卡），并使用它测试本例程，您需要安装libsophon、sophon-opencv、sophon-ffmpeg和sophon-sail，具体请参考[x86-pcie平台的开发和运行环境搭建](../../../docs/Environment_Install_Guide.md#3-x86-pcie平台的开发和运行环境搭建)或[arm-pcie平台的开发和运行环境搭建](../../../docs/Environment_Install_Guide.md#5-arm-pcie平台的开发和运行环境搭建)。

### 1.2 SoC平台

如果您使用SoC平台（如SE、SM系列边缘设备），并使用它测试本例程，刷机后在`/opt/sophon/`下已经预装了相应的libsophon、sophon-opencv和sophon-ffmpeg运行库包。您还需要交叉编译安装sophon-sail，具体可参考[交叉编译安装sophon-sail](../../../docs/Environment_Install_Guide.md#42-交叉编译安装sophon-sail)。

## 2. 测试
python例程不需要编译，可以直接运行，PCIe平台和SoC平台的测试参数和运行方式是相同的。
### 2.1 参数说明
```bash
usage: push_stream.py [--input_path INPUT_FILE_PATH] [--output_path OUTPUT_PATH] \
[--device_id DEVICE_ID] [--compressed_nv12 COMPRESSED_NV12] [--height HEIGHT] [--width WIDTH] \
[--enc_fmt ENC_FMT] [--bitrate BITRATE] [--pix_fmt PIX_FMT] [--gop GOP] [--gop_preset GOP_PRESET] \
[--framerate FRAMERATE]

--input_path: 输入视频文件的路径，例如 "input_video.mp4"；
--output_path: 推流输出的路径，默认是 "./output"；
--device_id: 使用的设备ID，默认为 0；
--compressed_nv12: 是否使用压缩的NV12格式，True 或 False，默认为 True；
--height: 视频帧的高度，默认为 1080；
--width: 视频帧的宽度，默认为 1920；
--enc_fmt: 编码格式，例如 "h264_bm"；
--bitrate: 码率（单位: Kbps），默认为 2000；
--pix_fmt: 像素格式，例如 "NV12"；
--gop: 关键帧间隔，默认为 32；
--gop_preset: GOP预设值，默认为 2；
--framerate: 帧率，默认为 25帧每秒。
```

### 2.2 测试视频：
视频测试实例1如下：
```bash
python3 python/encode_sail.py --input_path rtsp://127.0.0.1:8554/0 --output_path test.mp4
```
测试完成后，会将接受的rtsp流保存为test.mp4文件。

视频测试实例2如下：
```bash
python3 python/encode_sail.py --input_path rtsp://127.0.0.1:8554/0 --output_path rtsp://127.0.0.1:8554/1
```
测试开始后，会将接受的rtsp流转发到rtsp://127.0.0.1:8554/1。

# 文件: tutorial/yolov8_ffmpeg_encode/README.md

---

# 简介：
本例程的处理流程是：ffmpeg decode + bmcv preprocess + bmrt yolov8 inference + cpu postprocess + bmcv rectangle + ffmpeg encode，支持在BM1684X/BM1688/CV186X上测试，如果用户需要实现ffmpeg编解码、ffmpeg和bmcv格式转换等逻辑，可以参考本例程。

# 目录结构说明：

```bash
├── CMakeLists.txt
├── coco.names
├── ff_decode # ff_decode依赖，不同于别的例程的ff_decode，这里设置了解码器输出格式为压缩格式，并且优先把bm_image的内存放到heap2上。
├── ff_encode # ff_encode依赖，来自sophon-mw-soc_0.10.0_aarch64/opt/sophon/sophon-sample_0.10.0/samples/ff_bmcv_transcode/ff_video_encode
├── main.cpp  # 主程序，包含主要调用逻辑
├── README.md
├── utils.hpp # timestamp依赖，用于计时
├── yolov8_det.cpp # yolov8_det封装，来自sophon-demo/sample/YOLOv8_plus_det
├── yolov8_det.hpp
```

# 获取测试视频和模型：

本例程的测试视频和模型均来自[YOLOv8_plus_det](../../sample/YOLOv8_plus_det/README.md#31-数据准备)
```bash
pip3 install dfss --upgrade
python3 -m dfss --url=open@sophgo.com:sophon-demo/common/test_car_person_1080P.mp4

python3 -m dfss --url=open@sophgo.com:sophon-demo/YOLOv8_plus_det/BM1684X.tar.gz #bm1684x
tar xvf BM1684X.tar.gz && rm BM1684X.tar.gz

python3 -m dfss --url=open@sophgo.com:sophon-demo/YOLOv8_plus_det/BM1688.tar.gz #bm1688
tar xvf BM1688.tar.gz && rm BM1688.tar.gz

python3 -m dfss --url=open@sophgo.com:sophon-demo/YOLOv8_plus_det/CV186X.tar.gz #cv186x
tar xvf CV186X.tar.gz && rm CV186X.tar.gz
```


# 编译运行方法：

编译方法同[yolov8_bmcv](../../sample/YOLOv8_plus_det/cpp/README.md)。

运行方法：

首先在目标推流服务器上运行rtsp服务器，准备接收流。
然后在搭载BM1684X/BM1688/CV186X设备的机器上运行如下命令：
```bash
./yolov8_bmcv.soc --output=rtsp://172.21.80.56:8554/test --bmodel=BM1684X/yolov8s_int8_1b.bmodel --input=test_car_person_1080P.mp4
```
