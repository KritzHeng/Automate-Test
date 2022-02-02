import time
import math   

x_min = 0
x_max = 0
y_min = 0
y_max = 0

pass_count = 0
fail_count = 0

list_test=[]
list_input=[]
list_expected=[]

new_expected = []
list_error = []
list_output = []
a = []

start_time = time.ctime()


def bva(x_min, x_max, y_min, y_max):

        x.append((x_max+x_min)/2)
        y.append((y_max+y_min)/2)
        x.append((x_max+x_min)/2)
        y.append(y_min)
        x.append((x_max+x_min)/2)
        y.append(y_min+1)
        x.append(x_min)
        y.append(((y_max+y_min)/2))
        x.append(x_min+1)
        y.append((y_max+y_min)/2)
        x.append(x_max-1)
        y.append((y_max+y_min)/2)   
        x.append(x_max)
        y.append((y_max+y_min)/2)
        x.append((x_max+x_min)/2)
        y.append(y_max-1)
        x.append((x_max+x_min)/2)
        y.append(y_max)
         
def robustness(x_min, x_max, y_min, y_max):
        x.clear()
        y.clear()

        #left
        x.append(x_min-1)
        y.append(math.floor((y_min+y_max)/2))
        x.append(x_min)
        y.append(math.floor((y_min+y_max)/2))
        x.append(x_min+1)
        y.append(math.floor((y_min+y_max)/2))

        #lower
        x.append(math.floor((x_min+x_max)/2))
        y.append(y_min-1)
        x.append(math.floor((x_min+x_max)/2))
        y.append(y_min)
        x.append(math.floor((x_min+x_max)/2))
        y.append(y_min+1)

        #top
        x.append(math.floor((x_min+x_max)/2))
        y.append(y_max-1)
        x.append(math.floor((x_min+x_max)/2))
        y.append(y_max)
        x.append(math.floor((x_min+x_max)/2))
        y.append(y_max+1)

        #right
        x.append(x_max+1)
        y.append(math.floor((y_min+y_max)/2))
        x.append(x_max)
        y.append(math.floor((y_min+y_max)/2))
        x.append(x_max-1)
        y.append(math.floor((y_min+y_max)/2))

        #middle
        x.append(math.floor((x_min+x_max)/2))
        y.append(math.floor((y_min+y_max)/2))

def worse(x_min, x_max, y_min, y_max):
        x.clear()
        y.clear()
        x.append(math.floor((x_min+x_max)/2))
        y.append(y_min)
        x.append(math.floor((x_min+x_max)/2))
        y.append(y_min+1)
        x.append(math.floor((x_min+x_max)/2))
        y.append(y_max-1)
        x.append(math.floor((x_min+x_max)/2))
        y.append(y_max)
        x.append(x_max-1)
        y.append(math.floor((y_min+y_max)/2))
        x.append(x_max)
        y.append(math.floor((y_min+y_max)/2))
        x.append(x_min)
        y.append(math.floor((y_min+y_max)/2))
        x.append(x_min+1)
        y.append(math.floor((y_min+y_max)/2))
        x.append(x_min)
        y.append(y_max)
        x.append(x_min)
        y.append(y_max-1)
        x.append(x_min+1)
        y.append(y_max)
        x.append(x_min+1)
        y.append(y_max-1)
        x.append(x_min)
        y.append(y_min)
        x.append(x_min+1)
        y.append(y_min)
        x.append(x_min+1)
        y.append(y_min+1)
        x.append(x_min)
        y.append(y_min+1)
        x.append(x_max)
        y.append(y_min)
        x.append(x_max)
        y.append(y_min+1)
        x.append(x_max-1)
        y.append(y_min)
        x.append(x_max-1)
        y.append(y_min+1)
        x.append(x_max)
        y.append(y_max)
        x.append(x_max)
        y.append(y_max-1)
        x.append(x_max-1)
        y.append(y_max)
        x.append(x_max-1)
        y.append(y_max-1)
        x.append(math.floor((x_min+x_max)/2))
        y.append(math.floor((y_min+y_max)/2))
    


