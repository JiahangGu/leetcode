#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/10/28 16:14
# @Author:JiahangGu

from random import randint


class GeneUnit:
    def __init__(self):
        self.gene = [0, 0, 0, 0, 0, 0, 0]
        self.fitness = 1
        self.rf = 0.0
        self.cf = 0.0


class Solution:
    def __init__(self):
        self.amount = 7
        self.max_capacity = 150
        self.weights = [35,30,60,50,40,10,25]
        self.prices = [10,40,30,50,35,40,30]
        self.population = 20
        self.gene_units = []
        self.epochs = 20
        self.max_rand = 10
        self.pm = 0.2
        self.pc = 0.8

    def init(self):
        for i in range(self.population):
            gu = GeneUnit()
            gu.gene = [1 if randint(0, 9) >= 5 else 0 for _ in range(self.amount)]
            print(gu.gene)
            self.gene_units.append(gu)

    def eval_fitness(self):
        total_fitness = 0
        for i in range(self.population):
            total_weight = 0
            self.gene_units[i].fitness = 0
            for j in range(self.amount):
                if self.gene_units[i].gene[j]:
                    total_weight += self.weights[j]
                    self.gene_units[i].fitness += self.prices[j]
            if total_weight > self.max_capacity or total_weight == 0:
                self.gene_units[i].fitness = 1
            total_fitness += self.gene_units[i].fitness
        return total_fitness

    def select(self, total_fitness):
        last_cf = 0.0
        for i in range(self.population):
            self.gene_units[i].rf = self.gene_units[i].fitness / total_fitness
            self.gene_units[i].cf = last_cf + self.gene_units[i].rf
            last_cf = self.gene_units[i].cf
        new_pop = []
        for i in range(self.population):
            p = randint(0, self.max_rand) / (self.max_rand + 1)
            if p < self.gene_units[0].cf:
                new_pop.append(self.gene_units[0])
            else:
                for j in range(self.population - 1):
                    if self.gene_units[j].cf <= p <= self.gene_units[j + 1].cf:
                        new_pop.append(self.gene_units[j + 1])
                        break
        self.gene_units = new_pop

    def exchange_over(self, first, second):
        ecc = randint(1, self.amount)
        for i in range(ecc):
            idx = randint(0, self.amount - 1)
            # print(first, second, idx)
            tg = self.gene_units[first].gene[idx]
            self.gene_units[first].gene[idx] = self.gene_units[second].gene[idx]
            self.gene_units[second].gene[idx] = tg

    def crossover(self):
        first = -1
        for i in range(self.population):
            p = randint(0, self.max_rand) / self.max_rand
            if p < self.pc:
                if first < 0:
                    first = i
                else:
                    self.exchange_over(first, i)
                    first = -1

    def reverse_gene(self, idx):
        mcc = randint(1, self.amount)
        for i in range(mcc):
            gi = randint(0, self.amount - 1)
            self.gene_units[idx].gene[gi] = 1 - self.gene_units[idx].gene[gi]

    def mutation(self):
        for i in range(self.population):
            p = randint(0, self.max_rand) / (self.max_rand + 1)
            if p < self.pm:
                self.reverse_gene(i)

    def genetic(self):
        self.init()
        total_fitness = self.eval_fitness()
        for i in range(self.epochs):
            self.select(total_fitness)
            self.crossover()
            self.mutation()
            total_fitness = self.eval_fitness()


s = Solution()
s.genetic()
print([(item.gene, item.fitness) for item in s.gene_units])
