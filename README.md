machine_learning
================

machine learing examples

1.LDA 

线性判别分析（二类）的实现。并将其用于分类虹膜（Iris）。

Iris 格式： 每个输入4个维度+加一个类别。总共三个类别。

2.使用fisherFace实现人脸识别（OpenCV）
  数据来源：AT&T facadataset  http://www.cl.cam.ac.uk/research/dtg/attarchive/pub/data/att_faces.zip
  fisherFace 主要使用线性判别分析对人脸进行降维，然后训练。在求解w的最后阶段与一般LDA有所不同，因为会遇到奇异值。具体解法请参考：http://docs.opencv.org/modules/contrib/doc/facerec/facerec_tutorial.html#appendixft 或者 
