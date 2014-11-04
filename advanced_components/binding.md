# 绑定/Binding

<div id="youkuplayer" style="width:100%;height:450px;"></div>
<script type="text/javascript" src="http://player.youku.com/jsapi">
    player = new YKU.Player('youkuplayer',{
                                styleid: '0',
                                client_id: '35478c9be79d6b21',
                                vid: 'XODE3OTExMTI4',
                                autoplay: false,
                                show_related: true
                                });
</script>


Binding是EPUB360中一个特殊的交互组件。

Binding本身不能添加动画与触发器，它的主要作用是捆绑SLIDE、LAYER SLIDE或者LAYER组件使得他们可以同步滑动或者进行切换。

需要注意的是，Binding有一个主控元素的概念，可以使得其他捆绑的元素与主控元素正向或者反向绑定。

多组长度不同的LAYER可以通过Binding实现视差效果。
