FROM python:3.7-alpine
WORKDIR /all
EXPOSE 8000
RUN apk --no-cache --update-cache add libxml2-dev libxslt-dev gcc gfortran python python-dev py-pip build-base wget freetype-dev libpng-dev openblas-dev
RUN ln -s /usr/include/locale.h /usr/include/xlocale.h
RUN pip install "poetry"
ADD pyproject.toml .
RUN poetry config settings.virtualenvs.create false
RUN poetry install -n
