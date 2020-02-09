import numpy as np
import pandas as pd

# %% Vector Autoregression with Long-Run Restriction

def varlr(series, p=1):
    """
    Vector Autoregression with Long-Run Restriction
    (Blanchard-Quah restriction (1989))


    Parameters
    ----------
    series : DataFrame, Array (Automatically transformed to NumPy Array)
        Data Series.
    p : int, optional
        VAR Order. The default is 1.

    Returns
    -------
    b : Array
        VAR coefficient vector [A0,A1,...Ap]'.
    Sig : Array
        Variance-Covariance Matrix of Reduced Form Error.
    B : Array
        Structural Transform Matrix computed with Long-Run restriction imposed.

    """
    (nobs, nvar) = series.shape
    series = np.asarray(series)
    YY = series[p:nobs] 
    XX = (np.ones([nobs-p,1+nvar*p]))
    
    for i in range(1,p+1):
        XX[:, 1+nvar*(i-1):2+nvar*i] = series[p-i:nobs-i,:]

    # b = inv(XX`*XX) * XX` * YY;
    b = np.dot((np.dot(np.linalg.inv((np.dot((XX.conj().transpose()), XX))), (XX.conj().transpose()))), YY)  
    e = YY - np.dot(XX,b)  
    Sig = np.dot(e.conj().transpose(),e) / (nobs-p)  
    # AR Coefficient [A1,A2...,Ap]
    AR = b[1:,:].conj().transpose()
    # MA Representation 
    # Y_t = A0 + A1*Y_t(t-1) + ... + Ap*Y_(t-p) + e_t   :: AR(p)
    # Y_t = mu + Phi(L)*e_t :: MA(infinity)
    # where Phi(L) = (I-A1*L-A2*L^2-...-Ap*L^p)^(-1)
    # mu = Phi(1)*A0
    
    rep_m = np.kron(np.ones((p,1)),np.identity(nvar))
    Phi1 = (np.linalg.inv(np.dot((np.identity(nvar))-AR, rep_m)))
    mu = np.dot(Phi1,b[0].conj().transpose())
    lvar = (np.dot(np.dot(Phi1, Sig), Phi1.conj().transpose()))
    
    # Long-Run restriction
    # define 
    # Y_t = theta(L)*epsilon_t
    # where var(epsilon_t) = I
    # Let e_t = B*epsilon_t so that Phi(L)*B = theta(L)
    # Note that BB' = Sig
    # the longrun variance of Y is theta(1)*theta(1)'
    # long-run restriction here is theta(1) is lower triangular matrix
    theta1 = np.linalg.cholesky(lvar.conj().transpose())
    B = np.dot(np.linalg.inv(Phi1), theta1)
    
    return b, Sig, B


# %% Impulse Response Function 

import numpy as np

def irflr(b,B,nIR):
    """
    IRFLR Impulse Response of VAR

    Parameters
    ----------
    b : Array
        VAR coefficents [A0,A1,...,Ap]'.
    B : Array
        Structual vector for error.
    nIR : int
        periods of IRF.

    Returns
    -------
    IR : Array
        s-th column has (s-1) period of IRF
           [ t(11) t(21) ... t(n1) t(12)....]'
           t(ij) stands for effect of j shock on variable i.

    """
    
    nvar = b.shape[1]
    AR = b[1:,].conj().transpose()
    p = AR.shape[1]/nvar
    MA = np.zeros([nvar,int(nvar*nIR)])
    m = min(nIR,p)
    MA[:, 0:int(m*nvar)] = AR[:, 0:int(m*nvar)]

    for i in range(1, nIR):
        z = nvar*min(i+p,nIR)
        MA[:, int(i*nvar):int(z)] = MA[:, int(i*nvar):int(z)] + (np.dot(MA[:,(i-1)*nvar:i*nvar], AR[:, 0:int(z-i*nvar)]))
    
    theta = np.dot(np.column_stack((np.identity(nvar),MA)), (np.kron(np.identity(nIR+1),B)))
    theta_dim = theta.shape
    reshape_length = int(theta_dim[1] / nvar)
    IR = theta.transpose().reshape(reshape_length,nvar**2,).transpose()
    
    return IR 


