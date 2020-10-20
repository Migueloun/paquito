# http://www.cs.colby.edu/maxwell/courses/tutorials/maketutor/

# $@: left side of :
# $^: right side of :
# $<: first argument after :

# NAME OF PROJECT
PROJECT	=	SMMULT

# WRITE THE NAMES OF THE CUSTOM .h AND .o FILES CONTAINED IN
# THE SRC AND INCLUDE DIRECTORIES
_INCS	=	
_OBJS	=	main.o

SRCDIR	=	Libraries/src
INCDIR	=	Libraries/include
OBJDIR	=	Objects

CFLAGS	=	-I$(INCDIR) -Wall
LIBS	=	

CC		=	gcc
INCS	=	$(patsubst %,$(INCDIR)/%,$(_INCS))
OBJS	=	$(patsubst %,$(OBJDIR)/%,$(_OBJS))

all: $(OBJS)
	$(CC) -o $(PROJECT) $^ $(CFLAGS) $(LIBS)

clean:
	$(RM) Objects/*.o $(PROJECT)

$(OBJDIR)/%.o: $(SRCDIR)/%.c $(INCS)
	$(CC) -c -o $@ $< $(CFLAGS)

$(OBJDIR)/main.o: main.c $(INCS)
	$(CC) -c -o $@ $< $(CFLAGS)
