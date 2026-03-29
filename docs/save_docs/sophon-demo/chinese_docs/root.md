

# 文件: CONTRIBUTING_CN.md

---

[简体中文](./CONTRIBUTING_CN.md) | [English](./CONTRIBUTING_EN.md)

**介绍**

Sophon Demo，欢迎各位开发者

**贡献要求**

开发者提交的模型包括源码、README、参考模型、测试用例，并遵循以下标准

**一、源码**

1、推理请使用C++或python代码，符合第四部分编码规范

2、请将各模块的内容提交到相应的代码目录内

3、从其他开源迁移的代码，请增加License声明

**二、License规则**

1、若引用参考源项目的文件，且源项目已包含License文件则必须拷贝引用，否则在模型顶层目录下添加使用的深度学习框架或其他组件的必要的License

2、每个复制或修改于源项目的文件，都需要在源文件开头附上源项目的License头部声明，并在其下追加新增完整算能License声明

```
# ...... 源项目的License头部声明 ......
#===----------------------------------------------------------------------===#
#
# Copyright (C) 2022 Sophgo Technologies Inc.  All rights reserved.
#
# SOPHON-DEMO is licensed under the 2-Clause BSD License except for the
# third-party components.
#
#===----------------------------------------------------------------------===#
```

2、每个自己新编写的文件，都需要在源文件开头添加算能License声明

```
#===----------------------------------------------------------------------===#
#
# Copyright (C) 2022 Sophgo Technologies Inc.  All rights reserved.
#
# SOPHON-DEMO is licensed under the 2-Clause BSD License except for the
# third-party components.
#
#===----------------------------------------------------------------------===#
```

> 关于License声明时间，应注意：
>
> 1. 2021年新建的文件，应该是Copyright 2021 Sophgo Technologies Co.
> 2. Python文件的行注释符号为`#`，C/CPP文件中的注释符号为`//`

**三、README**

README用于指导用户理解和测试样例，要包含如下内容：

1. 关于例程功能的说明；
2. 编译或测试例程所需的环境的配置方法；
3. 例程的编译或者测试方法；

针对模型的参考样例，要包含如下内容：

1. 模型的来源及简介；
2. 相关模型和数据的下载方式；
3. FP32 BModel、FP16(BM1684X)及INT8 BModel（1batch及4batch）的生成脚本；
4. 模型推理的步骤和源码（Python、C++）；
5. 模型的性能测试方法和结果；
6. 模型的精度测试方法和结果。

- 关键要求：

1. 模型的出处、对数据的要求、免责声明等，开源代码文件修改需要增加版权说明；

2. 模型转换得到的模型对输入数据的要求；

3. 环境变量设置，依赖的第三方软件包和库，以及安装方法；

4. 精度和性能达成要求：尽量达到原始模型水平；

5. 原始模型及转换后FP32和INT8 BModel的下载地址。


**四、编程规范**

- 规范标准

