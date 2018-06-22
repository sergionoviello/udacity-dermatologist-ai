FROM ermaker/keras

RUN conda install -y \
    jupyter \
    matplotlib \
    seaborn

RUN pip install flask \
    tensorflow --upgrade

RUN  pip install numpy \
     scipy \
     scikit-learn

RUN pip install pillow
RUN pip install opencv-python

VOLUME /app
WORKDIR /app

EXPOSE 8888

#COPY . /app

ENTRYPOINT ["jupyter", "notebook", "--ip=0.0.0.0", "--allow-root", "--NotebookApp.token=''"]