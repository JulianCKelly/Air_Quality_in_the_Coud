"""OpenAQ Air Quality Dashboard with Flask."""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import openaq


app = Flask(__name__)
api = openaq.OpenAQ()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
DB = SQLAlchemy(app)


def get_results():
    status, body = api.measurements(city='Los Angeles', parameter='pm25')
    results = body['results']
    data = [(entry['date']['utc'], entry['value']) for entry in results]
    return data


@app.route('/')
def root():
    """Base view."""
    records = Record.query.filter(Record.value >= 18).all()
    return str(records)


class Record(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    datetime = DB.Column(DB.String)
    value = DB.Column(DB.Float, nullable=False)

    def __repr__(self):
        return f'Record(datetime={self.datetime}, value={self.value})'


@app.route('/refresh')
def refresh():
    """Pull fresh data from Open AQ and replace existing data."""
    DB.drop_all()
    DB.create_all()
    data = get_results()
    records = [Record(datetime=entry[0], value=entry[1]) for entry in data]
    DB.session.add_all(records)
    DB.session.commit()
    return 'Data refreshed!'


if __name__ == '__main__':
    app.run()
