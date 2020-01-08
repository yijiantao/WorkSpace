# -*- coding: UTF-8 -*-
"""
    一、定义
        命令模式的定义为：将一个请求封装成一个对象，从而可以使用不同的请求将客户端参数化，对请求排队或者记录请求日志，可以提供命令的撤销和恢复功能。
        命令模式中通常涉及三类对象的抽象：Receiver，Command，Invoker（本例中的waiterSys）。

        只有一个Invoker的命令模式也可以抽象成一个类似的“星形网络”，
        但与之前介绍的中介者模式不同，单纯的命令模式更像是一个辐射状的结构，由Invoker直接对Receiver传递命令，而一般不反向传递，
        中介者模式“星形网络”的中心，是个协调者，抽象结节间的信息流全部或者部分是双向的。
        另外，命令模式的定义中提到了“撤销和恢复功能”，也给了各位开发人员一个命令模式使用过程中的建议：各个Receiver中可以设计一个回滚接口，支持命令的“撤销”。

    二、场景
        一个饭店的点餐系统。饭店的点餐系统有什么不同嘛？
        大伙想想看，在大多数饭店中，当服务员已经接到顾客的点单，录入到系统中后，根据不同的菜品，会有不同的后台反应。
        比如，饭店有凉菜间、热菜间、主食间，那当服务员将菜品录入到系统中后，凉菜间会打印出顾客所点的凉菜条目，热菜间会打印出顾客所点的热菜条目，主食间会打印出主食条目。
        那这个系统的后台模式该如何设计？当然，直接在场景代码中加if…else…语句判断是个方法，可这样做又一次加重了系统耦合，违反了单一职责原则，遇到系统需求变动时，又会轻易违反开闭原则。
        所以，我们需要重新组织一下结构。
        可以将该系统设计成前台服务员系统和后台系统，后台系统进一步细分成主食子系统，凉菜子系统，热菜子系统。后台三个子系统设计如下：
"""


class backSys():    # 后台系统类
    def cook(self, dish):
        pass


class mainFoodSys(backSys):    # 主食子系统
    def cook(self, dish):
        print("MAINFOOD:Cook %s" % dish)


class coolDishSys(backSys):    # 凉菜子系统
    def cook(self, dish):
        print("COOLDISH:Cook %s" % dish)


class hotDishSys(backSys):    # 热菜子系统
    def cook(self, dish):
        print("HOTDISH:Cook %s" % dish)


class waiterSys():    # 前台服务员系统类
    menu_map = dict()
    commandList = []

    def setOrder(self, command):
        print("WAITER:Add dish")
        self.commandList.append(command)

    def cancelOrder(self, command):
        print("WAITER:Cancel order...")
        self.commandList.remove(command)

    def notify(self):    # 前台系统中的notify接口直接调用命令中的execute接口，执行命令。
        print("WAITER:Nofify...")
        for command in self.commandList:
            command.execute()


class Command():
    """
        前台服务员系统与后台系统的交互，我们可以通过命令的模式来实现，服务员将顾客的点单内容封装成命令，直接对后台下达命令，后台完成命令要求的事即可。

    """
    receiver = None

    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self):
        pass


class foodCommand(Command):
    dish = ""

    def __init__(self, receiver, dish):
        self.receiver = receiver
        self.dish = dish

    def execute(self):
        self.receiver.cook(self.dish)


class mainFoodCommand(foodCommand):
    pass


class coolDishCommand(foodCommand):
    pass


class hotDishCommand(foodCommand):
    pass


class menuAll:
    """
        foodCommand类是本例中涉及的类，相比于Command类进行了一定的改造。
        由于后台系统中的执行函数都是cook，因而在foodCommand类中直接将execute接口实现，如果后台系统执行函数不同，需要在三个子命令系统中实现execute接口。
        这样，后台三个命令类就可以直接继承，不用进行修改了。
        （这里子系统没有变动，可以将三个子系统的命令废弃不用，直接用foodCommand吗？当然可以，各有利蔽。请读者结合自身开发经验，进行思考相对于自己业务场景的使用，哪种方式更好。）
        为使场景业务精简一些，我们再加一个菜单类来辅助业务，菜单类在本例中直接写死。
    """
    menu_map = dict()

    def loadMenu(self):  # 加载菜单，这里直接写死
        self.menu_map["hot"] = ["Yu-Shiang Shredded Pork",
                                "Sauteed Tofu, Home Style", "Sauteed Snow Peas"]
        self.menu_map["cool"] = ["Cucumber", "Preserved egg"]
        self.menu_map["main"] = ["Rice", "Pie"]

    def isHot(self, dish):
        if dish in self.menu_map["hot"]:
            return True
        return False

    def isCool(self, dish):
        if dish in self.menu_map["cool"]:
            return True
        return False

    def isMain(self, dish):
        if dish in self.menu_map["main"]:
            return True
        return False


if __name__ == "__main__":
    """
        业务场景如下：
    """
    dish_list = ["Yu-Shiang Shredded Pork",
                 "Sauteed Tofu, Home Style", "Cucumber", "Rice"]  # 顾客点的菜
    waiter_sys = waiterSys()
    main_food_sys = mainFoodSys()
    cool_dish_sys = coolDishSys()
    hot_dish_sys = hotDishSys()
    menu = menuAll()
    menu.loadMenu()
    for dish in dish_list:
        if menu.isCool(dish):
            cmd = coolDishCommand(cool_dish_sys, dish)
        elif menu.isHot(dish):
            cmd = hotDishCommand(hot_dish_sys, dish)
        elif menu.isMain(dish):
            cmd = mainFoodCommand(main_food_sys, dish)
        else:
            continue
        waiter_sys.setOrder(cmd)
    waiter_sys.notify()
