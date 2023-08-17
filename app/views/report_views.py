from flask import Blueprint, render_template, session, abort
from models.reports import Reports

report_views = Blueprint('report',__name__)

@report_views .route("/reportes/")
def reports ():
<<<<<<< HEAD
    if session.get('user') and session.get('user')['role']==1:
        reports = Reports.get_all()
        return render_template('reports/reports.html',
                            reports= reports)
    else: 
=======
    if session.get('user')['rol'] == 1:
        reports = Reports.get_all()
        return render_template('reports/reports.html',
                           reports= reports)
    else:
>>>>>>> c48ae21c87754321f63b1dad2a4976c86d1d5810
        abort(403)