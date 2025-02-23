# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 19:30:26 2025

@author: asgun
"""

import math
import random
import matplotlib.pyplot as plt

#N candidatos
N = 16

#Corte entrevista 37%
corte = 0.37


Ncorte = math.floor(corte*N)

Ntrials = 1000
notaMedia =0
countMaior =0

for trial in range(Ntrials):
    #Gera notas aleatórias para os N candidatos
    notaCandidato = [round(random.random(),2) for _ in range(N)]
    melhorCandidato = N-1
    melhorNota = 0
    
    maiorNotaAbs = max(notaCandidato)

    for i in range(N):
        
        if i<Ncorte: #Só obtenho informação
            if melhorNota < notaCandidato[i]:
               melhorNota = notaCandidato[i]
        else:
            #Pego o melhor que aparecer
            if notaCandidato[i]>melhorNota:
               melhorNota = notaCandidato[i]
               melhorCandidato = i
               break
           #Se não conseguir ninguém, serei obrigado a pegar o último
    
    notaMedia += notaCandidato[melhorCandidato]
    if notaCandidato[melhorCandidato] == maiorNotaAbs:
        countMaior +=1
        
    if trial<3:
        print("Melhor Candidato:", melhorCandidato)
        print("Nota Candidato: ", notaCandidato[melhorCandidato])
        print("Notas: ", notaCandidato)
        
        cores = ['blue']*N
        
        cores[:Ncorte] = ['green']*Ncorte
        cores[melhorCandidato] = 'red'
        
        plt.bar(list(range(N)),notaCandidato, color = cores)
        plt.show()
        
 
notaMedia = notaMedia/Ntrials

print(f"Nota média: {notaMedia:.2f}")

print(f"Quantas vezes escolheu o melhor: {countMaior:d} de {Ntrials}")
