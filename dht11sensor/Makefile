CFLAGS=-Wall -lwiringPi -O2
TARGET=dht11
PREFIX=/usr/local/bin
SRCS=dht11.c
OBJS=$(SRCS:.c=.o)

.PHONY: all clean install uninstall

all: $(TARGET)
$(TARGET): $(OBJS)
				$(CC) -o $(TARGET) $(OBJS) $(CFLAGS)

.c.o:
				$(CC) $(CFLAGS)  -c $< -o $@

clean:
				rm -rf $(TARGET) $(OBJS)
install:
				install $(TARGET) $(PREFIX)
uninstall:
				rm -rf $(PREFIX)/$(TARGET)

