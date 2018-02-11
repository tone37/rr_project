"""Get data from USGS about data recording sites based on user parameters"""

import requests
import csv
import io
import matplotlib.pyplot as plt
import pandas as pd

payload = {'site': '', 'countyCd': '', 'stateCd': '', 'bBox': '', 'huc': '',
           'format': '', 'siteOutput': '', 'seriesCatalogOutput': '',
           'siteStatus': '', 'siteType': ''}


def main():
    inputs()
    fpl = filtered_pl()
    req = requests.get("http://waterservices.usgs.gov/nwis/site/?", params=fpl)

    print(type(req))

    # req_text = (req.text)
    # data = pd.read_csv(io.StringIO(req_text), sep='\t', engine='python',
    #                    comment='#')
    # df = pd.DataFrame(data)







def inputs():
    for key in payload:
        payload[key] = input("What value for {}? ('enter' to skip)".format(
                key)) or None
    return payload


def filtered_pl():
    filt_pl = {k: v for k, v in payload.items() if v is not None}
    return filt_pl


if __name__ == "__main__":
    main()











'''
hasDataType values:

    all - default (see above for qualifications). This is equivalent 
        to &seriesCatalogOutput=true.
    iv - Instantaneous values (time-series measurements typically recorded by 
        automated equipment at frequent intervals (e.g., hourly)
    uv - Unit values (alias for iv)
    rt - Real-time data (alias for iv). Unfortunately, using "rt" may retrieve 
        sites that are not "real-time" because it is simply an alias, e.g. it 
        may show discontinued sites. The closest approximation of a list of 
        real-time sites is to use &siteStatus=active
    dv - Daily values (once daily measurements or summarized information for a 
        particular day, such as daily maximum, minimum and mean)
    pk - Peaks measurements of water levels and streamflow for surface water 
        sites (such as during floods, may be either an automated or a 
        manual measurement)
    sv - Site visits (irregular manual surface water measurements, excluding 
        peak measurements)
    gw - Groundwater levels measured at irregular, discrete intervals. For 
        recorded, time series groundwater levels, use iv or id.
    qw - Water-quality data from discrete sampling events and analyzed in the 
        field or in a laboratory. For recorded time series water-quality 
        data, use iv or id.
    id - Historical instantaneous values (sites in the USGS Instantaneous Data 
        Archive External Link)
    aw - Sites monitored by the USGS Active Groundwater Level Network 
        External Link
    ad - Sites included in USGS Annual Water Data Reports External Link


'''