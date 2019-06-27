from luupsmap import app, db
from luupsmap.model import Venue, Location, Interval, Voucher


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Venue': Venue, 'Location': Location, 'Interval': Interval}
