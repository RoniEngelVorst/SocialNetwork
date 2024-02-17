from Post import Post


class salePost(Post):

    def __init__(self, owner, itemName, itemPrice, city):
        self._itemName = itemName
        self._itemPrice = itemPrice
        self._city = city
        self._owner = owner
        self._sold = False

    def discount(self, precents, password):
        if(self._owner.password() == password):
            self._itemPrice = (self._itemPrice/100)*(100-precents)
            print(f"Discount on {self._owner.username()} product! the new price is: {self._itemPrice}\n")
        else:
            raise ValueError("Not the correct password\n")

    def sold(self, password):
        if(self._owner.password() == password):
            self._sold = True
            print(f"{self._owner.username()}'s product is sold\n")

    def __str__(self):
        if self._sold == False:
            return f"{self._owner.username()} posted a product for sale:\nFor sale! {self._itemName}, price: {self._itemPrice}, pickup from: {self._city}\n"
        else:
            return f"{self._owner.username()} posted a product for sale:\nSold! {self._itemName}, price: {self._itemPrice}, pickup from: {self._city}\n"


