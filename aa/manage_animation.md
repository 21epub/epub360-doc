# 动画组织管理

####动画设定
在动画添加后，用户需要对动画属性进行相应的设定。

![](http://qn.media.epub360.com/materials/origin/97f2eab9f46c3e725e958efa0bbfe6eb_origin.png)


####动画时序面板设定
之后，用户可以通过“功能面板”——“动画次序面板”对动画进行重新设定与时序调整。

![](http://qn.media.epub360.com/materials/origin/7cafe2e7ff4e6abe31f28d852f812f92_origin.png)

在“动画次序面板”中，我们可以对直接拖动动画进行播放时序的调整。

![](http://qn.media.epub360.com/materials/origin/1cc6174de90a5ebd7be1252f382abb90_origin.png)

####动画时序机制
在动画时序调整时，我们需要注意动画的“出现方式”。

EPUB360目前有三种不同的动画出现方式：

* 点击后开始 ![](http://qn.media.epub360.com/materials/origin/d8cd115d5bef0d990070d704879d602f_origin.png)
* 上一个开始之后![](http://qn.media.epub360.com/materials/origin/5ad58f5d4ad190977b8447b5bbe690c4_origin.png)
* 和上一个一起开始 ![](http://qn.media.epub360.com/materials/origin/839ef19c37503a853b82689b8eb392a5_origin.png)

这里需要注意的是每一个动画始终参照前一个动画。

*例如：有A、B、C 三个动画，全部为“和上一个一起开始”，虽然三个动画是全部执行，但如果将B改为“上一个开始后”，那么，B和C会同时等待A的动画执行完再会执行。
*

#### 动画延迟机制
在动画播放的过程中，为了达到某些特定的播放次序，需要用户对动画播放进行延迟的设定。

EPUB360.COM中动画延迟的参考物始终为前一动画。

我们以A动画和B动画为例：

A动画持续时间为5S，B动画为3S。

如果需要A和B动画同时发生，那么只需要将B动画设定为与A一起开始即可。

![](http://qn.media.epub360.com/materials/origin/f89b4bb2eba864fe73ca815066409731_origin.jpg)

如果要A和B动画同时结束，那么需要将B动画设定为与A动画一起开始，并同时对B动画设定2S的延迟。已达到一起结束的效果。

![](http://qn.media.epub360.com/materials/origin/afd0fc2f1a3beb20540527734abe0e92_origin.jpg)

如果B动画设定为A动画播放后执行，并添加了2S的延迟，那么A+B的总体持续时间将变为5+2+3=10S。

![](http://qn.media.epub360.com/materials/origin/873ea97c1f442af783cdc4a00eb34c6d_origin.jpg)



