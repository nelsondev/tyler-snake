TARGET = tyler
USER = nelr
HOSTNAME = pi4

all: $(TARGET)

$(TARGET):
	sh ./scripts/push.sh
	ssh -T $(USER)@$(HOSTNAME) "cd $(TARGET) && git pull & exit"