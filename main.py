from datetime import datetime
import logging
import sys
import argparse


# Fonction qui lit et découpe le fichier

def read_plan(file):

    dic = {}
    res = []
    with open(file, "r") as f:
        for i in f:        
            res.append(i.split())
            logging.info("Lecture du fichier")
        for row in range(1, len(dic)):    
            newliner = " ".join(row[1:])
            time = " ".join(row[:1])
            timer = time.split("-")            
            start, end = "".join(timer[:1]), "".join(timer[1:])
            if row!=[]:
                dic[newliner]=[start, end]
                logging.info("découpage de la ligne")
                print(start, end)
            
            
            # print(start, end)
                
            
        #     return start, end

print(read_plan('planning.log'))

# Fontion pour calculer la duree

def times():
    a = read_plan("planning.log")
    with open("expected_output.txt", "r") as f:
        for i in a:
            start = str(a[0])
            end = str(a[1])
            FM = '%H:%M'
            duree = datetime.strptime(start, FM) - datetime.strptime(end, FM)    
    return duree

# times()

def print_result(dur):
    
    duree_total=sum(dur.values())
    for h in sorted(dur.keys()):
        a=h
        b=dur[h]
        # only want the truncated percentage
        c=int((b/total_min)*100)
        
        # transform to strings and compute necessary lengths
        b=str(b)+" minutes"
        c=str(c)+"%"
        c=" "*(6-len(c))+str(c)
        a=a+(43-(len(a)+len(b)+len(c)))*" "

        print(a+b+c)

# def all():
#     with open("planning.log", "r") as f:
#         e = f.readline()
#         for i in e:
#             print(times())

# all()




def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("path")
 
    args=parser.parse_args()
    with open(args.path,"r") as f:
        c,d = parse_file(f)
        print_result(d)



# if __name__=="__main__":
    # sys.exit(main()