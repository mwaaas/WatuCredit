from mwaaas/django:0.0.8

# copy requirements
COPY requirements.txt /root/requirements/

# install requirements
RUN pip install -r /root/requirements/requirements.txt --extra-index-url https://pypi.fury.io/HitVraqMKFjFX_af6rjN/afb/

# Add source code
ADD . .