1. C++代码遵循google编程规范：[Google C++风格指南](https://zh-google-styleguide.readthedocs.io/en/latest/google-cpp-styleguide)([Google C++ Coding Guidelines](https://google.github.io/styleguide/cppguide.html))；单元测试遵循规范： [Googletest Primer](https://google.github.io/googletest/primer.html)。
2. Python代码遵循PEP8规范：[Python PEP 8 Coding Style](https://www.python.org/dev/peps/pep-0008/)；单元测试遵循规范：[pytest](https://docs.pytest.org/en/stable/)
3. Shell脚本遵循google编程规范：[Google Shell风格指南](https://zh-google-styleguide.readthedocs.io/en/latest/google-shell-styleguide/contents/)([Google Shell Style Guide](https://google.github.io/styleguide/shellguide.html))
4. git commit信息遵循规范：[Angular规范](https://docs.google.com/document/d/1QrDFcIiPjSLDn3EL15IJygNPiHORgU1_OOAqWjiDU5Y/edit#)

- 规范补充

1. C++代码中使用cout而不是printf；
2. 内存管理尽量使用智能指针；
3. 控制第三方库依赖，如果引入第三方依赖，则需要提供第三方依赖安装和使用指导书；
4. 一律使用英文注释，注释率30%--40%，鼓励自注释；
5. 函数头必须有注释，说明函数作用，入参、出参；
6. 统一错误码，通过错误码可以确认那个分支返回错误；
7. 禁止出现打印一堆无影响的错误级别的日志。

# 文件: README.md

---

[简体中文](./README.md) | [English](./README_EN.md)

## SOPHON-DEMO介绍


## 简介
SOPHON-DEMO基于SOPHONSDK接口进行开发，提供一系列主流算法的移植例程。包括基于TPU-NNTC和TPU-MLIR的模型编译与量化，基于BMRuntime的推理引擎移植，以及基于BMCV/OpenCV的前后处理算法移植。

SOPHONSDK是算能科技基于其自主研发的深度学习处理器所定制的深度学习SDK，涵盖了神经网络推理阶段所需的模型优化、高效运行时支持等能力，为深度学习应用开发和部署提供易用、高效的全栈式解决方案。目前可兼容BM1684/BM1684X/BM1688(CV186X)。

## 目录结构与说明
SOPHON-DEMO提供的例子从易到难分为`tutorial`、`sample`、`application`三个模块，`tutorial`模块存放一些基础接口的使用示例，`sample`模块存放一些经典算法在SOPHONSDK上的串行示例，`application`模块存放一些典型场景的典型应用。

| tutorial                                                                 | 说明                                                                      |支持硬件                       |
| ----------------------------------------------------                     | ------------------------------------------------------------              |--------------                |
| [resize](./tutorial/resize/README.md)                                    | resize接口。针对图像做缩放操作                                               | BM1684/BM1684X/BM1688/CV186X |
| [crop](./tutorial/crop/README.md)                                        | crop接口，从输入图片中抠出需要用的图片区域                                    | BM1684/BM1684X/BM1688/CV186X |
| [crop_and_resize_padding](./tutorial/crop_and_resize_padding/README.md)  | 将图片指定位置指定大小部分图片抠出，缩放后填充到大图中，空余部分填充指定像素数值  | BM1684/BM1684X/BM1688/CV186X |
| [ocv_jpgbasic](./tutorial/ocv_jpubasic/README.md)                        | 使用sophon-opencv硬件加速实现图片编解码                                      | BM1684/BM1684X/BM1688/CV186X |
| [ocv_vidbasic](./tutorial/ocv_vidbasic/README.md)                        | 使用sophon-opencv硬件加速实现视频解码，并将视频记录为png或jpg格式              | BM1684/BM1684X/BM1688/CV186X |
| [blend](./tutorial/blend/README.md)                                      | 融合拼接两张图                                                              | BM1688/CV186X                |
| [stitch](./tutorial/stitch/README.md)                                    | 拼接两张图片                                                                | BM1684X/BM1688/CV186X        |
| [avframe_ocv](./tutorial/avframe_ocv/README.md)                          | avframe到cv::mat的转换例程                                                  | BM1684/BM1684X               |
| [ocv_avframe](./tutorial/ocv_avframe/README.md)                          | bgr mat到yuv420p avframe的转换例程                                          | BM1684/BM1684X/BM1688/CV186X |
| [bm1688_2core2task_yolov5](./tutorial/bm1688_2core2task_yolov5/README.md)| 使用bm1688的双核双任务推理部署的yolov5                                       | BM1688                       |
| [mmap](./tutorial/mmap/README.md)                                        | mmap接口，映射TPU内存到CPU                                                  | BM1684X/BM1688/CV186X         |
| [video_encode](./tutorial/video_encode/README.md)                        | 视频编码和推流                                                              | BM1684/BM1684X/BM1688/CV186X |
| [yolov8_ffmpeg_encode](./tutorial/yolov8_ffmpeg_encode/README.md)        | 解码+推理+画框+视频编码和推流                                                 | BM1684X |
| [DPU](./tutorial/DPU/README.md)                                          | 1688 DPU接口用例                                                             | BM1688/CV186X |
| [DWA](./tutorial/DWA/README.md)                                          | 1688 DWA接口用例                                                             | BM1688/CV186X |

| sample                                                        | 算法类别          | 编程语言    | BModel         |支持硬件                     |
|---                                                            |---               |---         | ---            |---                            |
| [LPRNet](./sample/LPRNet/README.md)                           | 车牌识别          | C++/Python | FP32/FP16/INT8 | BM1684/BM1684X/BM1688/CV186X |
| [ResNet](./sample/ResNet/README.md)                           | 图像分类          | C++/Python | FP32/FP16/INT8 | BM1684/BM1684X/BM1688/CV186X |
| [Recognize-Anything](./sample/Recogize-Anything/README.md)    | 图像分类          | Python     | FP32/FP16      | BM1684X                      |
| [YOLOv8_plus_cls](./sample/YOLOv8_plus_cls/README.md)         | 图像分类          | C++/Python | FP32/FP16/INT8 | BM1684X/BM1688/CV186X        |
| [RetinaFace](./sample/RetinaFace/README.md)                   | 人脸检测          | C++/Python | FP32/FP16/INT8 | BM1684/BM1684X/BM1688        |
| [SCRFD](./sample/SCRFD/README.md)                             | 人脸检测          | C++/Python | FP32/FP16/INT8 | BM1684/BM1684X/BM1688/CV186X |
| [segformer](./sample/segformer/README.md)                     | 语义分割          | C++/Python | FP32/FP16      | BM1684/BM1684X/BM1688/CV186X |
| [SAM](./sample/SAM/README.md)                                 | 语义分割          | Python     | FP32/FP16      | BM1684X                      |
| [SAM2](./sample/SAM2/README.md)                               | 语义分割          | Python     | FP32/FP16      | BM1688                       |
| [yolact](./sample/yolact/README.md)                           | 实例分割          | C++/Python | FP32/FP16/INT8 | BM1684/BM1684X               |
| [YOLOv8_plus_seg](./sample/YOLOv8_plus_seg/README.md)         | 实例分割          | C++/Python | FP32/FP16/INT8 | BM1684X/BM1688               |
| [YOLOv8_plus_seg_fuse](./sample/YOLOv8_plus_seg_fuse/README.md)| 实例分割(TPU后处理) | C++/Python | INT8          | BM1684X/BM1688               |
| [YOLOv9_seg](./sample/YOLOv8_plus_seg/README.md)              | 实例分割          | C++/Python | FP32/FP16/INT8 | BM1684X/BM1688               |
| [PP-OCR](./sample/PP-OCR/README.md)                           | OCR              | C++/Python | FP32/FP16      | BM1684/BM1684X/BM1688/CV186X  |
| [OpenPose](./sample/OpenPose/README.md)                       | 人体关键点检测    | C++/Python | FP32/FP16/INT8 | BM1684/BM1684X/BM1688        |
| [YOLOv8_pose](./sample/YOLOv8_pose/README.md)                 | 人体关键点检测    | C++/Python | FP32/FP16/INT8 | BM1684/BM1684X/BM1688/CV186X |
| [HRNet_pose](./sample/HRNet_pose/README.md)                   | 人体关键点检测    | C++/Python | FP32/FP16/INT8 | BM1684X/BM1688/CV186X        |
| [C3D](./sample/C3D/README.md)                                 | 视频动作识别      | C++/Python | FP32/FP16/INT8 | BM1684/BM1684X/BM1688/CV186X |
| [SlowFast](./sample/SlowFast/README.md)                       | 视频动作识别      | C++/Python | FP32/FP16/INT8 | BM1684X/BM1688               |
| [DeepSORT](./sample/DeepSORT/README.md)                       | 多目标跟踪        | C++/Python | FP32/FP16/INT8 | BM1684/BM1684X/BM1688/CV186X |
| [ByteTrack](./sample/ByteTrack/README.md)                     | 多目标跟踪        | C++/Python | FP32/FP16/INT8 | BM1684/BM1684X/BM1688/CV186X |
| [CenterNet](./sample/CenterNet/README.md)                     | 目标检测、姿态识别 | C++/Python | FP32/FP16/INT8 | BM1684/BM1684X/BM1688       |
| [YOLOv5](./sample/YOLOv5/README.md)                           | 目标检测          | C++/Python | FP32/FP16/INT8 | BM1684/BM1684X/BM1688/CV186X |
| [YOLOv34](./sample/YOLOv34/README.md)                         | 目标检测          | C++/Python | FP32/INT8      | BM1684/BM1684X/BM1688        |
| [YOLOX](./sample/YOLOX/README.md)                             | 目标检测          | C++/Python | FP32/INT8      | BM1684/BM1684X/BM1688/CV186X |
| [SSD](./sample/SSD/README.md)                                 | 目标检测          | C++/Python | FP32/INT8      | BM1684/BM1684X               |
| [YOLOv7](./sample/YOLOv7/README.md)                           | 目标检测          | C++/Python | FP32/FP16/INT8 | BM1684/BM1684X/BM1688/CV186X |
| [YOLOv8_det](./sample/YOLOv8_plus_det/README.md)              | 目标检测          | C++/Python | FP32/FP16/INT8 | BM1684/BM1684X/BM1688/CV186X |
| [YOLOv9_det](./sample/YOLOv8_plus_det/README.md)              | 目标检测          | C++/Python | FP32/FP16/INT8 | BM1684/BM1684X/BM1688/CV186X |
| [YOLOv11_det](./sample/YOLOv8_plus_det/README.md)             | 目标检测          | C++/Python | FP32/FP16/INT8 | BM1684X/BM1688/CV186X |
| [YOLOv12_det](./sample/YOLOv8_plus_det/README.md)             | 目标检测          | C++/Python | FP32/FP16/INT8 | BM1684X/BM1688/CV186X |
| [YOLOv5_opt](./sample/YOLOv5_opt/README.md)                   | 目标检测          | C++/Python | FP32/FP16/INT8 | BM1684X                      |
| [YOLOv5_fuse](./sample/YOLOv5_fuse/README.md)                 | 目标检测          | C++/Python | FP32/FP16/INT8 | BM1684X/BM1688/CV186X        |
| [YOLOv10](./sample/YOLOv10/README.md)                         | 目标检测          | C++/Python | FP32/FP16/INT8 | BM1684X/BM1688/CV186X        |
| [ppYOLOv3](./sample/ppYOLOv3/README.md)                       | 目标检测          | C++/Python | FP32/FP16/INT8 | BM1684/BM1684X/BM1688/CV186X |
| [ppYoloe](./sample/ppYoloe/README.md)                         | 目标检测          | C++/Python | FP32/FP16      | BM1684/BM1684X/BM1688/CV186X |
| [YOLO_world](./sample/YOLO_world/README.md)                   | 目标检测          | Python     | FP32/FP16/INT8 | BM1684X/BM1688/CV186X        |
| [D-FINE](./sample/D-FINE/README.md)                           | 目标检测          | Python     | FP16           | BM1684X/BM1688/CV186X        |
| [YOLOv8_obb](./sample/YOLOv8_plus_obb/README.md)              | 旋转框目标检测     | C++/Python | FP32/FP16      | BM1684X/BM1688/CV186X       |
| [YOLOv11_obb](./sample/YOLOv8_plus_obb/README.md)              | 旋转框目标检测     | C++/Python | FP32/FP16      | BM1684X/BM1688/CV186X       |
| [WeNet](./sample/WeNet/README.md)                             | 语音识别          | C++/Python | FP32/FP16      | BM1684/BM1684X/BM1688/CV186X |
| [Whisper](./sample/Whisper/README.md)                         | 语音识别          | Python     | FP16           | BM1684X                      |
| [Seamless](./sample/Seamless/README.md)                       | 语音识别          | Python     | FP32/FP16      | BM1684X/BM1688               |
| [BERT](./sample/BERT/README.md)                               | 语言模型          | C++/Python | FP32/FP16      | BM1684/BM1684X/BM1688/CV186X |
| [ChatGLM2](./sample/ChatGLM2/README.md)                       | 大规模语言模型     | C++/Python | FP16/INT8/INT4 | BM1684X                     |
| [Llama2](./sample/Llama2/README.md)                           | 大规模语言模型     | C++/Python | FP16/INT8/INT4 | BM1684X                     |
| [ChatGLM3](./sample/ChatGLM3/README.md)                       | 大规模语言模型     | Python     | FP16/INT8/INT4 | BM1684X/BM1688              |
| [Qwen](./sample/Qwen/README.md)                               | 大规模语言模型     | C++/Python | FP16/INT8/INT4 | BM1684X/BM1688/CV186X       |
| [MiniCPM](./sample/MiniCPM/README.md)                         | 大规模语言模型     | C++        | INT8/INT4      | BM1684X/BM1688/CV186X       |
| [Baichuan2](./sample/Baichuan2/README.md)                     | 大规模语言模型     | Python     | INT8/INT4      | BM1684X                     |
| [ChatGLM4](./sample/ChatGLM4/README.md)                       | 大规模语言模型     | Python     | INT8/INT4      | BM1684X                     |
| [MiniCPM3](./sample/MiniCPM3/README.md)                       | 大规模语言模型     | Python     | INT8/INT4      | BM1684X                     |
| [DeepSeek](./sample/DeepSeek/README.md)                       | 大规模语言模型     | Python     | INT4           | BM1684X/BM1688               |
| [Janus](./sample/Janus/README.md)                             | 大规模语言模型     | Python     | INT4           | BM1684X/BM1688               |
| [MiniCPM4](./sample/MiniCPM4/README.md)                       | 大规模语言模型     | C++/Python | INT4           | BM1684X/BM1688/CV186X       |
| [StableDiffusionV1.5](./sample/StableDiffusionV1_5/README.md) | 图像生成          | Python     | FP32/FP16      | BM1684X                      |
| [StableDiffusionXL](./sample/StableDiffusionXL/README.md)     | 图像生成          | Python     | FP32/FP16      | BM1684X                      |
| [FLUX.1](./sample/FLUX.1/README.md)                           | 图像生成          | Python     | FP32/INT4      | BM1684X                      |
| [GroundingDINO](./sample/GroundingDINO/README.md)             | 多模态目标检测     | Python     | FP16           | BM1684X/BM1688/CV186X       |
| [Qwen-VL-Chat](./sample/Qwen-VL-Chat/README.md)               | 大规模视觉语言模型 | Python     | FP16/INT8      | BM1684X                     |
| [Qwen2-VL](./sample/Qwen2-VL/README.md)                       | 大规模视觉语言模型 | Python     | INT4            | BM1684X                     |
| [Qwen2.5-VL](./sample/Qwen2_5-VL/README.md)                   | 大规模视觉语言模型 | Python     | INT4            | BM1684X/BM1688             |
| [InternVL2](./sample/InternVL2/README.md)                     | 大规模视觉语言模型 | Python     | INT4           | BM1684X/BM1688              |
| [InternVL3](./sample/InternVL3/README.md)                     | 大规模视觉语言模型 | Python     | INT4           | BM1684X/BM1688              |
| [Vila](./sample/Vila/README.md)                               | 大规模视觉语言模型 | Python     | INT8/INT4      | BM1684X/BM1688              |
| [Llama3_2_Vision](./sample/Llama3_2_Vision/README.md)         | 大规模视觉语言模型 | Python     | INT8/INT4      | BM1684X                     |
| [MiniCPMV](./sample/MiniCPMV/README.md)                       | 大规模视觉语言模型 | Python     | INT4            | BM1684X                     |
| [Phi4mm](./sample/Phi4mm/README.md)                           | 多模态大语言模型   | Python     | INT4           | BM1684X/BM1688               |
| [VITA1_5](./sample/VITA1_5/README.md)                         | 多模态大语言模型   | Python     | INT4           | BM1684X                     |
| [Real-ESRGAN](./sample/Real-ESRGAN/README.md)                 | 超分辨            | C++/Python | FP32/FP16/INT8 | BM1684X/BM1688/CV186X        |
| [P2PNet](./sample/P2PNet/README.md)                           | 人群计数          | C++/Python | FP32/FP16/INT8 | BM1684/BM1684X/BM1688/CV186X |
| [CLIP](./sample/CLIP/README.md)                               | 图文匹配          | C++/Python | FP16           | BM1684X/BM1688/CV186X        |
| [BLIP](./sample/BLIP/README.md)                               | 多模态图文模型     | Python     | FP32           | BM1684/BM1684X/BM1688       |
| [SuperGlue](./sample/SuperGlue/README.md)                     | 特征匹配          | C++        | FP32/FP16      | BM1684X/BM1688/CV186X        |
| [VITS_CHINESE](./sample/VITS_CHINESE/README.md)               | 语音生成          | Python     | FP32/FP16      | BM1684X/BM1688/CV186X        |
| [ChatTTS](./sample/ChatTTS/README.md)                         | 语音生成          | Python     | BF16/INT8/INT4 | BM1684X/BM1688        |
| [DirectMHP](./sample/DirectMHP/README.md)                     | 头部姿势估计      | C++/Python | FP32/FP16      | BM1684X/BM1688/CV186X        |
| [CAM++](./sample/CAM++/README.md)                             | 说话人识别        | C++/Python | FP32           | BM1684X/BM1688/CV186X        |
| [FaceFormer](./sample/FaceFormer/README.md)                   | 音频驱动口型      | Python     | FP32           | BM1684X        |
| [MP_SENet](./sample/MP_SENet/README.md)                       | 语音降噪          | Python     | FP32/BF16      | BM1684X        |
| [LightStereo](./sample/LightStereo/README.md)                 | 立体匹配          | C++/Python | FP32/FP16      | BM1684X/BM1688/CV186X        |

| application                                                              | 应用场景                  | 编程语言    | 支持硬件                     |
|---                                                                       |---                       |---          | ---                         |
| [VLPR](./application/VLPR/README.md)                                     | 多路车牌检测+识别          | C++/Python  | BM1684/BM1684X/BM1688/CV186X |
| [YOLOv5_multi](./application/YOLOv5_multi/README.md)                     | 多路目标检测               | C++         | BM1684/BM1684X/BM1688      |
| [YOLOv5_multi_QT](./application/YOLOv5_multi_QT/README.md)               | 多路目标检测+QT_HDMI显示   | C++         | BM1684X                    |
| [Grounded-sam](./application/Grounded-sam/README.md)                     | 自动化图像检测和分割系统    | Python      | BM1684X                    |
| [cv-demo](./application/cv-demo/README.md)                               | 双目鱼眼、广角拼接应用      | C++         | BM1688                      |
| [YOLOv5_fuse_multi_QT](./application/YOLOv5_fuse_multi_QT/README.md)     | 多路目标检测+QT_HDMI显示    | C++         | BM1688/CV186X               |
| [YOLOv8_multi_QT](./application/YOLOv8_multi_QT/README.md)               | 多路目标检测+QT_HDMI显示    | C++         | BM1684X/BM1688/CV186X               |
| [ChatDoc](./application/ChatDoc/README.md)                               | 快速提取文档内容并用于问答   | Python      | BM1684X/BM1688              |
| [LLM_api_server](./application/LLM_api_server/README.md)                 | 类Openai_api的LLM服务      | Python      | BM1684X/BM1688              |
| [Audio_assistant](./application/Audio_assistant/README.md)               | 语音助手                   | C++/Python  | BM1684X/BM1688              |

## 版本说明
| 版本    | 说明 | 
|---     |---   |
| 0.3.6  | 完善和修复文档、代码问题，application模块新增YOLOv8_multi_QT，sample模块新增MiniCPMV。|
| 0.3.5  | 完善和修复文档、代码问题，SAM例程适配mobilesam模型，ByteTrack例程支持yolov5_fuse检测器。|
| 0.3.4  | 完善和修复文档、代码问题，CLIP例程支持mobileclip，Qwen2.5-VL例程新增sample_head、动态模型支持，SuperGlue例程支持int8模型，GroundingDINO模型性能优化。|
| 0.3.3  | 完善和修复文档、代码问题，sample模块新增D-FINE、VITA1_5、MiniCPM4。|
| 0.3.2  | 完善和修复文档、代码问题，Qwen例程添加深度思考开关、penalty_sample，sample模块新增InternVL3，tutorial模块新增DWA接口用例。|
| 0.3.1  | 完善和修复文档、代码问题，Qwen例程支持Qwen3，Qwen2.5-VL支持AWQ量化模型和penalty_sample head，sample模块新增YOLOv11_obb、Phi4mm，tutorial模块新增DPU接口用例。|
| 0.3.0  | 完善和修复文档、代码问题，Qwen例程支持QwQ32B，sample模块新增Recognize-Anything、YOLOv8_plus_cls，Real-ESRGAN后处理优化，Qwen2.5-VL前处理优化，YOLOv8_plus_det支持输出未转置模型。|
| 0.2.10  | 完善和修复文档、代码问题，Qwen例程支持C++，sample模块新增YOLOv12_det、YOLOv8_plus_seg_fuse、Janus、Qwen2.5-VL。tutorial模块新增yolov8_ffmpeg_encode。|
| 0.2.9  | 完善和修复文档、代码问题，**Qwen例程支持deepseek-r1-distill-qwen2-1.5b、deepseek-r1-distill-qwen2-7b**，sample模块新增Llama3_2_Vision，新增YOLOv8_plus_det代替YOLOv8_det、YOLOv9_det、YOLOv11_det，新增YOLOv8_plus_seg代替YOLOv8_seg、YOLOv9_seg。|
| 0.2.8  | 完善和修复文档、代码问题，sample模块新增MiniCPM3、LightStereo、Qwen2-VL、YOLO-world例程。|
| 0.2.7  | 完善和修复文档、代码问题，sample模块新增CAM++、ChatTTS、FaceFormer、MP_SENet、Vila例程。application模块新增ChatDoc、LLM_api_server、Audio_assistant例程。|
| 0.2.6  | 完善和修复文档、代码问题，sample模块新增YOLOv11_det、FLUX.1、SlowFast、YOLOv8_obb例程。 |
| 0.2.5  | 完善和修复文档、代码问题，去除所有sample的公共依赖。sample模块新增SAM2、HRNet_pose、InternVL2、BLIP、DirectMHP、VITS_CHINESE例程，application新增cv-demo、YOLOv5_fuse_multi_QT例程。 |
| 0.2.4  | 完善和修复文档、代码问题，**修复VideoDecFFM系统内存泄漏问题**，sample模块新增YOLOv8_pose、Qwen-VL-Chat例程，application新增Grounded-sam例程。 |
| 0.2.3  | 完善和修复文档、代码问题，sample模块新增例程StableDiffusionXL、ChatGLM4、Seamless、YOLOv10，tutorial模块新增mmap、video_encode例程。 |
| 0.2.2  | 完善和修复文档、代码问题，部分例程补充CV186X支持，sample模块新增Whisper、Real-ESRGAN、SCRFD、P2PNet、MiniCPM、CLIP、SuperGlue、YOLOv5_fuse、YOLOv8_seg、YOLOv9_seg、Baichuan2等例程，tutorial模块新增avframe_ocv、ocv_avframe、bm1688_2core2task_yolov5例程。 |
| 0.2.1  | 完善和修复文档、代码问题，部分例程补充CV186X支持，YOLOv5适配SG2042，sample模块新增例程GroundingDINO、Qwen1_5，StableDiffusionV1_5新支持多种分辨率，Qwen、Llama2、ChatGLM3添加web和多会话模式。tutorial模块新增blend和stitch例程 |
| 0.2.0  | 完善和修复文档、代码问题，新增application和tutorial模块，新增例程ChatGLM3和Qwen，SAM添加web ui，BERT、ByteTrack、C3D适配BM1688，原YOLOv8更名为YOLOv8_det并且添加cpp后处理加速方法，优化常用例程的auto_test，更新TPU-MLIR安装方式为pip |
| 0.1.10 | 修复文档、代码问题，新增ppYoloe、YOLOv8_seg、StableDiffusionV1.5、SAM，重构yolact，CenterNet、YOLOX、YOLOv8适配BM1688，YOLOv5、ResNet、PP-OCR、DeepSORT补充BM1688性能数据，WeNet提供C++交叉编译方法 |
| 0.1.9	 | 修复文档、代码问题，新增segformer、YOLOv7、Llama2例程，重构YOLOv34，YOLOv5、ResNet、PP-OCR、DeepSORT、LPRNet、RetinaFace、YOLOv34、WeNet适配BM1688，OpenPose后处理加速，chatglm2添加编译方法和int8/int4量化。|
| 0.1.8  | 完善修复文档、代码问题，新增BERT、ppYOLOv3、ChatGLM2，重构YOLOX，PP-OCR添加beam search，OpenPose添加tpu-kernel后处理加速，更新SFTP下载方式。|
| 0.1.7	 | 修复文档等问题，一些例程支持BM1684 mlir，重构PP-OCR、CenterNet例程，YOLOv5添加sail支持 |
| 0.1.6	 | 修复文档等问题，新增ByteTrack、YOLOv5_opt、WeNet例程 |
| 0.1.5	 | 修复文档等问题，新增DeepSORT例程，重构ResNet、LPRNet例程 |
| 0.1.4	 | 修复文档等问题，新增C3D、YOLOv8例程 |
| 0.1.3	 | 新增OpenPose例程，重构YOLOv5例程（包括适配arm PCIe、支持TPU-MLIR编译BM1684X模型、使用ffmpeg组件替换opencv解码等） |
| 0.1.2	 | 修复文档等问题，重构SSD相关例程，LPRNet/cpp/lprnet_bmcv使用ffmpeg组件替换opencv解码 |
| 0.1.1	 | 修复文档等问题，使用BMNN相关类重构LPRNet/cpp/lprnet_bmcv |
| 0.1.0	 | 提供LPRNet等10个例程，适配BM1684X(x86 PCIe、SoC)，BM1684(x86 PCIe、SoC) |

## 环境依赖
SOPHON-DEMO主要依赖TPU-MLIR、LIBSOPHON、SOPHON-FFMPEG、SOPHON-OPENCV、SOPHON-SAIL，对于BM1684/BM1684X SOPHONSDK，其版本要求如下：
|SOPHON-DEMO|TPU-MLIR  |LIBSOPHON|SOPHON-FFMPEG|SOPHON-OPENCV|SOPHON-SAIL| SOPHONSDK   |
|-------- |------------|---------|---------    |----------   | ------    | --------  |
| 0.3.6  | >=1.15      | >=0.5.0 | >=0.7.3     | >=0.7.3     | >=3.8.0   | >=v24.04.01|
| 0.3.5  | >=1.15      | >=0.5.0 | >=0.7.3     | >=0.7.3     | >=3.8.0   | >=v24.04.01|
| 0.3.4  | >=1.15      | >=0.5.0 | >=0.7.3     | >=0.7.3     | >=3.8.0   | >=v24.04.01|
| 0.3.3  | >=1.15      | >=0.5.0 | >=0.7.3     | >=0.7.3     | >=3.8.0   | >=v24.04.01|
| 0.3.2  | >=1.15      | >=0.5.0 | >=0.7.3     | >=0.7.3     | >=3.8.0   | >=v24.04.01|
| 0.3.1  | >=1.15      | >=0.5.0 | >=0.7.3     | >=0.7.3     | >=3.8.0   | >=v24.04.01|
| 0.3.0  | >=1.15      | >=0.5.0 | >=0.7.3     | >=0.7.3     | >=3.8.0   | >=v24.04.01|
| 0.2.10 | >=1.15      | >=0.5.0 | >=0.7.3     | >=0.7.3     | >=3.8.0   | >=v24.04.01|
| 0.2.9  | >=1.15      | >=0.5.0 | >=0.7.3     | >=0.7.3     | >=3.8.0   | >=v24.04.01|
| 0.2.8  | >=1.9       | >=0.5.0 | >=0.7.3     | >=0.7.3     | >=3.8.0   | >=v24.04.01|
| 0.2.7  | >=1.9       | >=0.5.0 | >=0.7.3     | >=0.7.3     | >=3.8.0   | >=v24.04.01|
| 0.2.6  | >=1.9       | >=0.5.0 | >=0.7.3     | >=0.7.3     | >=3.8.0   | >=v24.04.01|
| 0.2.5  | >=1.9       | >=0.5.0 | >=0.7.3     | >=0.7.3     | >=3.7.0   | >=v24.04.01|
| 0.2.4  | >=1.9       | >=0.5.0 | >=0.7.3     | >=0.7.3     | >=3.7.0   | >=v24.04.01|
| 0.2.3  | >=1.8       | >=0.5.0 | >=0.7.3     | >=0.7.3     | >=3.7.0   | >=v24.04.01|
| 0.2.2  | >=1.8       | >=0.5.0 | >=0.7.3     | >=0.7.3     | >=3.7.0   | >=v23.10.01|
| 0.2.1  | >=1.7       | >=0.5.0 | >=0.7.3     | >=0.7.3     | >=3.7.0   | >=v23.10.01|
| 0.2.0  | >=1.6       | >=0.5.0 | >=0.7.3     | >=0.7.3     | >=3.7.0   | >=v23.10.01|
| 0.1.10 | >=1.2.2     | >=0.4.6 | >=0.6.0     | >=0.6.0     | >=3.7.0   | >=v23.07.01|
| 0.1.9  | >=1.2.2     | >=0.4.6 | >=0.6.0     | >=0.6.0     | >=3.7.0   | >=v23.07.01|
| 0.1.8  | >=1.2.2     | >=0.4.6 | >=0.6.0     | >=0.6.0     | >=3.6.0   | >=v23.07.01|
| 0.1.7  | >=1.2.2     | >=0.4.6 | >=0.6.0     | >=0.6.0     | >=3.6.0   | >=v23.07.01|
| 0.1.6  | >=0.9.9     | >=0.4.6 | >=0.6.0     | >=0.6.0     | >=3.4.0   | >=v23.05.01|
| 0.1.5  | >=0.9.9     | >=0.4.6 | >=0.6.0     | >=0.6.0     | >=3.4.0   | >=v23.03.01|
| 0.1.4  | >=0.7.1     | >=0.4.4 | >=0.5.1     | >=0.5.1     | >=3.3.0   | >=v22.12.01|
| 0.1.3  | >=0.7.1     | >=0.4.4 | >=0.5.1     | >=0.5.1     | >=3.3.0   |    -      |
| 0.1.2  | Not support | >=0.4.3 | >=0.5.0     | >=0.5.0     | >=3.2.0   |    -      |
| 0.1.1  | Not support | >=0.4.2 | >=0.4.0     | >=0.4.0     | >=3.1.0   |    -      |
| 0.1.0  | Not support | >=0.3.0 | >=0.2.4     | >=0.2.4     | >=3.1.0   |    -      |

对于BM1688/CV186AH SOPHONSDK，其版本要求如下：
|SOPHON-DEMO|TPU-MLIR  |LIBSOPHON|SOPHON-FFMPEG|SOPHON-OPENCV|SOPHON-SAIL| SOPHONSDK   |
|-------- |------------|---------|---------    |----------   | ------    | --------  |
| 0.3.6  | >=1.15      | >=0.4.9 | >=1.7.0     | >=1.7.0     | >=3.8.0   | >=v1.7.0  |
| 0.3.5  | >=1.15      | >=0.4.9 | >=1.7.0     | >=1.7.0     | >=3.8.0   | >=v1.7.0  |
| 0.3.4  | >=1.15      | >=0.4.9 | >=1.7.0     | >=1.7.0     | >=3.8.0   | >=v1.7.0  |
| 0.3.3  | >=1.15      | >=0.4.9 | >=1.7.0     | >=1.7.0     | >=3.8.0   | >=v1.7.0  |
| 0.3.2  | >=1.15      | >=0.4.9 | >=1.7.0     | >=1.7.0     | >=3.8.0   | >=v1.7.0  |
| 0.3.1  | >=1.15      | >=0.4.9 | >=1.7.0     | >=1.7.0     | >=3.8.0   | >=v1.7.0  |
| 0.3.0  | >=1.15      | >=0.4.9 | >=1.7.0     | >=1.7.0     | >=3.8.0   | >=v1.7.0  |
| 0.2.10 | >=1.15      | >=0.4.9 | >=1.7.0     | >=1.7.0     | >=3.8.0   | >=v1.7.0  |
| 0.2.9  | >=1.15      | >=0.4.9 | >=1.7.0     | >=1.7.0     | >=3.8.0   | >=v1.7.0  |
| 0.2.8  | >=1.10      | >=0.4.9 | >=1.7.0     | >=1.7.0     | >=3.8.0   | >=v1.7.0  |
| 0.2.7  | >=1.10      | >=0.4.9 | >=1.7.0     | >=1.7.0     | >=3.8.0   | >=v1.7.0  |
| 0.2.6  | >=1.10      | >=0.4.9 | >=1.7.0     | >=1.7.0     | >=3.8.0   | >=v1.7.0  |
| 0.2.5  | >=1.9       | >=0.4.9 | >=1.7.0     | >=1.7.0     | >=3.8.0   | >=v1.7.0  |
| 0.2.4  | >=1.9       | >=0.4.9 | >=1.7.0     | >=1.7.0     | >=3.8.0   | >=v1.7.0  |
| 0.2.3  | >=1.8       | >=0.4.9 | >=1.7.0     | >=1.7.0     | >=3.8.0   | >=v1.7.0  |
| 0.2.2  | >=1.8       | >=0.4.9 | >=1.6.0     | >=1.6.0     | >=3.8.0   | >=v1.6.0  |
| 0.2.1  | >=1.7       | >=0.4.9 | >=1.5.0     | >=1.5.0     | >=3.8.0   | >=v1.5.0  |
| 0.2.0  | >=1.6       | >=0.4.9 | >=1.5.0     | >=1.5.0     | >=3.7.0   | >=v1.5.0  |

> **注意**：
> 1. 不同例程对版本的要求可能存在差异，具体以例程的README为准，可能需要安装其他第三方库。
> 2. BM1688/CV186X与BM1684/BM1684X对应的sdk不是同一套，在官网上已作区分，请注意。

## 技术资料

请通过算能官网[技术资料](https://developer.sophgo.com/site/index.html)获取相关文档、资料及视频教程。

## 社区

算能社区鼓励开发者多交流，共学习。开发者可以通过以下渠道进行交流和学习。

算能社区网站：https://www.sophgo.com/

算能开发者论坛：https://developer.sophgo.com/forum/index.html


## 贡献

欢迎参与贡献。更多详情，请参阅我们的[贡献者Wiki](./CONTRIBUTING_CN.md)。

## 许可证
[Apache License 2.0](./LICENSE)

# 文件: application/Audio_assistant/README.md

---

# Audio_assistant 例程

## 目录

- [Audio\_assistant 例程](#audio_assistant-例程)
  - [目录](#目录)
  - [简介](#简介)
  - [特性](#特性)
  - [1. 工程目录](#1-工程目录)
  - [2. 运行环境准备](#2-运行环境准备)
  - [3. 例程](#3-例程)
  - [4. FAQ](#4-faq)


## 简介
Audio_assistant 例程是一个基于Whisper、MiniCPM、Llama3、VITS模型的语音助手系统，支持输入为音频，输出为音频，其中包括对输入音频内容回答的相关信息，暂只支持中文。可以实现流畅的人机交互，能够应用到智能机器人、智能家具、自动驾驶等多样化的应用场景。

## 特性
* 支持BM1688(SoC)
* 支持BM1684X(PCIE、SOC)
* 支持本机麦克风、文件输入，本机喇叭、文件输出
* 支持网络麦克风，网络喇叭

## 1. 工程目录

```bash
Audio_assistant
├── models
│   ├── BM1688
│   │   ├── minicpm    # BM1688 MiniCPM LLM模型文件夹	
│   │   ├── vits       # BM1688 VITS语音生成模型文件夹	
│   │   └── whisper    # BM1688 Whisper语音识别模型文件夹
│   ├── BM1684X
│   │   ├── llama3     # BM1684X Llama3 LLM模型文件夹	
│   │   ├── vits       # BM1684X VITS语音生成模型文件夹	
│   │   └── whisper    # BM1684X Whisper语音识别模型文件夹
├── datasets       # 包含了音频测试文件
├── python
│   ├── socket_demo       # socket网络应用文件夹
│   │   ├── client        # 客户端文件夹，包括源码和依赖库信息
│   │   └── service       # 服务端文件夹，包括源码和依赖库信息
│   ├── Llama3     # Llama3源码和依赖库文件夹
│   │   ├── python_demo   # Llama3源码文件夹
│   │   └── support       # Llama3依赖库文件夹
│   ├── libfirmware_core.so # Bmodel运行时库
│   ├── MiniCPM    # MiniCPM源码和依赖库文件夹
│   │   ├── demo          # MiniCPM源码文件夹
│   │   └── support       # MiniCPM依赖库文件夹
│   ├── whisper-TPU_py    # Whisper源码文件夹
│   ├── whisper_minicpm_llama3_vits.py     # 全流程串通源代码
│   └── whisperWrapper.py                  # Whisper接口源代码
└── scripts
    ├── download_bm1684x_whisper_llama3_vits.sh       # BM1684X模型下载脚本，包括Whisper-small、Whisper-medium、Whisper-base、Llama3-8b、VITS-chinese
    ├── download_bm1688_whisper_minicpm_vits.sh       # BM1688模型下载脚本，包括Whisper-small、Whisper-base、MiniCPM-2b、VITS-chinese
    ├── download_datasets.sh                          # 音频测试文件下载脚本
    └── download.sh                                   # 完整的模型、数据下载脚本
```

## 2. 运行环境准备
在PCIe和BM1688 SOC上无需修改内存，对于1684X SOC模式系列设备（如SE7/SM7），都可以通过如下方式完成环境准备，使得满足运行条件，参考如下命令修改设备内存分布：
```bash
cd /data/
mkdir memedit && cd memedit
wget -nd https://github.com/sophgo/sophon-tools/releases/download/v24.09.21/memory_edit_v2.10.tar.xz
tar xvf memory_edit_v2.10.tar.xz
cd memory_edit
./memory_edit.sh -p #这个命令会打印当前的内存布局信息
./memory_edit.sh -c -npu 6616 -vpu 512 -vpp 3072 #npu也可以访问vpu和vpp的内存
sudo cp /data/memedit/DeviceMemoryModificationKit/memory_edit/emmcboot.itb /boot/emmcboot.itb && sync
sudo reboot
```
> **注意：**
> 1. 更多教程请参考[SoC内存修改工具](https://doc.sophgo.com/sdk-docs/v23.09.01-lts/docs_latest_release/docs/SophonSDK_doc/zh/html/appendix/2_mem_edit_tools.html)。

## 3. 例程
- [Python例程](./python/README.md)
- [socket_demo例程](./python/socket_demo/README.md)

## 4. FAQ
- 若使用麦克风不能进行录音，则需要检查和修改参数`--microphone_devid`。排查流程如下：
  - 首先若使用的USB麦克风，不是则跳到下一步骤，需要添加当前用户到`audio`用户组，执行:
    ```bash
    sudo usermod -a -G audio $(whoami)
    ```

  - 然后需要使用如下命令查看所有音频输入设备，获得所有音频输入设备的`{card id}`和`{device id}`两个id
    ```bash
    # 安装必要的音频库
    sudo apt-get install alsa-utils
    arecord -l
    ```

  - 使用如下命令尝试录音，其中`-d 5`参数是指录5s音频，`-D hw:{card id},{device id}`参数用于指定设备，来自上一步骤命令输出，`{fs}`是指输入音频的采样率，部分麦克风仅仅支持`44100`或`16000`，需要测试获得
    ```bash
    arecord -D hw:{card id},{device id} -c 1 -f S16_LE -r {fs} -d 5 test.wav
    ```

  - 通过上述步骤即可获得能够录音的设备名称和采样率，接着执行如下命令即可将设备名称和程序里面音频输入设备id`microphone_devid`对应，即命令输出的输入设备里面的`index`字段
    ```bash
    python3 tools/get_audio_device.py
    ```

- 若使用喇叭不能进行播放，则需要检查和修改参数`--audio_devid`。排查流程如下：
  - 首先若使用的USB喇叭，不是则跳到下一步骤，需要添加当前用户到`audio`用户组，执行:
    ```bash
    sudo usermod -a -G audio $(whoami)
    ```

  - 然后需要使用如下命令查看所有音频输出设备，获得所有音频输出设备的`{card id}`和`{device id}`两个id
    ```bash
    # 安装必要的音频库
    sudo apt-get install alsa-utils
    aplay -l
    ```

  - 使用如下命令尝试播放，其中`-D plughw:{card id},{device id}`参数用于指定设备，来自上一步骤命令输出，`{fs}`是指输出音频的采样率，部分喇叭仅仅支持`44100`或`16000`，需要测试获得
    ```bash
    aplay -D plughw:{card id},{device id} -f S16_LE -r {fs} /path/to/audio/file
    ```

  - 通过上述步骤即可获得能够播放的设备名称和采样率，接着执行如下命令即可将设备名称和程序里面音频输出设备id`audio_devid`对应，即命令输出的输出设备里面的`index`字段
    ```bash
    python3 tools/get_audio_device.py
    ```

# 文件: application/Audio_assistant/python/README.md

---

# Python例程 <!-- omit in toc -->

## 目录 <!-- omit in toc -->
- [1. 环境准备](#1-环境准备)
  - [1.1 x86/arm PCIe平台](#11-x86arm-pcie平台)
  - [1.2 SoC平台](#12-soc平台)
- [2. 准备模型与数据](#2-准备模型与数据)
- [3. 推理测试](#3-推理测试)
  - [3.1 参数说明](#31-参数说明)
  - [3.2 使用方式](#32-使用方式)
- [4. 程序运行性能](#4-程序运行性能)
- [5. 流程图](#5-流程图)

python目录下提供了Python例程，具体情况如下：

| 序号  |             Python例程                    |             说明                |
| ---- | ----------------------------------------  | ------------------------------- |
| 1    |    whisper_minicpm_llama3_vits.py         |         使用SAIL和BMRT推理       |


## 1. 环境准备
### 1.1 x86/arm PCIe平台

如果您在x86/arm平台安装了PCIe加速卡（如SC系列加速卡），并使用它测试本例程，您需要安装libsophon、sophon-opencv、sophon-ffmpeg和sophon-sail，具体请参考[x86-pcie平台的开发和运行环境搭建](../../../docs/Environment_Install_Guide.md#3-x86-pcie平台的开发和运行环境搭建)或[arm-pcie平台的开发和运行环境搭建](../../../docs/Environment_Install_Guide.md#5-arm-pcie平台的开发和运行环境搭建)。

- Python >= 3.8.2环境，SDK >= v23.09。

- 如果您使用Llama3作为LLM，则需要执行如下步骤进行编译
```bash
sudo apt-get install pybind11-dev
# 编译库文件
cd Llama3/python_demo
python3 -m dfss --url=open@sophgo.com:sophon-demo/application/Audio_assistant/llama3/support.zip
unzip support.zip -d ../
rm -f support.zip
mkdir build
cd build && cmake -DTARGET_ARCH=pcie .. && make && mv *cpython* ../..
cd ../../..
```

- 接着需要下载Whisper的依赖文件
```bash
cd whisper-TPU_py/bmwhisper
python3 -m dfss --url=open@sophgo.com:sophon-demo/application/Audio_assistant/whisper-TPU_py/third_party.zip
unzip third_party.zip -d ./
rm -f third_party.zip
python3 -m dfss --url=open@sophgo.com:sophon-demo/application/Audio_assistant/whisper-TPU_py/assets.zip
unzip assets.zip -d ./
rm -f assets.zip
cd ../..
```

- 此外您还需要安装其他python第三方库：
```bash
sudo apt install portaudio19-dev
sudo apt-get install libsndfile1
pip3 install torch==2.2.2 torchvision==0.17.2 torchaudio==2.2.2 --index-url https://download.pytorch.org/whl/cpu
pip3 install -r requirements.txt
```

### 1.2 SoC平台

如果您使用SoC平台（如SE、SM系列边缘设备），并使用它测试本例程，刷机后在`/opt/sophon/`下已经预装了相应的libsophon、sophon-opencv和sophon-ffmpeg运行库包。

- SDK >= v23.09

- 如果您使用Llama3作为LLM，则需要在SOC平台执行如下步骤进行编译
```bash
sudo apt-get install pybind11-dev
# 编译库文件
cd Llama3/python_demo
python3 -m dfss --url=open@sophgo.com:sophon-demo/application/Audio_assistant/llama3/support.zip
unzip support.zip -d ../
rm -f support.zip
mkdir build
cd build && cmake -DTARGET_ARCH=soc .. && make && mv *cpython* ../..
cd ../../..
```

- 如果您使用MiniCPM作为LLM，则需要在SOC平台执行如下步骤进行编译
```bash
# 编译库文件
cd MiniCPM/demo
python3 -m dfss --url=open@sophgo.com:sophon-demo/application/Audio_assistant/minicpm/support.zip
unzip support.zip -d ../
rm -f support.zip
mkdir build
cd build && cmake -DTARGET_ARCH=soc .. && make && mv minicpm ..
cd ../../..
```

- 接着需要下载Whisper的依赖文件
```bash
cd whisper-TPU_py/bmwhisper
python3 -m dfss --url=open@sophgo.com:sophon-demo/application/Audio_assistant/whisper-TPU_py/third_party.zip
unzip third_party.zip -d ./
rm -f third_party.zip
python3 -m dfss --url=open@sophgo.com:sophon-demo/application/Audio_assistant/whisper-TPU_py/assets.zip
unzip assets.zip -d ./
rm -f assets.zip
cd ../..
```

- 此外您还需要在SOC平台安装其他python第三方库：
```bash
pip3 install dfss -i https://pypi.tuna.tsinghua.edu.cn/simple --upgrade
# 对于SE9平台
python3 -m dfss --url=open@sophgo.com:sophon-demo/application/Audio_assistant/sophon_arm-3.8.0-py3-none-any.whl
pip3 install sophon_arm-3.8.0-py3-none-any.whl --force-reinstall
rm -f sophon_arm-3.8.0-py3-none-any.whl
# 对于SE7平台
python3 -m dfss --url=open@sophgo.com:sophon-demo/application/Audio_assistant/84x_soc_sail/sophon-3.8.0-py3-none-any.whl
pip3 install sophon-3.8.0-py3-none-any.whl --force-reinstall
rm -f sophon-3.8.0-py3-none-any.whl
# 对于SE7、SE9平台
sudo apt install portaudio19-dev
sudo apt-get install libsndfile1
pip3 install networkx==2.8.8
pip3 install torch==2.2.2 torchvision==0.17.2 torchaudio==2.2.2 --index-url https://download.pytorch.org/whl/cpu
pip3 install requests==2.26.0
pip3 install -r requirements.txt
```

- 对于SE9平台，运行前需要下载额外动态库，然后设置环境变量
```bash
python3 -m dfss --url=open@sophgo.com:sophon-demo/application/Audio_assistant/libfirmware_core.so
export BMRUNTIME_USING_FIRMWARE=/path-to-current-dir/libfirmware_core.so
```

## 2. 准备模型与数据
该例程目前只支持在BM1684X和BM1688上运行，已提供编译好的bmodel和测试数据，​同时，您也可以自行准备用于测试的数据集。

​本例程在`scripts`目录下提供了相关模型和数据的下载脚本
```bash
└── scripts
    ├── download_bm1684x_whisper_llama3_vits.sh                              # 通过该脚本下载BM1684X平台运行所需要的BModel
    ├── download_bm1688_whisper_minicpm_vits.sh                              # 通过该脚本下载BM1688平台运行所需要的BModel
    ├── download_datasets.sh                                                 # 通过该脚本下载测试音频文件
    └── download.sh                                                          # 通过该脚本下载所有模型和测试数据
```

- 对于BM1688平台，执行如下命令下载模型
```bash
# 安装unzip，若已安装请跳过
sudo apt install unzip
cd ..
chmod -R +x scripts/
./scripts/download_bm1688_whisper_minicpm_vits.sh
cd python
```

下载的模型包括：
```
./models
└── BM1688
    ├── minicpm
    |   ├── minicpm-2b_int4_1core.bmodel                                                                 # MiniCPM-2B int4，1core BM1688 BModel
    |   └── tokenizer.model                                                                              # MiniCPM-2B 的Tokenizer模型
    ├── vits
    |   ├── bert_1688_f32_1core.bmodel                                                                   # VITS BERT fp32，1core BM1688 BModel
    |   └── vits_chinese_128_bm1688_f16_1core.bmodel                                                     # VITS fp16，1core BM1688 BModel
    └── whisper
        ├── all_quant_decoder_loop_with_kvcache_and_rearrange_base_5beam_128pad_bm1688_f16.bmodel        # Whisper-Base Decoder模型，beam size为5，输出最大token长度为128，fp16 BM1688 BModel
        ├── all_quant_decoder_loop_with_kvcache_and_rearrange_small_5beam_128pad_bm1688_f16.bmodel       # Whisper-Small Decoder模型，beam size为5，输出最大token长度为128，fp16 BM1688 BModel
        ├── all_quant_decoder_loop_with_kvcache_and_rearrange_small_5beam_448pad_bm1688_f16.bmodel       # Whisper-Small Decoder模型，beam size为5，输出最大token长度为448，效率相比128模型更低，fp16 BM1688 BModel
        ├── all_quant_decoder_main_with_kvcache_base_5beam_128pad_bm1688_f16.bmodel                      # Whisper-Base Decoder模型，beam size为5，输出最大token长度为128，fp16 BM1688 BModel
        ├── all_quant_decoder_main_with_kvcache_small_5beam_128pad_bm1688_f16.bmodel                     # Whisper-Small Decoder模型，beam size为5，输出最大token长度为128，fp16 BM1688 BModel
        ├── all_quant_decoder_main_with_kvcache_small_5beam_448pad_bm1688_f16.bmodel                     # Whisper-Small Decoder模型，beam size为5，输出最大token长度为448，效率相比128模型更低，fp16 BM1688 BModel
        ├── all_quant_decoder_post_base_5beam_128pad_bm1688_f16.bmodel                                   # Whisper-Base Decoder模型，beam size为5，fp16 BM1688 BModel
        ├── all_quant_decoder_post_small_5beam_128pad_bm1688_f16.bmodel                                  # Whisper-Small Decoder模型，beam size为5，fp16 BM1688 BModel
        ├── all_quant_decoder_post_small_5beam_448pad_bm1688_f16.bmodel                                  # Whisper-Small Decoder模型，beam size为5，fp16 BM1688 BModel
        ├── all_quant_encoder_base_5beam_128pad_bm1688_f16.bmodel                                        # Whisper-Base Encoder模型，beam size为5，fp16 BM1688 BModel
        ├── all_quant_encoder_small_5beam_128pad_bm1688_f16.bmodel                                       # Whisper-Small Encoder模型，beam size为5，fp16 BM1688 BModel
        ├── all_quant_encoder_small_5beam_448pad_bm1688_f16.bmodel                                       # Whisper-Small Encoder模型，beam size为5，fp16 BM1688 BModel
        ├── all_quant_logits_decoder_base_5beam_128pad_bm1688_f16.bmodel                                 # Whisper-Base 预测层，beam size为5，fp16 BM1688 BModel
        ├── all_quant_logits_decoder_small_5beam_128pad_bm1688_f16.bmodel                                # Whisper-Small 预测层，beam size为5，fp16 BM1688 BModel
        └── all_quant_logits_decoder_small_5beam_448pad_bm1688_f16.bmodel                                # Whisper-Small 预测层，beam size为5，fp16 BM1688 BModel
```

- 对于BM1684X平台，执行如下命令下载模型
```bash
# 安装unzip，若已安装请跳过
sudo apt install unzip
cd ..
chmod -R +x scripts/
./scripts/download_bm1684x_whisper_llama3_vits.sh
cd python
```

下载的模型包括：
```
./models
└── BM1684X
    ├── llama3
    |   ├── token_config                                                                                 # Llama3-8B Tokenizer配置文件 
    |   └── llama3-8b_int4_1dev_256.bmodel                                                               # Llama3-8B 最大输出长度为256个tokens，int4 Bmodel
    ├── vits
    |   ├── bert_1684x_f32.bmodel                                                                        # VITS BERT fp32 BModel
    |   └── vits_chinese_128_f16.bmodel                                                                  # VITS fp16 BModel
    └── whisper
        ├── all_quant_decoder_loop_with_kvcache_and_rearrange_base_5beam_448pad_1684x_f16.bmodel         # Whisper-Base Decoder模型，beam size为5，输出最大token长度为448，fp16 BM1684X BModel
        ├── all_quant_decoder_loop_with_kvcache_and_rearrange_large-v2_5beam_448pad_1684x_f16.bmodel     # Whisper-Large-v2 Decoder模型，beam size为5，输出最大token长度为448，fp16 BM1684X BModel
        ├── all_quant_decoder_loop_with_kvcache_and_rearrange_large-v3_5beam_448pad_1684x_f16.bmodel     # Whisper-Large-v3 Decoder模型，beam size为5，输出最大token长度为448，fp16 BM1684X BModel
        ├── all_quant_decoder_loop_with_kvcache_and_rearrange_medium_5beam_448pad_1684x_f16.bmodel       # Whisper-Medium Decoder模型，beam size为5，输出最大token长度为448，fp16 BM1684X BModel
        ├── all_quant_decoder_loop_with_kvcache_and_rearrange_small_5beam_448pad_1684x_f16.bmodel        # Whisper-Small Decoder模型，beam size为5，输出最大token长度为448，fp16 BM1684X BModel
        ├── all_quant_decoder_main_with_kvcache_base_5beam_448pad_1684x_f16.bmodel                       # Whisper-Base Decoder模型，beam size为5，输出最大token长度为448，fp16 BM1684X BModel
        ├── all_quant_decoder_main_with_kvcache_medium_5beam_448pad_1684x_f16.bmodel                     # Whisper-Medium Decoder模型，beam size为5，输出最大token长度为448，fp16 BM1684X BModel
        ├── all_quant_decoder_main_with_kvcache_small_5beam_448pad_1684x_f16.bmodel                      # Whisper-Small Decoder模型，beam size为5，输出最大token长度为448，fp16 BM1684X BModel
        ├── all_quant_decoder_post_base_5beam_448pad_1684x_f16.bmodel                                    # Whisper-Base Decoder模型，beam size为5，fp16 BM1684X BModel
        ├── all_quant_decoder_post_medium_5beam_448pad_1684x_f16.bmodel                                  # Whisper-Medium Decoder模型，beam size为5，fp16 BM1684X BModel
        ├── all_quant_decoder_post_small_5beam_448pad_1684x_f16.bmodel                                   # Whisper-Small Decoder模型，beam size为5，fp16 BM1684X BModel
        ├── all_quant_encoder_base_5beam_448pad_1684x_f16.bmodel                                         # Whisper-Base Encoder模型，beam size为5，fp16 BM1684X BModel
        ├── all_quant_encoder_medium_5beam_448pad_1684x_f16.bmodel                                       # Whisper-Medium Encoder模型，beam size为5，fp16 BM1688 BModel
        ├── all_quant_encoder_small_5beam_448pad_1684x_f16.bmodel                                        # Whisper-Small Encoder模型，beam size为5，fp16 BM1684X BModel
        ├── all_quant_logits_decoder_base_5beam_448pad_1684x_f16.bmodel                                  # Whisper-Base 预测层，beam size为5，fp16 BM1684X BModel
        ├── all_quant_logits_decoder_medium_5beam_448pad_1684x_f16.bmodel                                # Whisper-Medium 预测层，beam size为5，fp16 BM1684X BModel
        └── all_quant_logits_decoder_small_5beam_448pad_1684x_f16.bmodel                                 # Whisper-Small 预测层，beam size为5，fp16 BM1684X BModel
```

- 执行如下命令下载测试数据
```bash
# 安装unzip，若已安装请跳过
sudo apt install unzip
cd ..
chmod -R +x scripts/
./scripts/download_datasets.sh
cd python
```
下载的数据包括：
```
./datasets
└── ai_zh.wav                                 # 测试用音频文件，包含中文问题“什么是人工智能？”
```

## 3. 推理测试
python例程不需要编译，可以直接运行，不同平台的测试参数和运行方式是相同的。
### 3.1 参数说明

算法配置参数说明：
```bash
usage: whisper_minicpm_llama3_vits.py [-h] [--profile] [--audio_in AUDIO_IN] [--output_file] [--llm_type LLM_TYPE] [--microphone_devid MICROPHONE_DEVID] [--min_tts_input_len MIN_TTS_INPUT_LEN]

--profile: 打印一些性能数据，默认不打印。
--audio_in: 输入音频，默认不传入任何参数，输入是麦克风，或者传入音频文件路径。
--output_file: 是否输出到文件， 默认输出到喇叭。
--streaming_output: 是否采用流式输出音频，对于使用喇叭设备会获得更好的效果，文件输出建议关闭，避免输出过多子文件。
--llm_type: LLM的类型，目前仅支持minicpm-2b或llama3-8b，目前BM1688上仅仅支持minicpm-2b。
--microphone_devid: 麦克风设备的ID，当且仅当输入为麦克风时有效。
--min_tts_input_len: 最小的TTS输入文本的长度，默认为30，可减小长度以减小延时。
```

**注意**
>1. 对于其中包含的语音算法或语言算法的配置参数可参考`whisper_minicpm_llama3_vits.py`源码。


### 3.2 使用方式
为了测试实时的麦克风输入、喇叭输出，可以执行如下命令
```bash
# 对于BM1688平台
python3 whisper_minicpm_llama3_vits.py --streaming_output
# 对于BM1684X SOC平台
python3 whisper_minicpm_llama3_vits.py --bmodel_dir ../BM1684X/whisper --vits_model ../BM1684X/vits/vits_chinese_128_f16.bmodel --bert_model ../BM1684X/vits/bert_1684x_f32.bmodel --llm_type llama3-8b --chip 1684x --padding_size 448 --chip_mode soc --streaming_output
# 对于BM1684X PCIE平台
python3 whisper_minicpm_llama3_vits.py --bmodel_dir ../BM1684X/whisper --vits_model ../BM1684X/vits/vits_chinese_128_f16.bmodel --bert_model ../BM1684X/vits/bert_1684x_f32.bmodel --llm_type llama3-8b --chip 1684x --padding_size 448 --chip_mode pcie --streaming_output
```

为了测试语音文件输入、喇叭输出，可以执行如下命令
```bash
# 对于BM1688平台
python3 whisper_minicpm_llama3_vits.py --audio_in=../datasets/ai_zh.wav --streaming_output
# 对于BM1684X SOC平台
python3 whisper_minicpm_llama3_vits.py --bmodel_dir ../BM1684X/whisper --vits_model ../BM1684X/vits/vits_chinese_128_f16.bmodel --bert_model ../BM1684X/vits/bert_1684x_f32.bmodel --llm_type llama3-8b --audio_in=../datasets/ai_zh.wav --chip 1684x --padding_size 448 --chip_mode soc --streaming_output 
# 对于BM1684X PCIE平台
python3 whisper_minicpm_llama3_vits.py --bmodel_dir ../BM1684X/whisper --vits_model ../BM1684X/vits/vits_chinese_128_f16.bmodel --bert_model ../BM1684X/vits/bert_1684x_f32.bmodel --llm_type llama3-8b --audio_in=../datasets/ai_zh.wav --chip 1684x --padding_size 448 --chip_mode pcie --streaming_output 
```

为了测试语音文件输入、语音文件输出，可以执行如下命令
```bash
# 对于BM1688平台
python3 whisper_minicpm_llama3_vits.py --audio_in=../datasets/ai_zh.wav --output_file
# 对于BM1684X SOC平台
python3 whisper_minicpm_llama3_vits.py --bmodel_dir ../BM1684X/whisper --vits_model ../BM1684X/vits/vits_chinese_128_f16.bmodel --bert_model ../BM1684X/vits/bert_1684x_f32.bmodel --llm_type llama3-8b --audio_in=../datasets/ai_zh.wav --chip 1684x --padding_size 448 --chip_mode soc --output_file 
# 对于BM1684X PCIE平台
python3 whisper_minicpm_llama3_vits.py --bmodel_dir ../BM1684X/whisper --vits_model ../BM1684X/vits/vits_chinese_128_f16.bmodel --bert_model ../BM1684X/vits/bert_1684x_f32.bmodel --llm_type llama3-8b --audio_in=../datasets/ai_zh.wav --chip 1684x --padding_size 448 --chip_mode pcie --output_file 
```

> **注意**
> 1. 如果没有麦克风或喇叭设备，请使用文件的形式
> 2. 若使用麦克风作为输入，当终端输出`microphone running ...`，就可以通过麦克风说出问题，等待回答即可。

## 4 程序运行性能
在不同的测试平台上，测试`../datasets/ai_zh.wav`音频文件，使用3.2节中语音文件作为输入、喇叭作为输出的命令进行测试，性能测试结果如下：
|    测试平台  |  Latency  | 
| ----------- | --------- |
|   SE7-32    |    8.8    |
|   SE9-16    |    8.7    |

> **测试说明**：  
> 1. 性能Latency指标是指问题说完到开始输出回答音频的时间，单位为秒(s)。
> 2. 不同PCIE平台有差异，以实际性能为准。
> 3. 性能结果受LLM输出的第一段话长度、参数`--min_tts_input_len`的影响，两者长度越长延时越高，实际性能可以通过实际数据测试得到。
> 4. 对于SE7，不同SDK版本性能可能存在较大差异，以实测为准。

## 5. 流程图

`whisper_minicpm_llama3_vits.py`中的处理流程，遵循以下流程图：

![flowchart](../pics/assistant1.png)

# 文件: application/Audio_assistant/python/socket_demo/README.md

---

# Audio assistant websocket应用例程 <!-- omit in toc -->

## 目录 <!-- omit in toc -->
- [1. Server端环境准备](#1-Server端环境准备)
  - [1.1 x86/arm PCIe平台](#11-x86arm-pcie平台)
  - [1.2 SoC平台](#12-soc平台)
- [2. Client端环境准备](#2-Client端环境准备)
  - [2.1 x86/arm PCIe、SoC平台](#21-x86/arm-pcie、soc平台)
- [3. Server端准备模型](#3-Server端准备模型)
- [4. Client端准备数据](#4-Client端准备数据)
- [5. 推理测试](#5-推理测试)
  - [5.1 参数说明](#51-参数说明)
  - [5.2 使用方式](#52-使用方式)
- [6. 程序运行性能](#6-程序运行性能)
- [7. 流程图](#7-流程图)

websocket_demo目录下提供了一系列Python例程，具体情况如下：

| 序号  |             Python例程                    |             说明                |
| ---- | ----------------------------------------  | ------------------------------- |
| 1    |    service/server.py                      |         服务端代码               |
| 2    |    client/client.py                       |         客户端代码               |


## 1. Server端环境准备

### 1.1 x86/arm PCIe平台

如果您在x86/arm平台安装了PCIe加速卡（如SC系列加速卡），并使用它测试本例程，您需要安装libsophon、sophon-opencv、sophon-ffmpeg和sophon-sail，具体请参考[x86-pcie平台的开发和运行环境搭建](../../../../docs/Environment_Install_Guide.md#3-x86-pcie平台的开发和运行环境搭建)或[arm-pcie平台的开发和运行环境搭建](../../../../docs/Environment_Install_Guide.md#5-arm-pcie平台的开发和运行环境搭建)。

- Python >= 3.8.2环境，SDK >= v23.09。

- 如果您使用Llama3作为LLM，则需要执行如下步骤进行编译
```bash
sudo apt-get install pybind11-dev
# 编译库文件
cd ../Llama3/python_demo
python3 -m dfss --url=open@sophgo.com:sophon-demo/application/Audio_assistant/llama3/support.zip
unzip support.zip -d ../
rm -f support.zip
mkdir build
cd build && cmake -DTARGET_ARCH=pcie .. && make && mv *cpython* ../..
cd ../../../socket_demo
```

- 接着需要下载Whisper的依赖文件
```bash
cd ../whisper-TPU_py/bmwhisper
python3 -m dfss --url=open@sophgo.com:sophon-demo/application/Audio_assistant/whisper-TPU_py/third_party.zip
unzip third_party.zip -d ./
rm -f third_party.zip
python3 -m dfss --url=open@sophgo.com:sophon-demo/application/Audio_assistant/whisper-TPU_py/assets.zip
unzip assets.zip -d ./
rm -f assets.zip
cd ../../socket_demo
```

- 此外您还需要安装其他python第三方库：
```bash
sudo apt install portaudio19-dev
sudo apt-get install libsndfile1
pip3 install torch==2.2.2 torchvision==0.17.2 torchaudio==2.2.2 --index-url https://download.pytorch.org/whl/cpu
pip3 install -r service/server_requirements.txt
```

### 1.2 SoC平台
如果您使用SoC平台（如SE、SM系列边缘设备），并使用它测试本例程，刷机后在`/opt/sophon/`下已经预装了相应的libsophon、sophon-opencv和sophon-ffmpeg运行库包。

- SDK >= v23.09

- 如果您使用Llama3作为LLM，则需要在SOC平台执行如下步骤进行编译
```bash
sudo apt-get install pybind11-dev
# 编译库文件
cd ../Llama3/python_demo
python3 -m dfss --url=open@sophgo.com:sophon-demo/application/Audio_assistant/llama3/support.zip
unzip support.zip -d ../
rm -f support.zip
mkdir build
cd build && cmake -DTARGET_ARCH=soc .. && make && mv *cpython* ../..
cd ../../../socket_demo
```

- 如果您使用MiniCPM作为LLM，则需要在SOC平台执行如下步骤进行编译
```bash
# 编译库文件
cd ../MiniCPM/demo
python3 -m dfss --url=open@sophgo.com:sophon-demo/application/Audio_assistant/minicpm/support.zip
unzip support.zip -d ../
rm -f support.zip
mkdir build
cd build && cmake -DTARGET_ARCH=soc .. && make && mv minicpm ..
cd ../../../socket_demo
```

- 接着需要下载Whisper的依赖文件
```bash
cd ../whisper-TPU_py/bmwhisper
python3 -m dfss --url=open@sophgo.com:sophon-demo/application/Audio_assistant/whisper-TPU_py/third_party.zip
unzip third_party.zip -d ./
rm -f third_party.zip
python3 -m dfss --url=open@sophgo.com:sophon-demo/application/Audio_assistant/whisper-TPU_py/assets.zip
unzip assets.zip -d ./
rm -f assets.zip
cd ../../socket_demo
```

- 此外您还需要在SOC平台安装其他python第三方库：
```bash
pip3 install dfss -i https://pypi.tuna.tsinghua.edu.cn/simple --upgrade
# 对于SE9平台
python3 -m dfss --url=open@sophgo.com:sophon-demo/application/Audio_assistant/sophon_arm-3.8.0-py3-none-any.whl
pip3 install sophon_arm-3.8.0-py3-none-any.whl --force-reinstall
rm -f sophon_arm-3.8.0-py3-none-any.whl
# 对于SE7平台
python3 -m dfss --url=open@sophgo.com:sophon-demo/application/Audio_assistant/84x_soc_sail/sophon-3.8.0-py3-none-any.whl
pip3 install sophon-3.8.0-py3-none-any.whl --force-reinstall
rm -f sophon-3.8.0-py3-none-any.whl
# 对于SE7、SE9平台
sudo apt install portaudio19-dev
sudo apt install libsndfile1
pip3 install networkx==2.8.8
pip3 install torch==2.2.2 torchvision==0.17.2 torchaudio==2.2.2 --index-url https://download.pytorch.org/whl/cpu
pip3 install requests==2.26.0
pip3 install -r service/server_requirements.txt
```

- 对于SE9平台，运行前需要下载额外动态库，然后设置环境变量
```bash
python3 -m dfss --url=open@sophgo.com:sophon-demo/application/Audio_assistant/libfirmware_core.so
export BMRUNTIME_USING_FIRMWARE=/path-to-current-dir/libfirmware_core.so
```

## 2. Client端环境准备

### 2.1 x86/arm PCIe、SoC平台

您只需要执行如下命令安装其他第三方库：
```bash
sudo apt install portaudio19-dev
pip3 install torch==2.2.2 torchvision==0.17.2 torchaudio==2.2.2 --index-url https://download.pytorch.org/whl/cpu
pip3 install -r client/client_requirements.txt
```

## 3. Server端准备模型
目前只支持在BM1684X和BM1688上运行，已提供编译好的BModel。

​本例程在`scripts`目录下提供了相关模型的下载脚本
```bash
└── scripts
    ├── download_bm1684x_whisper_llama3_vits.sh                                      # 通过该脚本下载BM1684X平台的Whisper/Llama3/VITS BModels
    └── download_bm1688_whisper_minicpm_vits.sh                                      # 通过该脚本下载BM1688平台的Whisper/MiniCPM/VITS BModels
```

- 对于BM1688平台，执行如下命令下载模型
```bash
# 安装unzip，若已安装请跳过
sudo apt install unzip
cd ../..
chmod -R +x scripts/
./scripts/download_bm1688_whisper_minicpm_vits.sh
cd python/socket_demo
```

下载的模型包括：
```
./models
└── BM1688
    ├── minicpm
    |   ├── minicpm-2b_int4_1core.bmodel                                                                 # MiniCPM-2B int4，1core BM1688 BModel
    |   └── tokenizer.model                                                                              # MiniCPM-2B 的Tokenizer模型
    ├── vits
    |   ├── bert_1688_f32_1core.bmodel                                                                   # VITS BERT fp32，1core BM1688 BModel
    |   └── vits_chinese_128_bm1688_f16_1core.bmodel                                                     # VITS fp16，1core BM1688 BModel
    └── whisper
        ├── all_quant_decoder_loop_with_kvcache_and_rearrange_base_5beam_128pad_bm1688_f16.bmodel        # Whisper-Base Decoder模型，beam size为5，输出最大token长度为128，fp16 BM1688 BModel
        ├── all_quant_decoder_loop_with_kvcache_and_rearrange_small_5beam_128pad_bm1688_f16.bmodel       # Whisper-Small Decoder模型，beam size为5，输出最大token长度为128，fp16 BM1688 BModel
        ├── all_quant_decoder_loop_with_kvcache_and_rearrange_small_5beam_448pad_bm1688_f16.bmodel       # Whisper-Small Decoder模型，beam size为5，输出最大token长度为448，效率相比128模型更低，fp16 BM1688 BModel
        ├── all_quant_decoder_main_with_kvcache_base_5beam_128pad_bm1688_f16.bmodel                      # Whisper-Base Decoder模型，beam size为5，输出最大token长度为128，fp16 BM1688 BModel
        ├── all_quant_decoder_main_with_kvcache_small_5beam_128pad_bm1688_f16.bmodel                     # Whisper-Small Decoder模型，beam size为5，输出最大token长度为128，fp16 BM1688 BModel
        ├── all_quant_decoder_main_with_kvcache_small_5beam_448pad_bm1688_f16.bmodel                     # Whisper-Small Decoder模型，beam size为5，输出最大token长度为448，效率相比128模型更低，fp16 BM1688 BModel
        ├── all_quant_decoder_post_base_5beam_128pad_bm1688_f16.bmodel                                   # Whisper-Base Decoder模型，beam size为5，fp16 BM1688 BModel
        ├── all_quant_decoder_post_small_5beam_128pad_bm1688_f16.bmodel                                  # Whisper-Small Decoder模型，beam size为5，fp16 BM1688 BModel
        ├── all_quant_decoder_post_small_5beam_448pad_bm1688_f16.bmodel                                  # Whisper-Small Decoder模型，beam size为5，fp16 BM1688 BModel
        ├── all_quant_encoder_base_5beam_128pad_bm1688_f16.bmodel                                        # Whisper-Base Encoder模型，beam size为5，fp16 BM1688 BModel
        ├── all_quant_encoder_small_5beam_128pad_bm1688_f16.bmodel                                       # Whisper-Small Encoder模型，beam size为5，fp16 BM1688 BModel
        ├── all_quant_encoder_small_5beam_448pad_bm1688_f16.bmodel                                       # Whisper-Small Encoder模型，beam size为5，fp16 BM1688 BModel
        ├── all_quant_logits_decoder_base_5beam_128pad_bm1688_f16.bmodel                                 # Whisper-Base 预测层，beam size为5，fp16 BM1688 BModel
        ├── all_quant_logits_decoder_small_5beam_128pad_bm1688_f16.bmodel                                # Whisper-Small 预测层，beam size为5，fp16 BM1688 BModel
        └── all_quant_logits_decoder_small_5beam_448pad_bm1688_f16.bmodel                                # Whisper-Small 预测层，beam size为5，fp16 BM1688 BModel
```

- 对于BM1684X平台，执行如下命令下载模型
```bash
# 安装unzip，若已安装请跳过
sudo apt install unzip
cd ..
chmod -R +x scripts/
./scripts/download_bm1684x_whisper_llama3_vits.sh
cd python/socket_demo
```

下载的模型包括：
```
./models
└── BM1684X
    ├── llama3
    |   ├── token_config                                                                                 # Llama3-8B Tokenizer配置文件 
    |   └── llama3-8b_int4_1dev_256.bmodel                                                               # Llama3-8B 最大输出长度为256个tokens，int4 Bmodel
    ├── vits
    |   ├── bert_1684x_f32.bmodel                                                                        # VITS BERT fp32 BModel
    |   └── vits_chinese_128_f16.bmodel                                                                  # VITS fp16 BModel
    └── whisper
        ├── all_quant_decoder_loop_with_kvcache_and_rearrange_base_5beam_448pad_1684x_f16.bmodel         # Whisper-Base Decoder模型，beam size为5，输出最大token长度为448，fp16 BM1684X BModel
        ├── all_quant_decoder_loop_with_kvcache_and_rearrange_large-v2_5beam_448pad_1684x_f16.bmodel     # Whisper-Large-v2 Decoder模型，beam size为5，输出最大token长度为448，fp16 BM1684X BModel
        ├── all_quant_decoder_loop_with_kvcache_and_rearrange_large-v3_5beam_448pad_1684x_f16.bmodel     # Whisper-Large-v3 Decoder模型，beam size为5，输出最大token长度为448，fp16 BM1684X BModel
        ├── all_quant_decoder_loop_with_kvcache_and_rearrange_medium_5beam_448pad_1684x_f16.bmodel       # Whisper-Medium Decoder模型，beam size为5，输出最大token长度为448，fp16 BM1684X BModel
        ├── all_quant_decoder_loop_with_kvcache_and_rearrange_small_5beam_448pad_1684x_f16.bmodel        # Whisper-Small Decoder模型，beam size为5，输出最大token长度为448，fp16 BM1684X BModel
        ├── all_quant_decoder_main_with_kvcache_base_5beam_448pad_1684x_f16.bmodel                       # Whisper-Base Decoder模型，beam size为5，输出最大token长度为448，fp16 BM1684X BModel
        ├── all_quant_decoder_main_with_kvcache_medium_5beam_448pad_1684x_f16.bmodel                     # Whisper-Medium Decoder模型，beam size为5，输出最大token长度为448，fp16 BM1684X BModel
        ├── all_quant_decoder_main_with_kvcache_small_5beam_448pad_1684x_f16.bmodel                      # Whisper-Small Decoder模型，beam size为5，输出最大token长度为448，fp16 BM1684X BModel
        ├── all_quant_decoder_post_base_5beam_448pad_1684x_f16.bmodel                                    # Whisper-Base Decoder模型，beam size为5，fp16 BM1684X BModel
        ├── all_quant_decoder_post_medium_5beam_448pad_1684x_f16.bmodel                                  # Whisper-Medium Decoder模型，beam size为5，fp16 BM1684X BModel
        ├── all_quant_decoder_post_small_5beam_448pad_1684x_f16.bmodel                                   # Whisper-Small Decoder模型，beam size为5，fp16 BM1684X BModel
        ├── all_quant_encoder_base_5beam_448pad_1684x_f16.bmodel                                         # Whisper-Base Encoder模型，beam size为5，fp16 BM1684X BModel
        ├── all_quant_encoder_medium_5beam_448pad_1684x_f16.bmodel                                       # Whisper-Medium Encoder模型，beam size为5，fp16 BM1688 BModel
        ├── all_quant_encoder_small_5beam_448pad_1684x_f16.bmodel                                        # Whisper-Small Encoder模型，beam size为5，fp16 BM1684X BModel
        ├── all_quant_logits_decoder_base_5beam_448pad_1684x_f16.bmodel                                  # Whisper-Base 预测层，beam size为5，fp16 BM1684X BModel
        ├── all_quant_logits_decoder_medium_5beam_448pad_1684x_f16.bmodel                                # Whisper-Medium 预测层，beam size为5，fp16 BM1684X BModel
        └── all_quant_logits_decoder_small_5beam_448pad_1684x_f16.bmodel                                 # Whisper-Small 预测层，beam size为5，fp16 BM1684X BModel
```

## 4. Client端准备数据
已提供测试数据，​同时，您可以自行准备用于测试的数据集。

​本例程在`scripts`目录下提供了相关数据的下载脚本`download_datasets.sh`

```bash
# 安装unzip，若已安装请跳过
sudo apt install unzip
cd ../../
chmod -R +x scripts/
# 在客户端执行
./scripts/download_datasets.sh
cd python/socket_demo
```

下载的数据包括：
```
./datasets
└── ai_zh.wav                                 # 测试用音频文件，包含中文问题“什么是人工智能？”
```

## 5. 推理测试
python例程不需要编译，可以直接运行，PCIe平台和SoC平台的测试参数和运行方式是相同的。
### 5.1 参数说明

服务端参数说明如下：
```bash
usage: server.py [-h] [--host HOST] [--port PORT] [--profile] [--streaming_output] [--llm_type LLM_TYPE] [--min_tts_input_len MIN_TTS_INPUT_LEN]
--host: 主机的IP，默认本机
--port: 服务的端口
--streaming_output: 是否使用流式输出，即并行LLM和TTS两个模块
--llm_type: LLM的类型, 目前支持minicpm-2b, llama3-8b
--min_tts_input_len: 最小的TTS输入文本的长度，默认为6，可减小长度以减小延时。
--bmodel_dir: Whisper模型文件夹路径
--chip: 指定Whisper运行的平台，支持1684x、bm1688
--padding_size: 指定Whisper所使用模型的padding尺寸，可从模型的文件名获得
--chip_mode: 指定平台的模式，支持pcie、soc
--vits_model: VITS模型路径
--bert_model: VITS所使用的BERT模型路径
```

客户端参数说明如下：
```bash
usage: client.py [-h] [--host HOST] [--port PORT] [--chunk_duration_ms CHUNK_DURATION_MS] [--vad_level VAD_LEVEL] [--vad_type VAD_TYPE] [--audio_in AUDIO_IN] [--audio_fs AUDIO_FS]
                     [--microphone_dev_id MICROPHONE_DEV_ID] [--output_file]
--host: 服务端的IP，默认为本机
--port: 服务端端口
--chunk_duration_ms: VAD一次性输入的音频长度，单位为毫秒，默认为200
--vad_level: webrtcvad的粒度，支持[0,3], 值越大粒度越细
--vad_type: VAD模型的类型，支持webrtcvad、fsmn-vad
--audio_in: 输入音频文件，如果未给出则使用麦克风输入
--audio_fs: 程序使用的音频sample rate，包括输出音频，默认16000
--microphone_devid: 麦克风设备id
--audio_devid: 喇叭设备id
--output_file: 是否输出音频文件，如果未给出则输出到喇叭
```

### 5.2 使用方式

### 5.2.1 启动服务器
若使用非流式输出，则需要等待回答完全结束才输出音频数据到客户端
```bash
# 对于BM1688 SOC平台可以使用如下命令
python3 service/server.py --port 10095 --bmodel_dir=../../BM1688/whisper
# 对于BM1684X SOC平台可以使用如下命令
python3 service/server.py --bmodel_dir ../../BM1684X/whisper --vits_model ../../BM1684X/vits/vits_chinese_128_f16.bmodel --bert_model ../../BM1684X/vits/bert_1684x_f32.bmodel --llm_type llama3-8b --chip 1684x --padding_size 448 --chip_mode soc
# 对于BM1684X PCIE平台可以使用如下命令
python3 service/server.py --bmodel_dir ../../BM1684X/whisper --vits_model ../../BM1684X/vits/vits_chinese_128_f16.bmodel --bert_model ../../BM1684X/vits/bert_1684x_f32.bmodel --llm_type llama3-8b --chip 1684x --padding_size 448 --chip_mode pcie
```

若使用流式输出，则边回答边输出音频数据到客户端，会有更好的实时音频输出效果
```bash
# 对于BM1688 SOC平台可以使用如下命令
python3 service/server.py --port 10095 --bmodel_dir=../../BM1688/whisper --streaming_output
# 对于BM1684X SOC平台可以使用如下命令
python3 service/server.py --bmodel_dir ../../BM1684X/whisper --vits_model ../../BM1684X/vits/vits_chinese_128_f16.bmodel --bert_model ../../BM1684X/vits/bert_1684x_f32.bmodel --llm_type llama3-8b --chip 1684x --padding_size 448 --chip_mode soc --streaming_output
# 对于BM1684X PCIE平台可以使用如下命令
python3 service/server.py --bmodel_dir ../../BM1684X/whisper --vits_model ../../BM1684X/vits/vits_chinese_128_f16.bmodel --bert_model ../../BM1684X/vits/bert_1684x_f32.bmodel --llm_type llama3-8b --chip 1684x --padding_size 448 --chip_mode pcie --streaming_output
```

### 5.2.2 启动客户端
若使用音频文件作为输入输出，则使用如下命令，根据实际情况修改`--host`参数为服务器IP地址，`--port`参数修改为服务器端口
```bash
python3 client/client.py --host 127.0.0.1 --port 10095 --audio_in ../../datasets/ai_zh.wav --output_file
```

若使用麦克风、喇叭作为输入输出，使用如下命令，需根据实际情况修改麦克风设备id，`--host`参数修改为服务器IP地址，`--port`参数修改为服务器端口
```bash
python3 client/client.py --host 127.0.0.1 --port 10095 --microphone_devid 0
```

若使用文件作为输入、喇叭作为输出，使用如下命令，根据实际情况修改`--host`参数为服务器IP地址，`--port`参数修改为服务器端口
```bash
python3 client/client.py --host 127.0.0.1 --port 10095 --audio_in ../../datasets/ai_zh.wav 
```

> **注意**
> 1. 如果没有麦克风或喇叭设备，请使用文件的形式
> 2. 若使用麦克风作为输入，当终端输出`microphone running ...`，就可以通过麦克风说出问题，等待回答即可。

## 6 程序运行性能
在不同的测试平台上，测试`../datasets/ai_zh.wav`音频文件，使用5.2.1节中流式输出、5.2.2节中文件作为输入喇叭作为输出的命令进行测试，性能测试结果如下：
|    服务端测试平台  |  客户端测试平台  |  Latency  | 
| ----------------- | --------------- | --------- |
|   SE7-32          |    SE7-32       |    8.5    |
|   SE9-16          |    SE9-16       |    9.3    |

> **测试说明**：  
> 1. 性能Latency指标是指问题说完到开始输出回答音频的时间（包括网络传输时间），单位为秒(s)。
> 2. 不同PCIE平台有差异，以实际性能为准。
> 3. 性能结果受LLM输出的第一段话长度、参数`--min_tts_input_len`、网络的影响，前两者长度越长延时越高，实际性能可以通过实际数据测试得到。
> 4. 对于SE7，不同SDK版本性能可能存在较大差异，以实测为准。

## 7. 流程图
`socket_demo`中的处理流程，遵循以下流程图：

![flowchart](../../pics/assistant2.png)

# 文件: application/ChatDoc/README.md

---

# ChatDoc

## 目录
- [ChatDoc](#ChatDoc)
  - [简介](#简介)
  - [特性](#特性)
  - [1. 工程目录](#1-工程目录)
  - [2. 准备模型与数据](#2-准备模型与数据)
  - [3. 例程](#3-例程)

## 简介

ChatDoc例程是一个基于BM1684X构建的用自然语言与文档进行交互的服务，可快速提取文档内容并用于问答，此项目基于[LangChain](https://github.com/langchain-ai/langchain)。本项目需要和demo/application下的[LLM_api_server](../LLM_api_server/README.md)服务配合使用，先启动LLM_api_server服务，再启动本项目；加入[bce-reranker-base_v1](https://huggingface.co/maidalun1020/bce-reranker-base_v1)优化文本对话能力，总体流程如下图所示：![Flow](<./pics/embedding.png>)

## 特性

* 支持BM1684X(PCIE、SOC)和BM1688(SOC)
* 支持多种文档格式(PDF, DOCX, TXT)
* 提供用户界面
* 支持bce-reranker

## 1. 工程目录

```shell
├── models
│   ├── BM1684X                                       # BM1684X专用模型
│   │   ├── bce_embedding                             # BM1684X上运行的bce_embedding
│   │   │   ├── bce-embedding-base_v1.bmodel
│   │   │   └── token_config
│   │   │       ├── special_tokens_map.json
│   │   │       ├── tokenizer_config.json
│   │   │       └── tokenizer.json
│   │   ├── bce_reranker                              # BM1684X上运行的bce_reranker
│   │   │   ├── bce-reranker-base_v1.bmodel
│   │   │   └── token_config
│   │   │       ├── special_tokens_map.json
│   │   │       ├── tokenizer_config.json
│   │   │       └── tokenizer.json
│   │   └── qwen                                      # BM1684X上运行的qwen1.5-7b, int4量化, 上下文长度2k, 单芯模型
│   │       ├── qwen1.5-7b_int4_seq2048_1dev.bmodel
│   │       └── token_config
│   │           ├── tokenizer_config.json
│   │           ├── tokenizer.json
│   │           └── vocab.json
│   └── BM1688                                        # BM1688专用模型
│       ├── bce_embedding                             # BM1688上运行的bce_embedding
│       │   ├── bce-embedding-base_v1.bmodel
│       │   └── token_config
│       │       ├── special_tokens_map.json
│       │       ├── tokenizer_config.json
│       │       └── tokenizer.json
│       ├── bce_reranker                              # BM1688上运行的bce_reranker
│       │   ├── bce-reranker-base_v1.bmodel
│       │   └── token_config
│       │       ├── special_tokens_map.json
│       │       ├── tokenizer_config.json
│       │       └── tokenizer.json
│       └── qwen                                      # BM1688上运行的qwen2.5-1.5b, int4量化, 上下文长度2k, 双核模型
│           ├── qwen2.5-1.5b_int4_seq2048_1688_2core.bmodel
│           └── token_config
│               ├── tokenizer_config.json
│               ├── tokenizer.json
│               └── vocab.json
├── nltk_data
├── pics                            # 文档用图
│   ├── embedding.png
│   ├── img1.png
│   └── img2.png
├── python                          # python例程
│   ├── chat                        # 聊天机器人
│   │   ├── chatbot.py
│   │   ├── __init__.py
│   │   └── utils.py
│   ├── config.ini                  # 本项目的配置方法
│   ├── config.yaml                 # LLM_server_api服务的配置，LLM模型部分
│   ├── data                        # 存储文档和保存知识库
│   │   ├── db_tpu
│   │   └── uploaded
│   ├── doc_processor               # 文档处理模块
│   ├── embedding                   # embedding推理
│   │   ├── embedding.py
│   │   ├── __init__.py
│   │   ├── npuengine.py
│   │   └── sentence_model.py
│   ├── README.md                   # python例程的README
│   ├── requirements.txt            # 需要安装的第三方库
│   ├── reranker                    # reranker模块
│   │   ├── __init__.py
│   │   └── reranker_tpu.py
│   └── web_demo_st.py              # python例程启动文件
├── README.md                       # 项目总文档
└── scripts
    └── download.sh                 # 下载脚本
```

## 2. 准备模型与数据

```shell
# 安装unzip，若已安装请跳过，非ubuntu系统视情况使用yum或其他方式安装
sudo apt install unzip
chmod -R +x scripts/

# 下载BM1684X的模型文件和nltk
./scripts/download.sh 
# 下载BM1688的模型文件和nltk
./scripts/download.sh bm1688
```

## 3. 例程

- [Python例程](./python/README.md)


# 文件: application/ChatDoc/python/README.md

---

# Python例程

## 目录 
- [Python例程](#python例程)
  - [目录](#目录)
  - [1. 环境准备](#1-环境准备)
    - [1.1 x86/arm PCIe平台](#11-x86arm-pcie平台)
    - [1.2 SoC平台](#12-soc平台)
  - [2. 启动服务](#2-启动服务)
    - [2.1 参数说明](#21-参数说明)
    - [2.2 使用方式](#22-使用方式)
    - [2.3 操作说明](#23-操作说明)
    - [界面简介](#界面简介)
    - [上传文档](#上传文档)
    - [持久化知识库](#持久化知识库)
    - [导入知识库](#导入知识库)
    - [删除知识库](#删除知识库)
    - [重命名知识库](#重命名知识库)
    - [清除聊天记录](#清除聊天记录)
    - [移除选中文档](#移除选中文档)

python目录下提供了Python例程，具体情况如下：

| 序号  |             Python例程                    |             说明                |
| ---- | ----------------------------------------  | ------------------------------- |
| 1    |          web_demo_st.py                   |         用户交互界面             |

## 1. 环境准备

本例程需要配合sophon-demo/application下的[LLM_api_server](../../LLM_api_server/README.md)项目使用，请确保两个项目置于同一父目录下，并参考[LLM_api_server服务启动](../../LLM_api_server/python/README.md)配置好LLM_api_server所需的环境。以qwen1.5-7b, 2k上下文的模型为例，使用如下指令启动LLM_api_server服务：

```shell
# 进入LLM_api_server可执行脚本例程
cd LLM_api_server/python
# 启动LLM_api_server的OpenAI库调用方式，请确认config.yaml中的模型路径是否正确
python3 api_server.py --config ../../ChatDoc/python/config.yaml
```

### 1.1 x86/arm PCIe平台

如果您在x86/arm平台安装了PCIe加速卡（如SC系列加速卡），并使用它测试本例程，您需要安装libsophon，具体请参考[x86-pcie平台的开发和运行环境搭建](../../../docs/Environment_Install_Guide.md#3-x86-pcie平台的开发和运行环境搭建)或[arm-pcie平台的开发和运行环境搭建](../../../docs/Environment_Install_Guide.md#5-arm-pcie平台的开发和运行环境搭建)。

此外您还需要安装其他第三方库：
```bash
pip3 install -r python/requirements.txt
```

您还需要安装sophon-sail，由于本例程需要的sophon-sail版本较新，相关功能还未发布，这里暂时提供一个可用的sophon-sail源码，x86/arm PCIe环境可以通过下面的命令下载：
```bash
pip3 install dfss --upgrade #安装dfss依赖
python3 -m dfss --url=open@sophgo.com:sophon-demo/Qwen/sophon-sail.tar.gz
tar xvf sophon-sail.tar.gz
```
参考[sophon-sail编译安装指南](https://doc.sophgo.com/sdk-docs/v24.04.01/docs_latest_release/docs/sophon-sail/docs/zh/html/1_build.html#)编译不包含bmcv,sophon-ffmpeg,sophon-opencv的可被Python3接口调用的Wheel文件。

### 1.2 SoC平台

如果您使用SoC平台（如SE、SM系列边缘设备），并使用它测试本例程，刷机后在`/opt/sophon/`下已经预装了相应的libsophon运行库包。

此外您还需要安装其他第三方库：
```bash
pip3 install -r python/requirements.txt
```
由于本例程需要的sophon-sail版本较新，这里提供一个可用的sophon-sail whl包，SoC环境可以通过下面的命令下载：
```bash
pip3 install dfss --upgrade
python3 -m dfss --url=open@sophgo.com:sophon-demo/Qwen/sophon_arm-3.8.0-py3-none-any.whl  #arm soc, py38
```
如果whl包无法使用，也可以参考上一小节，下载源码自己编译。

对于soc系列设备（如SE7/SM7），需要参考如下命令修改设备内存，才能满足所提供的样例模型需要的显存:

```bash
cd /data/
mkdir memedit && cd memedit
wget -nd https://github.com/sophgo/sophon-tools/releases/download/v24.09.21/memory_edit_v2.10.tar.xz
tar xvf memory_edit_v2.10.tar.xz
cd memory_edit
./memory_edit.sh -p #这个命令会打印当前的内存布局信息
./memory_edit.sh -c -npu 7615 -vpu 800 -vpp 800 #npu也可以访问vpu和vpp的内存
sudo cp /data/memedit/DeviceMemoryModificationKit/memory_edit/emmcboot.itb /boot/emmcboot.itb && sync
sudo reboot
```

## 2. 启动服务

python例程不需要编译，可以直接运行，PCIe平台和SoC平台的测试参数和运行方式是相同的。

### 2.1 参数说明

web_demo_st.py使用config.ini配置文件进行参数配置。

config.ini内容如下
```yaml
bce_embedding/bce_reranker: # embedding 和 reranker模型
    bmodel_path: ../models/BM1684X/bce_embedding/bce-embedding-base_v1.bmodel # 模型路径
    token_path: ../models/BM1684X/bce_embedding/token_config  # tokenizer 路径

init_config:
    base_url: http://127.0.0.1:18080/v1/ # LLM_server服务ip和端口
    supported_model: qwen,chatglm3       # 支持的模型

environment_config:
    LLM_MODEL: qwen                      # 默认的LLM模型
    EMBEDDING_MODEL: bce_embedding        # 选择使用的embedding模型
    RERANKER_MODEL: bce_reranker          # 选择使用的reranker模型
    DEVICE_ID: 0                          # 设备号
    server_address: "0.0.0.0"             # streamlit服务ip
    server_port: ""                       # streamlit端口
```

### 2.2 使用方式

```bash
cd python
# 第一次运行时会下载nltk依赖的数据
streamlit run web_demo_st.py
```

### 2.3 操作说明

![UI](<../pics/img1.png>)

### 界面简介
ChatDoc由控制区和聊天对话区组成。控制区用于管理文档和知识库，聊天对话区用于输入和接受消息。

上图中的10号区域是 ChatDoc 当前选中的文档。若10号区域为空，即 ChatDoc 没有选中任何文档，仍在聊天对话区与 ChatDoc 对话，则此时的 ChatDoc 是一个单纯依托 LLM 的 ChatBot。

### 上传文档
点击`1`选择要上传的文档，然后点击按钮`4`构建知识库。随后将embedding文档，完成后将被选中，并显示在10号区域，接着就可开始对话。我们可重复上传文档，embedding成功的文档均会进入10号区域。

### 持久化知识库
10号区域选中的文档在用户刷新或者关闭页面时，将会清空。若用户需要保存这些已经embedding的文档，可以选择持久化知识库，下次进入时无需embedding计算即可加载知识库。具体做法是，在10号区域不为空的情况下，点击按钮`5`即可持久化知识库，知识库的名称是所有文档名称以逗号连接而成。

### 导入知识库

用户可以从选择框`2`查看目前已持久化的知识库。选中我们需要加载的知识库后，点击按钮`3`导入知识库。完成后即可开始对话。注意cpu版的知识库和tpu版的知识库不能混用，若启动tpu版程序，则不能加载已持久化的cpu版知识库；若启动cpu版程序，则不能加载已持久化的tpu版知识库。

### 删除知识库

当用户需要删除本地已经持久化的知识库时，可从选择框`2`选择要删除的知识库，然后点击按钮`6`删除知识库。

### 重命名知识库

![Rename](<../pics/img2.png>)

由于知识库的命名是由其文档的名称组合而来，难免造成知识库名称过长的问题。ChatDoc提供了一个修改知识库名称的功能，选择框`2`选择我们要修改的知识库，然后点击按钮`9`重命名知识库，随后ChatDoc将弹出一个输入框和一个确认按钮，如上图。在输出框输入修改后的名称，然后点击`确认重命名`按钮。

### 清除聊天记录

点击按钮`7`即可清除聊天对话区聊天记录。其他不受影响。

### 移除选中文档

点击按钮`8`将清空10号区域，同时清除聊天记录。

# 文件: application/Grounded-sam/README.md

---

# Grounded_SAM_WEB_UI 例程

## 目录

- [Grounded_SAM\_WEB\_UI 例程](#Grounded_SAM_web_ui-例程)
  - [目录](#目录)
  - [简介](#简介)
  - [1. 工程目录](#1-工程目录)
  - [2. 准备模型与数据](#2-准备模型与数据)
  - [3. 环境准备](#3-环境准备)
  - [4. 启动前后端程序](#4-启动前后端程序)


## 简介
Grounded_SAM_WEB_UI 例程是一个基于 Grounded_SAM 模型的图像检测和分割系统，支持输入为图像与文本，输出为检测和分割后的图片和文本输入相关信息。可以实现只输入图片，就可以无交互式完全自动化标注出图片的检测框和分割掩码，能够应对从自动驾驶、机器人视觉到医疗影像分析等多样化的应用场景。

此例程由三部分组成：

1. 业务中台：`../python/gdsam_server.py`， 使用了数据队列和线程，具有数据队列管理等功能，为网页后端提供接口服务；
2. 前端应用：`gd_server-front.py`， 为使用streamlit搭建的网页前端；运行在client客户端；
3. 后端应用：`gd_server-back.py`， 为后端接口服务，为前端提供接口请求调用；运行在server服务器端，如SE7 SE9微服务器；

## 1. 工程目录

```bash
Grounded-sam
├── assets
│   └── dog.jpg
├── models
│   ├── bert-base-uncased     # tokenizer 分词器文件夹	
│   └── BM1684X
│       ├── decode_bmodel
│       │   └── SAM-ViT-B_decoder_single_mask_fp16_1b.bmodel      
│       ├── embedding_bmodel
│       │   └── SAM-ViT-B_embedding_fp16_1b.bmodel
│       └── groundingdino
│           └── groundingdino_bm1684x_fp16.bmodel     # 用于BM1684X的FP16 BModel，batch_size=1
├── python
│   ├── custom_model.py   # 定制模块，用于初始化和创建groundingdino和sam实例
│   ├── gdsam_server.py   # 业务中台
│   ├── gdsam_util.py     # #辅助函数文件
│   ├── groundingdino     # groundingdino实现模块
│   │   ├── groundingdino_pil.py
│   │   ├── PostProcess.py
│   │   └── utils.py
│   └── sam               # sam实现模块
│       ├── predictor.py
│       ├── sam_amg.py
│       ├── sam_encoder.py
│       ├── sam_model.py
│       ├── sam_opencv.py
│       └── transforms.py
├── requirements.txt          #例程的依赖模块
├── scripts
│   └── download.sh           #下载脚本
└── web_server
    ├── gd_server-back.py     # 后端接口服务
    └── gd_server-front.py    # 前端网页
```

## 2. 准备模型与数据
​本例程在`scripts`目录下提供了相关模型和数据的下载脚本`download.sh`，
```bash
# 安装unzip，若已安装请跳过，非ubuntu系统视情况使用yum或其他方式安装
sudo apt install unzip
chmod -R +x scripts/
./scripts/download.sh
```

## 3. 环境准备

如果您在x86/arm平台安装了PCIe加速卡（如SC系列加速卡），并使用它测试本例程，您需要安装libsophon、sophon-opencv、sophon-ffmpeg和sophon-sail，具体请参考[x86-pcie平台的开发和运行环境搭建](../../docs/Environment_Install_Guide.md#3-x86-pcie平台的开发和运行环境搭建)或[arm-pcie平台的开发和运行环境搭建](../../docs/Environment_Install_Guide.md#5-arm-pcie平台的开发和运行环境搭建)。

此外您可能还需要安装其他第三方库：

```bash
pip3 install -r requirements.txt
```

## 4. 启动前后端程序

1. 您需要启动前后端程序，前端程序运行在您的客户端，后端程序运行在您的服务器端，如SC7服务器。

```bash
cd web_server
python3 gd_server-back.py --host 0.0.0.0 --port 8080 # 启动后端接口服务，在您的服务器端启动，如SE7 SE9微服务器，其中--host 0.0.0.0 --port 8080 用于指定后端服务器的地址和端口
streamlit run gd_server-front.py  # 启动前端网页，在您的客户端启动，会在终端显示前端网页的服务器地址和端口
```

推荐Prompt的使用语言为英文；

2. 您可以选择本地图片上传，并输入文本，点击“UPLOAD”按钮，您将看到预测结果；

  2.1 若您不选择本地图片，默认为本例程../assets/dog.jpg 的图片，直接在页面的Prompt处输入如下Prompt： 

    > dog and tree

  2.2. 点击“UPLOAD”按钮，您将看到预测结果

  2.3. 若您多次提交图片，您可以在“历史记录”中查看您的提交记录

# 文件: application/LLM_api_server/README.md

---

# LLM_api_server

## 目录
- [LLM\_api\_server](#llm_api_server)
  - [目录](#目录)
  - [简介](#简介)
  - [特性](#特性)
  - [1. 工程目录](#1-工程目录)
  - [2. 准备模型与数据](#2-准备模型与数据)
  - [3. 例程](#3-例程)
  - [4. 性能测试](#4-性能测试)

## 简介

LLM_api_server 例程是一个基于BM1684X构建的一个类Openai_api的LLM服务，目前支持ChatGLM3、Qwen、Qwen1.5、Qwen2。

## 特性

* 支持BM1684X(PCIe、SoC)、BM1688(SoC)
* 支持openai库进行调用
* 支持web接口调用

## 1. 工程目录

```bash
LLM_api_server
├── models
│   ├── BM1684X
│   │   ├── chatglm3-6b_int4.bmodel                # BM1684X chatglm3-6b模型
│   │   ├── qwen2-7b_int4_seq512_1dev.bmodel       # BM1684X qwen2-7b模型	
├── python
│   ├── utils                         # 工具库
│   ├── api_server.py                 # 服务启动程序
│   └── config.yaml                   # 服务配置文件
│   └── request.py                    # 请求示例程序
│   └── requirements.txt              # python依赖
└── scripts
    ├── download_model.sh       # 模型下载脚本
    ├── download_tokenizer.sh   # tokenizer下载脚本
```

## 2. 准备模型与数据

```bash
# 安装unzip，若已安装请跳过，非ubuntu系统视情况使用yum或其他方式安装
sudo apt install unzip
chmod -R +x scripts/

# 下载tokenizer
./scripts/download_tokenizer.sh 

# 下载模型文件
./scripts/download_model.sh 
```


## 3. 例程

- [Python例程](./python/README.md)

## 4. 性能测试

模型性能可参考sophon-demo/sample对应的模型仓库。



# 文件: application/LLM_api_server/python/README.md

---

# Python例程

## 目录 
- [1. 环境准备](#1-环境准备)
  - [1.1 x86/arm PCIe平台](#11-x86arm-pcie平台)
  - [1.2 SoC平台](#12-soc平台)
- [2. 启动服务](#2-启动服务)
  - [2.1 参数说明](#21-参数说明)
  - [2.2 使用方式](#32-使用方式)
- [3. 服务调用](#3-服务调用)

python目录下提供了Python例程，具体情况如下：

| 序号  |             Python例程                    |             说明                |
| ---- | ----------------------------------------  | ------------------------------- |
| 1    |    api_server.py                          |         LLM API 服务            |

## 1. 环境准备
### 1.1 x86/arm PCIe平台

如果您在x86/arm平台安装了PCIe加速卡（如SC系列加速卡），并使用它测试本例程，您需要安装libsophon，具体请参考[x86-pcie平台的开发和运行环境搭建](../../../docs/Environment_Install_Guide.md#3-x86-pcie平台的开发和运行环境搭建)或[arm-pcie平台的开发和运行环境搭建](../../../docs/Environment_Install_Guide.md#5-arm-pcie平台的开发和运行环境搭建)。

此外您还需要安装其他第三方库：
```bash
pip3 install -r python/requirements.txt
```

您还需要安装sophon-sail，由于本例程需要的sophon-sail版本较新，相关功能还未发布，这里暂时提供一个可用的sophon-sail源码，x86/arm PCIe环境可以通过下面的命令下载：
```bash
pip3 install dfss --upgrade #安装dfss依赖
python3 -m dfss --url=open@sophgo.com:sophon-demo/Qwen/sophon-sail.tar.gz
tar xvf sophon-sail.tar.gz
```
参考[sophon-sail编译安装指南](https://doc.sophgo.com/sdk-docs/v24.04.01/docs_latest_release/docs/sophon-sail/docs/zh/html/1_build.html#)编译不包含bmcv,sophon-ffmpeg,sophon-opencv的可被Python3接口调用的Wheel文件。

### 1.2 SoC平台

如果您使用SoC平台（如SE、SM系列边缘设备），并使用它测试本例程，刷机后在`/opt/sophon/`下已经预装了相应的libsophon运行库包。

此外您还需要安装其他第三方库：
```bash
pip3 install -r python/requirements.txt
```
由于本例程需要的sophon-sail版本较新，这里提供一个可用的sophon-sail whl包，SoC环境可以通过下面的命令下载：
```bash
pip3 install dfss --upgrade
python3 -m dfss --url=open@sophgo.com:sophon-demo/Qwen/sophon_arm-3.8.0-py3-none-any.whl  #arm soc, py38
```
如果whl包无法使用，也可以参考上一小节，下载源码自己编译。

## 2. 启动服务
python例程不需要编译，可以直接运行，PCIe平台和SoC平台的测试参数和运行方式是相同的。
### 2.1 参数说明
api_server.py使用config.yaml配置文件进行参数配置。

config.yaml内容如下
```yaml
models:  # 模型列表
  - name: qwen   # 模型名称，可选qwen/chatglm3
    bmodel_path: ../models/BM1684X/qwen2-7b_int4_seq512_1dev.bmodel # 模型路径，根据实际情况修改
    token_path: ./utils/qwen/token_config  # tokenizer 路径
    dev_id: 0  # tpu id


port: 18080 # 服务端口
```

### 2.2 使用方式

```bash
cd python
python3 api_server.py --config ./config.yaml
```
## 3. 服务调用
1. 可以使用OpenAI库进行调用
```bash
python3 request.py
```
2. 使用http接口调用

接口url： ip:port/v1/chat/completions
例如： 172.26.13.98:18080/v1/chat/completions

接口参数：
```json
{
    "model": "qwen",
    "messages": [
        {"role": "user", "content": "你好"}
    ],
    "stream": true
}
```
stream为true时为流式推理。

可以使用postman测试接口
![postman](../pics/postman.png)

# 文件: application/VLPR/README.md

---

[简体中文](./README.md)

# VLPR(Vehicle License Plate Recognition)

## 目录

- [VLPR(Vehicle License Plate Recognition)](#vlprvehicle-license-plate-recognition)
  - [目录](#目录)
  - [1. 简介](#1-简介)
  - [2. 特性](#2-特性)
  - [3. 准备模型与数据](#3-准备模型与数据)
  - [4. 模型编译](#4-模型编译)
  - [5. 例程测试](#5-例程测试)
  - [6. 性能测试](#6-性能测试)
    - [6.1 bmrt\_test](#61-bmrt_test)
    - [6.2 程序运行性能](#62-程序运行性能)
  - [7. FAQ](#7-faq)
  
## 1. 简介
本例程对[LPRNet_Pytorch](https://github.com/sirius-ai/LPRNet_Pytorch)的模型和算法进行移植，，使之能够完成全流程车牌检测识别业务，并在SOPHON BM1684/BM1684X/BM1688上进行推理测试。在您使用本例程之前，推荐先跑通[LPRNet](../../sample/LPRNet/README.md)和[YoLov5](../../sample/YOLOv5/README.md)

**论文:** [LPRNet: License Plate Recognition via Deep Neural Networks](https://arxiv.org/abs/1806.10447v1)
**LPRNET 车牌检测源代码**(https://github.com/sirius-ai/LPRNet_Pytorch)

## 2. 特性
* 支持BM1688/CV186X(SoC)、BM1684X(x86 PCIe、SoC)、BM1684(x86 PCIe、SoC、arm PCIe)
* LPRNet支持FP32、FP16(BM1684X/BM1688/CV186X)、INT8模型编译和推理
* YOLOv5支持FP32、INT8模型编译和推理
* 支持C++和Python
* 支持单batch和多batch模型推理
* 支持图片和视频测试
* pipeline式demo，支持解码、预处理和后处理多线程和推理线程并行运行，更充分利用硬件加速

## 3. 准备模型与数据
​本例程在`scripts`目录下提供了相关模型和数据的下载脚本`download.sh`，您也可以自己准备模型和数据集，并参考[4. 模型编译](#4-模型编译)进行模型转换。

```bash
chmod -R +x scripts/
./scripts/download.sh

```
执行后，模型保存至`models/`，数据集下载并解压至`datasets/`
```
下载的模型包括：
./models
├── lprnet
|   ├── BM1684
|   │   ├── lprnet_fp32_1b.bmodel                                     # 使用TPU-MLIR编译，用于BM1684的FP32 LPRNet BModel，batch_size=1，num_core=1
|   │   ├── lprnet_int8_1b.bmodel                                     # 使用TPU-MLIR编译，用于BM1684的INT8 LPRNet BModel，batch_size=1，num_core=1
|   │   └── lprnet_int8_4b.bmodel                                     # 使用TPU-MLIR编译，用于BM1684的INT8 LPRNet BModel，batch_size=4，num_core=1
|   ├── BM1684X
|   │   ├── lprnet_fp32_1b.bmodel                                     # 使用TPU-MLIR编译，用于BM1684X的FP32 LPRNet BModel，batch_size=1，num_core=1
|   │   ├── lprnet_fp16_1b.bmodel                                     # 使用TPU-MLIR编译，用于BM1684X的FP16 LPRNet BModel，batch_size=1，num_core=1
|   │   ├── lprnet_int8_1b.bmodel                                     # 使用TPU-MLIR编译，用于BM1684X的INT8 LPRNet BModel，batch_size=1，num_core=1
|   │   └── lprnet_int8_4b.bmodel                                     # 使用TPU-MLIR编译，用于BM1684X的INT8 LPRNet BModel，batch_size=4，num_core=1
|   ├── BM1688
|   │   ├── lprnet_fp32_1b.bmodel                                     # 使用TPU-MLIR编译，用于BM1688的FP32 LPRNet BModel，batch_size=1，num_core=1
|   │   ├── lprnet_fp16_1b.bmodel                                     # 使用TPU-MLIR编译，用于BM1688的FP16 LPRNet BModel，batch_size=1，num_core=1
|   │   ├── lprnet_int8_1b.bmodel                                     # 使用TPU-MLIR编译，用于BM1688的INT8 LPRNet BModel，batch_size=1，num_core=1
|   │   ├── lprnet_int8_4b.bmodel                                     # 使用TPU-MLIR编译，用于BM1688的INT8 LPRNet BModel，batch_size=4，num_core=1
|   │   ├── lprnet_fp32_1b_2core.bmodel                               # 使用TPU-MLIR编译，用于BM1688的FP32 LPRNet BModel，batch_size=1，num_core=2
|   │   ├── lprnet_fp16_1b_2core.bmodel                               # 使用TPU-MLIR编译，用于BM1688的FP16 LPRNet BModel，batch_size=1，num_core=2
|   │   ├── lprnet_int8_1b_2core.bmodel                               # 使用TPU-MLIR编译，用于BM1688的INT8 LPRNet BModel，batch_size=1，num_core=2
|   │   └── lprnet_int8_4b_2core.bmodel                               # 使用TPU-MLIR编译，用于BM1688的INT8 LPRNet BModel，batch_size=4，num_core=2
│   ├── CV186X
│   │   ├── lprnet_fp16_1b.bmodel                                     # 使用TPU-MLIR编译，用于CV186X的FP16 LPRNet BModel，batch_size=1，num_core=1
│   │   ├── lprnet_fp32_1b.bmodel                                     # 使用TPU-MLIR编译，用于CV186X的FP32 LPRNet BModel，batch_size=1，num_core=1
│   │   ├── lprnet_int8_1b.bmodel                                     # 使用TPU-MLIR编译，用于CV186X的INT8 LPRNet BModel，batch_size=1，num_core=1
│   │   └── lprnet_int8_4b.bmodel                                     # 使用TPU-MLIR编译，用于CV186X的INT8 LPRNet BModel，batch_size=4，num_core=1
|   │── torch
|   │   ├── Final_LPRNet_model.pth                                    # LPRNet 原始模型
|   │   └── LPRNet_model_trace.pt                                     # trace后的JIT LPRNet模型
|   └── onnx
|       ├── lprnet_1b.onnx                                            # 导出的onnx LPRNet模型，batch_size=1
|       └── lprnet_4b.onnx                                            # 导出的onnx LPRNet模型，batch_size=4   
└── yolov5s-licensePLate
    ├── BM1684
    │   ├── yolov5s_v6.1_license_3output_fp32_1b.bmodel               # 用于BM1684的FP32 YOLOv5 BModel，batch_size=1，num_core=1
    │   ├── yolov5s_v6.1_license_3output_int8_1b.bmodel               # 用于BM1684的INT8 YOLOv5 BModel，batch_size=1，num_core=1
    │   └── yolov5s_v6.1_license_3output_int8_4b.bmodel               # 用于BM1684的INT8 YOLOv5 BModel，batch_size=4，num_core=1             
    ├── BM1684X
    │   ├── yolov5s_v6.1_license_3output_fp32_1b.bmodel               # 用于BM1684X的FP32 YOLOv5 BModel，batch_size=1，num_core=1
    │   ├── yolov5s_v6.1_license_3output_int8_1b.bmodel               # 用于BM1684X的INT8 YOLOv5 BModel，batch_size=1，num_core=1
    │   └── yolov5s_v6.1_license_3output_int8_4b.bmodel               # 用于BM1684X的INT8 YOLOv5 BModel，batch_size=4，num_core=1     
    ├── BM1688
    |   ├── yolov5s_v6.1_license_3output_fp32_1b_2core.bmodel         # 用于BM1688的FP32 YOLOv5 BModel，batch_size=1，num_core=2
    |   ├── yolov5s_v6.1_license_3output_fp32_1b.bmodel               # 用于BM1688的FP32 YOLOv5 BModel，batch_size=1，num_core=1
    |   ├── yolov5s_v6.1_license_3output_fp32_4b_2core.bmodel         # 用于BM1688的FP32 YOLOv5 BModel，batch_size=4，num_core=2
    |   ├── yolov5s_v6.1_license_3output_fp32_4b.bmodel               # 用于BM1688的FP32 YOLOv5 BModel，batch_size=4，num_core=1
    |   ├── yolov5s_v6.1_license_3output_int8_1b_2core.bmodel         # 用于BM1688的INT8 YOLOv5 BModel，batch_size=1，num_core=2
    |   ├── yolov5s_v6.1_license_3output_int8_1b.bmodel               # 用于BM1688的INT8 YOLOv5 BModel，batch_size=1，num_core=1
    |   ├── yolov5s_v6.1_license_3output_int8_4b_2core.bmodel         # 用于BM1688的INT8 YOLOv5 BModel，batch_size=4，num_core=2
    |   └── yolov5s_v6.1_license_3output_int8_4b.bmodel               # 用于BM1688的INT8 YOLOv5 BModel，batch_size=4，num_core=1
    └── CV186X
        ├── yolov5s_v6.1_license_3output_fp16_1b.bmodel               # 用于CV186X的FP16 YOLOv5 BModel, batch_size=1, num_core=1
        ├── yolov5s_v6.1_license_3output_fp16_4b.bmodel               # 用于CV186X的FP16 YOLOv5 BModel, batch_size=4, num_core=1
        ├── yolov5s_v6.1_license_3output_fp32_1b.bmodel               # 用于CV186X的FP32 YOLOv5 BModel, batch_size=1, num_core=1
        ├── yolov5s_v6.1_license_3output_fp32_4b.bmodel               # 用于CV186X的FP32 YOLOv5 BModel, batch_size=4, num_core=1
        ├── yolov5s_v6.1_license_3output_int8_1b.bmodel               # 用于CV186X的INT8 YOLOv5 BModel, batch_size=1, num_core=1
        └── yolov5s_v6.1_license_3output_int8_4b.bmodel               # 用于CV186X的INT8 YOLOv5 BModel, batch_size=4, num_core=1

下载的数据包括：
./datasets
├── 1080_1920_30s_512kb.mp4                 # 默认测试视频1
└── 1080_1920_5s.mp4                        # 测试视频2

```

## 4. 模型编译
若需要使用自己的模型，需要保证模型的输入输出和本例程的前后处理相对应。
车牌识别模型编译过程参考[sophon-demo lprnet模型编译](../../sample/LPRNet/README.md#4-模型编译)，注意不能直接用该例程里面的模型。
车牌检测模型编译过程参考[sophon-demo yolov5模型编译](../../sample/YOLOv5/README.md#4-模型编译)，注意不能直接用该例程里面的模型。

> **说明**： 
> 本例程中提供的yolov5s-licenseplate模型为基于绿牌数据集训练的模型，供示例使用参考，无原始模型及精度数据。

## 5. 例程测试
- [C++例程](./cpp/README.md)
- [python例程](./python/README.md)

## 6. 性能测试
### 6.1 bmrt_test
LPRNet性能可参考[LPRNet bmrt_test](../../sample/LPRNet/README.md#71-bmrt_test)里面的性能数据。

使用bmrt_test测试模型的理论性能：
```bash
# 请根据实际情况修改要测试的bmodel路径和devid参数
bmrt_test --bmodel models/BM1684/yolov5s_v6.1_license_3output_fp32_1b.bmodel 
```
测试结果中的`calculate time`就是模型推理的时间，多batch size模型应当除以相应的batch size才是每张图片的理论推理时间。
测试各个模型每张图片的理论推理时间，结果如下：
| 测试模型                                                 | calculate time(ms) |
| -------------------------------------------------------- | ------------------ |
| BM1684/yolov5s_v6.1_license_3output_fp32_1b.bmodel       | 20.6               |
| BM1684/yolov5s_v6.1_license_3output_int8_1b.bmodel       | 12.4               |
| BM1684/yolov5s_v6.1_license_3output_int8_4b.bmodel       | 5.4                |
| BM1684X/yolov5s_v6.1_license_3output_fp32_1b.bmodel      | 18.6               |
| BM1684X/yolov5s_v6.1_license_3output_int8_1b.bmodel      | 2.4                |
| BM1684X/yolov5s_v6.1_license_3output_int8_4b.bmodel      | 1.8                |
| BM1688/yolov5s_v6.1_license_3output_fp32_1b_2core.bmodel | 59.5               |
| BM1688/yolov5s_v6.1_license_3output_fp32_1b.bmodel       | 93.7               |
| BM1688/yolov5s_v6.1_license_3output_fp32_4b_2core.bmodel | 48.0               |
| BM1688/yolov5s_v6.1_license_3output_fp32_4b.bmodel       | 92.9               |
| BM1688/yolov5s_v6.1_license_3output_int8_1b_2core.bmodel | 4.9                |
| BM1688/yolov5s_v6.1_license_3output_int8_1b.bmodel       | 5.8                |
| BM1688/yolov5s_v6.1_license_3output_int8_4b_2core.bmodel | 3.2                |
| BM1688/yolov5s_v6.1_license_3output_int8_4b.bmodel       | 5.6                |
| CV186X/yolov5s_v6.1_license_3output_fp32_1b.bmodel       | 101.8              |
| CV186X/yolov5s_v6.1_license_3output_fp16_1b.bmodel       | 34.9               |
| CV186X/yolov5s_v6.1_license_3output_int8_1b.bmodel       | 12.5               |
| CV186X/yolov5s_v6.1_license_3output_int8_4b.bmodel       | 7.0                |

> **测试说明**：  
> 1. 性能测试结果具有一定的波动性；
> 2. `calculate time`已折算为平均每张图片的推理时间；
> 3. SoC和PCIe的测试结果基本一致。

### 6.2 程序运行性能
参考[例程测试](#5-例程测试)运行程序，并查看统计的total fps。

在不同的测试平台上，使用不同的例程和对应的配置文件，性能测试结果如下：
| 测试平台 | 测试程序      | 测试模型                                                                       | 配置文件           | 路数 | FPS | tpu利用率(%) | cpu利用率(%) | 系统内存占用(MB) | 设备内存占用(MB) |
| -------- | ------------- | ------------------------------------------------------------------------------ | ------------------ | ---- | --- | ------------ | ------------ | ---------------- | ---------------- |
| SE9-8    | vlpr_bmcv.soc | lprnet_int8_4b.bmodel，yolov5s_v6.1_license_3output_int8_4b.bmodel             | config_se9-8.json  | 8    | 97  | 90-100       | 170-190      | 40-50            | 650-800         |
| SE9-16   | vlpr_bmcv.soc | lprnet_int8_4b_2core.bmodel，yolov5s_v6.1_license_3output_int8_4b_2core.bmodel | config_se9-16.json | 16   | 185 | 90-100       | 400-450      | 50-60            | 1200-1400        |
| SE9-8    | vlpr.py       | lprnet_int8_4b.bmodel，yolov5s_v6.1_license_3output_int8_4b.bmodel             | default            | 8    | 206 | 94-100       | 240-250      | 140-160          | 1720-1740        |
| SE9-16   | vlpr.py       | lprnet_int8_4b_2core.bmodel，yolov5s_v6.1_license_3output_int8_4b_2core.bmodel | default            | 16   | 380 | 95-99        | 400-480      | 272-320          | 3590-3595        |

> **测试说明**：  
> 1. 性能测试结果具有一定的波动性；
> 2. SE9-16的主控处理器为8核CA53@1.6GHz，SE9-8为6核CA53@1.6GHz，PCIe上的性能由于处理器的不同可能存在较大差异； 
> 3. 性能数据在程序启动前和结束前不准确，上面来自程序运行稳定后的数据；
> 4. 各项指标的查看方式可以参考[测试指标查看方式](../../docs/Check_Statis.md)；
> 5. 部署环境下的NPU等设备内存大小会显著影响例程运行的路数。如果默认的输入路数运行中出现了申请内存失败等错误，可以考虑把输入路数减少，或者参考[FAQ](../../docs/FAQ.md#73-程序运行时出现bm_ion_alloc-failed等报错)；
> 6. 若出现申请设备内存失败，错误返回-24，需要把指定同一时间最多可开启的文件数调大一点：比如SoC上可以设置`ulimit -n 4096`。

## 7. FAQ
其他问题请参考[FAQ](../../docs/FAQ.md)查看一些常见的问题与解答。


# 文件: application/VLPR/cpp/README.md

---

[简体中文](./README.md)

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
    * [3.2 运行程序](#32-运行程序)
    * [3.3 程序原理流程图](#33-程序原理流程图)

cpp目录下提供了C++例程以供参考使用，具体情况如下：
| 序号  | C++例程      | 说明                                 |
| ---- | ------------ | -----------------------------------  |
| 1    | vlpr_bmcv  | 使用opencv解码、BMCV前处理、BMRT推理   |


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
cd cpp/vlpr_bmcv
mkdir build && cd build
cmake .. 
make
cd ..
```
编译完成后，会在cpp/vlpr_bmcv目录下生成vlpr_bmcv.pcie。

### 2.2 SoC平台
通常在x86主机上交叉编译程序，您需要在x86主机上使用SOPHON SDK搭建交叉编译环境，将程序所依赖的头文件和库文件打包至soc-sdk目录中，具体请参考[交叉编译环境搭建](../../../docs/Environment_Install_Guide.md#41-交叉编译环境搭建)。本例程主要依赖libsophon、sophon-opencv和sophon-ffmpeg运行库包。

交叉编译环境搭建好后，使用交叉编译工具链编译生成可执行文件：
```bash
cd cpp/vlpr_bmcv
mkdir build && cd build
#请根据实际情况修改-DSDK的路径，需使用绝对路径。
cmake -DTARGET_ARCH=soc -DSDK=/path_to_sdk/soc-sdk ..  
make
```
编译完成后，会在cpp/vlpr_bmcv目录下生成vlpr_bmcv.soc。

## 3. 推理测试
对于PCIe平台，可以直接在PCIe平台上推理测试；对于SoC平台，需将交叉编译生成的可执行文件及所需的模型、测试数据拷贝到SoC平台中测试。测试的参数及运行方式是一致的，下面主要以PCIe模式进行介绍。

### 3.1 参数说明
本例程通过读取configs/config.json来配置参数。json格式如下：

```json
{
  "dev_id": 0,
  "yolov5_bmodel_path": "../../models/yolov5s-licensePLate/BM1684X/yolov5s_v6.1_license_3output_int8_1b.bmodel",
  "lprnet_bmodel_path": "../../models/lprnet/BM1684X/lprnet_int8_1b.bmodel",
  "channels": [
    {
      "url": "../../datasets/1080_1920_30s_512kb.mp4",
      "is_video": true
    },
    {
      "url": "../../datasets/1080_1920_30s_512kb.mp4",
      "is_video": true
    }
  ],
  "yolov5_num_pre": 8,
  "yolov5_num_post": 8,
  "lprnet_num_pre": 8,
  "lprnet_num_post": 8,
  "yolov5_queue_size": 50,
  "lprnet_queue_size": 200,
  "yolov5_conf_thresh": 0.6,
  "yolov5_nms_thresh": 0.6,
  
  "frame_sample_interval": 3,
  "in_frame_num": 5, 
  "out_frame_num": 3, 
  "crop_thread_num": 2, 
  "push_data_thread_num": 2,
  "perf_out_time_interval": 30
}
```
|   参数名               | 类型    |                               说明                       |
|------------------------|---------|-------------------------------------------------------- |
| dev_id                 | int     |                       设备号                             |
| yolov5_bmodel_path     | string  |                 yolov5 bmodel路径                        |
| lprnet_bmodel_path     | string  |                 lprnet bmodel路径                        |
| channels               | list    |                  多路数据地址设置                         |
| url                    | string  |      图片目录路径、本地视频路径或视频流地址                 |
| is_video               | bool    |                    是否是视频格式                         |
| yolov5_num_pre         | int     |   yolov5预处理线程个数，建议不要超过8，需要根据运行结果设置  |
| yolov5_num_post        | int     |   yolov5后处理线程个数，建议不要超过8，需要根据运行结果设置  |
| lprnet_num_pre         | int     |   lprnet预处理线程个数，建议不要超过8，需要根据运行结果设置  |
| lprnet_num_post        | int     |   lprnet后处理线程个数，建议不要超过8，需要根据运行结果设置  |
| yolov5_queue_size      | int     | yolov5线程之间缓存队列的长度，过小会影响性能，需根据结果设置 |
| lprnet_queue_size      | int     | lprnet线程之间缓存队列的长度，过小会影响性能，需根据结果设置 |
| yolov5_conf_thresh     | float   |                  yolov5后处理中置信度阈值                 |
| yolov5_nms_thresh      | float   |                 yolov5后处理中nms置信度阈值               |
| frame_sample_interval  | int     | 跳帧的数量，被跳过的帧会丢弃，由于解码性能原因需要根据结果设置|
| in_frame_num           | int     |           在逻辑处理中，设置多少帧判断为“进”的行为          |
| out_frame_num          | int     |           在逻辑处理中，设置多少帧判断为“出”的行为          |
| crop_thread_num        | int     | 在得到yolov5的检测框后，裁剪车牌函数的线程数，需根据结果设置  |
| push_data_thread_num   | int     | 传递数据给逻辑代码的线程数，建议设置小一点，该线程一般不是瓶颈 |
| perf_out_time_interval | int     | 运行时性能数据输出的时间间隔，以秒为单位，需参考3.2运行程序中打开宏 |


### 3.2 运行程序
配置好json后，运行应用程序即可
```bash
# 对于BM1684X pcie运行
./vlpr_bmcv.pcie --config_path=configs/config_se7.json
# 对于BM1684X soc运行
./vlpr_bmcv.soc --config_path=configs/config_se7.json
# 对于BM1684 pcie运行
./vlpr_bmcv.pcie --config_path=configs/config_se5.json
# 对于BM1684 soc运行
./vlpr_bmcv.soc --config_path=configs/config_se5.json
# 对于SE9-16(BM1688) soc运行
./vlpr_bmcv.soc --config_path=configs/config_se9-16.json
# 对于SE9-8(BM1688) soc运行
./vlpr_bmcv.soc --config_path=configs/config_se9-8.json
```
测试过程会打印被检测和识别到的有效车牌信息，测试结束后，会打印fps等信息。若打开检测可视化的宏开关，即在文件[vlpr_bmcv.cpp](./vlpr_bmcv/vlpr_bmcv.cpp)中设置`#define DET_VIS 1`，会将检测的结果保存在`vis/`目录下。

若打开运行时性能数据输出的宏开关，即在文件[vlpr_bmcv.cpp](./vlpr_bmcv/vlpr_bmcv.cpp)中设置`#define RUNTIME_PERFORMANCE 1`，会实时打印配置参数`perf_out_time_interval`指定的时间间隔内的fps。

若要进行压测，在文件[yolov5.cpp](./vlpr_bmcv/yolov5_multi/yolov5.cpp)中设置`#define PRESSURE 1`，会不断循环视频文件。

> **测试说明**：  
> 1. 出现打印信息"xxx pipe full"，若大部分是前处理流程或推理流程则是正常的，若出现后处理流程，可查看最后一个输出该信息的流程，尝试增加该流程后面一个流程的线程数，即后面一个流程是瓶颈点
> 2. 若结果输出被打印信息"xxx pipe full"覆盖，可设置[datapipe.hpp](vlpr_bmcv/lprnet_multi/datapipe.hpp)中的宏```PIPE_INFO```为0，来关闭打印信息"xxx pipe full"

### 3.3 程序原理流程图
可参考[C++程序原理流程图](../pics/cpp_pipeline.png)，其中yolo部分可参考[C++程序YOLOv5_multi流程图](../../YOLOv5_multi/pics/diagram.png)。


# 文件: application/VLPR/python/README.md

---

[简体中文](./README.md)

# python例程

## 目录

- [python例程](#python例程)
  - [目录](#目录)
  - [1. 环境准备](#1-环境准备)
    - [1.1 x86/arm PCIe平台](#11-x86arm-pcie平台)
    - [1.2 SoC平台](#12-soc平台)
  - [3. 推理测试](#3-推理测试)
    - [3.1 参数说明](#31-参数说明)
    - [3.2 运行程序](#32-运行程序)
    - [3.2 程序原理流程图](#32-程序原理流程图)

python目录下提供了python例程以供参考使用，具体情况如下：
| 序号 | python例程 | 说明                                 |
| ---- | ---------- | ------------------------------------ |
| 1    | vlpr.py    | 使用SAIL解码、SAIL前处理、BMRT推理 |
| 2    | chars.py   | lprnet后处理使用的汉字字典           |


## 1. 环境准备
### 1.1 x86/arm PCIe平台
如果您在x86/arm平台安装了PCIe加速卡（如SC系列加速卡），可以直接使用它作为开发环境和运行环境。您需要安装libsophon、sophon-opencv、sophon-ffmpeg、sophon-sail，具体步骤可参考[x86-pcie平台的开发和运行环境搭建](../../../docs/Environment_Install_Guide.md#3-x86-pcie平台的开发和运行环境搭建)或[arm-pcie平台的开发和运行环境搭建](../../../docs/Environment_Install_Guide.md#5-arm-pcie平台的开发和运行环境搭建)。

注意：由于本例程中所用sophon-sail接口较新，请使用如下命令下载最新sophon-sail，并参考[编译安装sophon-sail](../../../docs/Environment_Install_Guide.md###5.3编译安装sophon-sail)进行安装：

```
pip3 install dfss -i https://pypi.tuna.tsinghua.edu.cn/simple --upgrade
python3 -m dfss --url=open@sophgo.com:/sophon-demo/VLPR/sophon-sail.zip
unzip sophon-sail.zip 
```

### 1.2 SoC平台
如果您使用SoC平台（如SE、SM系列边缘设备），刷机后在`/opt/sophon/`下已经预装了相应的libsophon、sophon-opencv和sophon-ffmpeg运行库包，可直接使用它作为运行环境。
您还需要安装sophon-sail，具体步骤可参考[编译安装sophon-sail](../../../docs/Environment_Install_Guide.md###5.3编译安装sophon-sail)。

## 3. 推理测试
对于PCIe平台和SoC平台，均可以直接在进行推理测试。

### 3.1 参数说明


| 参数名        | 类型   | 说明                                            |
| ------------- | ------ | ----------------------------------------------- |
| max_que_size  | int    | 队列长度，默认为4，不可小于输入模型的batch_size |
| video_nums    | string | 视频测试路数，默认为16                          |
| batch_size    | int    | 为输入bmodel的batch_size，默认为4               |
| loops         | int    | 对于一个进程的循环测试图片数，默认为2000        |
| input         | string | 本地视频路径或视频流地址                        |
| yolo_bmodel   | int    | yolov5 bmodel路径                               |
| lprnet_bmodel | int    | lprnet bmodel路径                               |
| dev_id        | int    | 使用的设备id，默认为0号设备                     |
| draw_images   | bool   | 是否保存图片，默认为False                       |
| stress_test   | bool   | 是否循环压测，默认为False                       |

### 3.2 运行程序
运行应用程序即可
```bash
python3 vlpr.py --input ../datasets/1080_1920_30s_512kb.mp4   --loops 2000 --video_nums 16 \
    --yolo_bmodel ../models/yolov5s-licensePlate/BM1684/yolov5s_v6.1_license_3output_int8_4b.bmodel \
    --lprnet_bmodel ../models/lprnet/BM1684/lprnet_int8_4b.bmodel
```
测试过程会打印被检测和识别到的有效车牌信息，测试结束后，会在log中打印FPS等信息。


### 3.2 程序原理流程图
[flow-diagram](../pics/python_pipeline.png)

# 文件: application/YOLOv5_fuse_multi_QT/README.md

---

# YOLOv5_fuse_multi_QT
  
## 1. 简介

YOLOv5_fuse_multi_QT 是在例程 [YOLOv5_multi](../YOLOv5_multi/README.md) 实现 pipeline 的基础上，进一步适配了 [YOLOv5_fuse](../../sample/YOLOv5_fuse/README.md) 模型，并接入 QT 显示模块（显示模块参考了例程 [YOLOv5_multi_QT](../YOLOv5_multi_QT/README.md)），从而在算能SE9系列上实现了低延时的视频流解码+QT显示功能。

## 2. 特性
* 支持 SE7、SE9-16/SE9-8
* 全流程实现方式针对低延时做了特殊优化
* 支持FP32、FP16、INT8模型编译和推理
* 解码、前处理、推理、后处理通过pipeline的形式实现
 
## 3. 准备模型和依赖库

​本例程在`scripts`目录下提供了相关模型、数据集以及公版QT库的下载脚本`download.sh`。

您也可以自己准备模型和数据集，具体转模型方法请参考 sophon-demo/sample 中例程 [YOLOv5_fuse](../../sample/YOLOv5_fuse/README.md#4-模型编译) 模型编译步骤。

```bash
# 安装unzip，若已安装请跳过，非ubuntu系统视情况使用yum或其他方式安装
sudo apt install unzip
chmod -R +x scripts/
./scripts/download.sh
```

执行下载脚本后，YOLOv5_fuse_multi_QT例程文件结构如下：
```
.
├── cpp
│   ├── qt_bm168X                           # 解压后的公版QT库（5.12.8）
│   ├── README.md                           # C++ 例程文档
│   ├── run_hdmi_show.sh                    # 例程执行脚本
│   ├── workflow.png                        # 程序流程图
│   └── yolov5_bmcv                         # C++ bmcv 例程 
├── datasets
│   ├── coco
│   ├── coco128
│   ├── coco.names                          # 类别名
│   ├── test
│   └── test_car_person_1080P.mp4           # 测试视频
├── models       
│   ├── BM1684X                             # BModel 模型
│   ├── BM1688
│   └── CV186X
├── README.md                               # C++ BMCV 例程文档
└── scripts
    └── download.sh                         # 数据、模型、QT库下载脚本
```


## 4. 例程测试

- [C++例程](./cpp/README.md)

## 5. FAQ

其他问题请参考[FAQ](../../docs/FAQ.md)查看一些常见的问题与解答。

# 文件: application/YOLOv5_fuse_multi_QT/cpp/README.md

---

[简体中文](./README.md) 

# C++例程

## 目录

- [C++例程](#c例程)
  - [目录](#目录)
  - [1. 环境准备](#1-环境准备)
  - [2. 程序编译](#2-程序编译)
  - [3. 推理测试](#3-推理测试)
    - [3.1 参数说明](#31-参数说明)
    - [3.2 运行程序](#32-运行程序)
    - [3.3 程序流程图](#33-程序流程图)

cpp目录下提供了C++例程以供参考使用，具体情况如下：
| 序号  | C++例程      | 说明                                 |
| ---- | ------------- | -----------------------------------  |
| 1    | yolov5_bmcv   | 使用opencv解码、BMCV前处理、BMRT推理   |


## 1. 环境准备

SE、SM系列边缘设备刷机后在`/opt/sophon/`下已经预装了相应的libsophon、sophon-opencv和sophon-ffmpeg运行库包，可直接使用它作为运行环境。通常还需要一台x86主机作为开发环境，用于交叉编译C++程序。


## 2. 程序编译
C++程序运行前需要编译可执行文件。

通常在x86主机上交叉编译程序，您需要在x86主机上使用SOPHON SDK搭建交叉编译环境，将程序所依赖的头文件和库文件打包至soc-sdk目录中，具体请参考[交叉编译环境搭建](../../../docs/Environment_Install_Guide.md#41-交叉编译环境搭建)。本例程主要依赖libsophon、sophon-opencv和sophon-ffmpeg运行库包。

- 请准备与设备架构匹配的 aarch64 Qt Base 依赖库。
- 如果你已运行过 `download.sh`，脚本会自动下载我们编译好的 Qt Base。
- 不同设备对应的依赖库路径：
  - BM1684X：`cpp/qt_bm1684x/install`
  - BM1688 / CV186：`cpp/qt_bm1688/install`
- 使用时，请根据设备型号选择并指定对应目录中的 Qt 依赖库。

交叉编译环境搭建好后，使用交叉编译工具链编译生成可执行文件：

```bash
cd cpp/yolov5_bmcv
mkdir build && cd build
# 请根据实际情况修改-DSDK的路径，需使用绝对路径。
# 请根据实际情况修改-DQT_PATH的路径，需要用绝对路径:/your_workspace_path/sophon-demo/application/YOLOv5_fuse_multi_QT/cpp/qt_bm1684x/install
cmake -DTARGET_ARCH=soc -DSDK=/path_to_sdk/soc-sdk ..  -DQT_PATH=/path_to_qtlib 
make
```
编译完成后，会在yolov5_bmcv目录下生成yolov5_bmcv.soc。


## 3. 推理测试
需将交叉编译生成的可执行文件及所需的模型、测试数据拷贝到SoC平台中测试。

### 3.1 参数说明
本例程通过读取json来配置参数。json格式如下：

```json
{
  "dev_id": 0,
  "bmodel_path": "../../models/CV186X/yolov5s_v6.1_fuse_int8_4b.bmodel",
  "channels": [
    {
      "url": "../../datasets/test_car_person_1080P.mp4",
      "is_video": true,
      "skip_frame": 0
    },
    {
      "url": "../../datasets/test_car_person_1080P.mp4",
      "is_video": true,
      "skip_frame": 0
    },
    {
      "url": "../../datasets/test_car_person_1080P.mp4",
      "is_video": true,
      "skip_frame": 0
    },
    {
      "url": "../../datasets/test_car_person_1080P.mp4",
      "is_video": true,
      "skip_frame": 0
    }
  ],
  "queue_size": 10,
  "num_pre": 1,
  "num_post": 1,
  "class_names": "../../datasets/coco.names",
  "conf_thresh": 0.5,
  "nms_thresh": 0.5,
  # 显示窗口的个数，应与视频流数量匹配。
  # QT中的低延时优化说明：窗口分辨率<w_widget, h_widget>等于显示器分辨率<w_hdmi / display_cols, h_hdmi / display_rows>。
  # 窗口的分辨率越小，qt的渲染速度越快。如果窗口的分辨率和输入流的分辨率相同，还可以节省掉一个resize的时间。用户可以根据实际情况做调整。
  "display_rows": 2,
  "display_cols": 2
}
```
|   参数名      | 类型    | 说明 |
|-------------|---------|-----  |
|dev_id       | int     | 设备号|
|bmodel_path  | string  | bmodel路径 |
| channels    | list    | 多路设置 |
| url         | string  | 图片目录路径(以/结尾)、视频路径或视频流地址 |
| is_video    | bool    | 是否是视频格式 |
| skip_frame  | int     | 跳帧，间隔多少帧处理一次，图片设置为0 |
| queue_size  | int     | 缓存队列长度 |
| num_pre     | int     | 预处理线程个数 |
| num_post    | int     | 后处理线程个数 |
| class_name  | string  | 类别名 |
| conf_thresh | float   | 置信度 | 
| nms_thresh  | float   | nms阈值 |
|display_rows|int|qt界面显示行数|
|display_cols|int|qt界面显示列数|


### 3.2 运行程序
将YOLOv5_fuse_multi_QT整个文件夹放到设备上；如有修改视频地址的需求，可修改 YOLOv5_fuse_multi/cpp/yolov5_bmcv/config_yolov5_fuse_mluti_qt.json 中的 url。
在YOLOv5_fuse_multi/cpp/目录下执行以下脚本：
```
./run_hdmi_show.sh
```

如有需求，可在该脚本中的以下内容，按需修改可执行文件 yolov5_bmcv.soc 的路径、json 配置文件的路径：
```
./yolov5_bmcv/yolov5_bmcv.soc --config=./yolov5_bmcv/config_yolov5_fuse_mluti_qt.json
```

为了测试时延，程序中加了一些时间打印，这里是相关打印的说明：
```bash
Channel: 0, cap_init_delay: 8.61 ms;                                 # 打开videocapture的时间
Channel: 0, worker_decode: first_frame_delay: 282.37 ms;             # 初始化videocapture前---获取到第一帧的时间
Channel: 0, worker_pre: first_preprocessed_frame_delay: 283.62 ms;   # 初始化videocapture前---第一帧前处理完的时间
Channel: 0, worker_infer: first_inferenced_frame_delay: 290.85 ms;   # 初始化videocapture前---第一帧推理完的时间
Channel: 0, worker_post: first_postprocessed_frame_delay: 290.97 ms; # 初始化videocapture前---第一帧后处理完的时间
<qt><duration> before_cap_init --- first_show_img_start: 293.50      # 初始化videocapture前---第一帧送到qtgui队列的时间。
<qt><duration> before_cap_init --- first_emit: 296.55                # 初始化videocapture前---qt第一次emit绘图事件的时间。
<qt><duration> before_cap_init --- first_painted: 297.95             # 初始化videocapture前---qt第一帧绘图事件结束的时间。
```

### 3.3 程序流程图

整体流程如下：
![alt text](workflow.png)

pipeline的实现请参考 [YOLOv5_multi](../../YOLOv5_multi/cpp/README.md#33)






# 文件: application/YOLOv5_multi/README.md

---

[简体中文](./README.md)

# YOLOv5

## 目录

* [1. 简介](#1-简介)
* [2. 特性](#2-特性)
* [3. 准备模型与数据](#3-准备模型与数据)
* [4. 模型编译](#4-模型编译)
* [5. 例程测试](#5-例程测试)
* [6. 精度测试](#6-精度测试)
  * [6.1 测试方法](#61-测试方法)
  * [6.2 测试结果](#62-测试结果)
* [7. 性能测试](#7-性能测试)
  * [7.1 bmrt_test](#71-bmrt_test)
  * [7.2 程序运行性能](#72-程序运行性能)
* [8. FAQ](#8-faq)
  
## 1. 简介
​YOLOv5是非常经典的基于anchor的One Stage目标检测算法，因其优秀的精度和速度表现，在工程实践应用中获得了非常广泛的应用。本例程对[​YOLOv5官方开源仓库](https://github.com/ultralytics/yolov5)v6.1版本的模型和算法进行移植，使之能在SOPHON BM1684\BM1684X\BM1688上进行推理测试。

## 2. 特性
* 支持BM1688(SoC)，BM1684X(x86 PCIe、SoC)，BM1684(x86 PCIe、SoC)
* 支持FP32、FP16(BM1684X、BM1688)、INT8模型推理
* 支持C++多线程，前后处理推理并行的pipeline推理
* 支持单batch和多batch模型推理
* 支持图片和视频测试

## 3. 准备模型与数据
参考[sophon-demo yolov5模型编译](../../sample/YOLOv5/README.md#3-准备模型与数据)

## 4. 模型编译
参考[sophon-demo yolov5模型编译](../../sample/YOLOv5/README.md#4-模型编译)

## 5. 例程测试
- [C++例程](./cpp/README.md)

## 6. 精度测试
### 6.1 测试方法

首先，参考[C++例程](cpp/README.md#32-测试图片)推理要测试的数据集，生成预测的json文件，注意修改数据集(datasets/coco/val2017_1000)和相关参数(conf_thresh=0.001、nms_thresh=0.6)。  
然后，使用`tools`目录下的`eval_coco.py`脚本，将测试生成的json文件与测试集标签json文件进行对比，计算出目标检测的评价指标，命令如下：
```bash
# 安装pycocotools，若已安装请跳过
pip3 install pycocotools
# 请根据实际情况修改程序路径和json文件路径
python3 tools/eval_coco.py --gt_path datasets/coco/instances_val2017_1000.json --result_json cpp/yolov5_bmcv/results/yolov5.json
```
### 6.2 测试结果
在coco2017val_1000数据集上，精度测试结果如下：
|   测试平台    |      测试程序     |              测试模型               |AP@IoU=0.5:0.95|AP@IoU=0.5|
| ------------ | ---------------- | ----------------------------------- | ------------- | -------- |
| BM1684 PCIe  | yolov5_bmcv.pcie | yolov5s_v6.1_3output_fp32_1b.bmodel | 0.375         | 0.573    |
| BM1684 PCIe  | yolov5_bmcv.pcie | yolov5s_v6.1_3output_int8_1b.bmodel | 0.339         | 0.544    |
| BM1684X PCIe | yolov5_bmcv.pcie | yolov5s_v6.1_3output_fp32_1b.bmodel | 0.375         | 0.573    |
| BM1684X PCIe | yolov5_bmcv.pcie | yolov5s_v6.1_3output_fp16_1b.bmodel | 0.375         | 0.573    |
| BM1684X PCIe | yolov5_bmcv.pcie | yolov5s_v6.1_3output_int8_1b.bmodel | 0.358         | 0.562    |
| BM1688 soc   | yolov5_bmcv.soc  | yolov5s_v6.1_3output_fp32_1b.bmodel | 0.375         | 0.573    |
| BM1688 soc   | yolov5_bmcv.soc  | yolov5s_v6.1_3output_fp16_1b.bmodel | 0.375         | 0.573    |
| BM1688 soc   | yolov5_bmcv.soc  | yolov5s_v6.1_3output_int8_1b.bmodel | 0.355         | 0.565    |


> **测试说明**：  
> 1. batch_size=4和batch_size=1的模型精度一致；
> 2. 由于sdk版本之间可能存在差异，实际运行结果与本表有<0.01的精度误差是正常的；
> 3. AP@IoU=0.5:0.95为area=all对应的指标。


## 7. 性能测试
### 7.1 bmrt_test
参考[sophon-demo yolov5性能测试](../../sample/YOLOv5/README.md#71-bmrt_test)

### 7.2 程序运行性能
参考[C++例程](cpp/README.md)运行程序，并查看统计的fps。

在不同的测试平台上，使用不同的例程、模型测试`datasets/test_car_person_1080P.mp4`，conf_thresh=0.5，nms_thresh=0.5，4预处理线程，8推理线程，性能测试结果如下：
|    测试平台 |     测试程序       |             测试模型                    |   config           | 路数    | tpu利用率(%)| 设备内存(MB) | cpu利用率(%) | 系统内存(MB) | fps  |
| ----------- | ---------------- | ----------------------------------------- | ----------------   | ------- | ----------  | ---------- | ----------  | ------------| ---- |
| SE5-16      | yolov5_bmcv.soc  | yolov5s_v6.1_3output_fp32_1b.bmodel       | config_se5.json    | 16      |  90~100     | 1650~1750  | 80~100      | 190~210     |  42  |
| SE5-16      | yolov5_bmcv.soc  | yolov5s_v6.1_3output_int8_1b.bmodel       | config_se5.json    | 16      |  85~100     | 1490~1520  | 150~180     | 190~210     |  77  |
| SE5-16      | yolov5_bmcv.soc  | yolov5s_v6.1_3output_int8_4b.bmodel       | config_se5.json    | 16      |  75~95      | 2800~2900  | 270~310     | 190~210     |  129 |
| SE7-32      | yolov5_bmcv.soc  | yolov5s_v6.1_3output_fp32_1b.bmodel       | config_se7.json    | 32      |  90~100     | 2220~2270  | 70~100      | 220~250     |  35  |
| SE7-32      | yolov5_bmcv.soc  | yolov5s_v6.1_3output_fp16_1b.bmodel       | config_se7.json    | 32      |  75~90      | 2220~2260  | 190~230     | 220~250     |  95  |
| SE7-32      | yolov5_bmcv.soc  | yolov5s_v6.1_3output_int8_1b.bmodel       | config_se7.json    | 32      |  60~80      | 2230~2260  | 350~400     | 230~250     |  167 |
| SE7-32      | yolov5_bmcv.soc  | yolov5s_v6.1_3output_int8_4b.bmodel       | config_se7.json    | 32      |  60~85      | 4180~4250  | 390~430     | 230~250     |  180 |
| SE9-8       | yolov5_bmcv.soc  | yolov5s_v6.1_3output_int8_4b_2core.bmodel | config_se9-8.json  | 8       |  70~90      | 1650~1800  | 250~300     | 160~190     |  91 |
| SE9-16      | yolov5_bmcv.soc  | yolov5s_v6.1_3output_int8_4b_2core.bmodel | config_se9-16.json | 16      |  60~75      | 4300~4500  | 390~470     | 200~220     |  132 |


> **测试说明**：  
> 1. 性能测试结果具有一定的波动性，建议多次测试取平均值；
> 2. BM1684/1684X SoC的主控处理器均为8核 ARM A53 42320 DMIPS @2.3GHz，SE9-16的主控处理器为8核CA53@1.6GHz，PCIe上的性能由于处理器的不同可能存在较大差异；
> 3. 各项指标的查看方式可以参考[测试指标查看方式](../../docs/Check_Statis.md)


## 8. FAQ
其他问题请参考[FAQ](../../docs/FAQ.md)查看一些常见的问题与解答。

# 文件: application/YOLOv5_multi/cpp/README.md

---

[简体中文](./README.md) 

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
    * [3.2 运行程序](#32-运行程序)
    * [3.3 程序流程图](#33-程序流程图)

cpp目录下提供了C++例程以供参考使用，具体情况如下：
| 序号  | C++例程      | 说明                                 |
| ---- | ------------- | -----------------------------------  |
| 1    | yolov5_bmcv   | 使用opencv解码、BMCV前处理、BMRT推理   |


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
cd cpp/yolov5_bmcv
mkdir build && cd build
cmake .. 
make
cd ..
```
编译完成后，会在yolov5_bmcv目录下生成yolov5_bmcv.pcie。


### 2.2 SoC平台
通常在x86主机上交叉编译程序，您需要在x86主机上使用SOPHON SDK搭建交叉编译环境，将程序所依赖的头文件和库文件打包至soc-sdk目录中，具体请参考[交叉编译环境搭建](../../../docs/Environment_Install_Guide.md#41-交叉编译环境搭建)。本例程主要依赖libsophon、sophon-opencv和sophon-ffmpeg运行库包。

交叉编译环境搭建好后，使用交叉编译工具链编译生成可执行文件：
#### 2.2.1 bmcv
```bash
cd cpp/yolov5_bmcv
mkdir build && cd build
#请根据实际情况修改-DSDK的路径，需使用绝对路径。
cmake -DTARGET_ARCH=soc -DSDK=/path_to_sdk/soc-sdk ..  
make
```
编译完成后，会在yolov5_bmcv目录下生成yolov5_bmcv.soc。


## 3. 推理测试
对于PCIe平台，可以直接在PCIe平台上推理测试；对于SoC平台，需将交叉编译生成的可执行文件及所需的模型、测试数据拷贝到SoC平台中测试。测试的参数及运行方式是一致的，下面主要以PCIe模式进行介绍。

### 3.1 参数说明
本例程通过读取json来配置参数。json格式如下：

```json
{
  "dev_id": 0,
  "bmodel_path": "../../models/BM1684/yolov5s_v6.1_3output_int8_1b.bmodel",
  "channels": [
    {
      "url": "../../datasets/coco/val2017_1000/",
      "is_video": false,
      "skip_frame": 0
    },
    {
      "url": "../../datasets/test_car_person_1080P.mp4",
      "is_video": true,
      "skip_frame": 5
    }
    

  ],
  "queue_size": 50,
  "num_pre": 2,
  "num_post": 4,
  "class_names": "../../datasets/coco.names",
  "conf_thresh": 0.5,
  "nms_thresh": 0.5
  

}
```
|   参数名      | 类型    | 说明 |
|-------------|---------|-----  |
|dev_id       | int     | 设备号|
|bmodel_path  | string  | bmodel路径 |
| channels    | list    | 多路设置 |
| url         | string  | 图片目录路径(以/结尾)、视频路径或视频流地址 |
| is_video    | bool    | 是否是视频格式 |
| skip_frame  | int     | 跳帧，间隔多少帧处理一次，图片设置为0 |
| queue_size  | int     | 缓存队列长度 |
| num_pre     | int     | 预处理线程个数 |
| num_post    | int     | 后处理线程个数 |
| class_name  | string  | 类别名 |
| conf_thresh | float   | 置信度 | 
| nms_thresh  | float   | nms阈值 |


### 3.2 运行程序
配置好json后，运行应用程序即可，请自行根据您的配置文件修改路径

```bash
./yolov5_bmcv.pcie --config=config.json
```
如果需要保存图片，请修改main.cpp中的宏定义为如下：
```cpp
#define DRAW_ACC 1
```
预测的图片或视频帧将保存在`results/images`下，预测的结果保存在`results/yolov5.json`下


### 3.3 程序流程图

整体流程和相关数据结构如下：

![diagram](../pics/diagram_cpp.png)

注：解码部分一路一个线程，预处理和后处理线程数可根据实际情况自定义，处理速度慢的部分可以使用相对较多的线程处理。不同路共用相同的缓存队列。

线程内部逻辑和pipeline示意图如下：

![worker_details](../pics/worker_details.png)
![pipeline](../pics/pipeline.png)




# 文件: application/YOLOv5_multi_QT/README.md

---

# YOLOv5_multi_QT
  
## 1. 简介

YOLOv5_multi_QT在算能SE7上实现了低延时的视频流解码+QT显示模块，可选择性的开启YOLOv5算法模块对视频流进行实时目标检测。

main.cpp 中 #define OPEN_YOLOV5 1 即为开始YOLOv5检测，0 即为纯解码+QT显示。

## 2. 特性

* 全流程实现方式针对低延时做了特殊优化
* 使用tpu_kernel进行后处理加速，仅支持BM1684X设备
* 支持FP32、FP16(BM1684X)、INT8模型编译和推理，仅支持1batch模型
 
## 3. 准备模型和依赖库

​本例程在`scripts`目录下提供了相关模型和数据集的下载脚本`download.sh`。

您也可以自己准备模型和数据集，具体转模型方法请参考sophon-demo中sample/YOLOv5_opt示例的模型编译步骤。

```bash
# 安装unzip，若已安装请跳过，非ubuntu系统视情况使用yum或其他方式安装
sudo apt install unzip
chmod -R +x scripts/
./scripts/download.sh
```

下载的模型包括：
```
./models
├── BM1684X
│   ├── yolov5s_tpukernel_fp32_1b.bmodel   # 使用TPU-MLIR编译，用于BM1684X的FP32 BModel，batch_size=1
│   ├── yolov5s_tpukernel_fp16_1b.bmodel   # 使用TPU-MLIR编译，用于BM1684X的FP16 BModel，batch_size=1
│   └── yolov5s_tpukernel_int8_1b.bmodel   # 使用TPU-MLIR编译，用于BM1684X的INT8 BModel，batch_size=1
└── onnx
    └── yolov5s_tpukernel.onnx             # 导出的onnx动态模型       
```

下载的tools和依赖库包括：
```
./tools
├── install     # sophon-qt 的 qmake编译工具
├── lib         # 低延时版本的SDK库
└── tpu_kernel_module  # 后处理加速依赖库，demo中自带，请勿删除。  
```

## 4. 例程测试

- [C++例程](./cpp/README.md)

## 5. FAQ

其他问题请参考[FAQ](../../docs/FAQ.md)查看一些常见的问题与解答。

# 文件: application/YOLOv5_multi_QT/cpp/README.md

---


# YOLOv5_multi_QT

YOLOv5_multi_QT在算能SE7上实现了低延时的视频流解码+QT显示模块，可选择性的开启YOLOv5算法模块对视频流进行目标检测。

main.cpp 中 #define OPEN_YOLOV5 1 即为开始YOLOv5检测，0 即为纯解码+QT显示。

* 本demo为sophon-demo中YOLOv5_opt的功能扩展，建议运行本demo前，优先按说明文档跑通YOLOv5_opt的例程，本例程中将延用YOLOv5_opt中的模型，具体模型转换过程请参考YOLOv5_opt。

## 环境准备

### 获取交叉编译需要使用的libsophon,sophon-ffmpeg,sophon-opencv

*此章节所有的编译操作都是在x86主机上,使用交叉编译的方式进行编译。下面示例中选择libsophon的版本为0.5.0, sophon-ffmpeg的版本为0.7.3,sophon-opencv的版本为0.7.3。*

1) 从算能官网中获取`libsophon_soc_0.5.0_aarch64.tar.gz`,并解压
    ```
    tar -xvf libsophon_soc_0.5.0_aarch64.tar.gz
    ```
解压后libsophon的目录为`libsophon_soc_0.5.0_aarch64/opt/sophon/libsophon-0.5.0`

2) 从算能官网中获取`sophon-mw-soc_0.7.3_aarch64.tar.gz`,并解压
    ```
    tar -xvf sophon-mw-soc_0.7.3_aarch64.tar.gz
    ```

解压后sophon-ffmpeg的目录为`sophon-mw-soc_0.7.3_aarch64/opt/sophon/sophon-ffmpeg_0.7.3`。

解压后sophon-opencv的目录为`sophon-mw-soc_0.7.3_aarch64/opt/sophon/sophon-opencv_0.7.3`。

3) 可将libsophon-0.5.0、sophon-ffmpeg_0.7.3、sophon-opencv_0.7.3三个目录放置在同一目录下，构成SOC_SDK

- SOC_SDK  
    |- libsophon-0.5.0  
    |- sophon-ffmpeg_0.7.3  
    |- sophon-opencv_0.7.3  

### 安装gcc-aarch64-linux-gnu工具链

*如果已经安装,可忽略此步骤*

```
sudo apt-get install gcc-aarch64-linux-gnu g++-aarch64-linux-gnu
```

## 编译程序

1) 根据SOC_SDK路径及版本号修改yolov5_app.pro中对应路径，主要是23~26行

2) 编译程序

```
mkdir build && cd build
../../tools/install/bin/qmake ../yolov5_app.pro
make -j
cd ..
```

## 执行程序

1) 修改yolov5_app.json文件对程序进行配置

```
{
    "decoder":{
        "urls":[
            "rtsp_url_0", 
            "rtsp_url_1",
            "rtsp_url_2",
            "rtsp_url_3"
        ]
    },
    "yolov5":{
        "dev_id": 0,
        "bmodel_path": "../models/BM1684X/yolov5s_tpukernel_int8_1b.bmodel",
        "tpu_kernel_module_path": "../tools/tpu_kernel_module/libbm1684x_kernel_module.so",
        "que_size": 1,
        # 视频每跳过skip_num帧检测1帧
        "skip_num": 0,
        "nmsThreshold": 0.5,
        "confThreshold": 0.5
    },
    # 显示窗口的个数，应与视频流数量匹配。
    "display":{
        "rows": 2,
        "cols": 2
    }
}
```

2) 将YOLOv5_multi_QT完整目录拷贝至SOC上，sudo bash ./run_hdmi_show.sh 即可执行程序。

* 注意：如果SE7上的桌面程序正在运行，需要先停止服务 sudo systemctl stop SophonHDMI.service


## 程序流程图及二次开发说明

demo中各个功能均为模块化设计，便于用户直接取其中的功能类进行二次开发，后续将简要介绍各个模块的流程图。

### DecoderConsole

![Alt text](../pics/DecoderConsole.png)

DecoderConsole实现了多路视频解码功能，可以通过addChannel接口接入视频流，read接口可以从指定id的ChannelDecoder中获取shared_ptr<bm_image>，此处的shared_ptr自定义了删除器，在析构时可以自动释放bm_image的资源，无需再额外的进行destroy，否则可能造成内存double free！

ChannelDecoder实现了单路的视频解码功能，该类内部启动了一个解码线程，且存在一个默认长度为1的非阻塞队列，对外暴露从队列中的获取image的接口get_img。ChannelDecoder可以作为解码器单独使用，也可与DecoderConsole配套使用。

注意：此处长度为1的非阻塞队列保证每次read时，取走的都是最新的帧，这保证了显示的低延时，但是如果算法处理较慢时，可能会出现丢帧现象。


### VideoConsole

![Alt text](../pics/VideoConsole.png)

VideoConsole实现了多路视频的QT同窗显示功能。VideoConsole是一个模板类，可以实现bm_image,cv::Mat或额外带有检测框信息的FrameInfoDetect的显示；VideoConsole内部初始化了QT布局，包含rows*cols个BMLabel，一个输入队列，并默认启动rows*cols个线程从输入队列中获取数据，并按channel_id分配至对应的BMLabel.

BMLabel继承了QLable，具备QLable的全部功能，且重载实现了show_img，实现了三个类型的画面显示和检测框绘制，BMLabel也可以单独使用。


### Yolov5

![Alt text](../pics/Yolov5.png)

Yolov5类中实现yolov5算法的pipeline全流程，只需调用push_img接口送入数据，就可以get_img获得带有检测框信息的图片。

需要注意的是，为了第一时间获取最低延时视频帧，yolov5的preprocess并不是在类中单独起线程进行处理的，而是由外部执行push_img的线程承担，这样降低了从解码到算法处理的滞后缓存帧数量。


### main.cpp构造
![Alt text](../pics/main.png)

在主函数中，利用两个线程将三个模块串联起来，实现解码——检测——显示全流程。decode_thread通过轮询的方式汇聚各个channel解出的视频帧并送入Yolov5中进行检测。display_thread只起到了从Yolov5到VideoConsole中的搬运功能，并未做额外处理。

# 文件: application/YOLOv8_multi_QT/README.md

---

# YOLOv8_multi_QT
  
## 1. 简介

YOLOv8_multi_QT 是在例程 [YOLOv5_multi](../YOLOv5_multi/README.md) 实现 pipeline 的基础上，进一步适配了 [YOLOv8_plus_det](../../sample/YOLOv8_plus_det/README.md) 模型，并接入 QT 显示模块（显示模块参考了例程 [YOLOv5_multi_QT](../YOLOv5_multi_QT/README.md)），从而在算能SE9系列上实现了低延时的视频流解码+QT显示功能。

## 2. 特性
* 支持 SE7、SE9-16/SE9-8
* 全流程实现方式针对低延时做了特殊优化
* 支持FP32、FP16、INT8模型编译和推理
* 解码、前处理、推理、后处理通过pipeline的形式实现
 
## 3. 准备模型和依赖库

​本例程在`scripts`目录下提供了相关模型、数据集以及公版QT库的下载脚本`download.sh`。

您也可以自己准备模型和数据集，具体转模型方法请参考 sophon-demo/sample 中例程 [YOLOv8_plus_det](../../sample/YOLOv8_plus_det/README.md#32-模型编译) 模型编译步骤。

```bash
# 安装unzip，若已安装请跳过，非ubuntu系统视情况使用yum或其他方式安装
sudo apt install unzip
chmod -R +x scripts/
./scripts/download.sh
```

执行下载脚本后，YOLOv8_multi_QT例程文件结构如下：
```
.
├── cpp
│   ├── qt_bm168X                           # 解压后的公版QT库
│   ├── README.md                           # C++ 例程文档
│   ├── run_hdmi_show.sh                    # 例程执行脚本
│   └── yolov8_bmcv                         # C++ bmcv 例程 
├── datasets
│   ├── coco
│   ├── coco128
│   ├── coco.names                          # 类别名
│   ├── test
│   └── test_car_person_1080P.mp4           # 测试视频
├── models       
│   ├── BM1684X                             # BModel 模型
│   ├── BM1688
│   └── CV186X
├── README.md                               # C++ BMCV 例程文档
└── scripts
    └── download.sh                         # 数据、模型、QT库下载脚本
```


## 4. 例程测试

- [C++例程](./cpp/README.md)

## 5. FAQ

其他问题请参考[FAQ](../../docs/FAQ.md)查看一些常见的问题与解答。

# 文件: application/YOLOv8_multi_QT/cpp/README.md

---

[简体中文](./README.md) 

# C++例程

## 目录

- [C++例程](#c例程)
  - [目录](#目录)
  - [1. 环境准备](#1-环境准备)
  - [2. 程序编译](#2-程序编译)
  - [3. 推理测试](#3-推理测试)
    - [3.1 参数说明](#31-参数说明)
    - [3.2 运行程序](#32-运行程序)
    - [3.3 程序流程图](#33-程序流程图)

cpp目录下提供了C++例程以供参考使用，具体情况如下：
| 序号  | C++例程      | 说明                                 |
| ---- | ------------- | -----------------------------------  |
| 1    | yolov8_bmcv   | 使用opencv解码、BMCV前处理、BMRT推理   |


## 1. 环境准备

SE、SM系列边缘设备刷机后在`/opt/sophon/`下已经预装了相应的libsophon、sophon-opencv和sophon-ffmpeg运行库包，可直接使用它作为运行环境。通常还需要一台x86主机作为开发环境，用于交叉编译C++程序。


## 2. 程序编译
C++程序运行前需要编译可执行文件。

通常在x86主机上交叉编译程序，您需要在x86主机上使用SOPHON SDK搭建交叉编译环境，将程序所依赖的头文件和库文件打包至soc-sdk目录中，具体请参考[交叉编译环境搭建](../../../docs/Environment_Install_Guide.md#41-交叉编译环境搭建)。本例程主要依赖libsophon、sophon-opencv和sophon-ffmpeg运行库包。

- 请准备与设备架构匹配的 aarch64 Qt Base 依赖库。
- 如果你已运行过 `download.sh`，脚本会自动下载我们编译好的 Qt Base。
- 不同设备对应的依赖库路径：
  - BM1684X：`cpp/qt_bm1684x/install`
  - BM1688 / CV186：`cpp/qt_bm1688/install`
- 使用时，请根据设备型号选择并指定对应目录中的 Qt 依赖库。

交叉编译环境搭建好后，使用交叉编译工具链编译生成可执行文件：

```bash
cd cpp/yolov8_bmcv
mkdir build && cd build
# 请根据实际情况修改-DSDK的路径，需使用绝对路径。
# 请根据实际情况修改-DQT_PATH的路径，需要用绝对路径:/your_workspace_path/sophon-demo/application/YOLOv8_multi_QT/cpp/qt_bm1684x/install
cmake -DTARGET_ARCH=soc -DSDK=/path_to_sdk/soc-sdk ..  -DQT_PATH=/path_to_qtlib 
make
```
编译完成后，会在yolov8_bmcv目录下生成yolov8_bmcv.soc。


## 3. 推理测试
需将交叉编译生成的可执行文件及所需的模型、测试数据拷贝到SoC平台中测试。

### 3.1 参数说明
本例程通过读取json来配置参数。json格式如下：

```json
{
  "dev_id": 0,
  "bmodel_path": "../models/BM1684X/yolov8s_int8_4b.bmodel",
  "channels": [
    {
      "url": "../../datasets/test_car_person_1080P.mp4",
      "is_video": true,
      "skip_frame": 0
    },
    {
      "url": "../../datasets/test_car_person_1080P.mp4",
      "is_video": true,
      "skip_frame": 0
    },
    {
      "url": "../../datasets/test_car_person_1080P.mp4",
      "is_video": true,
      "skip_frame": 0
    },
    {
      "url": "../../datasets/test_car_person_1080P.mp4",
      "is_video": true,
      "skip_frame": 0
    }
  ],
  "queue_size": 10,
  "num_pre": 1,
  "num_post": 1,
  "class_names": "../../datasets/coco.names",
  "conf_thresh": 0.5,
  "nms_thresh": 0.5,
  # 显示窗口的个数，应与视频流数量匹配。
  # QT中的低延时优化说明：窗口分辨率<w_widget, h_widget>等于显示器分辨率<w_hdmi / display_cols, h_hdmi / display_rows>。
  # 窗口的分辨率越小，qt的渲染速度越快。如果窗口的分辨率和输入流的分辨率相同，还可以节省掉一个resize的时间。用户可以根据实际情况做调整。
  "display_rows": 2,
  "display_cols": 2
}
```
|   参数名      | 类型    | 说明 |
|-------------|---------|-----  |
|dev_id       | int     | 设备号|
|bmodel_path  | string  | bmodel路径 |
| channels    | list    | 多路设置 |
| url         | string  | 图片目录路径(以/结尾)、视频路径或视频流地址 |
| is_video    | bool    | 是否是视频格式 |
| skip_frame  | int     | 跳帧，间隔多少帧处理一次，图片设置为0 |
| queue_size  | int     | 缓存队列长度 |
| num_pre     | int     | 预处理线程个数 |
| num_post    | int     | 后处理线程个数 |
| class_name  | string  | 类别名 |
| conf_thresh | float   | 置信度 | 
| nms_thresh  | float   | nms阈值 |
|display_rows|int|qt界面显示行数|
|display_cols|int|qt界面显示列数|


### 3.2 运行程序
将YOLOv8_multi_QT整个文件夹放到设备上；如有修改视频地址的需求，可修改 YOLOv8_multi/cpp/yolov8_bmcv/config_yolov8_mluti_qt.json 中的 url。
在YOLOv8_multi/cpp/目录下执行以下脚本：
```
./run_hdmi_show.sh
```

如有需求，可在该脚本中的以下内容，按需修改可执行文件 yolov8_bmcv.soc 的路径、json 配置文件的路径：
```
./yolov8_bmcv/yolov8_bmcv.soc --config=./yolov8_bmcv/config_yolov8_mluti_qt.json
```

为了测试时延，程序中加了一些时间打印，这里是相关打印的说明：
```bash
Channel: 0, cap_init_delay: 8.61 ms;                                 # 打开videocapture的时间
Channel: 0, worker_decode: first_frame_delay: 282.37 ms;             # 初始化videocapture前---获取到第一帧的时间
Channel: 0, worker_pre: first_preprocessed_frame_delay: 283.62 ms;   # 初始化videocapture前---第一帧前处理完的时间
Channel: 0, worker_infer: first_inferenced_frame_delay: 290.85 ms;   # 初始化videocapture前---第一帧推理完的时间
Channel: 0, worker_post: first_postprocessed_frame_delay: 290.97 ms; # 初始化videocapture前---第一帧后处理完的时间
<qt><duration> before_cap_init --- first_show_img_start: 293.50      # 初始化videocapture前---第一帧送到qtgui队列的时间。
<qt><duration> before_cap_init --- first_emit: 296.55                # 初始化videocapture前---qt第一次emit绘图事件的时间。
<qt><duration> before_cap_init --- first_painted: 297.95             # 初始化videocapture前---qt第一帧绘图事件结束的时间。
```

### 3.3 程序流程图

pipeline的实现请参考 [YOLOv5_multi](../../YOLOv5_multi/cpp/README.md#33)





# 文件: application/cv-demo/README.md

---

# cv Demo

## 目录
- [cv Demo](#cv_demo)
  - [目录](#目录)
  - [1. 简介](#1-简介)
  - [2. 特性](#2-特性)
  - [3. 准备数据](#3-准备数据)
  - [4. 例程测试](#4-例程测试)
  - [5. 性能测试](#5-性能测试)

## 1. 简介

本例程用于说明如何使用BM1688快速构建双目鱼眼或者广角拼接应用。

本例程中，cv_demo算法的dwa展开、blend拼接分别在两个线程上进行运算，保证了一定的运行效率。

## 2. 特性

* 支持BM1688(SoC)
* 支持二路视频流
* 支持多线程

## 3. 准备数据

​在`scripts`目录下提供了相关数据的下载脚本 [download.sh](./scripts/download.sh)。

```bash
# 安装unzip，若已安装请跳过，非ubuntu系统视情况使用yum或其他方式安装
sudo apt install unzip
chmod -R +x scripts/
./scripts/download.sh
```

脚本执行完毕后，会在当前目录下生成`data`目录,子目录如下。

.
├── gridinfo # 用于dwa模块的参数文件
├── images   # 测试图片
└── wgt     # 用于拼接的权重文件


## 4. 例程测试

- [C++例程](./cpp/README.md)

## 5. 性能测试

目前，鱼眼和广角拼接算法只支持在BM1688 SOC模式下进行推理。按照默认设置可以达到30fps。



# 文件: application/cv-demo/cpp/README.md

---

# cv Demo

## 目录
- [cv Demo](#cv_demo)
  - [目录](#目录)
  - [1. 环境准备](#1-环境准备)
    - [1. SoC平台](#1-soc平台)
  - [2. 程序编译](#2-程序编译)
    - [2.1 SoC平台](#21-soc平台)
  - [3. 程序运行](#3-程序运行)
    - [3.1 Json配置说明](#31-json配置说明)
    - [3.2 运行](#32-运行)
  - [4. 可视化](#4-可视化)





## 1. 环境准备

### 1. SoC平台

如果您使用SoC平台（如SE、SM系列边缘设备），刷机后在`/opt/sophon/`下已经预装了相应的libsophon、sophon-opencv和sophon-ffmpeg运行库包，可直接使用它作为运行环境。通常还需要一台x86主机作为开发环境，用于交叉编译C++程序。
(1) 安装摄像头
本例程适用于提供使用带J1901(母座)-Rx接口的算能模组二次开发底板或者算能evb板
(2) 安装驱动
安装驱动需要进入到超级权限，接着系统驱动目录，安装驱动：
鱼眼拼接使用04e10镜头，安装对应驱动
```bash
sudo -s
insmod /mnt/system/ko/v4l2_os04e10.ko
```

广角拼接使用04a10镜头，安装对应驱动
```bash
sudo -s
insmod /mnt/system/ko/v4l2_os04a10_sync.ko
```
（2）isp参数文件配置,cvi_sdr_bin在准备数据章节下载的data路径中

```bash
sudo -s
mkdir -p /mnt/cfg/param
cp data/param/cvi_sdr_bin /mnt/cfg/param
```

注意:每重启一次，应重新加载相应的驱动
## 2. 程序编译

### 2.1 SoC平台
通常在x86主机上交叉编译程序，您需要在x86主机上使用SOPHON SDK搭建交叉编译环境，将程序所依赖的头文件和库文件打包至soc-sdk目录中，具体请参考[交叉编译环境搭建](../../../docs/Environment_Install_Guide.md#41-交叉编译环境搭建)。本例程主要依赖libsophon、sophon-opencv和sophon-ffmpeg运行库包。

交叉编译环境搭建好后，使用交叉编译工具链编译生成可执行文件：
#### 2.1.1 bmcv
```bash
cd cv-demo/cpp
mkdir build && cd build
#请根据实际情况修改-DSDK的路径，需使用绝对路径。
cmake -DTARGET_ARCH=soc -DSDK=/path_to_sdk/soc-sdk ..  
make
```
编译完成后，会在cv-demo/cpp目录下生成cvdemo.soc。

## 3. 程序运行

### 3.1 Json配置说明

cv_demo demo中各部分参数位于 [config](./config-04e10/) 与 [config](./config-04a10/)目录，结构如下所示：

```bash
./config-04e10/
├── camera_cv_demo.json          # demo按sensor输入的配置文件
├── cv_demo.json            # demo按图片输入的配置文件
├── dwa_L.json                  # 左侧输入的鱼眼展开配置文件
├── dwa_R.json                  # 右侧输入的鱼眼展开配置文件
└── blend.json                  # 拼接配置文件
./config-04a10/
├── camera_cv_demo.json          # demo按sensor输入的配置文件
├── cv_demo.json            # demo按图片输入的配置文件
├── dwa_L.json                  # 左侧输入的鱼眼展开配置文件
├── dwa_R.json                  # 右侧输入的鱼眼展开配置文件
└── blend.json                  # 拼接配置文件
```

其中，[camera_cv_demo.json](./config-04e10/camera_cv_demo.json)是例程的整体配置文件，管理输入码流等信息。在一张图上可以支持多路数据的输入，channels参数配置输入的路数，channel中包含码流url等信息。

已提供默认的config文件，运行时只需要将config-04e10或config-04a10改名为config即可，如
```bash
mv config-04e10/ config
```
### 3.2 运行

对于SoC平台，需将交叉编译生成的动态链接库、可执行文件、所需的模型和测试数据拷贝到SoC平台中测试。

SoC平台上，动态库、可执行文件、配置文件、模型、视频数据的目录结构关系应与原始sophon-demo仓库中的关系保持一致。


1. 运行可执行文件
```bash
./cvdemo.soc
```


## 4. 可视化
运行程序后修改cv_demo.html中 connectWebSocket 的对应ip与端口，默认端口为9002，可在代码对应main函数修改，并在可以与soc网络相通的机器客户端浏览器上打开cv_demo.html，注意前端没有帧率控制，网络不好的情况下可能会卡顿
效果如下所示[config](../pic/pic.jpg)

## 5. 常用debug命令
一般运行demo之前请保证ut出图正常

ut测试命令如下
```bash
cd /opt/sophon/sophon-soc-libisp_1.0.0/bin/
./ispv4l2_ut 6
```
原始yuv图片会保存在/opt/sophon/sophon-soc-libisp_1.0.0/bin/路径下

# 文件: docs/Calibration_Guide.md

---

[简体中文](./Calibration_Guide.md) | [English](./Calibration_Guide_EN.md.md)

# 模型量化
更多模型量化教程请参考
《TPU-MLIR开发参考手册》和《TPU-NNTC开发参考手册》的“模型量化”(请从[算能官网](https://developer.sophgo.com/site/index.html?categoryActive=material)相应版本的SDK中获取)。

## 1. 注意事项
### 1.1 量化数据集
建议从训练集随机抽取100~500张样本作为量化数据集，量化数据集应尽量涵盖测试场景和类别，量化时可尝试不同的iterations进行量化以获得最优的量化精度。

### 1.2 前处理对齐
量化数据集的预处理应该和推理测试的预处理保持一致，否则会导致较大的精度损失。在mlir制作npz/npy数据集、nntc制作lmdb量化数据集时，应当预先完成数据的预处理。

### 1.3 特定模型优化技巧
#### 1.3.1 YOLOv5系列模型
由于yolov5系列的输出分类和回归任务耦合在一起,致使输出在统计学上的分布不均匀，所以通常不量化最后三个conv层及其之后的所有层，有时候最开始的几个conv层也不量化，具体效果如何需要实际操作下。

MLIR具体步骤如下：
1. 可以先用mlir2onnx.py这个工具，将model_transform生成的mlir文件转化成onnx，然后通过netron查看onnx网络结构。
   ```bash
   mlir2onnx.py -m xxx.mlir -o xxx.onnx
   ```
2. 使用fp_forward.py生成qtable，--fpfwd_outputs、--fpfwd_inputs功能与以前nntc一样，指定层名即可将对应的所有层指定对应的fp_type。
   ![Alt text](../pics/cali_guide_image0.webp)
   如上图所示，最后三个的卷积层的名称分别为390，416，442，因此使用以下fp_forward指令，生成qtable:
   ```bash
   fp_forward.py xxx.mlir --fpfwd_outputs 390,416,442 --chip bm1684 -o xxx_qtable 
   ```
   将最后三个卷积以及后续所有的计算层采用float进行计算，可有效提高模型精度。
   
   **注意，在部分版本mlir中，--chip参数或许不支持bm1688/cv186x，您可以使用bm1684x代替，生成的qtable都是通用的，您也可以自由地更改qtable中每一层对应的的fp_type。**

3. 生成的qtable传给model_deploy.py，配合加入test_input和test_reference来验证混精度策略是否有效。

NNTC具体步骤如下：
1. 生成fp32 umodel的prototxt文件；
2. 用Netron打开fp32 umodel的prototxt文件，选择后面三个branch（大目标，中目标，小目标）的conv层，记下名字；
3. 在分步量化或一键量化中通过--fpfwd_outputs指定步骤2所获得的conv层。可通过--help查看具体方法或参考YOLOv5的量化脚本。

#### 1.3.2 YOLOv8系列模型
YOLOv8系列模型采用解耦头结构 (Decoupled-Head), 将分类和检测头分离，经验性地，对于改类，一般都需要从坐标回归分支的Conv层、概率预测分支的Sigmoid层开始，将它们设为浮点数计算。

MLIR具体步骤如下：
1. 可以先用mlir2onnx.py这个工具，将model_transform生成的mlir文件转化成onnx，然后通过netron查看onnx网络结构。
   ```bash
   mlir2onnx.py -m xxx.mlir -o xxx.onnx
   ```
2. 使用fp_forward.py生成qtable，--fpfwd_outputs、--fpfwd_inputs功能与以前nntc一样，指定层名即可将对应的所有层指定对应的fp_type。
   ![Alt text](../pics/cali_guide_image1.webp)
   如上图所示，层名一般是该层在netron.app中对应的OUTPUTS name。参考如下命令生成qtable：
   ```bash
   fp_forward.py xxx.mlir --fpfwd_outputs /model.22/dfl/conv/Conv_output_0_Conv --chip bm1684 -o xxx_qtable 
   ```
   **然后在qtable中直接添加Sigmoid层**，由于在之前的fp_forward过程中，卷积层已经包含了Sigmoid后续的操作，因此只需在量化表的最后一行加入
   ```bash
   /model.22/Sigmoid_output_0_Sigmoid F16。
   ```
   
   **注意，在部分版本mlir中，--chip参数或许不支持bm1688/cv186x，您可以使用bm1684x代替，生成的qtable都是通用的，您也可以自由地更改qtable中每一层对应的的fp_type。**

3. 生成的qtable传给model_deploy.py，配合加入test_input和test_reference来验证混精度策略是否有效。

## 2. 常见问题
### 2.1 量化后检测框偏移严重
在以上注意事项都确认无误的基础上，尝试不同的门限策略th_method，推荐ADMM, MAX,PERCENTILE9999。

### 2.2 NNTC量化过程中精度对比不通过导致量化中断
NNTC相关报错：
```bash
w0209 14:47:33.992739 3751 graphTransformer.cpp:515] max diff = 0.00158691 max diff blob id : 4 blob name : out put
Fail: only one compare!
```
原因：量化过程中fp32精度对比超过设定阈值(默认值为0.001)。
解决办法：修改fp32精度对比阈值，如-fp32_diff=0.01。

### 2.3 MLIR量化过程中model_deploy出现精度比对错误：
MLIR相关报错如：
```bash
min_similiarity = (0.7610371112823486, -0.6141192159850581, -16.15570902824402)
Target    yolov8s_bm1684_int8_sym_tpu_outputs.npz
Reference yolov8s_top_outputs.npz
npz compare FAILED.
compare output0_Concat: 100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 1/1 [00:00<00:00,  3.88it/s]
Traceback (most recent call last):
  File "/usr/local/lib/python3.10/dist-packages/tpu_mlir/python/tools/model_deploy.py", line 335, in <module>
    tool.lowering()
  File "/usr/local/lib/python3.10/dist-packages/tpu_mlir/python/tools/model_deploy.py", line 132, in lowering
    tool.validate_tpu_mlir()
  File "/usr/local/lib/python3.10/dist-packages/tpu_mlir/python/tools/model_deploy.py", line 225, in validate_tpu_mlir
    f32_blobs_compare(self.tpu_npz, self.ref_npz, self.tolerance, self.excepts)
  File "/usr/local/lib/python3.10/dist-packages/tpu_mlir/python/utils/mlir_shell.py", line 190, in f32_blobs_compare
    _os_system(cmd)
  File "/usr/local/lib/python3.10/dist-packages/tpu_mlir/python/utils/mlir_shell.py", line 50, in _os_system
    raise RuntimeError("[!Error]: {}".format(cmd_str))
RuntimeError: [!Error]: npz_tool.py compare yolov8s_bm1684_int8_sym_tpu_outputs.npz yolov8s_top_outputs.npz --tolerance 0.8,0.5 --except - -vv 
mv: cannot stat 'yolov8s_int8_1b.bmodel': No such file or directory
```
可能是由于用户使用自己的onnx，例程提供的qtable中的层名，与生成的mlir的层名对不上。此时需要重新生成qtable，如果是yolo系列模型，可以参考[特定模型优化技巧](#13-特定模型优化技巧)，如果是其他模型，可以参考[TPU-MLIR Github](https://github.com/sophgo/tpu-mlir/blob/master/docs/quick_start/source_zh/07_quantization.rst)中的`run_sensitive_layer`功能。


# 文件: docs/Check_Statis.md

---

[简体中文](./Check_Statis.md) | [English](./Check_Statis_EN.md)

# 常用指标查看方法

## 1. TPU利用率
可以通过以下两种命令查看：
```bash
bm-smi #右上角的Tpu-Util表示TPU瞬时利用率，PCIe和SoC均可使用，PCIe下需要搭载SOPHON板卡并安装驱动和LIBSOPHON。
cat /sys/class/bm-tpu/bm-tpu0/device/npu_usage #SoC下可以使用，打印usage:0 avusage:0，Usage表示过去一个时间窗口内的npu利用率，AvUsage表示自安装驱动以来npu的利用率。
```
更多详细信息，可以参考《LIBSOPHON 使用手册》。

## 2. 设备内存占用
可以通过`bm-smi`右上角的`Memory-Usage`查看，它表示gmem总数和已使用数量；`bm-smi`还会显示每个设备上每个进程（或者线程）占用的gmem的数量。

更多详细信息，可以参考《LIBSOPHON 使用手册》。

## 3. CPU利用率
这里指的是某个程序的利用率，可以通过`top`或者`htop`查看`CPU%`字段下对应程序的值，用户可以自行搜索它们的用法。

## 4. 系统内存占用
这里指的是某个程序的占用，可以通过`top`或者`htop`查看`RES`字段下对应程序的值，用户可以自行搜索它们的用法。

# 文件: docs/Environment_Install_Guide.md

---

[简体中文](./Environment_Install_Guide.md) | [English](./Environment_Install_Guide_EN.md)

# sophon-demo环境安装指南
## 目录
- [sophon-demo环境安装指南](#sophon-demo环境安装指南)
  - [目录](#目录)
  - [1 TPU-MLIR环境搭建](#1-tpu-mlir环境搭建)
  - [2 TPU-NNTC环境搭建](#2-tpu-nntc环境搭建)
  - [3 x86 PCIe平台的开发和运行环境搭建](#3-x86-pcie平台的开发和运行环境搭建)
    - [3.1 安装libsophon](#31-安装libsophon)
    - [3.2 安装sophon-ffmpeg和sophon-opencv](#32-安装sophon-ffmpeg和sophon-opencv)
    - [3.3 编译安装sophon-sail](#33-编译安装sophon-sail)
  - [4 SoC平台的开发和运行环境搭建](#4-soc平台的开发和运行环境搭建)
    - [4.1 交叉编译环境搭建](#41-交叉编译环境搭建)
    - [4.2 交叉编译安装sophon-sail](#42-交叉编译安装sophon-sail)
  - [5 arm PCIe平台的开发和运行环境搭建](#5-arm-pcie平台的开发和运行环境搭建)
    - [5.1 安装libsophon](#51-安装libsophon)
    - [5.2 安装sophon-ffmpeg和sophon-opencv](#52-安装sophon-ffmpeg和sophon-opencv)
    - [5.3 编译安装sophon-sail](#53-编译安装sophon-sail)
  - [6 riscv PCIe平台的开发和运行环境搭建](#6-riscv-pcie平台的开发和运行环境搭建)
    - [6.1 安装libsophon](#61-安装libsophon)
    - [6.2 安装sophon-ffmpeg和sophon-opencv](#62-安装sophon-ffmpeg和sophon-opencv)
    - [6.3 编译安装sophon-sail](#63-编译安装sophon-sail)
    - [6.4 安装构建工具](#64-安装构建工具)
    - [6.5 注意事项](#65-注意事项)

Sophon Demo所依赖的环境主要包括用于编译和量化模型的TPU-NNTC、TPU-MLIR环境，用于编译C++程序的开发环境以及用于部署程序的运行环境。

## 1 TPU-MLIR环境搭建
使用TPU-MLIR编译BModel，通常需要在x86主机上安装TPU-MLIR环境，x86主机已安装Ubuntu16.04/18.04/20.04系统，并且运行内存在12GB以上。TPU-MLIR环境安装步骤主要包括：

1. 安装Docker
   若已安装docker，请跳过本节。
    ```bash
    # 如果您的docker环境损坏，可以先卸载docker
    sudo apt-get remove docker docker.io containerd runc

    # 安装依赖
    sudo apt-get update
    sudo apt-get install \
            ca-certificates \
            curl \
            gnupg \
            lsb-release

    # 获取密钥
    sudo mkdir -p /etc/apt/keyrings
    curl -fsSL \
        https://download.docker.com/linux/ubuntu/gpg | \
        gpg --dearmor -o docker.gpg && \
        sudo mv -f docker.gpg /etc/apt/keyrings/

    # 添加 docker 软件包
    echo \
        "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] \
        https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | \
        sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

    # 安装 docker
    sudo apt-get update
    sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin
    
    # docker命令免root权限执行
    # 创建docker用户组，若已有docker组会报错，没关系可忽略
    sudo groupadd docker
    # 将当前用户加入docker组
    sudo usermod -aG docker $USER
    # 切换当前会话到新group或重新登录重启X会话
    newgrp docker​ 
    ```
    > **提示**：需要logout系统然后重新登录，再使用docker就不需要sudo了。

2. 创建并进入docker

    TPU-MLIR使用的docker是sophgo/tpuc_dev:latest, docker镜像和tpu-mlir有绑定关系，少数情况下有可能更新了tpu-mlir，需要新的镜像。
    ```bash
    docker pull sophgo/tpuc_dev:latest
    # 这里将本级目录映射到docker内的/workspace目录,用户需要根据实际情况将demo的目录映射到docker里面
    # myname只是举个名字的例子, 请指定成自己想要的容器的名字
    docker run --privileged --name myname --network host -v $PWD:/workspace -it sophgo/tpuc_dev:latest
    # 此时已经进入docker，并在/workspace目录下  
    ```

3. 安装TPU-MLIR
    
    目前支持三种安装方法：

    (1)直接从pypi下载并安装：
    ```bash
    pip install tpu_mlir -i https://pypi.tuna.tsinghua.edu.cn/simple 
    ```
    (2)从[TPU-MLIR Github](https://github.com/sophgo/tpu-mlir/releases)下载最新`tpu_mlir-*-py3-none-any.whl`，然后使用pip安装：
    ```bash
    pip install tpu_mlir-*-py3-none-any.whl
    ```

    TPU-MLIR在对不同框架模型处理时所需的依赖不同，对于onnx或torch生成的模型文件，
    使用下面命令安装额外的依赖环境:
    ```bash
    pip install tpu_mlir[onnx]
    pip install tpu_mlir[torch]
    ```
    目前支持五种配置: onnx, torch, tensorflow, caffe, paddle。可使用一条命令安装多个配置，也可直接安装全部依赖环境:
    ```bash
    pip install tpu_mlir[onnx,torch,caffe]
    pip install tpu_mlir[all]
    ```
    (3)如果您获取了类似`tpu-mlir_${version}-${hash}-${date}.tar.gz`这种形式的发布包，可以通过这种方式配置：
    ```bash
    # 如果此前有通过pip安装过mlir，需要卸载掉
    pip uninstall tpu_mlir
    
    tar xvf tpu-mlir_${version}-${hash}-${date}.tar.gz
    cd tpu-mlir_${version}-${hash}-${date}
    source envsetup.sh #配置环境变量
    ```

建议TPU-MLIR的镜像仅用于编译和量化模型，程序编译和运行请在开发和运行环境中进行。更多TPU-MLIR的教程请参考[算能官网](https://developer.sophgo.com/site/index.html?categoryActive=material)的《TPU-MLIR快速入门手册》和《TPU-MLIR开发参考手册》。

## 2 TPU-NNTC环境搭建

**注意，TPU-NNTC已停止维护，如果使用TPU-NNTC出现问题，建议您使用TPU-MLIR。**

使用TPU-NNTC编译BModel，通常需要在x86主机上安装TPU-NNTC环境，x86主机已安装Ubuntu16.04/18.04/20.04系统，并且运行内存在12GB以上。TPU-NNTC环境安装步骤主要包括：

1. 安装Docker

   若已安装docker，请跳过本节。
    ```bash
    # 安装docker
    sudo apt-get install docker.io
    # docker命令免root权限执行
    # 创建docker用户组，若已有docker组会报错，没关系可忽略
    sudo groupadd docker
    # 将当前用户加入docker组
    sudo usermod -aG docker $USER
    # 切换当前会话到新group或重新登录重启X会话
    newgrp docker​ 
    ```
    > **提示**：需要logout系统然后重新登录，再使用docker就不需要sudo了。

2. 下载并解压TPU-NNTC

    从[算能官网](https://developer.sophgo.com/site/index.html?categoryActive=material)上下载符合[环境依赖](../README.md#环境依赖)的TPU-NNTC压缩包，命名如tpu-nntc_vx.y.z-hash-date.tar.gz，x.y.z表示版本号，并进行解压。
    ```bash
    mkdir tpu-nntc
    # 将压缩包解压到tpu-nntc
    tar zxvf tpu-nntc_vx.y.z-<hash>-<date>.tar.gz --strip-components=1 -C tpu-nntc
    ```

3. 创建并进入docker

    TPU-NNTC使用的docker是sophgo/tpuc_dev:2.1, docker镜像和tpu-nntc有绑定关系，少数情况下有可能更新了tpu-nntc，需要新的镜像。
    ```bash
    cd tpu-nntc
    # 进入docker，如果当前系统没有对应镜像，会自动从docker hub上下载
    # 这里将tpu-nntc的上一级目录映射到docker内的/workspace目录,用户需要根据实际情况将demo的目录映射到docker里面
    # 这里用了8001到8001端口映射，之后在使用ufw可视化工具会用到
    # 如果端口已经占用，请更换其他未占用端口，后面根据需要更换进行调整
    docker run --privileged --name myname -v $PWD/..:/workspace -p 8001:8001 -it sophgo/tpuc_dev:v2.1
    # 此时已经进入docker，并在/workspace目录下
    # 下面初始化软件环境
    cd /workspace/tpu-nntc
    source scripts/envsetup.sh
    ```
此镜像仅用于编译和量化模型，程序编译和运行请在开发和运行环境中进行。更多TPU-NNTC的教程请参考[算能官网](https://developer.sophgo.com/site/index.html?categoryActive=material)的《TPU-NNTC快速入门指南》和《TPU-NNTC开发参考手册》。



## 3 x86 PCIe平台的开发和运行环境搭建
如果您在x86平台安装了PCIe加速卡，开发环境与运行环境可以是统一的，您可以直接在宿主机上搭建开发和运行环境。

**注意：** mlir提供的docker环境用来编译模型的，不建议与运行环境混用，如果您需要在主机上搭建docker测试环境，请参考官网《LIBSOPHON使用手册.pdf》第6章-使用Docker搭建测试环境。

### 3.1 安装libsophon
从[算能官网](https://developer.sophgo.com/site/index.html?categoryActive=material)上下载符合[环境依赖](../README.md#环境依赖)的SOPHONSDK，解压后在libsophon_{date}_{time}文件夹下面有这几个文件:
* sophon-driver_x.y.z_amd64.deb
* sophon-libsophon_x.y.z_amd64.deb
* sophon-libsophon-dev_x.y.z_amd64.deb

其中：x.y.z表示版本号；sophon-driver包含了PCIe加速卡驱动；sophon-libsophon包含了运行时环境（库文件、工具等）；sophon-libsophon-dev包含了开发环境（头文件等）。如果只是在部署环境上安装，则不需要安装 sophon-libsophon-dev。
```bash
# 安装依赖库，只需要执行一次
sudo apt install dkms libncurses5
# 安装libsophon
sudo dpkg -i sophon-*amd64.deb
# 在终端执行如下命令，或者登出再登入当前用户后即可使用bm-smi等命令：
source /etc/profile
```

更多libsophon信息请参考《LIBSOPHON使用手册.pdf》。

### 3.2 安装sophon-ffmpeg和sophon-opencv
从[算能官网](https://developer.sophgo.com/site/index.html?categoryActive=material)上下载符合[环境依赖](../README.md#环境依赖)的SOPHONSDK，解压后在sophon-mw_{date}_{time}文件夹下面有这几个文件:
* sophon-mw-sophon-ffmpeg_x.y.z_amd64.deb
* sophon-mw-sophon-ffmpeg-dev_x.y.z_amd64.deb
* sophon-mw-sophon-opencv_x.y.z_amd64.deb
* sophon-mw-sophon-opencv-dev_x.y.z_amd64.deb

其中：x.y.z表示版本号；sophon-ffmpeg/sophon-opencv包含了ffmpeg/opencv运行时环境（库文件、工具等）；sophon-ffmpeg-dev/sophon-opencv-dev包含了开发环境（头文件、pkgconfig、cmake等）。如果只是在部署环境上安装，则不需要安装 sophon-ffmpeg-dev/sophon-opencv-dev。

sophon-mw-sophon-ffmpeg依赖sophon-libsophon包，而sophon-mw-sophon-opencv依赖sophon-mw-sophon-ffmpeg，因此在安装次序上必须
先安装libsophon, 然后sophon-mw-sophon-ffmpeg, 最后安装sophon-mw-sophon-opencv。

如果运行环境中使用的libstdc++库使用GCC5.1之前的旧版本ABI接口（典型的有CENTOS系统），请使用sophon-mw-sophon-opencv-abi0相关安装包。

```bash
# 安装sophon-ffmpeg
sudo dpkg -i sophon-mw-sophon-ffmpeg_*amd64.deb sophon-mw-sophon-ffmpeg-dev_*amd64.deb
# 安装sophon-opencv
sudo dpkg -i sophon-mw-sophon-opencv_*amd64.deb sophon-mw-sophon-opencv-dev_*amd64.deb
# 在终端执行如下命令，或者logout再login当前用户后即可使用安装的工具
source /etc/profile
```

更多sophon-mw信息请参考《MULTIMEDIA使用手册.pdf》、《MULTIMEDIA开发参考手册.pdf》。

### 3.3 编译安装sophon-sail
如果例程依赖sophon-sail则需要编译和安装sophon-sail，否则可跳过本章节。

目前dfss可以直接安装供**Python**使用的sail，您可以通过如下命令直接安装：
```bash
pip3 install dfss && python3 -m dfss --install sail
```

如果您无法通过以上命令安装，那么您需要自己编译，需从[算能官网](https://developer.sophgo.com/site/index.html?categoryActive=material)上下载符合[环境依赖](../README.md#环境依赖)的SOPHONSDK，解压后在sophon-sail_{date}_{time}文件夹里面有sophon-sail的压缩包，命名如sophon-sail_x.y.z.tar.gz，x.y.z表示版本号。
您可以打开sophon-sail压缩包里面提供的用户手册(命名为sophon-sail_zh.pdf)，参考编译安装指南章节，选择您需要的模式(C++/Python，PCIE MODE)进行安装。


## 4 SoC平台的开发和运行环境搭建
对于SoC平台，安装好SophonSDK(>=v22.09.02)后内部已经集成了相应的libsophon、sophon-opencv和sophon-ffmpeg运行库包，位于`/opt/sophon/`下，可直接用于运行环境。通常在x86主机上交叉编译程序，使之能够在SoC平台运行。SophonSDK固件刷新方法可参考[FAQ文档](./FAQ.md#12-soc模式下如何使用sd卡刷更新固件).

### 4.1 交叉编译环境搭建
需要在x86主机上使用SOPHONSDK搭建交叉编译环境，将程序所依赖的头文件和库文件打包至soc-sdk目录中。
1. 搭建交叉编译环境，这里提供两种方式：
    
    (1)通过apt安装交叉编译工具链：

    如果您的系统和目标SoC平台的libc版本相同，那么您可以使用如下命令安装：
    ```bash
    sudo apt-get install gcc-aarch64-linux-gnu g++-aarch64-linux-gnu
    ```
    卸载方法：
    ```bash
    sudo apt remove cpp-*-aarch64-linux-gnu
    ```

    如果您的环境不满足上述要求，建议使用第(2)种方法。

    (2)通过docker搭建交叉编译环境：
    
    **请注意，不要将下文的stream_dev镜像和用于模型编译的tpuc_dev镜像混用。**

    可以使用我们提供的docker镜像作为交叉编译环境，通过dfss下载：
    ```bash
    pip3 install dfss
    python3 -m dfss --url=open@sophgo.com:sophon-demo/common/docker/stream_dev.tar # ubuntu 20.04, gcc-9
    ```

    如果您的设备为BM1688/CV186AH，SDK版本1.9以上(可以使用bm_version命令查看版本)，那么您需要使用这个镜像:
    ```bash
    python3 -m dfss --url=open@sophgo.com:sophon-demo/common/docker/stream_dev_22.04.tar # ubuntu 22.04, gcc-11
    ```

    如果是首次使用Docker, 可执行下述命令进行安装和配置(仅首次执行):
    ```bash
    sudo apt install docker.io
    sudo systemctl start docker
    sudo systemctl enable docker
    sudo groupadd docker
    sudo usermod -aG docker $USER
    newgrp docker
    ```

    在下载好的镜像目录中加载镜像
    ```bash
    docker load -i stream_dev.tar
    ```
    可以通过`docker images`查看加载好的镜像，默认为stream_dev:latest

    创建容器
    ```bash
    docker run --privileged --name stream_dev -v $PWD:/workspace  -it stream_dev:latest
    # stream_dev只是举个名字的例子, 请指定成自己想要的容器的名字
    ```
    容器中的`workspace`目录会挂载到您运行`docker run`时所在的宿主机目录，您可以在此容器中编译项目

    > 注：该镜像来自[sophon-stream](https://github.com/sophgo/sophon-stream/blob/master/docs/HowToMake.md#使用开发镜像编译)。

2. 打包libsophon

    从[算能官网](https://developer.sophgo.com/site/index.html?categoryActive=material)上下载符合[环境依赖](../README.md#环境依赖)的SOPHONSDK，在sophon-img_{date}_{time}文件夹中包括libsophon_soc_x.y.z_aarch64.tar.gz，x.y.z表示版本号，并进行解压。

    ```bash
    # 创建依赖文件的根目录
    mkdir -p soc-sdk
    # 解压libsophon_soc_x.y.z_aarch64.tar.gz
    tar -zxf libsophon_soc_${x.y.z}_aarch64.tar.gz
    # 将相关的库目录和头文件目录拷贝到依赖文件根目录下
    cp -rf libsophon_soc_${x.y.z}_aarch64/opt/sophon/libsophon-${x.y.z}/lib ${soc-sdk}
    cp -rf libsophon_soc_${x.y.z}_aarch64/opt/sophon/libsophon-${x.y.z}/include ${soc-sdk}
    ```

3. 打包sophon-ffmpeg和sophon-opencv

    从[算能官网](https://developer.sophgo.com/site/index.html?categoryActive=material)上下载符合[环境依赖](../README.md#环境依赖)的SOPHONSDK，在sophon-mw_{date}_{time}文件夹中包括sophon-mw-soc_x.y.z_aarch64.tar.gz，x.y.z表示版本号，并进行解压，如果您使用BM1688 SOPHONSDK，“sophon-mw”这个名字或许需要替换成“sophon-media”。
    ```bash
    # 解压sophon-mw-soc_x.y.z_aarch64.tar.gz
    tar -zxf sophon-mw-soc_${x.y.z}_aarch64.tar.gz
    # 将ffmpeg和opencv的库目录和头文件目录拷贝到soc-sdk目录下
    cp -rf sophon-mw-soc_${x.y.z}_aarch64/opt/sophon/sophon-ffmpeg_${x.y.z}/lib ${soc-sdk}
    cp -rf sophon-mw-soc_${x.y.z}_aarch64/opt/sophon/sophon-ffmpeg_${x.y.z}/include ${soc-sdk}
    cp -rf sophon-mw-soc_${x.y.z}_aarch64/opt/sophon/sophon-opencv_${x.y.z}/lib ${soc-sdk}
    cp -rf sophon-mw-soc_${x.y.z}_aarch64/opt/sophon/sophon-opencv_${x.y.z}/include ${soc-sdk}
    ```

4. 如果您使用BM1688 & CV186AH v1.3以上版本SOPHONSDK，您还需要做这些操作：
    从sdk中获取sophon-img/bsp-debs/目录下的sophon-soc-libisp_${x.y.z}_arm64.deb，然后运行如下命令：
    ```
    dpkg -x sophon-soc-libisp_${x.y.z}_arm64.deb sophon-libisp
    cp -rf sophon-libisp/opt/sophon/sophon-soc-libisp_${x.y.z}/lib ${soc-sdk}
    ```

这里，交叉编译环境已经搭建完成，接下来可以使用打包好的soc-sdk编译需要在SoC平台上运行的程序。更多交叉编译信息请参考《LIBSOPHON使用手册.pdf》。

### 4.2 交叉编译安装sophon-sail
如果例程依赖sophon-sail则需要编译和安装sophon-sail，否则可跳过本章节。需要在x86主机上交叉编译sophon-sail，并在SoC平台上安装。

目前dfss可以直接安装供**Python**使用的sail，您可以通过如下命令直接安装：
```bash
pip3 install dfss && python3 -m dfss --install sail
```

如果您无法通过以上命令安装，那么您需要自己编译，从[算能官网](https://developer.sophgo.com/site/index.html?categoryActive=material)上下载符合[环境依赖](../README.md#环境依赖)的SOPHONSDK，进入sophon-sail_{date}_{time}文件夹，sophon-sail的发布包命名如sophon-sail_x.y.z.tar.gz，x.y.z表示版本号，您可以打开同级目录下的用户手册(命名为sophon-sail_zh.pdf或SOPHON-SAIL_zh.pdf)。
参考编译安装指南章节，选择您需要的模式(C++/Python，SoC MODE)进行安装，**注意需要选择包含ffmpeg和opencv的编译方式。**


在您按照教程将sophon-sail的库文件拷贝到目标soc上之后，您还需要设置以下环境变量：
```bash
echo 'export LD_LIBRARY_PATH=/opt/sophon/sophon-sail/lib/:$LD_LIBRARY_PATH' >> ~/.bashrc
source ~/.bashrc
```
## 5 arm PCIe平台的开发和运行环境搭建
如果您在arm平台安装了PCIe加速卡，开发环境与运行环境可以是统一的，您可以直接在宿主机上搭建开发和运行环境。
这里提供银河麒麟v10机器的环境安装方法，其他类型机器具体请参考官网开发手册。
### 5.1 安装libsophon
从[算能官网](https://developer.sophgo.com/site/index.html?categoryActive=material)上下载符合[环境依赖](../README.md#环境依赖)的SOPHONSDK，解压后在libsophon_{date}_{time}文件夹下面有安装包，
安装包由一个文件构成，其中“$arch”为当前机器的硬件架构，使用以下命令可以获取当前服务器的arch：
```
uname -m
```
通常x86_64机器对应的硬件架构为x86_64，arm64机器对应的硬件架构为aarch64：
```
libsophon_x.y.z_$arch.tar.gz，x.y.z表示版本号
```
可以通过如下步骤安装：

**注意：如果有旧版本，先参考下面的卸载方式步骤卸载旧版本。**
```
tar -xzvf libsophon_${x.y.z}_aarch64.tar.gz
sudo cp -r libsophon_${x.y.z}_aarch64/* /
sudo ln -s /opt/sophon/libsophon-${x.y.z} /opt/sophon/libsophon-current
```
接下来请先按照您所使用Linux发行版的要求搭建驱动编译环境，然后做如下操作：
```
sudo ln -s /opt/sophon/driver-${x.y.z}/$bin /lib/firmware/bm1684x_firmware.bin
sudo ln -s /opt/sophon/driver-${x.y.z}/$bin /lib/firmware/bm1684_ddr_firmware.bin
sudo ln -s /opt/sophon/driver-${x.y.z}/$bin /lib/firmware/bm1684_tcm_firmware.bin
cd /opt/sophon/driver-${x.y.z}
```
此处“$bin”是带有版本号的bin文件全名, 对于bm1684x板卡，为a53lite_pkg.bin，对于bm1684板卡，如bm1684_ddr.bin_v3.1.1-63a8614d-220906和bm1684_tcm.bin_v3.1.1-63a8614d-220906。

之后就可以编译驱动了（这里不依赖于dkms）：
```
sudo make SOC_MODE=0 PLATFORM=asic SYNC_API_INT_MODE=1 \
          TARGET_PROJECT=sg_pcie_device FW_SIMPLE=0 \
          PCIE_MODE_ENABLE_CPU=1
sudo cp ./bmsophon.ko /lib/modules/$(uname -r)/kernel/
sudo depmod
sudo modprobe bmsophon
```
最后是一些配置工作：

添加库和可执行文件路径：
```
sudo cp /opt/sophon/libsophon-current/data/libsophon.conf /etc/ld.so.conf.d/
sudo ldconfig
sudo cp /opt/sophon/libsophon-current/data/libsophon-bin-path.sh /etc/profile.d/
```
在终端执行如下命令，或者登出再登入当前用户后即可使用bm-smi等命令：
```
source /etc/profile
```
添加cmake config文件：
```
sudo mkdir -p /usr/lib/cmake/libsophon
sudo cp /opt/sophon/libsophon-current/data/libsophon-config.cmake /usr/lib/cmake/libsophon/
```
卸载方式：
```
sudo rm -f /etc/ld.so.conf.d/libsophon.conf
sudo ldconfig
sudo rm -f /etc/profile.d/libsophon-bin-path.sh
sudo rm -rf /usr/lib/cmake/libsophon
sudo rmmod bmsophon
sudo rm -f /lib/modules/$(uname -r)/kernel/bmsophon.ko
sudo depmod
sudo rm -f /lib/firmware/bm1684x_firmware.bin
sudo rm -f /lib/firmware/bm1684_ddr_firmware.bin
sudo rm -f /lib/firmware/bm1684_tcm_firmware.bin
sudo rm -f /opt/sophon/libsophon-current
sudo rm -rf /opt/sophon/libsophon-0.4.6
sudo rm -rf /opt/sophon/driver-0.4.6
```
其他平台机器请参考《LIBSOPHON使用手册.pdf》

### 5.2 安装sophon-ffmpeg和sophon-opencv
从[算能官网](https://developer.sophgo.com/site/index.html?categoryActive=material)上下载符合[环境依赖](../README.md#环境依赖)的SOPHONSDK，解压后在sophon-mw_{date}_{time}文件夹下面有安装包，
安装包由一个文件构成：
```
sophon-mw_x.y.z_aarch64.tar.gz，x.y.z表示版本号
```
可以通过如下步骤安装：

先按照《LIBSOPHON使用手册》安装好libsophon包，然后，
```
tar -xzvf sophon-mw_${x.y.z}_aarch64.tar.gz
sudo cp -r sophon-mw_${x.y.z}_aarch64/* /
sudo ln -s /opt/sophon/sophon-ffmpeg_${x.y.z} /opt/sophon/sophon-ffmpeg-latest
sudo ln -s /opt/sophon/sophon-opencv_${x.y.z} /opt/sophon/sophon-opencv-latest
sudo ln -s /opt/sophon/sophon-sample_${x.y.z} /opt/sophon/sophon-sample-latest
sudo sed -i "s/usr\/local/opt\/sophon\/sophon-ffmpeg-latest/g" /opt/sophon/sophon-ffmpeg-latest/lib/pkgconfig/*.pc
sudo sed -i "s/^prefix=.*$/prefix=\/opt\/sophon\/sophon-opencv-latest/g" /opt/sophon/sophon-opencv-latest/lib/pkgconfig/opencv4.pc
```
最后，**安装bz2 libc6 libgcc依赖库**（这部分需要根据操作系统不同，选择对应的安装包，这里不统一介绍）
然后是一些配置工作：

添加库和可执行文件路径：
```
sudo cp /opt/sophon/sophon-ffmpeg-latest/data/01_sophon-ffmpeg.conf /etc/ld.so.conf.d/
sudo cp /opt/sophon/sophon-opencv-latest/data/02_sophon-opencv.conf /etc/ld.so.conf.d/
sudo ldconfig
sudo cp /opt/sophon/sophon-ffmpeg-latest/data/sophon-ffmpeg-autoconf.sh /etc/profile.d/
sudo cp /opt/sophon/sophon-opencv-latest/data/sophon-opencv-autoconf.sh /etc/profile.d/
sudo cp /opt/sophon/sophon-sample-latest/data/sophon-sample-autoconf.sh /etc/profile.d/
source /etc/profile
```
其他平台机器请参考《MULTIMEDIA使用手册.pdf》、《MULTIMEDIA开发参考手册.pdf》。

### 5.3 编译安装sophon-sail
如果例程依赖sophon-sail则需要编译和安装sophon-sail，否则可跳过本章节。

需从[算能官网](https://developer.sophgo.com/site/index.html?categoryActive=material)上下载符合[环境依赖](../README.md#环境依赖)的SOPHONSDK，解压后在sophon-sail_{date}_{time}文件夹里面有sophon-sail的压缩包，命名如sophon-sail_x.y.z.tar.gz，x.y.z表示版本号。
您可以打开sophon-sail压缩包里面提供的用户手册(命名为sophon-sail_zh.pdf)，参考编译安装指南章节，选择您需要的模式(C++/Python, ARM PCIE MODE)进行安装。

## 6 riscv PCIe平台的开发和运行环境搭建
如果您在riscv平台安装了PCIe加速卡，开发环境与运行环境可以是统一的，您可以直接在宿主机上搭建开发和运行环境。
这里提供SG2042服务器的环境安装方法，其他类型机器具体请参考官网开发手册。

### 6.1 安装libsophon
从[算能官网](https://developer.sophgo.com/site/index.html?categoryActive=material)上下载符合[环境依赖](../README.md#环境依赖)的SOPHONSDK，解压后在libsophon_{date}_{time}文件夹下面有安装包，
安装包由以下3个文件构成：
```bash
sophon-libsophon-dev-{x.y.z}.riscv64.rpm
sophon-libsophon-{x.y.z}.riscv64.rpm
sophon-driver-{x.y.z}.riscv64.rpm
```
安装前需要通过后面“卸载方式”中的步骤卸载旧版本libsophon，可以通过如下步骤安装：
```bash
安装依赖库，只需要执行一次:
sudo yum install -y epel-release
sudo yum install -y dkms
sudo yum install -y ncurses*
安装libsophon：
sudo rpm -ivh sophon-driver-{x.y.z}.riscv64.rpm
sudo rpm -ivh sophon-libsophon-{x.y.z}.riscv64.rpm
sudo rpm -ivh --force sophon-libsophon-dev-{x.y.z}.riscv64.rpm
在终端执行如下命令，或者登出再登入当前用户后即可使用bm-smi等命令：
source /etc/profile
```
卸载方式：
```bash
sudo rpm -e sophon-driver
sudo rpm -e sophon-libsophon-dev
sudo rpm -e sophon-libsophon
```
其他平台机器请参考《LIBSOPHON使用手册.pdf》。

### 6.2 安装sophon-ffmpeg和sophon-opencv
从[算能官网](https://developer.sophgo.com/site/index.html?categoryActive=material)上下载符合[环境依赖](../README.md#环境依赖)的SOPHONSDK，解压后在sophon-mw_{date}_{time}文件夹下面有安装包，

sophon-mw安装包由四个文件构成：
```bash
sophon-mw-sophon-ffmpeg_{x.y.z}_riscv64.rpm
sophon-mw-sophon-ffmpeg-dev_{x.y.z}_riscv64.rpm
sophon-mw-sophon-opencv_{x.y.z}_riscv64.rpm
sophon-mw-sophon-opencv-dev_{x.y.z}_riscv64.rpm
```
其中：

1. sophon-ffmpeg/sophon-opencv包含了ffmpeg/opencv运行时环境（库文件、工具等）；sophon-ffmpeg-dev/sophon-opencv-dev包含了开发环境（头文件、pkgconfig、cmake等）。如果只是在部署环境上安装，则不需要安装sophon-ffmpeg-dev/sophon-opencv-dev。

2. sophon-mw-sophon-ffmpeg依赖sophon-libsophon包，而sophon-mw-sophon-opencv依赖sophon-mw-sophon-ffmpeg，因此在安装次序上必须先安装libsophon,然后sophon-mw-sophon-ffmpeg,最后安装sophon-mw-sophon-opencv。

安装之前请参考"卸载方式"卸载老版本，安装步骤如下：
```bash
sudo rpm -ivh sophon-mw-sophon-ffmpeg_{x.y.z}_riscv64.rpm sophon-mw-sophon-ffmpeg-dev_{x.y.z}_riscv64.rpm
sudo rpm -ivh sophon-mw-sophon-opencv_{x.y.z}_riscv64.rpm sophon-mw-sophon-opencv-dev_{x.y.z}_riscv64.rpm
在终端执行如下命令，或者logout再login当前用户后即可使用安装的工具：
source /etc/profile
```

卸载方式：
```bash
sudo rpm -e sophon-mw-sophon-opencv-dev
sudo rpm -e sophon-mw-sophon-opencv
sudo rpm -e sophon-mw-sophon-ffmpeg-dev
sudo rpm -e sophon-mw-sophon-ffmpeg
```

其他平台机器请参考《MULTIMEDIA使用手册.pdf》、《MULTIMEDIA开发参考手册.pdf》。

### 6.3 编译安装sophon-sail
如果例程依赖sophon-sail则需要编译和安装sophon-sail，否则可跳过本章节。

需从[算能官网](https://developer.sophgo.com/site/index.html?categoryActive=material)上下载符合[环境依赖](../README.md#环境依赖)的SOPHONSDK，解压后在sophon-sail_{date}_{time}文件夹里面有sophon-sail的压缩包，命名如sophon-sail_x.y.z.tar.gz，x.y.z表示版本号。
您可以打开sophon-sail压缩包里面提供的用户手册(命名为sophon-sail_zh.pdf)，参考编译安装指南章节，选择您需要的模式(C++/Python，RISCV PCIE MODE)进行安装。

### 6.4 安装构建工具
如果您使用的是fedora系统，没有默认安装构建工具的话容易导致pip安装第三方包时失败，因为大部分第三方包在riscv上安装需要重新编译，您可以通过以下命令安装构建工具，防止出现pip安装失败的情况。

```bash
sudo dnf install ninja-build
sudo dnf groupinstall "Development Tools"
sudo dnf install cmake automake autoconf libtool
sudo dnf install openssl-devel
pip3 install opencv-python-headless #尝试使用pip安装第三方包。
```

### 6.5 注意事项
如果您在RISC-V平台上运行需要torch的demo，需要自行编译安装2.4.0版本的torch。如果demo依赖torchaudio或torchvision，则需要编译安装与torch适配的版本，其中torchaudio版本为2.4.0，torchvision版本为0.19.0。
另外您可以通过我们预构建好的wheel文件直接安装这些依赖，通过dfss下载：

```bash
pip3 install dfss -i https://pypi.tuna.tsinghua.edu.cn/simple --upgrade
python3 -m dfss --url=open@sophgo.com:/sophon-demo/RISCV_Packages/wheels.tar.gz
tar xvf wheels.tar.gz
#根据对应例程的requirements.txt要求选择安装，例如：
pip3 install -r requirements.txt --no-index --find-links=wheels/
```


# 文件: docs/FAQ.md

---

[简体中文](./FAQ.md) | [English](./FAQ_EN.md)

# 常见问题解答

## 目录

* [1 环境安装相关问题](#1-环境安装相关问题)
* [2 模型导出相关问题](#2-模型导出相关问题)
* [3 模型编译和量化相关问题](#3-模型编译和量化相关问题)
* [4 算法移植相关问题](#4-算法移植相关问题)
* [5 精度测试相关问题](#5-精度测试相关问题)
* [6 性能测试相关问题](#6-性能测试相关问题)
* [7 其他问题](#7-其他问题)

我们列出了一些用户和开发者在开发过程中会遇到的常见问题以及对应的解决方案，如果您发现了任何问题，请随时联系我们或创建相关issue，非常欢迎您提出的任何问题或解决方案。

## 1 环境安装相关问题
### 1.1 sophon-demo涉及的开发和运行环境安装可以参考[相关文档](./Environment_Install_Guide.md)。

### 1.2 SoC模式下如何使用SD卡刷更新固件
下载解压v22.09.02以后的SophonSDK，找到sophon-img文件夹下的sdcard刷机包，并参考[相关文档](https://doc.sophgo.com/docs/3.0.0/docs_latest_release/faq/html/devices/SOC/soc_firmware_update.html#id6)刷新固件。

### 1.3 SE7安装python3.10
由于新版本transformer需要python3.10才能支持，SE7上默认的python版本是3.8，这里提供一个在SE7安装python3.10的方法供用户参考：
```bash
sudo apt update
sudo apt install build-essential checkinstall zlib1g-dev libncurses5-dev libncursesw5-dev libsqlite3-dev liblzma-dev tk-dev uuid-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev libbz2-dev wget curl -y
wget https://www.python.org/ftp/python/3.10.12/Python-3.10.12.tgz 
tar -xaf Python-3.10.12.tgz
cd Python-3.10.12/
ls
./configure --enable-optimizations --enable-shared --prefix=/usr 
make -j4
sudo make altinstall
cd /data
python3.10 -m venv py310env
source py310env/bin/activate
```

## 2 模型导出相关问题

### 2.1 Pytorch模型如何进行jit.trace
**如果您使用TPU-NNTC来编译BModel，注意在TPU-NNTC支持的Pytorch版本`1.8.0+cpu`的环境下进行torchscript模型导出。**
部分开源仓库提供了模型导出的脚本，如果没有则需要参考[相关文档](./torch.jit.trace_Guide.md)或者[Pytorch官方文档](https://pytorch.org/docs/stable/jit.html)编写jit.trace脚本。jit.trace通常是在模型开发(torch)环境中进行，不需要安装SophonSDK。
- YOLOv5模型jit.trace的方法可参考[相关文档](../sample/YOLOv5/docs/YOLOv5_Export_Guide.md)

### 2.2 ONNX模型导出过程使用的算子集
如果pytorch版本过低，可能无法支持高版本ONNX算子集，导致ONNX输出失败。
需要根据当前环境使用pytorch版本，设置支持的ONNX算子集版本。以设置使用ONNX算子集版本13为例，设置方式如下：
```python
torch.onnx.export(
    ...
    opset_version=13,
    ...
)
```

## 3 模型编译和量化相关问题
### 3.1 使用TPU-NNTC量化的相关问题
详见[相关文档](./Calibration_Guide.md)。

### 3.2 使用TPU-NNTC编译大模型(如resnet260)耗时长
resnet260编译会这么耗时有可能是二次搜索时间太长的原因。我们在做编译优化的时候对已经做完初次layergroup后又结果做一次再分组搜索，这个搜索结果对于resnet这类网络性能收益不大，反倒会增加编译优化的时间。为了解决这类模型问题，我们增加了二次搜索的上限值，通过以下环境变量来控制二次搜索的上限：
```bash
export BMCOMPILER_GROUP_SEARCH_COUNT=1
```

## 4 算法移植相关问题
### 4.1 Sophon OpenCV和原生OpenCV、BMCV的关系
Sophon OpenCV继承和优化了原生OpenCV，修改了原生mat，增加了设备内存，部分接口（如imread，videocapture，videowriter，resize，convert等）增加了硬件加速支持，保持了跟原生OpenCV操作的接口一致性，修改内容具体信息请查看[相关文档](https://doc.sophgo.com/sdk-docs/v22.12.01/docs_latest_release/docs/sophon-mw/guide/html/1_guide.html)。

BMCV是我们提供的一套基于硬件VPP和TPU进行图像处理以及部分数学运算的加速库，是C接口的库。在我们修改的Sophon OpenCV底层，相关操作的硬件加速调用的也是BMCV的接口。

Sophon OpenCV使用TPU中的硬件加速单元进行解码，相比原生OpenCV采用了不同的upsample算法，解码和前后处理的方式与原生的OpenCV存在一定差异，可能影响最终的预测结果，但通常不会对鲁棒性好的模型造成明显影响。

### 4.2 基于OpenCV的Python例程如何调用Sophon OpenCV进行加速
使用v22.09.02以后的SophonSDK，不管是PCIe，还是SoC模式，基于OpenCV的Python例程默认都使用安装的原生OpenCV，可以通过设置环境变量使用Sophon OpenCV：
```bash
export PYTHONPATH=$PYTHONPATH:/opt/sophon/sophon-opencv-latest/opencv-python/
```
注意使用sophon-opencv可能会导致推理结果的差异。

### 4.3 基于OpenCV的C++例程使用Sophon OpenCV还是原生OpenCV
基于OpenCV的C++例程在CMakeLists.txt中设置了OpenCV_DIR路径，链接Sophon OpenCV的相关头文件和库文件。如果需要调用原生OpenCV，需自行安装原生OpenCV，并修改相关链接路径。

### 4.4 C++例程使用ff_decode解码视频提示“vid reset unlock flock failed”，但不影响正常运行
这是由于缓存没有及时清除导致的，不影响推理结果。可以通过运行如下命令解决：
```bash
sudo rm /tmp/vid_*
```

### 4.5 bm_free_device失败
可能的原因：
1. 这块device_mem没有被分配过内存，或者已经被释放过。

2. 如果一个bm_image的内存是attach过来的，注意只调用detach函数就好，不要调用bm_image_free_contiguous_mem释放它，否则后续那块device_mem会释放失败。

## 5 精度测试相关问题
### 5.1 FP32 BModel的推理结果与原模型的推理结果不一致
在前后处理与原算法对齐的前提下，FP32 BModel的精度与原模型的最大误差通常在0.001以下，不会对最终的预测结果造成影响。FP32 BModel精度对齐的方法可以参考[相关文档](./FP32BModel_Precise_Alignment.md)。

## 6 性能测试相关问题
### 6.1 部分FP32 BModel的BM1684X性能低于BM1684
BM1684X的local memory相比BM1684少了一半，参数量较大的模型有可能放不下，导致gdma访问ddr次数大量增加。

### 6.2 基于opencv-python的例程int8bmodel推理时间没有比fp32bmodel快
int8bmodel的输入层数据类型是int8，scale不等1，基于opencv-python的例程以numpy.array为输入，推理接口内部需要进行乘scale操作，而fp32bmodel输入层的scale是1，推理接口内部不需要进行乘scale操作，这部分时间可能会抵掉模型推理优化的时间。可以在代码中添加`sail.set_print_flag(1)`，打印推理接口的具体耗时。  
如果要使用opencv-python例程进行部署，建议将int8bmodel的输入、输出层保留为浮点计算。

### 6.3 sophon-demo能否用于性能压测
不建议。sophon-demo提供一系列主流算法的移植例程，用户可以根据sophon-demo进行模型算法移植和精度测试。但sophon-demo的前处理/推理/后处理是串行的，即使开多个进程也很难将TPU的性能充分发挥出来。[sophon-stream](https://github.com/sophgo/sophon-stream)是一套支持多路数据流并发处理的流水线框架，可以充分发挥算丰硬件的编解码能力及深度学习算法的推理能力，从而获得较高的性能。因此建议使用sophon-stream进行性能压测。

### 6.4 测试性能相比README下降
如果性能下降超过10%，需要确认产品型号，sophon-demo的各个例程都是基于标准版的产品（如SE-16）来测试的，如果您使用的是低配版产品（如SE5-8），性能下降是正常的，SE5-16的int8算力是17.6TOPS，SE5-8是10.6TOPS，所以大概会有2/5的性能损失。
如果您使用的产品也是标准版，也遇到了性能下降的问题，可以将问题反馈给算能工作人员或者在github上创建issue。

### 6.5 性能测试表格的作用
sophon-demo提供的性能测试表格一般包含解码、前处理、推理、后处理这四个部分，业界对于算法部署也大多是这么划分的。对于算能的AI处理器而言，这四个部分都是可以并发的，因为它们各自依赖的器件不同，比如解码依赖VPU、前处理依赖VPP、推理依赖TPU、后处理则依赖中央处理器，这些元器件是可以并发工作且不会受到各自影响的。sophon-demo提供的性能测试表格将这些信息列出来，可以直观地分析出当前算法的瓶颈以及它能达到的理论最高每秒处理次数。

## 7 其他问题
### 7.1 编译时出现`Unkown CMake command "add_compile_definitions".`
这是你的cmake没有add_compile_definition这个函数，可以修改成add_definitions，或者升级cmake到3.12之后。

### 7.2 有些图片的数据重叠到一起，有的图片框上面没数据，有些图片没有框
图片和视频测试结果存在少数的漏检、误检，这是正常的，sophon-demo的例程只需要保证移植后的模型和源模型的精度可以对齐就行了，判断模型效果应当以精度指标测试为准。

### 7.3 程序运行时出现`bm_ion_alloc failed`等报错
首先排查程序是否出现设备内存泄漏，代码中是否存在分配设备内存没有及时释放的问题。如果确认没有内存泄漏，那么可能是由于某个heap太小导致的，可以观察一下设备内存各个heap的使用情况：
```bash
#在SE5/SE7系列上使用以下命令查看：
sudo cat /sys/kernel/debug/ion/bm_vpu_heap_dump/summary
sudo cat /sys/kernel/debug/ion/bm_vpp_heap_dump/summary
sudo cat /sys/kernel/debug/ion/bm_npu_heap_dump/summary
#在SE9上使用以下命令查看：
sudo cat /sys/kernel/debug/ion/cvi_vpp_heap_dump/summary
sudo cat /sys/kernel/debug/ion/cvi_npu_heap_dump/summary
#会打印类似这种信息
Summary:
[1] vpp heap size:4294967296 bytes, used:144646144 bytes
usage rate:4%, memory usage peak 144646144 bytes #memory usage peak是该heap的内存使用峰值
```
如果某个heap的`memory usage peak`已经接近`heap size`了，那么可以考虑用这个工具调整设备内存各个heap的大小：[sophon内存修改工具](https://doc.sophgo.com/sdk-docs/v23.07.01/docs_latest_release/docs/SophonSDK_doc/zh/html/appendix/2_mem_edit_tools.html)。

### 7.4 刚开机首次执行某个函数慢(比如解码)，重启进程再次运行程序，时间正常

可能是因为文件还没有缓存到内存中导致的刚开始比较慢。
可以做个验证，如果不重启可复现，就说明是刚开机运行程序比较慢，是文件还没缓存的原因，步骤如下：
    
1. 上电后执行程序，第一次执行慢，第二次执行正常。

2. 之后进入root用户清除cache，运行命令`echo 3 > /proc/sys/vm/drop_caches`。
    
3. 再次执行程序，运行慢，即可确定是cache导致的。

### 7.5 运行下载脚本`scripts/download.sh`报错

可能有以下原因：

1. 网络环境不好或者有防火墙。

2. 一般下载脚本会最先安装dfss，如果是非ubuntu系统出现dfss安装失败，中间可能会打印类似`ERROR: Failed building wheel for cff`这种报错，这是因为缺少libffi-devel这个依赖，可以通过以下命令安装：

    ```bash
    sudo yum install libffi-devel
    #然后重新运行下载脚本
    ```
    
### 7.6 pycocotools等包通过pip安装失败，报错中含有`RequiredDependencyException: jpeg`

该问题可能会发生在Risc-V架构的机器上，如SG2042，可以通过以下方法解决：
```bash
sudo dnf install libjpeg-turbo-devel #如果是fedora系统
sudo apt install libjpeg-dev #如果是ubuntu系统
```

### 7.7 解码超过一定路数开始报错，但是设备内存没有满

很可能是因为fd数量不足问题，使用ulimit -n 65536解决，如果还是不够可以调地更大，注意，ulimit -n只在当前终端生效。

# 文件: docs/FAQ_EN.md

---

[简体中文](./FAQ.md) | [English](./FAQ_EN.md)

# FAQ

## Directory

* [1 Environment installation related Problems](#1-environment-installation-related-problems)
* [2 Model derived Problems](#2-model-derived-related-problems)
* [3 Issues related to Model compilation and Quantization](#3-issues-related-to-model-compilation-and-quantization)
* [4 Algorithm migration related problems](#4-algorithm-migration-related-problems)
* [5 Accuracy test related Problems](#5-accuracy-test-related-issues)
* [6 Performance Test Related Issues](#6-performance-test-related-issues)
* [7 Other questions](#7-other-questions)

We have listed some common problems that users and developers will encounter during the development process and corresponding solutions. If you find any problems, please feel free to contact us or create a related issue. Any questions or solutions you put forward are very welcomed.


## 1 Environment installation related problems
### 1.1 The installation of development and running environments of sophon-demo can be found in [related documentation](./Environment_Install_Guide_EN.md).

### 1.2 How Do I Use an SD Card to update Firmware in SoC Mode
Download and decompress SophonSDK after v22.09.02, find sdcard swiping package in sophon-img folder, refer to [relative document](https://doc.sophgo.com/docs/3.0.0/docs_latest_release/faq/html/devices/SOC/soc_firmware_update.html#id6) to refresh the firmware.

### 1.3 Install python3.10 for SE7
Since the new version of the transformer requires Python 3.10, and the default Python version on SE7 is 3.8, here we provide a method for installing Python 3.10 on SE7 for users' reference:
```bash
sudo apt update
sudo apt install build-essential checkinstall zlib1g-dev libncurses5-dev libncursesw5-dev libsqlite3-dev liblzma-dev tk-dev uuid-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev libbz2-dev wget curl -y
wget https://www.python.org/ftp/python/3.10.12/Python-3.10.12.tgz 
tar -xaf Python-3.10.12.tgz
cd Python-3.10.12/
ls
./configure --enable-optimizations --enable-shared --prefix=/usr 
make -j4
sudo make altinstall
cd /data
python3.10 -m venv py310env
source py310env/bin/activate
```

## 2 Model derived related problems
### 2.1 How to jit.trace the Pytorch Model
**You should use the torch vision of`1.8.0+cpu`to avoid model compilation failures due to the pytorch version.** Some open source repositories provide scripts for model exports. If not provided, you need to learn from   [relative document](./torch.jit.trace_Guide_EN.md) or [Pytorch official document](https://pytorch.org/docs/stable/jit.html) and write 'jit.trace' script. 'jit.trace' is usually done in torch environment and does not require a SophonSDK installation.
- 'jit.trace' method of YOLOv5 model is available in [related documentation](../sample/YOLOv5/docs/YOLOv5_Export_Guide_EN.md)

## 3 Issues related to model compilation and quantization
### 3.1 Problems related to quantization using TPU-NNTC
For details, see [documentation](./Calibration_Guide_EN.md).

### 3.2 Long time to compile large models (such as resnet260) using TPU-NNTC
It is possible that the resnet260 compilation took so long because the second search took too long. When compiling and optimizing, we conducted a group search on the results after the initial layergroup. This search result did not bring much benefit to the network performance like resnet, but would increase the time of compiling and optimizing. In order to solve such model problems, we increase the upper limit of secondary search and control the upper limit of secondary search through the following environment variables:

```bash
export BMCOMPILER_GROUP_SEARCH_COUNT=1
```

## 4 Algorithm migration related problems
### 4.1 Relationship between Sophon OpenCV and native OpenCV and BMCV
Sophon OpenCV inherits and optimizes native OpenCV, modifies native mat, increases device memory, and adds hardware acceleration support for some interfaces (such as imread, videocapture, videowriter, resize, convert, etc.), keeping the interface consistent with native OpenCV operations. The specific information of modifying please see the [relevant documentation](https://doc.sophgo.com/sdk-docs/v22.12.01/docs_latest_release/docs/sophon-mw/guide/html/1_guide.html).

BMCV is a set of acceleration library provided by us, based on hardware VPP and TPU for image processing and some mathematical operations. It is a library of C interface. At the bottom of our modified Sophon OpenCV, hardware-accelerated operations use the interface of BMCV as well.

Compared with native OpenCV, Sophon OpenCV adopts different upsample algorithms for decoding using hardware-accelerated units in TPU. The decoding and pre-processing methods of Sophon OpenCV are different from those of native OpenCV to some degree, which may affect the final prediction results, but usually does not have a significant impact on robust models.

### 4.2 How do OpenCV-based Python demos call Sophon OpenCV for acceleration
Using SophonSDK after v22.09.02, whether in PCIe or SoC mode, Python demos based on OpenCV use the installed native OpenCV by default. Sophon OpenCV can be used by setting environment variables:
```bash
export PYTHONPATH=$PYTHONPATH:/opt/sophon/sophon-opencv-latest/opencv-python/
```
Note that the use of sophon-opencv may lead to differences in reasoning results.

### 4.3 OpenCV-based C++ demos using Sophon OpenCV or native OpenCV
The OpenCV-based C++ demo sets the OpenCV_DIR path in CMakeLists.txt, linking Sophon OpenCV's relevant headers and library files. To invoke native OpenCV, install native OpenCV and modify the link path.

### 4.4 The C++ demo decoding video using ff_decode displays "vid reset unlock flock failed", but normal operation is not affected
This is because the cache is not cleared in time, and the inference result is not affected. To solve the problem, run the following command:
```bash
sudo rm /tmp/vid_*
```
### 4.5 bm_free_device failed
May be caused by:
1. This device_mem has not been allocated memory, or has been freed.

2. If the memory of a bm_image is attached, it is better to call only the detach function, not to call the bm_image_free_contiguous_mem to release it, otherwise the subsequent device_mem will fail to be released.

## 5 Accuracy test related issues
### 5.1 The inference result of FP32 BModel is inconsistent with that of the original model
Under the premise that the pre and post processing is aligned with the original algorithm, the maximum error between the accuracy of FP32 BModel and the original model is usually less than 0.001, which will not affect the final prediction results. Refer to [related documentation](./FP32BModel_Precise_Alignment_EN.md) for precision alignment of the FP32BModel.

## 6 Performance test related issues
### 6.1 Part of FP32 BModel BM1684X performance is lower than BM1684
The local memory of the BM1684X is half of that of the BM1684. The model with a large number of parameters may not be able to fit, which results in a large increase in the number of accessing ddr by gdma.

### 6.2 Inference time of int8bmodel demo based on opencv-python is not faster than fp32bmodel
The input data type of int8bmodel is int8 with a scale factor that is not equal to 1. The opencv-python demo based on numpy.array as input needs to perform a multiplication operation with the scale factor inside the inference interface. On the other hand, the scale factor of the input layer of fp32bmodel is 1, and there is no need to perform multiplication with the scale factor inside the inference interface. This part of the time may offset the time saved by model inference optimization. You can add `sail.set_print_flag(1)` in the code to print the specific inference time of the interface.

If you want to use the opencv-python demo for deployment, it is recommended to keep the input and output layers of int8bmodel as floating-point calculations.

### 6.3 Can sophon-demo be used for performance testing?
It is not recommended. Sophon-demo provides a series of transplant demos for mainstream algorithms, and users can perform model algorithm transplantation and accuracy testing based on sophon-demo. However, the preprocessing/inference/post-processing of sophon-demo is serial, and even if multiple processes are opened, it is difficult to fully utilize the performance of TPU.
[sophon-stream](https://github.com/sophgo/sophon-stream) is a framework which supports concurrent processing of multiple video streams, it can fully utilize the decoding/encoding/inference capabilities that SOPHON hardware provide, so that it will achieve higher performance. We recommend you use sophon-stream to do performance stress testing.
是一套支持多路数据流并发处理的流水线框架，可以充分发挥算丰硬件的编解码能力及深度学习算法的推理能力，从而获得较高的性能。因此建议使用sophon-stream进行性能压测。

### 6.4 Performance testing results are lower than README
If the performance drops more than 10% compared to the README, you need to confirm the product model. The sophon-demo demos are all based on standard products (such as SE-16) for testing. If you are using a low-end product (such as SE5-8), performance degradation is normal. The int8 computing power of SE5-16 is 17.6 TOPS, while that of SE5-8 is 10.6 TOPS, so there may be a loss of 2/5 of the performance.

If you are also using a standard product and encounter performance degradation issues, you can report the issue to the Sophon team or create an issue on GitHub.

### 6.5 What does the performance test table do?
The performance test table provided by sophon-demo generally includes four parts: decode\preprocess\inference\postprocess. This is how algorithm deployment is mostly divided in the industry. For Sophgo AI processors, these four parts can all be concurrent because they each rely on different devices. For example, decode relies on VPU, preprocess relies on VPP, inference relies on TPU, and postprocess relies on the central processor. These components can work concurrently without being affected individually. The performance test table provided by sophon-demo lists this information and can intuitively analyze the bottlenecks of the current algorithm and the theoretical maximum number of processing times per second it can achieve.


## 7 Other questions
### 7.1 `Unkown CMake command "add_compile_definitions".` when compiling C++ programs.
This is because your cmake do not have `add_compile_definitions` function, you can change it to `add_definitions` or upgrade your cmake to 3.12 or higher.

### 7.2 Some images have data overlapped, some have no data on the frame, and some images have no frame
It is normal for there to be a small number of missed and false detections in the image and video test results. Our samples only needs to ensure that the accuracy of the transplanted model and the source model can be aligned, and the accuracy index test should prevail to judge the model effect.

### 7.3 `bm_ion_alloc failed` occured during program running.
First, check if there is any device memory leak, such as alloc a piece of device memory but do not release after its life cycle.
If you can confirm no device memory leak happened, then this issue is probably because a device memory heap being too small, use these commands to see each heap's memory usage.
```bash
#on SE5/SE7 series use:
sudo cat /sys/kernel/debug/ion/bm_vpu_heap_dump/summary
sudo cat /sys/kernel/debug/ion/bm_vpp_heap_dump/summary
sudo cat /sys/kernel/debug/ion/bm_npu_heap_dump/summary
#on SE5/SE7 series use:
sudo cat /sys/kernel/debug/ion/cvi_vpp_heap_dump/summary
sudo cat /sys/kernel/debug/ion/cvi_npu_heap_dump/summary
#such command will print
Summary:
[1] vpp heap size:4294967296 bytes, used:144646144 bytes
usage rate:4%, memory usage peak 144646144 bytes #memory usage peak is the highest usage since startup
```
if a heap's `memory usage peak` is very closed to its `heap size`, you can use this tool to manually set each heap's size: [sophon memedit tool](https://doc.sophgo.com/sdk-docs/v23.07.01/docs_latest_release/docs/SophonSDK_doc/zh/html/appendix/2_mem_edit_tools.html).

### 7.4 The first time a function is executed slowly (such as decoding) just after booting, restart the process and run the program again, the time is normal

It may be that the file has not been cached in memory, which is slow at first.
You can do a verification, if you don't restart it can be reproduced, it means that the program is slow to run just now, and the file has not been cached, the steps are as follows:
    
1. Execute the program after powering on, the first execution is slow, and the second execution is normal.

2. Then go to the root user to clear the cache and run the command `echo 3 > /proc/sys/vm/drop_caches`.
    
3. If the program is slow to run again, it can be determined that it is caused by cache.

### 7.5 `scripts/download.sh` failed

May be caused by:

1. The network environment is not good or there is a firewall.

2. If the dfss installation fails on a non-ubuntu system, an error like `ERROR: Failed building wheel for cff` may be printed in the middle, which is due to the lack of libffi-devel dependency, which can be installed with the following command:

    ```bash
    sudo yum install libffi-devel
    #then re-execute script/download.sh
    ```
    
### 7.6 pip install pycocotools failed，error contains `RequiredDependencyException: jpeg`

This problem may occurs on Risc-V arch marchine, like SG2042, it can be solved by:
```bash
sudo dnf install libjpeg-turbo-devel #fedora
sudo apt install libjpeg-dev #ubuntu
```

### 7.7 Error occurs when the number of decoding channels exceeds a certain number, but the device memory is not full

It is likely that the problem of insufficient number of fds is solved, use `ulimit -n 65536` to solve it, if it is still not enough, you can adjust it to a larger one, note that `ulimit -n` only takes effect in the current terminal.

# 文件: docs/FP32BModel_Precise_Alignment.md

---

[简体中文](./FP32BModel_Precise_Alignment.md) | [English](./FP32BModel_Precise_Alignment_EN.md)

# FP32 BModel精度对齐参考方法(Python)

## 1 前言

使用算丰平台部署深度学习模型时，我们通常需要进行模型和算法移植，并进行精度测试。如果原框架的预测结果与移植后的预测结果不一致，我们经常需要排查产生误差的原因。本文主要以Python接口为例，介绍产生精度误差的常见原因和误差排查的参考方法。

## 2 注意事项

关于精度对齐，有几点需要说明：

- 原始模型转FP32 BModel存在一定的精度误差，如果开启精度对比(cmp=True)，且精度对比通过，FP32 BModel的最大误差通常在0.001以下，不会对最终的预测结果造成影响。
- Sophon OpenCV使用TPU中的硬件加速单元进行解码，相比原生OpenCV采用了不同的upsample算法。若移植的Python代码中使用Sophon OpenCV或SAIL进行解码和前后处理，解码和前后处理的方式与原生的OpenCV存在一定差异，可能影响最终的预测结果，但通常不会对鲁棒性好的模型造成明显影响。
- debian9系统的SoC模式(如SE5盒子)默认使用Sophon OpenCV，ubuntu系统的SoC模式和PCIe模式默认使用原生OpenCV，可以通过设置环境变量使用Sophon OpenCV。
- 我们通常使用静态尺寸的bmodel，如果原程序中的模型输入尺寸是不固定的，建议修改原程序中的预处理操作，使原程序的模型输入尺寸与bmodel一致，再进行精度对齐。

## 3 精度误差常见原因

- 没有正确导出模型，导出后的模型与原始模型推理结果不一致。

- 移植的python代码使用Sophon OpenCV或sail进行解码和预处理，解码和前后处理的方式与原生OpenCV存在一定差异，可能影响最终的预测结果。可以参考步骤七进行对齐评估影响，通常不会对鲁棒性较好的模型造成明显影响，如果影响较大，可以尝试通过增加原模型的鲁棒性来减少影响。

- 移植程序resize的接口或插值方式与原程序不同，导致精度差异。比如原程序中使用`transforms.Resize`，而移植程序使用`cv2.resize`，`transforms.Resize`除了默认的双线性插值，还会进行antialiasing，与`cv2.resize`处理后的数据有较大差异。建议原程序中使用opencv进行解码和预处理。

- 移植程序中的填充策略和像素值与原程序不同，可能导致细微差别。

- 移植程序中预处理图片的通道排序(BGR或RGB)与原程序不一致，可能导致较大差异。

- 移植程序中第三方库(如opencv)的版本与原程序不一致，可能导致精度差异。

- 移植程序中标准化的参数设置错误，导致预测结果存在较大差异。比如原程序的标准化操作是`transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])`，移植程序中对应的标准化如下：

  ```python
  # 使用numpy进行标准化
  mean = np.array([0.485, 0.456, 0.406]).reshape((1, 1, 3)) * 255.0
  scale = np.array([1/0.229, 1/0.224, 1/0.225]).reshape((1, 1, 3)) * 1 / 255.0
  img = img - mean
  img = img * scale
  # 使用sail.Bmcv.convert_to进行标准化
  self.ab = [x * self.input_scale for x in [1/0.229/255.0, -0.485/0.229, 1/0.224/255.0, -0.456/0.224, 1/0.225/255.0, -0.406/0.225]]
  self.bmcv.convert_to(input_bmimg, output_bmimg, ((self.ab[0], self.ab[1]), \
                                                   (self.ab[2], self.ab[3]), \
                                                   (self.ab[4], self.ab[5])))
  ```

  **注意**：标准化之前应先对齐通道的排序是BGR还是RGB。

- 多输出模型的输出是以字典形式保存的，如果将输出字典values转list，可能出现输出顺序错误的问题，建议使用输出名称获取对应的输出数据。比如：
  ```python
  # 将输出字典values转list
  outputs_sail = list(outputs_sail.values())
  # 根据输出名称获取对应的输出数据
  outputs_sail_0 = outputs_sail['17']
  outputs_sail_1 = outputs_sail['18']
  outputs_sail_2 = outputs_sail['28']
  outputs_sail_3 = outputs_sail['29']
  ```

- 目标检测算法中的nms接口不一致，导致预测结果差异。如原程序使用`torchvision.ops.nms`，移植程序使用`cv2.dnn.NMSBoxes`，会导致细微的精度差异。

- 在使用coco2017验证数据集进行精度测试时，注意保存检测数据到JSON文件时：
  1. bbox坐标的精度是否需要保留3位浮点数并进行四舍五入操作
  2. score的精度是否需要保留5位浮点数并进行四舍五入操作

  ```python
    bbox_dict['bbox'] = [float(round(x1, 3)), float(round(y1, 3)), float(round(x2 - x1,3)), float(round(y2 -y1, 3))]
    bbox_dict['score'] = float(round(score,5))
  ```
  
## 4 精度对齐参考步骤

以CV算法模型为例，从输入到获取预测结果通常可以分为解码、预处理、网络推理、后处理四个阶段，每个阶段包含一个或多个操作。每个操作的差异都有可能造成最后预测结果的不同，因此我们需要保证各个操作的输入数据相同，对比各个操作的输出数据，来排查各个操作所产生的精度误差。具体可参考以下步骤：

**步骤一**：检查解码和前后处理的接口和参数，尽量保持移植前后各个操作的一致性，避免常见的移植问题带来精度误差。具体可参考[3 精度误差常见原因](#3-精度误差常见原因)。

**步骤二**：使用batch_size=1的FP32 BModel进行测试，如果测试结果与原程序的测试结果相差较大，则需要找出测试结果不一致的样本，作为精度对齐的测试样本。

**步骤三**：设置环境变量`BMRT_SAVE_IO_TENSORS=1`，然后使用`batch_size=1`的FP32 BModel测试步骤二挑选的样本，会在当前目录下自动保存bmodel推理前后的数据，`input_ref_data.dat.bmrt`和`output_ref_data.dat.bmrt`。

```bash
export BMRT_SAVE_IO_TENSORS=1
```

**步骤四**：使用原程序测试同一张样本，在原程序中加载`input_ref_data.dat.bmrt`，并对比原模型推理前的数据。若推理前的数据一致，可认为解码和预处理已对齐，否则需要对解码和预处理的各个操作进行对齐。以Pytorch的原程序为例：

```python
import numpy as np
# 加载input_ref_data.dat.bmrt，并转成numpy.array
# 根据bmodel的输入尺寸修改reshape参数，可通过bm_model.bin --info *.bmodel查看模型输入信息
input_bmrt_array = np.fromfile("input_ref_data.dat.bmrt", dtype=np.float32).reshape(1,3,224,224)
# 将原模型的输入转成numpy.array
input_torch_array = input_tensor.detach().numpy()
# 对比input_bmrt_array和input_torch_array的最大误差
print("input_diff_max:", np.abs(input_bmrt_array - input_torch_array).max())
```

**步骤五**：使用`input_bmrt_array`作为原模型的输入，对比输出数据，若最大误差在0.001以下，通常不会对最终的预测结果造成影响。以Pytorch的原程序为例：

```python
# 将input_bmrt_array转成torch.tensor
input_tensor = torch.from_numpy(input_bmrt_array).to(device)
# 使用原模型进行推理
output_torch_tensor = model_torch(input_tensor)
# 将原模型的输出转成numpy.array
output_torch_array = output_torch_tensor.detach().numpy()
# 加载output_ref_data.dat.bmrt，并转成numpy.array
# 根据bmodel的输出尺寸修改reshape参数，可通过bm_model.bin --info *.bmodel查看bmodel输出信息
output_bmrt_array = np.fromfile("output_ref_data.dat.bmrt", dtype=np.float32).reshape(1,8)
# 对比原模型输出和bmodel输出的最大误差
print("output_diff_max:", np.abs(output_bmrt_array - output_torch_array).max())
```

**步骤六**：使用`output_bmrt_array`在原程序中进行后处理，对比原程序与移植程序的预测结果，若预测结果不一致，则说明后处理操作存在精度误差，需要对后处理的各个操作进行对齐。

**步骤七**：根据步骤四至步骤六可初步确定解码和前后处理是否对齐，若没有对齐，可以保存移植程序中各个操作的数据，在原程序对应的操作中加载并进行对比，若输入相同但输出不一致，则该操作可能存在误差，视情况进行对齐或优化。

以对齐resize操作为例，原程序使用`transforms.Resize`，而移植程序使用`cv2.resize`，可参考以下步骤进行排查：

1.在移植程序中保存resize前后的数据。

```python
# 保存resize前的数据
np.save('img_read_cv.npy', img_read_cv)
# 移植程序中的resize操作
img_resize_cv = cv2.resize(img_read_cv, (resize_w, resize_h))
# 保存resize后的数据
np.save('img_resize_cv.npy', img_resize_cv)
```

2.在原程序使用`img_read_cv.npy`进行resize，并对比resize的结果。

```python
# 加载img_read_cv.npy
img_read_cv = np.load('img_read_cv.npy')
# 将img_read_cv转换成相应格式，并进行resize
img_read_PIL = transforms.ToPILImage()(img_read_cv)
img_resize_PIL = transforms.Resize((resize_w, resize_h))(img_read_PIL)
# 将resize后的数据转为numpy.array
img_resize_transforms = np.array(img_resize_PIL)
# 加载img_resize_cv.npy
img_resize_cv = np.load('img_resize_cv.npy')
# 对比resize操作的最大误差
print("resize_diff_max:", np.abs(img_resize_cv - img_resize_transforms).max())
```

若移植的Python代码使用sail.Decoder和sail.Bmcv，可以将sail.BMImage转成numpy.array，再进行保存和对比：

```python
# 初始化sail.Tensor，根据实际情况修改初始化参数
sail_tensor = sail.Tensor(self.handle, (h, w), sail.Dtype.BM_FLOAT32, True, True)
# 将sail.BMImage转成sail.Tensor
self.bmcv.bm_image_to_tensor(bmimage, sail_tensor)
# 将sail.Tensor转成numpy.array
sail_array = sail_tensor.asnumpy()
```

## 5 Resnet分类模型精度对齐示例
**环境准备：**

- pytorch原代码运行环境：需安装opencv-python、torchvision>=0.11.2、pytorch>=1.10.1
- 移植代码运行环境：在PCIe模式下使用官网所提供的Docker镜像和SophonSDK，并安装Sophon Inference。

**相关文件可通过以下方式下载：**
```bash
pip3 install dfss -i https://pypi.tuna.tsinghua.edu.cn/simple --upgrade
python3 -m dfss --url=open@sophgo.com:sophon-demo/common/bmodel_align.zip
unzip bmodel_align.zip
```
**`bmodel_align`文件夹中的各个文件介绍如下：**
```bash
├── resnet_torch.py #pytorch源代码
├── resnet_torch_new.py #用于加载和对比数据的源代码
├── resnet_sail.py #对齐前的移植代码
├── resnet_sail_new.py #用于保存操作数据的移植代码
├── resnet_sail_align.py #对齐后的移植代码
├── resnet18_fp32_b1.bmodel #转换后的FP32 BModel
├── resnet18_traced.pt #trace后的原模型
└── test.jpg #测试图片
```

**复现步骤：**

- 步骤一：下载相关文件，可在`TPU-NNTC`开发环境中编译FP32 BModel模型，也可直接使用转换后的FP32 BModel。
  ```bash
  python3 -m bmnetp --model=resnet18_traced.pt --shapes=[1,3,224,224] --target="BM1684"
  ```

- 步骤二：分别运行pytorch原代码和对齐前的移植代码，发现测试结果差别较大。
  
  ```bash
  # 运行原代码
  python resnet_torch.py
  # 原代码运行结果
  INFO:root:filename: test.jpg, res: 751, score: 9.114608764648438
  # 运行对齐前的移植代码
  python3 resnet_sail.py
  # 移植代码运行结果
  INFO:root:filename: test.jpg, res: 867, score: 9.796974182128906
  ```
  
- 步骤三：修改移植代码，在移植代码中保存各个操作的数据（参考resnet_sail_new.py），设置环境变量，运行修改后的移植代码。
  
  ``` bash
  export BMRT_SAVE_IO_TENSORS=1
  python3 resnet_sail_new.py
  ```
  
  生成以下文件：
  ```bash
  img_read_cv.npy：解码后数据
  img_resize_cv.npy：resize后数据
  img_normalize_cv.npy：标准化后数据
  input_ref_data.dat.bmrt：模型推理的输入数据
  output_ref_data.dat.bmrt：模型推理的输出数据
  ```
  
- 步骤四：将以上文件拷贝至与原代码同一目录下，修改原代码，在原代码中加载移植程序生成的数据并进行对比（参考resnet_torch_new.py）。
  ```bash
  python resnet_torch_new.py
  ```
  打印对比结果如下：
  ```bash
  DEBUG:root:read aligned.
  DEBUG:root:PIL aligned.
  WARNING:root:resize unaligned!
  WARNING:root:resize_diff_max:255
  WARNING:root:normalize unaligned!
  WARNING:root:normalize_diff_max:0.9098039269447327
  WARNING:root:input unaligned!
  WARNING:root:input_diff_max:0.9098039269447327
  DEBUG:root:model infer aligned.
  DEBUG:root:res aligned.
  DEBUG:root:score aligned.
  DEBUG:root:sail: res=867, score=9.796974182128906
  INFO:root:filename: test.jpg, res: 751, score: 9.114608764648438
  ```
  
- 步骤五：从对比结果来看，图片解码、网络推理和后处理的操作基本对齐，而预处理从resize操作开始没有对齐，因此需要修改移植代码的resize操作使之对齐（详见resnet_sail_align.py）。修改内容如下：

  ```bash
  # 对齐前
  # h, w, _ = img.shape
  # if h != self.net_h or w != self.net_w:
  #     img = cv2.resize(img, (self.net_w, self.net_h))
  # 对齐后
  img = transforms.ToPILImage()(img)
  img = transforms.Resize((self.net_w, self.net_h))(img)
  img = np.array(img)
  ```

- 步骤六：运行对齐后的移植代码，保存各个操作的数据，并重复步骤四进行验证。

  ```bash
  # 运行对齐后的移植代码，保存各个操作的数据
  python3 resnet_sail_align.py
  # 对齐后的移植代码运行结果
  INFO:root:filename: test.jpg, res: 751, score: 9.114605903625488
  # 拷贝生成的数据，并运行修改后的原程序
  python resnet_torch_new.py
  # 打印对比结果
  DEBUG:root:read aligned.
  DEBUG:root:PIL aligned.
  DEBUG:root:resize aligned.
  DEBUG:root:normalize aligned.
  DEBUG:root:input aligned.
  DEBUG:root:model infer aligned.
  DEBUG:root:res aligned.
  DEBUG:root:score aligned.
  DEBUG:root:sail: res=751, score=9.114605903625488
  INFO:root:filename: test.jpg, res: 751, score: 9.114608764648438
  ```

**结果分析：**

- 误差原因：`transforms.Resize`除了默认的双线性插值，还会进行antialiasing，与`cv2.resize`处理后的数据有较大差异，导致明显的精度误差。FP32 BModel与原模型的推理结果存在细微差别，基本不会影响预测精度。
- 对齐后，移植程序和原程序的预测结果基本一致。


# 文件: docs/torch.jit.trace_Guide.md

---

[简体中文](./torch.jit.trace_Guide.md) | [English](./torch.jit.trace_Guide_EN.md)

 ## 1. 什么是JIT（torch.jit）？

答：JIT（Just-In-Time）是一组编译工具，用于弥合PyTorch研究与生产之间的差距。它允许创建可以在不依赖Python解释器的情况下运行的模型，并且可以更积极地进行优化。

 ## 2. 如何得到JIT模型？

答：在已有PyTorch的Python模型（基类为torch.nn.Module）的情况下，通过torch.jit.trace得到；traced_model=torch.jit.trace(python_model, torch.rand(input_shape))，然后再用traced_model.save(‘jit.pt’)保存下来。注意在trace前，加载PyTorch的源模型时，使用map_location参数：torch.load(python_model, map_location = ‘cpu’)。

## 3. 为什么不能使用torch.jit.script得到JIT模型？

答：BMNETP暂时不支持带有控制流操作（如if语句或循环）的JIT模型，但torch.jit.script可以产生这类模型，而torch.jit.trace却不可以，仅跟踪和记录张量上的操作，不会记录任何控制流操作。

