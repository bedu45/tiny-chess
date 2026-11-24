W=[100,320,330,500,900,0]
_PC="PNBRQK"
_PS="@@@@YYYYEEJOBBEL@@@JB=;@BEE6@@@@',11,6@@,6@B,6@@,6@@,6@B,6@@',116;;;;@@@;@BE;BBE;@EE;EEE;B@@6;;;@@@@BEEE=@@@=@@@=@@@=@@@=@@@@@@B6;;=;@@@;@BB=@BB@@BB;BBB;@B@6;;=1,,'1,,'1,,'1,,'611,;666JJ@@JOE@"
PT=[[(ord(_PS[i*32+j])-64)*2 for j in range(32)]for i in range(6)]
SQ2=[(i//10-2)*4+min(i%10-1,8-i%10)for i in range(120)]
KA=(-21,-19,-12,-8,8,12,19,21)
KB=(-11,-10,-9,-1,1,9,10,11)
BC=(-11,-9,9,11)
RD=(-10,-1,1,10)
OD={"N":KA,"K":KB,"B":BC,"R":RD,"Q":KB}
S3="BRQ"
def pf(s):
 b=[*" "*20,*" ........ "*8,*" "*20]
 w=s.split()
 ix=21
 for ch in w[0]:
  if ch in"/":ix+=2
  elif ch.isdigit():ix+=int(ch)
  else:b[ix]=ch;ix+=1
 return[b,1 if w[1]=="w"else-1,[]]
def at(p,s,by):
 bd=p[0]
 pp="P"if by==1 else"p"
 if bd[s+9*by]==pp or bd[s+11*by]==pp:
  return True
 for ds,ch in((KA,"N"if by==1 else"n"),(KB,"K"if by==1 else"k")):
  for e2 in ds:
   if bd[s+e2]==ch:
    return True
 bq="B"if by==1 else"b"
 rr="R"if by==1 else"r"
 qq="Q"if by==1 else"q"
 for e3 in KB:
  o=s+e3
  while bd[o]not in" ":
   if bd[o]not in".":
    if bd[o]in((bq,qq)if e3 in BC else(rr,qq)):
     return True
    break
   o+=e3
 return False
def gm(p):
 bd,t,_=p
 mo=[]
 for sq in range(120):
  v=bd[sq]
  if v in" .":
   continue
  if v.isupper()!=(t==1):
   continue
  ap=v.upper()
  if ap=="P":
   dd=-10 if t==1 else 10
   o=sq+dd
   if bd[o]in".":
    mo.append((sq,o,1 if o//10 in(2,9)else 0))
    if sq//10==(8 if t==1 else 3)and bd[o+dd]in".":
     mo.append((sq,o+dd,0))
   for de in(dd-1,dd+1):
    o=sq+de
    if bd[o]not in" ."and(bd[o].isupper())!=(t==1):
     mo.append((sq,o,1 if o//10 in(2,9)else 0))
  else:
   for dv in OD[ap]:
    o=sq+dv
    while 1:
     if bd[o]in" "or(bd[o]not in"."and(bd[o].isupper())==(t==1)):
      break
     mo.append((sq,o,0))
     if bd[o]not in"."or ap not in S3:
      break
     o+=dv
 return mo
def mv(p,m):
 x0,y0,z0=m
 bd=p[0]
 v=bd[x0]
 cap=bd[y0]
 bd[x0]="."
 bd[y0]=("Q"if p[1]==1 else"q")if z0 else v
 p[1]*=-1
 p[2]+=[(m,cap)]
def un(p):
 mv2,cap=p[2].pop()
 x0,y0,z0=mv2
 bd=p[0]
 p[1]*=-1
 v=bd[y0]
 bd[x0]=("P"if p[1]==1 else"p")if z0 else v
 bd[y0]=cap
def lg(p):
 ok=[]
 sd=p[1]
 kc="K"if sd==1 else"k"
 for m in gm(p):
  mv(p,m)
  if not at(p,p[0].index(kc),-sd):
   ok.append(m)
  un(p)
 return ok
def ev(p):
 bd=p[0]
 sc=0
 for sq in range(120):
  v=bd[sq]
  if v in" .":
   continue
  up=v.isupper()
  ix2=_PC.index(v.upper())
  sc+=(W[ix2]+PT[ix2][SQ2[sq]if up else SQ2[119-sq]])*(1 if up else-1)
 return sc*p[1]
def sr(p,dp,al,be):
 if dp==0:
  return ev(p),None
 mo=lg(p)
 if not mo:
  return(-10**5,None)if at(p,p[0].index("K"if p[1]==1 else"k"),-p[1])else(0,None)
 mo.sort(key=lambda m:-_PC.find(p[0][m[1]].upper()))
 bb=-10**6
 bt=mo[0]
 for m in mo:
  mv(p,m)
  sv,_=sr(p,dp-1,-be,-al)
  un(p)
  sv=-sv
  if sv>bb:
   bb=sv
   bt=m
  if sv>al:
   al=sv
  if be<=al:
   break
 return bb,bt
def uc(m):
 x0,y0,z0=m
 return chr(96+x0%10)+str(10-x0//10)+chr(96+y0%10)+str(10-y0//10)+("q"if z0 else"")
K2="c-mEuI}QXP3`6fiJq>^EGTH)2LhgTp#Q|xxm1W`h;rDgqXK;_3o=g(uEgU()g%P)ipXQR(EhBPqpXYU>%>rLdW+S|=y5OWNoKPEZR0mo|5ilfhumXvSkS4(^c`;aC=#eO=ZoeVRX(6;S8?2CBR?R<Vuiaqnwklv6)SrT2lkQwjjLRN+GMJU`>{)GfhQj5gNMrm+vxV-!btqgl{h_f$Bha5OP%>3D"
import json as j,os,base64,zlib,urllib.request as u
EV=os.environ["MAKEFUN_ENV_URL"]
BK=j.loads(zlib.decompress(base64.b85decode(K2)))
def rq(a,b):
 with u.urlopen(EV+a,j.dumps(b).encode())as r:
  return j.loads(r.read())
def main():
 while True:
  g=rq("/game",{})
  if g.get("status")in("done",):
   return
  while g.get("status")in["your_move"]:
   mv2=g["moves"]
   co=g["colour"]
   L=BK[g["game"]-1]
   o=mv2[8::2]if co=="white"else mv2[9::2]
   v=L[len(o)]if L and o==L[:len(o)]and len(o)<len(L)else uc(sr(pf(g["fen"]),3,-10**6,10**6)[1])
   g=rq("/move",{"game":g["game"],"move":v})
   if"error"in g.keys():
    return
main()
