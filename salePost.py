from Post import Post


class salePost(Post):

    def __init__(self, user, itemName, itemPrice, city):
        super().__init__(user)
        self._itemName = itemName
        self._itemPrice = itemPrice
        self._city = city
        self._sold = False

    def discount(self, precents, password):
        if(self._user.password() == password):
            self._itemPrice = (self._itemPrice/100)*(100-precents)
            print(f"Discount on {self._user.username()} product! the new price is: {self._itemPrice}")
        else:
            raise ValueError("Not the correct password\n")

    def sold(self, password):
        if(self._user.password() == password):
            self._sold = True
            print(f"{self._user.username()}'s product is sold")

    def __str__(self):
        if self._sold == False:
            return f"{self._user.username()} posted a product for sale:\nFor sale! {self._itemName}, price: {self._itemPrice}, pickup from: {self._city}\n"
        else:
            return f"{self._user.username()} posted a product for sale:\nSold! {self._itemName}, price: {self._itemPrice}, pickup from: {self._city}\n"


