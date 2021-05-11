import datetime as dt
import logging
import sys, os
import argparse



def read_plan(planning):

    """ This function allows to read the specified file """

    planning = []
    with open(planning, "r") as f:
        # logging.warning("Ouverture du fichier")
        for row in f.readlines():
            logging.info("Lecture du fichier")
            if row != "\n":
                logging.info("Ajouter des lignes")
                planning += [row.strip()]
        
    return planning


# print(read_plan("planning.log"))

def times(start,end):

    """ This function allows to read the specified file """

    FM = '%H:%M'
    start = dt.datetime.strptime(start, FM)
    end = dt.datetime.strptime(end, FM)  
    time_delta = end-start  
    return time_delta.seconds//60
    

def list_duree():

    """ this function returns the activities with their schedules to a dictionary """

    dic = {}
    f = read_plan("planning.log")
    for line in f:
        if not line.isspace():
            activity = line[12:].strip()
            lines = line.split()
            hour = lines[0].split("-")
            time = times(hour[0],hour[1])
            if activity not in dic:
                dic[activity]=time
            else :
                dic[activity]+=time

    return dic

def pourcent():
    res = []
    total = 0
    duree = list_duree()
    if duree != "None":
        for i in duree.items():
            total+=1
    for e in duree.values():
        res.append(e)
    return res

    
def write_plan():
    space = " "
    duree = list_duree()
    sum_time = sum(duree.values())
    for activity, time in duree.items():
        result = f'{activity:19} {time:5} minutes {space*5} {int(time/sum_time*100):3} %'
        print(result)
    
    
# write_plan()




def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("path")
 
    args=parser.parse_args()
    with open(args.path,"r") as f:
        c,d = parse_file(f)
        print_planningult(d)



# if __name__=="__main__":
    # sys.exit(main()