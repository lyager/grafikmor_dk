FROM arm64v8/alpine

RUN apk --update add go
RUN apk --upgrade add libc-dev
# RUN apk --upgrade add gcc
RUN apk --update add git
ADD . /root/go/src/github.com/lyager/grafikmor_dk
RUN cd /root/go/src/github.com/lyager/grafikmor_dk && go get

CMD /root/go/bin/grafikmor_dk

