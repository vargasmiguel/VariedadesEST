import pandas as pd
import streamlit as st
import numpy as np
from time import sleep
#from sympy import simplify

st.set_page_config(layout="centered",
    page_title="Lie Groups Geometry",
    page_icon="🕰️"
)


# Simbolos de Christoppher

def displaylatex(s, l):
    c = st.columns(l)
    with c[1]:
        st.markdown('$\displaystyle {}$'.format(s))
    #return st.html('''<p style="text-align: center;><span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mstyle scriptlevel="0" displaystyle="true"><mo stretchy="false">[</mo><msub><mi>e</mi><mi>i</mi></msub><mo separator="true">,</mo><msub><mi>e</mi><mi>j</mi></msub><mo stretchy="false">]</mo><mo>=</mo><munderover><mo>∑</mo><mrow><mi>k</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></munderover><msubsup><mi>c</mi><mrow><mi>i</mi><mi>j</mi></mrow><mi>k</mi></msubsup><msub><mi>e</mi><mi>k</mi></msub></mstyle></mrow><annotation encoding="application/x-tex">\displaystyle {}</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 1.0361em; vertical-align: -0.2861em;"></span><span class="mopen">[</span><span class="mord"><span class="mord mathnormal">e</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height: 0.3117em;"><span style="top: -2.55em; margin-left: 0em; margin-right: 0.05em;"><span class="pstrut" style="height: 2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight">i</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height: 0.15em;"><span></span></span></span></span></span></span><span class="mpunct">,</span><span class="mspace" style="margin-right: 0.1667em;"></span><span class="mord"><span class="mord mathnormal">e</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height: 0.3117em;"><span style="top: -2.55em; margin-left: 0em; margin-right: 0.05em;"><span class="pstrut" style="height: 2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight" style="margin-right: 0.05724em;">j</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height: 0.2861em;"><span></span></span></span></span></span></span><span class="mclose">]</span><span class="mspace" style="margin-right: 0.2778em;"></span><span class="mrel">=</span><span class="mspace" style="margin-right: 0.2778em;"></span></span><span class="base"><span class="strut" style="height: 2.9535em; vertical-align: -1.3021em;"></span><span class="mop op-limits"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height: 1.6514em;"><span style="top: -1.8479em; margin-left: 0em;"><span class="pstrut" style="height: 3.05em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathnormal mtight" style="margin-right: 0.03148em;">k</span><span class="mrel mtight">=</span><span class="mord mtight">1</span></span></span></span><span style="top: -3.05em;"><span class="pstrut" style="height: 3.05em;"></span><span><span class="mop op-symbol large-op">∑</span></span></span><span style="top: -4.3em; margin-left: 0em;"><span class="pstrut" style="height: 3.05em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight">n</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height: 1.3021em;"><span></span></span></span></span></span><span class="mspace" style="margin-right: 0.1667em;"></span><span class="mord"><span class="mord mathnormal">c</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height: 0.8991em;"><span style="top: -2.453em; margin-left: 0em; margin-right: 0.05em;"><span class="pstrut" style="height: 2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathnormal mtight" style="margin-right: 0.05724em;">ij</span></span></span></span><span style="top: -3.113em; margin-right: 0.05em;"><span class="pstrut" style="height: 2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight" style="margin-right: 0.03148em;">k</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height: 0.3831em;"><span></span></span></span></span></span></span><span class="mord"><span class="mord mathnormal">e</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height: 0.3361em;"><span style="top: -2.55em; margin-left: 0em; margin-right: 0.05em;"><span class="pstrut" style="height: 2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight" style="margin-right: 0.03148em;">k</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height: 0.15em;"><span></span></span></span></span></span></span></span></span></span></span></p>'''.format(s))


st.html('<h1 style="text-align: center;">Lie Groups Geometry</h1>')

