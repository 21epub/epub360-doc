# MasterPage

<div id="youkuplayer" style="width:100%;height:450px;"></div>
<script type="text/javascript" src="http://player.youku.com/jsapi">
    player = new YKU.Player('youkuplayer',{
                                styleid: '0',
                                client_id: '35478c9be79d6b21',
                                vid: 'XNjgzMzU4Mzgw',
                                autoplay: false,
                                show_related: true
                                });
</script>

MasterPage主要用来对交互内容进行一些全局性的设定。例如：背景音乐、全局导航、全局性的提示等等。

用户可以点击页面列表区域的PAGE按钮进入MASTER PAGE进行设定。

![](http://qn.media.epub360.com/materials/origin/e96d7d2c9b3b8f220e60d04ffefee8dd_origin.png)

MASTER PAGE会覆盖在PAGE的最上层，所以，要注意，不要在MASTER PAGE中进行无效的设定，以免影响PAGE中的交互操作。

在PAGE中用户可以通过功能面板进行设定决定MASTER PAGE是否作用于当前页。

![](http://qn.media.epub360.com/materials/origin/997430fc84058092317ff93e342b4ed0_origin.png)
