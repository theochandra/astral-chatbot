def sum_of_carousel(len_data_carousel):
    switch = {
        1 : {
                "sum_of_carousel": 1,
                "sum_of_button": 1
            },
        2 : {
                "sum_of_carousel": 2,
                "sum_of_button": 1
            },
        3 : {
                "sum_of_carousel": 3,
                "sum_of_button": 1
            },
        4 : {
                "sum_of_carousel": 4,
                "sum_of_button": 1
            },
        5 : {
                "sum_of_carousel": 5,
                "sum_of_button": 1
            },
    }
    
    sum = switch.get(len_data_carousel, lambda: "nothing")
    
    return sum
    
dict_of_format = sum_of_carousel(2)     
print dict_of_format['sum_of_carousel']