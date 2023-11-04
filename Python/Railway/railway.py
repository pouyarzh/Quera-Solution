import decimal

dic_passenger = {}

class Train:
    
    def __init__(self, last_visited_city, weight_capacity, is_on_trip):
        self.last_visited_city = last_visited_city
        self.weight_capacity = weight_capacity
        self.is_on_trip = is_on_trip


class Trip:

    all_cities = ('Arak', 'Ardabil', 'Urmia', 'Isfahan', 'Ahvaz', 'Ilam', 'Bojnord', 'Bandar Abbas', 'Bushehr', 'Birjand', 'Tabriz', 'Tehran', 'Khorramabad', 'Rasht', 'Zahedan', 'Zanjan', 'Sari', 'Semnan', 'Sanandaj', 'Shahr-e Kord', 'Shiraz', 'Qazvin', 'Qom', 'Karaj', 'Kermanshah', 'Gorgan', 'Mashhad', 'Hamadan', 'Yasuj', 'Yazd')

    def __init__(self, origin_city, destination_city, train):
        self.train = self.train_validation(train)
        self.destination_city = destination_city
        self.origin_city = self.origin_city_validation(origin_city)
        self.passengers = []
    
    def origin_city_validation(self, origin_city):
        if not self.all_cities.__contains__(origin_city):
            raise Exception("This input is not a verified city!")
        if self.destination_city == origin_city:
            raise Exception("Origin and destination cities can't be the same!")
        if self.train.last_visited_city != origin_city:
            raise Exception("The train of the trip is not available in the origin city!")
        return origin_city
        
    def train_validation(self, train):
        if not isinstance(train,Train):
            raise Exception("This input is not a train!")
        if train.is_on_trip:
            raise Exception("This train is not available!")
        return train

    # here implement the magic method
    def __call__(self):
        temp = 0.0
        for item in self.passengers:
            temp = decimal.Decimal(dic_passenger[str(item)]) + decimal.Decimal(str(temp))
        return decimal.Decimal(str(self.train.weight_capacity)) - decimal.Decimal(str(temp))


class Passenger:

    def __init__(self, fullname, load_weight):
        global dic_passenger
        self.fullname = str(fullname)
        self.load_weight = load_weight
        dic_passenger.update({self.fullname: decimal.Decimal(str(self.load_weight))})

    def __repr__(self):
        return f'{self.fullname}'

    def attend_trip(self, trip):
        global dic_passenger
        # print( decimal.Decimal(trip()),decimal.Decimal(str(self.load_weight)))
        if decimal.Decimal(str(self.load_weight)) <= decimal.Decimal(str(trip())):
            trip.passengers.append(self.fullname)
        else:
            del dic_passenger[str(self.fullname)]
            raise Exception("Heavy load!")
        pass

    def cancel_trip(self, trip):
        temp = False
        global dic_passenger
        for item in range(len(trip.passengers)):
            if str(trip.passengers[item]) == str(self.fullname):
                temp = True
                del dic_passenger[str(trip.passengers[item])]
                del trip.passengers[item]

                break
        if not temp:
            raise Exception("This passenger is not attended to this trip!")

    # here implement the magic method

    # def __str__(self):
    #     return str(self.fullname)




def test_str():
    passenger1 = Passenger(fullname='Ali Saeedi', load_weight=616)

    if str(passenger1) == 'Ali Saeedi':
        print('success')
    else:
        print('failed')

def test_call():
    train = Train(last_visited_city='Sanandaj', weight_capacity=5661.212, is_on_trip=False)

    passenger1 = Passenger(fullname='Ali Saeedi', load_weight=661.072)
    passenger2 = Passenger(fullname='Abolfazl Zandi1', load_weight=2500.016)
    passenger3 = Passenger(fullname='Abolfazl Zandi2', load_weight=2400.014)
    passenger4 = Passenger(fullname='Abolfazl Zandi3', load_weight=25.005)
    passenger5 = Passenger(fullname='Abolfazl Zandi4', load_weight=25.003698413)
    passenger6 = Passenger(fullname='Abolfazl Zandi5', load_weight=25.001301587)
    passenger7 = Passenger(fullname='Abolfazl Zandi6', load_weight=24.5)
    passenger8 = Passenger(fullname='Abolfazl Zandi7', load_weight=0.5)
    passenger9 = Passenger(fullname='Abolfazl Zandi8', load_weight=0.05)
    passenger10 = Passenger(fullname='Abolfazl Zandi9', load_weight=0.0000000000000000000000000000000000001)


    trip = Trip(origin_city='Sanandaj', destination_city='Rasht', train=train)


    try:
        # trip.passengers = [passenger1,passenger2]
        # print(trip.passengers)

        passenger1.attend_trip(trip)
        # print(trip.passengers)

        passenger2.attend_trip(trip)
        # print(trip.passengers)

        passenger3.attend_trip(trip)
        # print(trip.passengers)

        passenger4.attend_trip(trip)
        # print(trip.passengers)

        passenger5.attend_trip(trip)
        # print(trip.passengers)

        passenger6.attend_trip(trip)
        # print(trip.passengers)

        passenger7.attend_trip(trip)
        # print(trip.passengers)

        passenger8.attend_trip(trip)

        passenger9.attend_trip(trip)

        passenger10.attend_trip(trip)

        print(trip())



        listTest = [passenger1, passenger2, passenger3, passenger4, passenger5, passenger6]
        # print(listTest)


        print(trip.passengers == [str(item) for item in [passenger1, passenger2, passenger3, passenger4, passenger5, passenger6,passenger7,passenger8,passenger9,passenger10]])

    except Exception as e:
        print(trip.passengers)
        print(e)



if __name__ == "__main__":
    # test_str()
    test_call()
    # print(decimal.Decimal(str('25.000000000')))
    # print(decimal.Decimal(str('25.000000000')) - decimal.Decimal(str('24.5')))