from Util.logger import Logger

logger = Logger().get_application_logger

class Store:
    def __init__(self):
        self._countries = {}

    def get_stat(self, country_codes, devices):
        country_store = list(filter(lambda country: country in country_codes, self._countries.keys())) if len(country_codes) > 0 else self._countries.keys()
        response = {}
        web_req_count = 0
        time_spent_count = 0
        dim = []

        # Add country filter details in response
        for country in country_codes:
            dim.append({'key': 'country', 'val': country})
        
        # Add device filter details in resposne
        for device in devices:
            dim.append({'key': 'device', 'val': device})
        
        # Add stat accoriding to filters in response
        for country in country_store:
            country_count = self._countries[country].get_stat(devices)
            web_req_count += country_count['web_req_count']
            time_spent_count += country_count['time_spent_count']
        
        response['dim'] = dim
        response['metrics'] = [{'key': 'webreq', 'val': web_req_count}, {'key': 'timespent', 'val': time_spent_count}]
        return response

    def init_country(self, country_code):
        if self._countries.get(country_code):
            return True
        logger.info('Initialising a new Country in Tree DB => {}'.format(country_code))
        country = self.Country()
        self._countries[country_code] = country
    
    def update_country_stat(self, country_code, device_name, no_of_req, time_spent):
        if not country_code in self._countries.keys():
            self.init_country(country_code)
        country = self._countries[country_code]
        country.add_device(device_name, self.Device(device_name, no_of_req, time_spent))
        return True

    class Country():
        def __init__(self):
            self._devices = []

        def add_device(self, device_name, device):
            self._devices.append(device)

        def get_stat(self, device_names):
            web_req_count = 0
            time_spent_count = 0
            devices = list(filter(lambda device : device.get_device_name in device_names, self._devices)) if len(device_names) > 0 else self._devices
            for device in devices:
                web_req_count += device.web_req_stat
                time_spent_count += device.time_spent_stat
            return {'web_req_count': web_req_count, 'time_spent_count': time_spent_count}

    class Device:
        def __init__(self, name=None, web_req = 0, time_spent = 0):
            self._web_req = web_req
            self._time_spent = time_spent
            self._name = name

        @property
        def web_req_stat(self):
            return self._web_req

        @property
        def time_spent_stat(self):
            return self._time_spent

        @property
        def get_device_name(self):
            return self._name


DataStore = Store()
