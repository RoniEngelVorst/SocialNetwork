from Post import Post


class salePost(Post):

    def __init__(self, user, itemName, itemPrice, city):
        super().__init__(user)
        self._itemName = itemName
        self._itemPrice = itemPrice
        self._city = city
        self._sold = False

    #discounting a price using number of percents
    def discount(self, percents, password):
        #making sure that the password belongs to the user posted the post
        if(self._user.password() == password):
            self._itemPrice = (self._itemPrice/100)*(100 - percents)
            print(f"Discount on {self._user.username()} product! the new price is: {self._itemPrice}")
        else:
            raise ValueError("Not the correct password\n")

    #updating the post to be sold and printing a notification
    def sold(self, password):
        if(self._user.password() == password):
            self._sold = True
            print(f"{self._user.username()}'s product is sold")

    def __str__(self):
        if self._sold == False:
            return f"{self._user.username()} posted a product for sale:\nFor sale! {self._itemName}, price: {self._itemPrice}, pickup from: {self._city}\n"
        else:
            return f"{self._user.username()} posted a product for sale:\nSold! {self._itemName}, price: {self._itemPrice}, pickup from: {self._city}\n"


