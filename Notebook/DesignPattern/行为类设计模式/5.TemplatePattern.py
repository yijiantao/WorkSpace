# -*- coding -*- 
"""
    一、定义：
        模板模式定义如下：定义一个操作中的算法的框架，而将一些步骤延迟到子类中，使得子类可以不改变一个算法的结构即可重新定义该算法的某些特定的步骤。
        子类实现的具体方法叫作基本方法，实现对基本方法高度的框架方法，叫作模板方法。

    二、场景： [股票查询客户端]
        投资股票是种常见的理财方式，我国股民越来越多，实时查询股票的需求也越来越大。
        今天，我们通过一个简单的股票查询客户端来认识一种简单的设计模式：模板模式。
        根据股票代码来查询股价分为如下几个步骤：登录、设置股票代码、查询、展示。构造如下的虚拟股票查询器：
"""