st.html('<p style="text-align: right;"><span style="font-size: 12px; color: rgb(124, 112, 107);">Andr&eacute;s Villab&oacute;n</span> &nbsp;<a href="https://orcid.org/0000-0002-9022-4459" target="_blank" rel="noopener noreferrer"><img alt="ORCID logo" src="https://info.orcid.org/wp-content/uploads/2019/11/orcid_16x16.png" width="12" height="12"></a>&nbsp;<a href="https://www.linkedin.com/in/andres-villabon-95ba37232" target="_blank" rel="noopener noreferrer"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/81/LinkedIn_icon.svg/72px-LinkedIn_icon.svg.png" width="12" height="12"></a><br><span style="font-size: 12px; color: rgb(124, 112, 107);">Miguel Vargas</span>&nbsp; <a href="https://orcid.org/0000-0002-7624-9756" target="_blank" rel="noopener noreferrer"><img alt="ORCID logo" src="https://info.orcid.org/wp-content/uploads/2019/11/orcid_16x16.png" width="12" height="12"></a>&nbsp;<a href="https://www.linkedin.com/in/miguel-vargas-valencia-51146b101" target="_blank" rel="noopener noreferrer"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/81/LinkedIn_icon.svg/72px-LinkedIn_icon.svg.png" width="12" height="12"></a></p>')


steps=st.tabs(["Set dimension", "Structure constants $c_{i,j}^{k}$", "Semi-Metric", "Compute Symbols", "Curvature"])

with steps[0]:
    n=st.number_input("Lie Group dimension",min_value=2,max_value=10,step=1)

    if st.button("Set dimension", type="primary"):
        for key in st.session_state.keys():
            del st.session_state[key]
        st.session_state["n"]=n 
        st.success("Dimension set. Go to structure constants tab ➡️", icon=":material/thumb_up:")
    
with steps[1]:
    ## Creación de plantilla Excel
    st.markdown('Recall that, if $\mathfrak{g}$ a Lie algebra with basis $\{e_1, \ldots, e_n\}$, its structure constants $c_{ij}^k$ are given by')
    displaylatex('[e_i,e_j]=\sum_{k=1}^nc_{ij}^ke_k',[1,1,1])
    if "n" in st.session_state:
        ij=[]
        for i in range(1,n+1):
            for j in range(i+1,n+1):
                s=str(i)+ ","+str(j)
                ij.append(s)

        df=pd.DataFrame({"ij-k":ij})

        for i in range(1,n+1):
            df[str(i)] = pd.Series(dtype='float')
        st.session_state["df"]=df.fillna(0)
    if 'df' in st.session_state:
        st.markdown('In the following table, define the values of the structure constants $c^k_{ij}$ of the Lie algebra. The rows show the subscripts $ij$ and the columns the superscripts $k$. Note that you only need to define them for the values $i < j$, as the constants satisfy $c^k_{ij} = -c^k_{ji}$ and $c^k_{ii} = 0$.')
        df=st.data_editor(st.session_state.df , hide_index=True, disabled=["ij-k"])
        st.html('''<p><span style="color: #999999;"><span style="font-size: 11px;"><strong>Note:</strong>&nbsp;With the table's top right menu, you can easily copy and paste variables from an xlsx or csv file. Additionally, you have the option to download your constants table.</span></p>''')
    else:
        st.warning("⚠️ Dimension not defined ⚠️")
    
    if st.button("Save structure", type="primary"):
        st.session_state["df"]=df.fillna(0)
        struc={}
        for low in range(len(df)):
            for up in range(1,len(df.columns)):
                key=df.iloc[low]["ij-k"]+":"+str(df.columns[up])
                struc[key]=df.iloc[low][up]
    ### --- Verify
        with st.spinner('Verifying Jacobi Conditions'):
                sleep(1)
                #Antisimétricas
                keys=list(struc.keys())
                for p in keys:
                    i=p.split(',')[0]
                    j=p.split(',')[1].split(":")[0]
                    k=p.split(':')[1]
                    p_new=j+","+i+":"+k
                    struc[p_new]=(-1)*struc[p]
                # Creando diagonales
                n=st.session_state.n
                for i in range(1,n+1):
                    for j in range(1,n+1):
                        key="{},{}:{}".format(i,i,j)
                        struc[key]=0
                #st.write(struc)
                ix=lambda i,j,k: "{},{}:{}".format(i,j,k)
                si=0
                no_cond=[]
                for i in range(1,n+1):
                    for j in range(1,n+1):
                        for k in range(1,n+1):
                            for t in range(1,n+1):
                                suma=0
                                for l in range(1,n+1):
                                    c=struc
                                    suma += c[ix(i,j,l)]*c[ix(l,k,t)]+c[ix(j,k,l)]*c[ix(l,i,t)]+c[ix(k,i,l)]*c[ix(l,j,t)]
                                if suma!=0:
                                    si += 1
                                    no_cond.append((i,j,k,t,suma))
                                    
                if si==0:
                    st.session_state['cond']=True
                    st.success("You have a Lie Algebra Structure. Go to Metric tab ➡️",  icon=":material/thumb_up:")
                    st.session_state["structure"]=struc

                else:
                    st.session_state['cond']=False
                    st.error("Nop, you have not a Lie Algebra Structure")
                    st.markdown("The following cases do not satisfy Jacobi conditions")
                    st.markdown('$$\displaystyle \sum_{l=1}^{n} c_{i,j}^{l} c_{l,k}^{t} + c_{j,k}^{l} c_{l,i}^{t} + c_{k,i}^{l} c_{l,j}^{t} = 0$$')
                    for noc in no_cond:
                        st.write("For i={}, j={}, k={}, t={}, result {}".format(*noc))
    ### ----- End Verify


