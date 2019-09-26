class CallDetail:
    def __init__(self, phone_no, called_no, call_duration, call_type):
        self.phone_no = phone_no
        self.called_no = called_no
        self.call_duration = call_duration
        self.call_type = call_type

    def details(self):
        print(self.phone_no,'\t', self.called_no,'\t  ', self.call_duration,'\t\t', self.call_type)

class Util:
    def __init__(self):
        self.list_of_call_objects = None

    def parse_customer(self, list_of_call_string):
        #self.list_of_call_objects = []

        print(" Phone No\t Called No\tCall Duration\tCall Type")

        for i in list_of_call_string:
            phone_no, called_no, call_duration, call_type = map(str, i.split(","))
            self.list_of_call_objects.append([phone_no, called_no, call_duration, call_type])
            call = CallDetail(phone_no, called_no, call_duration, call_type)
            call.details()

call_1 = '9990000001,9330000001,23,STD'
call_2 = '9990000001,9330000002,54,Local'
call_3 = '9990000003,9330000003,6,ISD'

ut = Util()

list_of_call_string = [call_1, call_2, call_3]
ut.parse_customer(list_of_call_string)
