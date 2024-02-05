import os 

header_art = "\n"\
             "d888888b  .d88b.  d8b   db  .d88b.  d8888b. d8888b.  .d88b.  d8888b. d88888b\n"\
             "  `88'   .8P  Y8. 888o  88 .8P  Y8. 88  `8D 88  `8D .8P  Y8. 88  `8D 88'    \n"\
             "   88    88    88 88V8o 88 88    88 88oodD' 88oobY' 88    88 88oooY' 88ooooo\n"\
             "   88    88    88 88 V8o88 88    88 88~~~   88`8b   88    88 88~~~b. 88~~~~~\n"\
             "  .88.   `8b  d8' 88  V888 `8b  d8' 88      88 `88. `8b  d8' 88   8D 88.    \n"\
             "Y888888P  `Y88P'  VP   V8P  `Y88P'  88      88   YD  `Y88P'  Y8888P' Y88888P\n"

# Base path names
base_path_names_dict = {
    'config': 'config',
    'data': 'data',
    'data_DIGISONDE': os.path.join('data', 'digisonde'),
    'logs': 'logs',
    'output': 'output'
}

# Base file names
base_file_names_dict = {
    'config_fn': 'config.json',
    'data_DIGISONDE_feather_fn': 'digisonde_data.feather',
}


s3_bucket_name = "ionoprobe"

# GOES DATA
GOES_SWPC_NOAA_s3_path = "GOES_SWPC_NOAA"






# DIGISONDE DATA
station_legend = ['Station', 'YYYY', 'DAY', 'DDD', 'HHNMSS', 'P1', 'FFS', 'S', 'AXN', 'PPS', 'IGA', 'PS']
f_legend = ['foF2', 'foF1', 'foF1p', 'foFE', 'foFEp', 'fxI', 'foEs', 'fmin']

# DIGISONDE GIRO STATIONS (COOR, NAME, COUNTRY)
# sta_dict = {"EB040": ("40.8N", "0.5E", "ROQUETES", "SPAIN"),
#             "EA036": ("37.1N", "353.3E", "EL ARENOSILLO", "SPAIN"),
#             "AT138": ("38.0N", "23.5E", "ATHENS", "GREECE"),
#             "AU930": ("30.4N", "262.3E", "AUSTIN", "USA"),
#             "BLJ03": ("1.43N", "311.56E", "BELEM", "BRAZIL"),
#             "BC840": ("40.0N", "254.7E", "BOULDER", "USA"),
#             "CAJ2M": ("-22.7N", "315.0E", "CACHOEIRA PAULISTA", "BRAZIL"),
#             "DW41K": ("-12.45N", "130.95E", "DARWIN", "AUSTRALIA"),
#             "DB049": ("50.1N", "4.6E", "DOURBES", "BELGIUM"),
#             "FZA0M": ("-3.9N", "321.6E", "FORTALEZA", "BRAZIL"),
#             "GA762": ("62.38N", "215.0E", "GAKONA", "USA"),
#             "GM037": ("37.9N", "14.0E", "GIBILMANNA", "ITALY"),
#             "GU513": ("13.62N", "144.86E", "GUAM", "USA"),
#             "HO54K": ("-42.92N", "147.32E", "HOBART", "AUSTRALIA"),
#             "IC437": ("37.14N", "127.54E", "I-CHEON", "SOUTH KOREA"),
#             "IF843": ("43.81N", "247.32E", "IDAHO NATIONAL LAB", "USA"),
#             "JB57N": ("-74.62N", "164.24E", "JANG BOGO", "ANTARTICA"),
#             "JJ433": ("33.43N", "126.3E", "JEJU", "JAPAN"),
#             "LL721": ("21.43N", "201.85E", "LUALUALEI", "USA"),
#             "MHJ45": ("42.6N", "288.5E", "MILLSTONE HILL", "USA"),
#             "NI135": ("35.025N", "33.157E", "NICOSIA", "CYPRUS"),
#             "ND61R": ("-19.07N", "190.07E", "NIUE", "NEW ZELAND"),
#             "NI63_": ("-29.03N", "167.97E", "NORFOLK", "NEW ZELAND"),
#             "PE43K": ("-32.0N", "116.13E", "PERTH", "AUSTRALIA"),
#             "PF765": ("65.13N", "212.55E", "POKER FLAT", "USA"),
#             "PQ052": ("50.0N", "14.6E", "PRUHONICE", "CZECHIA"),
#             "PA836": ("34.8N", "239.5E", "PT ARGUELLO", "USA"),
#             "RM041": ("41.8N", "12.5E", "ROME", "ITALY"),
#             "VT139": ("40.6N", "17.8E", "SAN VITO", "ITALY"),
#             "SMK29": ("-29.728N", "306.286E", "SANTA MARIA", "BRAZIL"),
#             "SO148": ("47.63N", "16.72E", "SOPRON", "HUNGARY"),
#             "THJ76": ("76.54N", "291.56E", "THULE", "GREENLAND"),
#             "TV51R": ("-19.63N", "146.85E", "TOWNSVILLE", "AUSTRALIA"),
#             "TR169": ("69.6N", "19.2E", "TROMSO", "NORWAY"),
#             "TR170": ("69.583N", "19.217E", "EISCAT TROMSO", "NORWAY"),
#             "WA619": ("19.294N", "166.647E", "WAKE IS", "USA"),
#             "WP937": ("37.9N", "284.5E", "WALLOPS IS", "USA"),
#             "MZ152": ("52.2N", "21.1E", "WARSAW", "POLAND")
#             } 

