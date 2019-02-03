class friend:
    def __init__(self, f_name, l_name, contact):
        self.f_name = f_name
        self.l_name = l_name
        self.contact = str(contact)
        self.price = 0.0
        self.message = ''
        # you owe this amount: % of name;...% of name.


    def __repr__(self):
        return "<friend name:%s %s>" % (self.f_name, self.l_name)


    def __str__(self):
        return "Member of people class. Name: %s %s. Contact: %s" % (self.f_name, self.l_name, self.contact)


    def add_amount(self, cost, message):
        self.price += cost
        self.message += message
        return 1


    def out(self):
        self.price = float("{:0.2f}".format(self.price))
        prefix = 'You owe ${0:.2f} from: '.format(self.price)
        self.message = prefix + self.message
        self.message = self.message[:-2] + "."
        return [self.f_name, self.l_name, self.contact, self.price, self.message]

    def interac_request(self):
        self.out()
        r_val = "{\n\t\"amount\": %.2f,\n\t\"contactName\": \"%s\",\n\t\"email\": \"%s\",\n\t\"requesterMessage\": \"%s\"\n}" %(self.price, self.f_name + ' ' + self.l_name, self.contact, self.message)
        return r_val