with steps[2]:
    st.markdown(r'Given a bi-invariant semi-Riemannian metric $k^+$ on a Lie group $G$ is eqivalent to give a scalar product $k$ on its Lie algebra $\mathfrak{g}$ such that')
    displaylatex(r'k(ad_xy,z)+k(y,ad_xz)=0',[1,2,1])
    st.markdown(r'for all $x,y,z\in\mathfrak{g}$.')
    if 'cond' in st.session_state:
        if st.session_state['cond']==False:
            st.error("You don't have a Lie Algebra yet.")
        else:
            n=st.session_state.n
            indx=[]
            for i in list(range(1,n+1)):
                indx.append(str(i))
            m={"i-j":indx}
            for i in range(1,n+1):
                m[i]=n*[0]

            matrix_df=pd.DataFrame(data=m)

            st.session_state["matrix_df"]=matrix_df.fillna(0)
            if 'matrix_df' in st.session_state:
                st.write('In the table below, please input the matrix that defines your semi-metric in relation to the basis you utilized for the structure constants.')
                matrix_df=st.data_editor(st.session_state.matrix_df, hide_index=True, disabled=["i-j"])
            
            if st.button("Set Semi-metric", type='primary'):
                del st.session_state["matrix_df"]
                st.session_state["matrix_df"]=matrix_df
                m_c=matrix_df.columns[1:]
                metric=matrix_df[m_c].to_numpy()
                if (np.array_equal(metric.transpose(), metric)) and (np.linalg.det(metric) !=0):
                    st.session_state["metric"]=metric
                    n=st.session_state.n
                    c=st.session_state.structure
                    bi_inv={}
                    ix=lambda i,j,k: "{},{}:{}".format(i,j,k)
                    for k in range(1,n+1):
                        a=np.empty((n,n))
                        for i in range(1,n+1):
                            col=[]
                            for j in range(1,n+1):
                                col.append(c[ix(k,j,i)])
                            a[i-1]=col
                        if np.array_equal(np.matmul(a.transpose(),metric), (-1)*np.matmul(metric,a)):
                            bi_inv[k]=1
                        else:
                            bi_inv[k]=0
                    bi_inv_f={k: v for k, v in bi_inv.items() if v==0}
                    falses=bi_inv_f.keys()
                    if len(falses)>0:
                        f_str=', '.join([str(x) for x in falses])
                        st.markdown("$ad_{e_{i}}^{T} \; k \\neq - k \; ad_{e_{i}}$")
                        st.warning("Your Semi-metric is not Bi-invariant. Condition fails for i={}".format(f_str))
                    else:
                        st.success("You have a Bi-invariant Semi-metric.")
                    
                    st.success("You set a Semi-metric. Go to Compute Symbols tab ➡️",  icon=":material/thumb_up:")

                else:
                    st.error("Your matrix does not define a Semi-metric. Rebemer that you need a symmetric and non-degenerate matrix")
    else:
        st.warning("⚠️ You don't have a Lie Algebra yet. ⚠️")

