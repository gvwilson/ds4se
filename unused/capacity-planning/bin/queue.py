#!/usr/bin/env python

def fac(N):
    result = 1
    for i in range(2, N+1):
        result *= i
    return result

def C(λ, μ, s):
    ρ = λ / μ
    sum_term = sum([((s * ρ) ** k) / fac(k) for k in range(s-1)])
    prod_term = fac(s) / ( (s * ρ) ** s )
    return 1 / (1 + (1 - ρ) * prod_term * sum_term)

def queue_length(λ, μ, s):
    ρ = λ / μ
    return (C(λ, μ, s) * (1 - ρ) / ρ) + (s * ρ)

def response_time(λ, μ, s):
    return (C(λ, μ, s) / (s * μ - λ)) + (1 / μ)

def main():
    print('| λ (req/sec) | μ (req/sec) | servers | response (msec) |')
    print('| ----------: | ----------: | ------: | --------------: |')
    for (λ, μ, s) in [[20, 40, 1],
                      [20, 40, 2],
                      [20, 80, 1]]:
        time = response_time(λ, μ, s) * 1000
        print(f'| {λ} | {μ} | {s} | {time:6.3} |')

if __name__ == '__main__':
    main()
