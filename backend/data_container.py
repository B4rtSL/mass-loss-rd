class airplane:
    def __init__(self, startmass, empty_mass, nompow, fuelcons, propnumber, aspectratio, cx0, area, vmin, vmax, wmax, fuelmass, proptype: str, czmax):
         self.startmass = startmass
         self.empty_mass = empty_mass
         self.nompow = nompow
         self.fuelcons = fuelcons
         self.propnumber = propnumber
         self.aspectratio = aspectratio
         self.cx0 = cx0
         self.area = area
         self.vmin = vmin
         self.vmax = vmax
         self.wmax = wmax
         self.fuelmass = fuelmass
         self.proptype = proptype
         self.czmax = czmax

cessna = airplane(725.75, 504, 74.6, 0.233385, 1, 2.855, 0.0269, 14.865, 26.05, 56.60, 2.88, 71, 'propeller', 1.156)

class Cessna150:
    startmass = 727.75
    empty_mass = 504
    nompow = 74.6
    fuelcons = 0.266655496
    propnumber = 1
    aspectratio = 2.855
    cx0 = 0.0269
    area = 14.865
    vmin = 26.05
    vmax = 54.98
    wmax = 2.88
    fuelmass = 71
    proptype = 'propeller'
    czmax = 1.156


class Hawker:
    startmass = 6140
    empty_mass = 4080
    nompow = 1292
    fuelcons = 0.305
    propnumber = 1
    aspectratio = 4.656
    cx0 = 0.0252
    area = 28.06
    vmin = 47
    vmax = 194.44
    wmax = 24
    fuelmass = 832.35
    proptype = 'propeller'
    czmax = 1.51