# Test
sta_dict = {"EB040": ("40.8N", "0.5E", "ROQUETES", "SPAIN"),
            } 

DIGISONDE_GIRO_fn = "digisonde_giro_raw"
DIGISONDE_GIRO_s3_path = "DIGISONDE_GIRO"

# Each data must be request in a different get
DIGISONDE_GIRO_data = {"foF2": "F2 layer critical frequency",
                        "foF1": "F1 layer critical frequency",
                        "foE": "E layer critical frequency",
                        "foEs": "Es layer critical frequency",
                        "foEa": "Critical frequency of auroral E-layer",
                        "fbEs": "Blanketing frequency of Es-layer",
                        "foP": "Critical frequency of F region patch trace",
                        "fxI": "Maximum frequency of F trace",
                        "MUFD": "Maximum usable frequency, 3000 km",
                        "MD": "MUF(3000)/foF2",
                        "hF2": "Minimum virtual height of F2 trace",
                        "hF": "Minimum virtual height of F trace",
                        "hE": "Minimum virtual height of E trace",
                        "hEs": "Minimum virtual height of Es trace",
                        "hEa": "Minimum virtual height of auroral E trace",
                        "hP": "Minimum virtual height of F patch trace",
                        "TypeEs": "Type of Es layer(s)",
                        "hmF2": "Peak height F2-layer",
                        "hmF1": "Peak height F1-layer",
                        "hmE": "Peak height of E-layer",
                        "zhalfNm": "True height at 1/2 NmF2",
                        "yF2": "Half thickness of F2-layer",
                        "yF1": "Half thickness of F1-layer",
                        "yE": "Half thickness of E-layer",
                        "scaleF2": "Scale height at the F2-peak",
                        "B0": "IRI thickness parameter",
                        "B1": "IRI profile shape parameter",
                        "D1": "IRI profile shape parameter",
                        "TEC": "Ionogram-derived total electron content",
                        "FF": "Frequence spread between fxF2 and fxI",
                        "FE": "Frequence spread beyond foE",
                        "QF": "Range spread of F-layer",
                        "QE": "Range spread of E-layer",
                        "fmin": "Minimum frequency of echoes",
                        "fminF": "Minimum frequency of F-layer echoes",
                        "fminE": "Minimum frequency of E-layer echoes",
                        "fminEs": "Minimum frequency of Es-layer",
                        "foF2p": "foF2 prediction by IRI no-storm option",
                        }