def WorseRobustness(x_min, x_max, y_min, y_max):
        x.clear()
        y.clear()
        x.append((x_min+x_max)/2)
        y.append(y_min-1)
        x.append((x_min+x_max)/2)
        y.append(y_min)
        x.append((x_min+x_max)/2)
        y.append(y_min+1)
        x.append((x_min+x_max)/2)
        y.append(y_max-1)
        x.append((x_min+x_max)/2)
        y.append(y_max)  
        x.append((x_min+x_max)/2)
        y.append(y_max+1) 
        x.append(x_min)
        y.append(y_max)
        x.append(x_min)
        y.append(y_max-1)
        x.append(x_min+1)
        y.append(y_max)
        x.append(x_min+1)
        y.append(y_max-1)
        x.append(x_min)
        y.append(y_min)
        x.append(x_min+1)
        y.append(y_min)
        x.append(x_min+1)
        y.append(y_min+1)
        x.append(x_min)
        y.append(y_min+1)
        #
        x.append(x_max)
        y.append(y_min)
        x.append(x_max)
        y.append(y_min+1)
        x.append(x_max-1)
        y.append(y_min)
        x.append(x_max-1)
        y.append(y_min+1)
        #
        x.append(x_max)
        y.append(y_max)
        x.append(x_max)
        y.append(y_max-1)
        x.append(x_max-1)
        y.append(y_max)
        x.append(x_max-1)
        y.append(y_max-1)
        x.append(x_max+1)
        y.append((y_min+y_max)/2)
        x.append(x_max)
        y.append((y_min+y_max)/2)
        x.append(x_max-1)
        y.append((y_min+y_max)/2)
        x.append(x_min+1)
        y.append((y_min+y_max)/2)
        x.append(x_min)
        y.append((y_min+y_max)/2)
        x.append(x_min-1)
        y.append((y_min+y_max)/2)
        x.append(x_min-1)
        y.append(y_max-1)
        x.append(x_min-1)
        y.append(y_max)
        x.append(x_min-1)
        y.append(y_max+1)
        x.append(x_min)
        y.append(y_max+1)
        x.append(x_min+1)
        y.append(y_max+1)
        x.append(x_min+1)
        y.append(y_min-1)
        x.append(x_min)
        y.append(y_min-1)
        x.append(x_min-1)
        y.append(y_min-1)
        x.append(x_min-1)
        y.append(y_min)
        x.append(x_min-1)
        y.append(y_min+1)
        x.append(x_max-1)
        y.append(y_min-1)
        x.append(x_max)
        y.append(y_min-1)
        x.append(x_max+1)
        y.append(y_min-1)
        x.append(x_max+1)
        y.append(y_min)
        x.append(x_max+1)
        y.append(y_min+1)
        x.append(x_max-1)
        y.append(y_max+1)
        x.append(x_max)
        y.append(y_max+1)
        x.append(x_max+1)
        y.append(y_max+1)
        x.append(x_max+1)
        y.append(y_max)
        x.append(x_max+1)
        y.append(y_max-1)  
        x.append((x_min+x_max)/2)
        y.append((y_min+y_max)/2)


def using_listinput(n):
    try:
        x_min = int(n[0])
        x_max = int(n[1])
        y_min = int(n[2])
        y_max = int(n[3])
        choice = n[4]
        if(x_min > x_max or y_min > y_max):
            list_error.append(1)
            # 1
        else:
            if choice.upper() == "BVA":
                bva(x_min, x_max, y_min, y_max)
                list_error.append(0)
            elif choice.upper() == "ROBUSTNESS":
                robustness(x_min, x_max, y_min, y_max)
                list_error.append(0)
            elif choice.upper() == "WORSE CASE":
                worse(x_min, x_max, y_min, y_max)
                list_error.append(0)
            elif choice.upper() == "WORSE CASE FOR ROBUSTNESS":
                WorseRobustness(x_min, x_max, y_min, y_max)
                list_error.append(0)
            else:
                list_error.append(1)
                # 1
    except ValueError:
        list_error.append(1)
        # 1
    except IndexError:
        list_error.append(2)
        # 2

try:
	fh = open('Test_Case.txt', 'r')
	count = 0
	for i in (fh):
		a.append(i.split("|"))
		count+=1
	fh.close()	
except FileNotFoundError:
	log = open('Log.txt', 'a')
	log.write("{\n")
	log.write("\tStart Date : " + str(start_time))
	log.write("\n")
	log.write("\tEnd Date : " + str(time.ctime()))
	log.write("\n")
	log.write("\tError : " + str(3))
	log.write("\n")
	log.write("}\n")
	quit()
for i in a:
    for x,j in enumerate(i):
        if(x == 0):
            list_test.append(j)
        elif(x == 1):
            list_input.append(j)
        elif(x == 2):
            list_expected.append(j)

for i in list_expected:
    a = i.replace("[","")
    a = a.replace("]","")
    a = a.replace("\n","")
    new_expected.append("["+a+"]")
count = 0
for i in list_input:
    string_input = ""
    x = []
    y = []
    a = i.replace("{","")
    a = a.replace("}","")
    a = a.split(",")
    using_listinput(a)
    merge_list = list(zip(x, y))
    r = set(tuple(element) for element in merge_list)
    list_output.append(list(r))
    r = list(r)
    for x, i in enumerate(r):
        if x!=len(r)-1:
            string_input+=str(i)+", "
        else:
            string_input+=str(i)
    string_input = "["+string_input+"]"
    if string_input == new_expected[count]:
        pass_count +=1
    else:
        fail_count +=1
    
    count+=1

log = open('Log.txt', 'a')
log.write("{\n")
log.write("\tStart Date : " + str(start_time))
log.write("\n")
log.write("\tEnd Date : " + str(time.ctime()))
log.write("\n")
log.write("\tPass Test Case : " + str(pass_count))
log.write("\n")
log.write("\tFail Test Case : " + str(fail_count))
log.write("\n")

def check(list_actual,list_output):
    if str(list_actual) == str(list_output):
        return "Pass"
    else:
        return "Fail"

for x, i in enumerate(new_expected):
    log.write("\tTC#"+str(list_test[x])+" : "+ check(i,list_output[x])+" | Error code: "+str(list_error[x]) +"\n\t\tExpected result: "+ str(i)+"\n\t\tActual result: "+ str(list_output[x])+"\n")
log.write("}\n")
fh.close()