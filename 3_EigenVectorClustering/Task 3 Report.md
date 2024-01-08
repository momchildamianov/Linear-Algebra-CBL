# Task 3
## 3. a Briefly explain your items and graph. 
Our graphs consists of 11 nodes representing people in a social network. The goal of clustering task is to split people to two groups based on friendship connections (edges) between people. These two groups should represent separate friend circles in which most people has a mutual friendship connection with each other in the same cluster. 

The desired result of clustering is to have one group of friends formed during first year at TU/e (Svetlana, Emo, Iva, Teddie, Martina, Momo) and the other friend group (Subo, Dimitko, Naiden, Annie, Radi) formed during high school in Bulgaria. These two groups are interconnected by Teddie and Momo who are friends with Naiden and Dimitko respectively. 

## 3. b Plot the graph, by computer or by hand
![[Pasted image 20240108063529.png]]

> **Graph of friendship connections between people**
> To plot an undirected graph Python packages networkx and matplotlib vere used in Jupyter notebook.

## 3. c Set up the symmetric Laplacian matrix L 
$$
\begin{bmatrix}
&Svetlana & Emo & Iva & Teddie & Martina & Momo & Dimitko & Naiden & Ani & Radi & Subo \\ 
Svetlana & 4 & -1 & -1 & -1 & -1 & 0 & 0 & 0 & 0 & 0 & 0\\
Emo      & -1 & 3 & 0 & 0 & -1 & -1 & 0 & 0 & 0 & 0 & 0\\
Iva      & -1 & 0 & 3 & -1 & 0 & -1 & 0 & 0 & 0 & 0 & 0 \\
Teddie   & -1 & 0 & -1 & 4 & 0 & -1 & 0 & -1 & 0 & 0 & 0\\
Martina  & -1 & -1 & 0 & 0 & 3 & -1 & 0 & 0 & 0 & 0 & 0\\
Momo     & 0 & -1 & -1 & -1 & -1 & 5 & -1 & 0 & 0 & 0 & 0 \\
Dimitko  & 0 & 0 & 0 & 0 & 0 & -1 & 3 & -1 & 0 & 0 & -1 \\
Naiden   & 0 & 0 & 0 & -1 & 0 & 0 & -1 & 5 & -1 & -1 & -1 \\
Ani      & 0 & 0 & 0 & 0 & 0 & 0 & 0 & -1 & 3 & -1 & -1 \\
Radi     & 0 & 0 & 0 & 0 & 0 & 0 & 0 & -1 & -1 & 2 & 0 \\
Subo     & 0 & 0 & 0 & 0 & 0 & 0 & -1 & -1 & -1 & 0 & 3\\
\end {bmatrix}
$$

## 3. d Compute the Fiedler vector
Eigenvalues and Fiedler vector was obtained from Laplacian matrix by Python script. 
```start-multi-column
ID: ID_h61r
Number of Columns: 2
Largest Column: standard
```

Eigenvalues were computed using linealg.eigvals(..) python module:
$$
\begin{bmatrix}
3.55e^{-17} \\
\textbf{0.48} \\
1.90 \\
2.19 \\
3.18 \\
4.00 \\
4.24 \\
4.34 \\
4.79 \\
5.94 \\
6.94 \\
\end{bmatrix}
$$

--- column-end ---

Fiedler vector corresponding to $\lambda = 0.48$ using module networkx.fiedler_vector(...):
$$
\begin{bmatrix}
\textcolor{red}{-0.328} \\
\textcolor{red}{-0.304} \\
\textcolor{red}{-0.233} \\
\textcolor{red}{-0.141} \\
\textcolor{red}{-0.305} \\
\textcolor{red}{-0.240} \\
\textcolor{green}{0.177} \\
\textcolor{green}{0.374} \\
\textcolor{green}{0.413} \\
\textcolor{green}{0.338} \\
\textcolor{green}{0.346}
\end {bmatrix}
$$
--- end-multi-column

## 3. e Color the nodes corresponding to the sign of the Fiedler vector
![[Pasted image 20240108072446.png]]
The result of clustering is as expected since it correctly splits people into two friend clusters. Most people in the positive (green) cluster do not have connection with people in the negative (red) cluster and vice versa.

## 3. f Observe another graphs with more and fewer edges
For this experiment, the same nodes were used and the graph was modified only by adding / removing edges between nodes.
### Graph with more edges
We tested a scenario with adding edge (Emo, Naiden) and (Iva, Radi) to have now most people in the green cluster connected to people in the red cluster.
![[Pasted image 20240108073229.png]]
The procedure for extracting eigenvalues and Fidler vector was the same as for 3. d. The 2nd smallest eigenvalue is $\lambda=1.56$.

![[Pasted image 20240108073628.png]]
