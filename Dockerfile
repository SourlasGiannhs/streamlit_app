#Για την εκτέλεση της εφαρμογής θα χρειαστούμε ενα official image της Python ως βάση
FROM python:3.9
#Ορίζουμε το directory μέσα στο container
WORKDIR /usr/src/app
#Αντιγράφουμε τα requirements.txt στο container
COPY requirements.txt ./
#εγκαθιστούμε τις απαραίτητες επεκτάσεις για την εφαρμογή
RUN pip install --no-cache-dir -r requirements.txt
#Αντιγράφουμε ολα τα αρχεία 
COPY . .
#Εκθέτουμε την θύρα στην οποία τρέχει η εφαρμογή μας
EXPOSE 8501
#Ορίζουμε την εντολή για εκτέλεση κατα την εκκίνηση του container
CMD ["streamlit", "run", "Home.py"]