with steps[3]:
    st.html('<h3>Levi-Civita Connection</h3>')
    st.markdown("A basis $\{e_1,\ldots,e_n\}$ for the Lie algebra $\mathfrak{g}$ define left-invariant vector field $\{e_1^+,\ldots,e_n^+\}$ on the Lie group $G$. Hence, the Christoffel symbols can be written")
    displaylatex("\\nabla_{e_i^+}e_j^+=\sum_{k=1}^n\Gamma_{ij}^ke_k^+",[1,2,1])
    if st.button('Compute', type='primary'):
        if "metric" in st.session_state:
            K=st.session_state["metric"]
            K_inv=np.linalg.inv(K)
            c=st.session_state.structure
            n=st.session_state.n
            ix=lambda i,j,k: "{},{}:{}".format(i,j,k)
            # Christoffel symbols Levi-Civita
            c_nn=0
            gammaK = [[[0 for i in range(n)] for j in range(n)] for k in range(n)]
            for i in range(1,n+1):
                for j in range(1,n+1):
                    for k in range(1,n+1):
                        gammaK[i-1][j-1][k-1]=0
                        for l in range(1,n+1):
                            for m in range(1,n+1):
                                gammaK[i-1][j-1][k-1] += 0.5 * (K_inv[k-1,l-1]*(-K[j-1,m-1]*c[ix(i,l,m)]-K[l-1,m-1]*c[ix(j,i,m)]+K[i-1,m-1]*c[ix(l,j,m)]))
                        if gammaK[i-1][j-1][k-1] != 0:
                            c_nn=+1
            st.session_state["symbols"]=gammaK

            if c_nn >0 :
                st.write("Non-null Christoffel symbols: ")
            
                for i in range(n):
                    for j in range(n):
                        for k in range(n):
                            if gammaK[i][j][k]!=0:
                                st.write("$\Gamma"+'_{'+ str(i+1) +','+  str(j+1) +'}^{'+  str(k+1) +  "} = "+ "{:.2f}".format(gammaK[i][j][k])+"$")
            else:
                st.success("You set a flat space. All Christoffel symbols are zero")
        else:
            st.warning("⚠️ You have to define a Semi-metric ⚠️")
with steps[4]:
    st.markdown("In terms of the parallelims $\{e_1^+,\ldots,e_n^+\}$ on the Lie group $G$, the curvature of the connection $\\nabla$ is")
    displaylatex("R\left(e_i^+,e_j^+\\right)=\\nabla_{e_i^+}\\nabla_{e_j^+}-\\nabla_{e_j^+}\\nabla_{e_i^+}-\\nabla_{\left[e_i^+,e_j^+\\right]}",[1,3,1])
    if st.button("Curvature", type="primary"):
        if 'symbols' in st.session_state:
            G=st.session_state["symbols"]
            n=st.session_state["n"]
            c=st.session_state["structure"]
            ix=lambda i,j,k: "{},{}:{}".format(i,j,k)
            Ds={}
            for k in range(n):
                D=np.empty((n,n))
                for i in range(n):
                    col=[]
                    for j in range(n):
                        col.append(G[k][j][i])
                    D[i]=col
                Ds[k+1]=D
            curvature=0
            for i in range(1,n+1):
                for j in range(1,n+1):
                    nab_ij=np.zeros((n,n))
                    for k in range(1,n+1):
                        nab_ij=nab_ij+c[ix(i,j,k)]*Ds[k]
                    R=np.matmul(Ds[i],Ds[j])-np.matmul(Ds[j],Ds[i])-nab_ij
                    if R.any() != 0:
                        st.markdown("$R\left(e_{}^+,e_{}^+\\right) \\neq \mathbf{}$".format(i,j,0))
                        curvature+=1
            if curvature == 0:
                st.success("You have null curvature", icon=":material/thumb_up:")
            else:
                st.warning("⚠️ You have Non-null curvature ⚠️")


        else:
            st.warning("⚠️ You have to Compute the Christoffel Symbols ⚠️")

st.html('<p><br></p>')
st.caption("This application is part of the research project PGI2101ECBTI2024 of [UNAD](https://www.unad.edu.co/).")


hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.html(hide_st_style)
