
def allowance(hra,ta,da):
    sum_allowance=hra+ta+da
    print("allowance:",sum_allowance)
    return sum_allowance

def dedutions(loan,pt):
    sum_dedutions=loan+pt
    print("dedutions:",sum_dedutions)
    return sum_dedutions

def grossal(basic,allowance):
    sum_grossal=basic+allowance
    print("netsal:",sum_grossal)
    return sum_grossal

def netsalary(grs,ded):        
    sum_netsalary=grs-ded
    print("netsalary:",sum_netsalary)
    return sum_netsalary

eno=int(input("enter employee number"))
basic=int(input("enter basic salary"))
da=int(input("enter DA:"))
ta=int(input("enter TA:"))
hra=int(input("enter HRA:"))           
pt=int(input("enter PT:"))           
loan=int(input("enter loan:"))
a= allowance(hra,ta,da)
b=grossal(basic,a)
c=dedutions(loan,pt)
d=netsalary(b,c)
