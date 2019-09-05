# Created by Oleksandr Sorochynskyi
# On 05/09/2019

# import libares --------------------------------------------------------------

library(mvtnorm)

# Generate example data -------------------------------------------------------

n_period <- 365
n_asets <- 3
ret_exp <- c(0.01, 0.02, -0.01)
ret_sd <- c(0.005, 0.01, 0.01)
ret_cor <- matrix(c(1.0, 0.2, -.1,
                    0.2, 1.0, -.3,
                    -.1, -.3, 1.0), ncol=3, nrow=3, byrow=TRUE)
ret_cov <- ret_cor * ret_sd %*% t(ret_sd)

returns <- rmvnorm(n_period, mean=ret_exp, sigma=ret_cov)

# Run MEDAF -------------------------------------------------------------------

norisk <- 0.001

target_ret <- 0.01

mu <- apply(returns, 2, mean)
sigma <- cov(returns)
sigma_inv <- solve(sigma)
u <- rep(1, ncol(returns))

z <- cbind(mu, u)
A <- t(z) %*% sigma_inv %*% z
A_inv <- solve(A)
x <- sigma_inv %*% z %*% A_inv %*% c(target_ret, 1)
x_var <- t(c(target_ret, 1)) %*% A_inv %*% c(target_ret, 1)