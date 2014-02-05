##Methods

We performed a series of simulations to assess the impact of long-branch attraction in this dataset. In order to simulate appropriate nucleotide sequences, we first used Mr. Bayes[1,2] to obtain the per-site substitution rate for the empirical sequences. We then used these per-site mutation rates, along with the best-supported model of DNA sequence evolution to simulate DNA sequences in Seq-Gen[3] equal to the length of the empirical sequences. In these simulations, we assumed that the clade Npomorpha is monophyletic. Therefore, we evolved 1,000 replicate sequences along the tree in Fig. 2. 

To estimate the effects of long branch attraction, then created two versions of each replicate sequence. One replicate contained the full compliment of simulated sequences, corresponding to the tree estimated in this paper. The second replicate did not contain the taxon Paraplea. For each set of replicates, the results were analysed in PAUP[5] under the appropriate model of evolution to find the maximum likelihood tree for each replicate. We analyzed the frequency with which Pleoidea is placed within Nepomorpha using a custom script built with the Dendropy Python library.

##Results
===

The simulation results in which Paraplea was included unanimously supported the placement of Pleoidea within Nepomorpha. In data sets in which Paraplea was removed, Pleioidea was still placed within Nepomorpha in 99% of cases. These results strongly support the placement of Pleoidea within Nepomorpha.

1. Huelsenbeck, J. P. and F. Ronquist. 2001. MRBAYES: Bayesian inference of phylogeny. Bioinformatics 17:754-755.                      
2. Ronquist, F. and J. P. Huelsenbeck. 2003. MRBAYES 3: Bayesian phylogenetic inference under mixed models. Bioinformatics 19:1572-1574.   
3. Rambaut, A. and Grassly, N. C. (1997) Seq-Gen: An application for the Monte Carlo simulation of DNA sequence evolution along phylogenetic trees. Comput. Appl. Biosci. 13: 235-238.
4. Sukumaran, J. and Mark T. Holder. 2010. DendroPy: A Python library for phylogenetic computing. Bioinformatics 26: 1569-1571.
5.  Swofford, D. L. 2003. PAUP*. Phylogenetic Analysis Using Parsimony (*and Other Methods). Version 4. Sinauer Associates, Sunderland, Massachusetts.

##Results table 1

| Paraplea included | Percentage of replicates in which Nepomorpha is monophyletic |
|------------------|---------------------------------------------------------------|
| No | 99.75 |
| Yes | 100 |
