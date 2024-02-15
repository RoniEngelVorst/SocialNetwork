from Post import Post


class salePost(Post):
    sold = False
    def __init__(self, postType, itemName, itemPrice, city, owner):
        self._itemName = itemName
        self._itemPrice = itemPrice
        self._city = city
        self._owner = owner

    def discount(self, precents, password):
        if(self._owner._password == password):
            self._itemPrice = (self._itemPrice/100)*(100-precents)
        else:
            raise ValueError("Not the correct password")

    def sold(self, password):
        if(self._owner._password == password):
            self._sold = True

    def __str__(self):
        if self.sold == False:
            return f"{self._owner.username} posted a product for sale:\n For sale! {self._itemName}, price: {self._itemPrice}, pickup from: {self._city}"
        else:
            return f"{self._owner.username} posted a product for sale:\n Sold! {self._itemName}, price: {self._itemPrice}, pickup from: {self._city}"


