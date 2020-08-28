import requests

class Covid:
    def __init__(self):
        self.source_url='https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-json/dpc-covid19-ita-andamento-nazionale.json' 
        y, length = self.get_covid()
        x = y[length]
        self.nuovi_deceduti = self.get_nuovi_deceduti(y, length)
        self.stato = x['stato']
        self.ricoverati_con_sintomi = x['ricoverati_con_sintomi']
        self.terapia_intensiva = x['terapia_intensiva']
        self.totale_ospedalizzati = x['totale_ospedalizzati']
        self.isolamento_domiciliare = x['isolamento_domiciliare']
        self.totale_positivi = x['totale_positivi']
        self.variazione_totale_positivi = x['variazione_totale_positivi']
        self.nuovi_positivi = x['nuovi_positivi']
        self.dimessi_guariti = x['dimessi_guariti']
        self.deceduti = x['deceduti']
        self.casi_da_sospetto_diagnostico = x['casi_da_sospetto_diagnostico']
        self.casi_da_screening = x['casi_da_screening']
        self.totale_casi = x['totale_casi']
        self.tamponi = x['tamponi']
        self.casi_testati = x['casi_testati']
        self.note = x['note']   
    

    def get_covid(self):
        response = requests.get(self.source_url)
        x = response.json()
        length = -1
        for item in x:
            length = length+1
        return x, length

    def get_nuovi_deceduti(self, y, length):
        new = y[length]['deceduti'] - y[length-1]['deceduti']
        if new < 0:
            return 'ERROR'
        else:
            return new

    def getSmallReport(self):
        message = 'Totale positivi: {}\nNuovi positivi: {}\nGuariti: {}\nDeceduti: {}\nNuovi Deceduti: {}\nTamponi: {}'.format(self.totale_positivi, self.nuovi_positivi,self.dimessi_guariti,self.deceduti,self.nuovi_deceduti, self.tamponi)
        return message

    def getFullReport(self):
        message = '=======\nStato: {}\nRicoverati con sintomi: {}\nTerapia intensiva: {}\nTotale ospedalizzati: {}\nIsolamento domiciliare: {}\n\nTotale positivi: {}\nVariazione totale positivi: {}\n\nNuovi positivi: {}\nGuariti: {}\nDeceduti: {}\nNuovi Deceduti: {}\nCasi da sospetto diagnostico: {}\nCasi da screening: {}\nTotale casi: {}\nTamponi: {}\nCasi testati: {}\nNote {}\n======='.format(self.stato,self.ricoverati_con_sintomi,self.terapia_intensiva,self.totale_ospedalizzati ,self.isolamento_domiciliare ,self.totale_positivi ,self.variazione_totale_positivi ,self.nuovi_positivi ,self.dimessi_guariti ,self.deceduti ,self.nuovi_deceduti,self.casi_da_sospetto_diagnostico ,self.casi_da_screening ,self.totale_casi,self.tamponi ,self.casi_testati ,self.note)
        return message