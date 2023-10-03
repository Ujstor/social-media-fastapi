FROM python:3.9.7

WORKDIR /src/

COPY . .

EXPOSE 8010

RUN pip install --no-cache-dir -r requirements.txt

RUN chmod +x build.sh

ENTRYPOINT ["/src/build.sh"]
