
header_art = "\n"\
             "d888888b  .d88b.  d8b   db  .d88b.  d8888b. d8888b.  .d88b.  d8888b. d88888b\n"\
             "  `88'   .8P  Y8. 888o  88 .8P  Y8. 88  `8D 88  `8D .8P  Y8. 88  `8D 88'    \n"\
             "   88    88    88 88V8o 88 88    88 88oodD' 88oobY' 88    88 88oooY' 88ooooo\n"\
             "   88    88    88 88 V8o88 88    88 88~~~   88`8b   88    88 88~~~b. 88~~~~~\n"\
             "  .88.   `8b  d8' 88  V888 `8b  d8' 88      88 `88. `8b  d8' 88   8D 88.    \n"\
             "Y888888P  `Y88P'  VP   V8P  `Y88P'  88      88   YD  `Y88P'  Y8888P' Y88888P\n"

config_fn = "config.json"

# DIGISONDE DATA
station_legend = ['Station', 'YYYY', 'DAY', 'DDD', 'HHNMSS', 'P1', 'FFS', 'S', 'AXN', 'PPS', 'IGA', 'PS']
f_legend = ['foF2', 'foF1', 'foF1p', 'foFE', 'foFEp', 'fxI', 'foEs', 'fmin']

# DIGISONDE GIRO STATIONS (COOR, NAME, COUNTRY)
sta_dict = {"EB040": ("40.8N", "0.5E", "ROQUETES", "SPAIN"),
            "EA036": ("37.1N", "353.3E", "EL ARENOSILLO", "SPAIN"),
            "AT138": ("38.0N", "23.5E", "ATHENS", "GREECE"),
            "AU930": ("30.4N", "262.3E", "AUSTIN", "USA"),
            "BLJ03": ("1.43N", "311.56E", "BELEM", "BRAZIL"),
            "BC840": ("40.0N", "254.7E", "BOULDER", "USA"),
            "CAJ2M": ("-22.7N", "315.0E", "CACHOEIRA PAULISTA", "BRAZIL"),
            "DW41K": ("-12.45N", "130.95E", "DARWIN", "AUSTRALIA"),
            "DB049": ("50.1N", "4.6E", "DOURBES", "BELGIUM"),
            "FZA0M": ("-3.9N", "321.6E", "FORTALEZA", "BRAZIL"),
            "GA762": ("62.38N", "215.0E", "GAKONA", "USA"),
            "GM037": ("37.9N", "14.0E", "GIBILMANNA", "ITALY"),
            "GU513": ("13.62N", "144.86E", "GUAM", "USA"),
            "HO54K": ("-42.92N", "147.32E", "HOBART", "AUSTRALIA"),
            "IC437": ("37.14N", "127.54E", "I-CHEON", "SOUTH KOREA"),
            "IF843": ("43.81N", "247.32E", "IDAHO NATIONAL LAB", "USA"),
            "JB57N": ("-74.62N", "164.24E", "JANG BOGO", "ANTARTICA"),
            "JJ433": ("33.43N", "126.3E", "JEJU", "JAPAN"),
            "LL721": ("21.43N", "201.85E", "LUALUALEI", "USA"),
            "MHJ45": ("42.6N", "288.5E", "MILLSTONE HILL", "USA"),
            "NI135": ("35.025N", "33.157E", "NICOSIA", "CYPRUS"),
            "ND61R": ("-19.07N", "190.07E", "NIUE", "NEW ZELAND"),
            "NI63_": ("-29.03N", "167.97E", "NORFOLK", "NEW ZELAND"),
            "PE43K": ("-32.0N", "116.13E", "PERTH", "AUSTRALIA"),
            "PF765": ("65.13N", "212.55E", "POKER FLAT", "USA"),
            "PQ052": ("50.0N", "14.6E", "PRUHONICE", "CZECHIA"),
            "PA836": ("34.8N", "239.5E", "PT ARGUELLO", "USA"),
            "RM041": ("41.8N", "12.5E", "ROME", "ITALY"),
            "VT139": ("40.6N", "17.8E", "SAN VITO", "ITALY"),
            "SMK29": ("-29.728N", "306.286E", "SANTA MARIA", "BRAZIL"),
            "SO148": ("47.63N", "16.72E", "SOPRON", "HUNGARY"),
            "THJ76": ("76.54N", "291.56E", "THULE", "GREENLAND"),
            "TV51R": ("-19.63N", "146.85E", "TOWNSVILLE", "AUSTRALIA"),
            "TR169": ("69.6N", "19.2E", "TROMSO", "NORWAY"),
            "TR170": ("69.583N", "19.217E", "EISCAT TROMSO", "NORWAY"),
            "WA619": ("19.294N", "166.647E", "WAKE IS", "USA"),
            "WP937": ("37.9N", "284.5E", "WALLOPS IS", "USA"),
            "MZ152": ("52.2N", "21.1E", "WARSAW", "POLAND")
            } 
