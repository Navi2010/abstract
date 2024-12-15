class India:
    def capital(self):
        print('the capital of india is new delhi')
    def language(self):
        print('the primary language in india is hindi')
    def type(self):
        print('india is a developing country')

class USA:
    def capital(self):
        print('the capitial of the USA is Washington D.C.')
    def language(self):
        print('the primary language that is spoken in the USA is english')
    def type(self):
        print('USA is a developed country')

obj_india = India()
obj_USA = USA()

for country in (obj_india, obj_USA):
    country.capital()
    country.language()
    country.type()