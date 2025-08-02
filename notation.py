

# %%
not_V = r"\(V\)"
not_T = r"\(T\)"
not_transformation = r"\(T: V \rightarrow V\)"
not_v_exists_in_v = r"\(\mathbf{v} \in V\)"
not_Tv = r"\(T\mathbf{v}\)"
not_v = r"\(\mathbf{v}\)"
not_lamda = r"\(\lambda\)"


eqn_tv_lamdav = r"\(T\mathbf{v}=\lambda \mathbf{v}\)"
eqn_associativity_of_additions = r"\((\mathbf{u} + \mathbf{v}) + \mathbf{w} = \mathbf{u} + (\mathbf{v} + \mathbf{w})\)"



not_example_matrix = r"\( \begin{bmatrix} a & b \\ c & d \\ \end{bmatrix}\)" 



not_char_eqn = r"\( \text{det}(A - \lambda I) = 0 \)" 

not_identity_matrix = r"""\(
\begin{bmatrix}
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1 \\
\end{bmatrix}
\)"""

not_inverse_matrix = r"AB = BA = I"

# %%
not_V = r"\(V\)"
not_T = r"\(T\)"
not_transformation = r"\(T: V \rightarrow V\)"
not_v_exists_in_v = r"\(\mathbf{v} \in V\)"
not_Tv = r"\(T\mathbf{v}\)"
not_v = r"\(\mathbf{v}\)"
not_lamda = r"\(\lambda\)"


eqn_tv_lamdav = r"\(T\mathbf{v}=\lambda \mathbf{v}\)"
eqn_associativity_of_additions = r"\((\mathbf{u} + \mathbf{v}) + \mathbf{w} = \mathbf{u} + (\mathbf{v} + \mathbf{w})\)"



# %%
# MATHEMATICAL FINANCE
not_zero_coupon_bond_price = r"\(B(t,T)\)"
not_forward_rate = r"\(F(t,S,T)\)" 
not_spot_rate = r"\(R(t,t)\)"

eqn_spot_rate_zero_coupon_price = r"\(R(t,T)= \frac{-1}{T-t}\log{B(t,T)} \forall \, t < T\)"
eqn_zero_coupon_price_spot_rate = r"\(B(t,T)= \exp{(T-t)B(t,T)} \forall \, t < T\)"
eqn_spt_rate_forward_rate = r"\((1 + R(t, T))^{T-t} = (1 + R(t, T - 1))^{T - t-1} \cdot (1 + F(t, T - 1, T))\)"




not_fractional = r"""
\text{Let:} \\
R = \text{Reserve ratio (fraction of deposits that must be held in reserve)} \\
D = \text{Initial deposit} \\
C = \text{Total credit created} \\

\text{The formula for total credit created is:} \\
C = \frac{D}{R} - D \\
\text{or equivalently:} \\
C = D \left( \frac{1}{R} - 1 \right) \\

\text{This formula shows the additional credit created in the system due to fractional reserving.}
"""


