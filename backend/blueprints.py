from app.views.jobs import jobs_bp

def register_bps(app):
    app.register_blueprint(jobs_bp, url_prefix="/api/v1/jobs")