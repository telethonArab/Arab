FROM telethonArab/telethonAr:slim-buster

#clonning repo 
RUN git clone https://github.com/telethonArab/Arab /root/Arab
#working directory 
WORKDIR /root/Arab

# Install requirements
RUN pip3 install --no-cache-dir -r requirements.txt

ENV PATH="/home/Arab/bin:$PATH"

CMD ["python3","-m","Arab"
