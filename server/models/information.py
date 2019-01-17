from peewee import Model, BigIntegerField, FloatField, IntegerField
from server import db


class Information(Model):
    captured_time = BigIntegerField()
    climat = IntegerField()
    temperature = FloatField()
    pressure = FloatField()
    humidity = FloatField()
    wind_velocity = FloatField()
    wind_direction = FloatField()
    rain_fall = FloatField()

    def serialize(self):
        return {
            'captured_time': self.captured_time,
            'climat': self.climat,
            'temperature': self.temperature,
            'pressure': self.pressure,
            'humidity': self.humidity,
            'wind_velocity': self.wind_velocity,
            'wind_direction': self.wind_direction,
            'rain_fall': self.rain_fall,
        }

    class Meta:
        database = db
