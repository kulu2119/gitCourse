class item:
    def __init__(self,item,price) -> None:
        self.item=item
        self.price=price
        pass
class shopping_cart:
    p_list=[]
    def add(item:item):
        p_list.append(item)
        print(p_list)
