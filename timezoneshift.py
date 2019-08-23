import pytz
import pandas
import datetime

def cst_tz_to_iata_tz(cst_datetime, iata):
    """
    Convert given time in cst timezone to local time of specified airport.
    vars
        [cst_datetime] [string] [month/day/year hour:minute:second]
        [iata] [string]
    return
        [local_time] [string]
    """
    iata_tz_names = pandas.read_csv('iata_tz_name.csv')
    iata_tz_names = dict(zip(iata_tz_names.IATA, iata_tz_names.Timezone))
    iata_tz_name = iata_tz_names[iata]

    iata_tz = pytz.timezone(iata_tz_name)
    cst_tz = pytz.timezone('America/Mexico_City')

    cst_datetime = datetime.datetime.strptime(cst_datetime, '%m/%d/%Y %H:%M:%S')

    local_time = cst_tz.localize(cst_datetime).astimezone(iata_tz)
    local_time_string = local_time.strftime('%m/%d/%Y %H:%M:%S')
    return local_time_string

print cst_tz_to_iata_tz('8/23/2019 06:35:00', 'LHR')