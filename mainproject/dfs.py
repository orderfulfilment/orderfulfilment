def traverse( N, ts, minu, patternutility,ubitem, ubfpe,trans,qty,prf,rs1):
    patternutility = 0;
    ubitem = 0;
    ubfpe = 0;
    LN = N[len(N) - 1]


    for i in range(len(trans)):
        flg=0
        transaction = trans[i]
        quantity = qty[i]
        profit =prf[i]
        transactionrv=""
        quantityrv=""
        profitrv=""
        
        for j in transaction: 
            transactionrv = j + transactionrv
        for j in quantity: 
            quantityrv = j + quantityrv
        for j in profit: 
            profitrv = j + profitrv
        sp = transactionrv.split(':');
        q = quantityrv.split(':');
        p = profitrv.split(':');
        
        p=' '.join(p).split()
        q=' '.join(q).split()
        sp=' '.join(sp).split()
        
        
        tu = prf[i]
        sp1 = N.split(':');
        prefixendbeforechar = "";
        
        
        
        lsp1=[]
        for n in range(len(sp1)):
            
            lsp1.append(sp1[n])
                
#         print('lsp1',lsp1)
        lsp= []
        for b in range(len(sp)):
            lsp.append(sp[b])

#         print('lsp',lsp)
        count = 0;
        
        for j in range(len(sp)):
            for k in range(len(sp1)):
                if (sp[j] == sp1[k]):
                    count=count+1
                   
#         print('cnt',count)     
#                     //checking the patter is contain in transation 
        if len(sp1) == count: 
            frst = sp1[0]
            nn = N;
            nnarray = nn.split(':')
            nlist = []  
            
            for y in range(len(nnarray)- 1):
                nlist.append(nnarray[y])
                    


            prefixendindex = 0;
            prefixend = sp1[len(sp1) - 1]
            
            
            if len(sp1) >= 2:
                prefixendbeforechar = sp1[1];
                prefixendbeforecharindex = 0;
                for  m1 in range (len(sp)):
                    if (sp[m1] == prefixendbeforechar):
                        prefixendbeforecharindex = m1;
                        break;

                            
                        
                for  m2 in range( prefixendbeforecharindex,len(sp)):
                    a = int(p[m2])
                    b = int(q[m2])
#                             //ubfpe += a * b;
            lastnode = []
            for j1 in range(len(rs1)):
                if (LN != rs1[j1][0]):
                               
                    lastnode.append(rs1[j1][0])
                else:
                    break

            lastnode.append(LN)
            d=len(lastnode)-1
            while d >=0:
               
                if lastnode[d] in lsp:
                    for z in range (len(sp)):
                        if (lastnode[d] ==sp[z] ):
                           
                            for y in range(z,len(sp)):
                                if(lastnode[d] in lsp):
                                    a = int(p[y])
                                    b = int(q[y])
                                    ubfpe += a * b;
                d=d-1
                                        
                                    

                                   
            mbbbb=0;
                            



            for  m in range(len(sp)):
                if (sp[m] == prefixend):
                    prefixendindex = m;
                    break;
            p=' '.join(p).split()
            q=' '.join(q).split()
            for  n in range( prefixendindex):
               
                
                a = int(p[n])
                b = int(q[n]);


                if(sp[n] in nlist):
                    ubfpe += (a * b); 
                                


                if ((sp[n] == frst) or (flg==1)):
                       

                    flg = 1

                    ubitem += a * b;

                                 
                                

#                                 /////l2 do




                if (sp[n] in lsp1):
                    patternutility = patternutility + (a * b);
                              
            n=prefixendindex+1
            
            while n<len(sp):
                a1 = int(p[n])
                b1 =int(q[n])


                if ((flg == 1)):
                    flg = 1
                    ubitem += a1 * b1;
                n=n+1

        flg=0 
#     print('ub',ubitem)
#     print('pt',patternutility)
#     print('ubf',ubfpe)
    return ubfpe,ubitem,patternutility  
def getremainingprefixitems(patternend,rs):
    res =[]
   
    for i in range(len( rs)):
       
        if (str(patternend )!= str(rs[i][0])):
            
            res.append(rs[i][0])
                
        else:
           
            break;
               
   
    return res;

                             


            
                            




                               
                            
            

                        

                    
            

        
#         
    