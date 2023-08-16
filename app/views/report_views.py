from flask import Blueprint, render_template, session, abort
from models.reports import Reports

report_views = Blueprint('report',__name__)

@report_views .route("/reportes/")
def reports ():
    if session.get('user')['rol'] == 1:
        reports = Reports.get_all()
        return render_template('reports/reports.html',
                           reports= reports)
    else:
        abort(403)