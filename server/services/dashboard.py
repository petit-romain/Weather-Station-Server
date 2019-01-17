from server.models.information import Information


class Dashboard():

    def getWindVelocities(self):
        return {"windVelocities": [0.5, 25.5, 50.5, 75.5, 100.5, 125.5, 150.5]}

    def getWindDirection(self):
        return {"windDirection": 45.0}

    def getTemperature(self):
        return {"temperature": 37.0}

    def getTemperatures(self):
        return {"temperatures": [-15.5, -5.5, 5.5, 15.5, 25.5, 35.5, 45.5]}

    def getHumidities(self):
        return {"humidities": [5, 20, 35, 50, 65, 80, 95]}

    def getPressures(self):
        return {"pressures": [950, 1000, 1050, 1100, 1150, 1200, 1250]}

    def getClimates(self):
        return {"climates": [0, 1, 2, 0, 1, 2, 0]}

    def getRainFallHour(self):
        return {"rainFallHou": 35.0}

    def getRainFallDay(self):
        return {"rainFallDay": 36.5}

    def getDashboard(self):
        dashboard = dict()
        dashboard.update(self.getWindVelocities())
        dashboard.update(self.getWindDirection())
        dashboard.update(self.getTemperature())
        dashboard.update(self.getTemperatures())
        dashboard.update(self.getHumidities())
        dashboard.update(self.getPressures())
        dashboard.update(self.getClimates())
        dashboard.update(self.getRainFallHour())
        dashboard.update(self.getRainFallDay())
        return dashboard
