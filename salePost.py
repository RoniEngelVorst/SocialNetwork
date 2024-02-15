from Post import Post


class salePost(Post):
    sold = False
    def __init__(self, postType, itemName, itemPrice, city, owner):
        self._itemName = itemName
        self._itemPrice = itemPrice
        self._city = city
        self._owner = owner

    def discount(self, new_price, password):
        if(self._owner._password == password):
            self._itemPrice = new_price
        else:
            raise ValueError("Not the correct password")

    def sold(self, password):
        if(self._owner._password == password):
            self._sold = True

