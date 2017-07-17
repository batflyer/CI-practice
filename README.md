<p align="center">
   <img src="media/box2.png" />
</p>

---

| License | Build Status |
| --- | --- |
| [![][license img]][license] | [![Build Status](https://travis-ci.org/batflyer/CI-practice.svg?branch=master)](https://travis-ci.org/batflyer/CI-practice) |

---

**BoostSRL** (Boosting for Statistical Relational Learning) is a gradient-boosting based approach to learning different types of SRL models. As with the standard gradient-boosting approach, our approach turns the model learning problem to learning a sequence of regression models. The key difference to the standard approaches is that we learn relational regression models i.e., regression models that operate on relational data. We assume the data in a predicate logic format and the output are essentially first-order regression trees where the inner nodes contain conjunctions of logical predicates. For more details on the models and the algorithm, we refer to our book on this topic.

Sriraam Natarajan, Tushar Khot, Kristian Kersting and Jude Shavlik, Boosted Statistical Relational Learners: From Benchmarks to Data-Driven Medicine . SpringerBriefs in Computer Science, ISBN: 978-3-319-13643-1, 2015 

## Installation

Python 2.7:

Python 3:

[license]:license.txt
[license img]:https://img.shields.io/aur/license/yaourt.svg