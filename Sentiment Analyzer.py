

def read_list():
    source=[]
    with open ("Trial.txt","r") as file1:
        for item in file1:
            source=file1.read().split()
    return source

def positive_reference():
    positive=[]
    with open("Positive_reference.txt","r") as file2:
        positive=file2.read().split()
        return positive

def overlap_checker(source,positive):
    overlap=[]
    for x in source:
            if x in positive: 
                overlap.append(x)
            else: continue
    return overlap 

def main():
    x=[]
    read_list()
    source=read_list()
    positive_reference()
    positive=positive_reference()
    overlap_checker(source,positive)
    x=overlap_checker(source,positive)
    l=len(x)
    o=len(source)
    percent=l/o*100
    print(x)
    print(round(percent,2),"% of total press release is positive adjectives") 
 
main()
