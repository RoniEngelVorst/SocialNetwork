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
            print(f"Discount on {self._owner._username} product! the new price is: {self._itemPrice}\n")
        else:
            raise ValueError("Not the correct password\n")

    def sold(self, password):
        if(self._owner._password == password):
            self._sold = True
            print(f"{self._owner._username}'s product is sold\n")
            print(str(self))

    def __str__(self):
        if self.sold == False:
            return f"{self._owner.username} posted a product for sale:\n For sale! {self._itemName}, price: {self._itemPrice}, pickup from: {self._city}\n"
        else:
            return f"{self._owner.username} posted a product for sale:\n Sold! {self._itemName}, price: {self._itemPrice}, pickup from: {self._city}\n"