# %% Correlation Function 

def cor(MA): 
    """
    

    Parameters
    ----------
    MA : Array
        This is the impulse response of VAR.

    Returns
    -------
    cor : Array
        Correlation Coefficients.

    """
    a, b = MA.shape
    
    nvar = round(a**(1/2))
    nIR = b-1
    
    varmat = MA**2
    covmat = MA[[0,2],:] * MA[[1,3],:]
    
    cova = covmat.sum(axis=1)	
    vari = varmat.sum(axis=1)
    
    unccor = cova.sum(axis=0) / (((vari[0]+vari[2])**(1/2)) * ((vari[1]+vari[3])**(1/2)))
    cor1 =  cova[0] / ((vari[0]*vari[1])**(1/2))
    cor2 = cova[1] / ((vari[2]*vari[3])**(1/2))
    
    cor = np.column_stack([unccor, cor1, cor2])
    
    return cor

# %% Bootstrap Function

def bootstrap(y,p,k):
    """
    

    Parameters
    ----------
    y : Array
        The series to bootstrap.
    p : int
        Order of lags.
    k : int
        Number of initial trimming observation.

    Returns
    -------
    yb : Array
        Bootstrapped series.

    """
    y = np.asarray(y)
    (nobs, nvar) = y.shape
    
    YY = y[p:nobs]
    XX = np.ones([nobs-p,1+nvar*p])
    
    for i in range(1,p+1):
        XX[:, 1+nvar*(i-1):2+nvar*i] = y[p-i:nobs-i]
    
    b = np.dot((np.dot(np.linalg.inv((np.dot((XX.conj().transpose()), XX))),
                       (XX.conj().transpose()))), YY) 
    
    e = YY - np.dot(XX,b)
    e = np.asarray(e)
    
    
    # Generating the Pseudo-Sample
    # Psuedo-Disturbance
    T = len(YY)
    
        
    segment = []
    for i in range(1,T+1):
        segment.append(i/T)
    segment = np.asarray(segment)[np.newaxis]  
    
    eb = np.zeros([T+k+p,nvar])
    
    # distributing disturbances
    for i in range(1,T+k+p+1):
        u = np.random.random()
        test = (segment >= u).astype(int)
        idx = (segment.shape[1]) - (test.sum())
        eb[i-1,:] = e[idx,:]
    
    # Pesudo-Sample
    yb = np.zeros([T+k+p,nvar])
    r = XX[0,:][np.newaxis]

    for i in range(1,T+k+p+1):
        yb[i-1,:] = np.dot(r,b) + eb[i-1,:]
   
        r = [1,yb[i-1,:], r[2:len(r)-nvar]]
        r_1 = r[0]
        r_2 = r[1]
        r = np.insert(r_2,0,r_1)
    # Trim Dataset 
    
    yb = yb[k:len(yb)]
    
    return yb
    

# %% Band Function

def band(mat,ptg):
    """
    Calculate minimum-distance interval

    Parameters
    ----------
    mat : Array
        Array to calculate minimum-distance intervals from.
    ptg : float
        Decimal representation of confidence interval percentage.

    Returns
    -------
    band : Array
        Confidence intervals.

    """
    F,n = mat.shape
    mat.sort(axis=0)
    t = round((1-ptg)*F)
    band = []
    
    for i in range(1,n+1):
        temp = mat[len(mat)-t-1:len(mat),i-1] - mat[:t+1,i-1]
        m = min(temp)
        I = temp.argmin()
        band.append(mat[[I,((F-I)-2)],i-1][np.newaxis])

    band = np.vstack(band)
    band = band.T
    return band
