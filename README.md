machine_learning
================

machine learing examples

1.LDA 

   a.线性判别分析（二类）的实现。并将其用于分类虹膜（Iris）。

    Iris 格式： 每个输入4个维度+加一个类别。总共三个类别。
    详细介绍：https://github.com/PhenixI/machine_learning/blob/master/LDA/LDA%20introduction%20simple.docx

   b.使用fisherFace实现人脸识别（OpenCV）
     数据来源：AT&T facadataset  http://www.cl.cam.ac.uk/research/dtg/attarchive/pub/data/att_faces.zip
   fisherFace 主要使用线性判别分析对人脸进行降维，然后训练。在求解w的最后阶段与一般LDA有所不同，因为会遇到奇异值。具体解法请    参考：http://docs.opencv.org/modules/contrib/doc/facerec/facerec_tutorial.html#appendixft 或者
   https://github.com/PhenixI/machine_learning/blob/master/LDA/LDA%20introduction%20simple.docx

2.PLA
   
   a.感知机算法的实现。感知机算法的原始形式可参考《统计机器学习》、台湾大学 林轩田的机器学习课程、pattern recognition and machine learning或者https://github.com/PhenixI/machine_learning-applications-and-implementations/blob/master/PLA(Perceptron)/PLA%20introduction%20simple.docx

3.AdaBoost
   a.AdaBoost 算法的实现
   b.AdaBoost 相关内容可参考https://github.com/PhenixI/machine_learning-applications-and-implementations/blob/master/AdaBoost/Introduction%20of%20AdaBoost%20%E7%AE%80%E4%BB%8B.docx 或machine learning in action 以及统计机器学习
   
4.k-means
   包括k-means的实现以及二分kMenas的实现
