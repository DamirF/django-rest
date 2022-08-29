def create_calc_parameter():
    calc_parameters = {
        'Key': 'Parameters',
        'List': [
            {
                'Key': 'countingresults',
                'Value': 'true',
                'ValueType': 'boolean'
            },
            {
                'Key': 'ipaddress',
                'Value': {'type': 'string', '#text': '10.0.0.1'},
                'ValueType': 'string'
            }
        ]
    }
    return calc_parameters


def create_geography_parameter(city):
    geography_parameter = {
        'Key': 'parameters',
        'List': [{
            'Key': 'Reference',
            'Value': 'Geography',
            'ValueType': 'string'
        },
            {
                'Key': 'Search',
                'Value': f'{city} г',
                'ValueType': 'string'
            }]
    }
    return geography_parameter


def create_calc_data(city_sender, city_recipient, weight, volume, declared_value_rate):
    calc_data = {
        'Key': 'Destinations',
        'List': {
            'Key': 'Destination',
            'Fields': [{'Key': 'SenderGeography', 'Value': f'{city_sender}', 'ValueType': 'string'},
                       {'Key': 'RecipientGeography', 'Value': f'{city_recipient}',
                        'ValueType': 'string'},
                       {'Key': 'TypeOfCargo', 'Value': '4aab1fc6-fc2b-473a-8728-58bcd4ff79ba',
                        'ValueType': 'string'},
                       {'Key': 'Weight', 'Value': f'{float(weight)}', 'ValueType': 'float'},
                       {'Key': 'Qty', 'Value': '1', 'ValueType': 'int'},
                       {'Key': 'DeclaredValueRate', 'Value': f'{float(declared_value_rate)}', 'ValueType': 'float'},
                       {'Key': 'Volume', 'Value': f'{float(volume)}', 'ValueType': 'float'},
                       {'Key': 'CountOnlyAddServices', 'Value': 'false', 'ValueType': 'boolean'}
                       ],
            'Tables': {'Key': 'AdditionalServices',
                       'List': {'Key': 'Объявленная стоимость',
                                'Value': '6da21fe7-4f13-11dc-bda1-0015170f8c09',
                                'ValueType': 'string'
                                },
                       },
        }
    }
    return calc_data
