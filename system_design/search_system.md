# Question

How to build a Boolean Retrieval Search System on the plays of Shakespeare that handles Boolean Queries of the form:
Are there plays which has words like:
a. Brutus and Caesar
b. Caesar or Cleopatra
c. Not Calpurnia

# Solution
__Naive Approach__

1. Searching words across all plays. Not scalable as the number of plays increases.

__Transform and Conquer__

1. Create a Term Document Incidence Matrix
    - Columns index are the play names
    - Row index represent the unique vocabulary across all plays

[TODO-ADD IMAGE]

Issues - Sparse Matrix
Consider:
N = 1 million documents,each with 1000 words 
Avg 6 bytes/word including spaces/punctuations ~ 6GB data in the document
Distinct words ~500k 

If we look at one column, as avg 1000 words /document ,so only 1000 rows will be 1 and remaining ~499k rows will be 0.

Use Adjacency List<br>
1. For each term t, we must store a list of all documents[doc_id] in the **increasing order** that contains t.<br>
2. The adjlist of every term[word] will not be of fixed size.

[TODO Image]

### Inverted Index
This representation of term and doc_id in increasing order in the adjlist.

**AND Operation on Inverted Index**<br>
Looking at the example below:
Find plays containing Brutus and Caesar.

1. Get document ids for Brutus
2. Get document ids for Caesar
3. Find the intersection between the two.[Using a 2 pointer merge approach as the two result list is sorted.]

	len(adjlist[Brutus]) = m<br>
	len(adjlist[Caesar]) = n<br>
	Two pointer Approach T(n) = O(m+n) 

**NOT Operation on Inverted Index**<br>
NOT Ceasar<br>
1. Get all doc_ids where Ceasar is present.eg:[2,5,6]
2. For each index, fill the result table with the missing doc_ids. result = [1,3,4]

T(n) = O(D) where D= No of documents

## Handling Scale Issues

Corpus is huge and ,the inverted index cannot fit into main memory(but could fit into the disk of a single machine.

How do we build index? [Batch Processing Job]<br>
How do we serve queries? [Online Processing Job]


## External Merge Sort
Sorting when data[inverted index] does not fit into the main memory.

1. Go over each document and create (term,doc_id) table for each document and put it in disk (internall it get sorted by doc_id).
2. Read blocks of data from disk into the memory and do internal sorting[merge/quick/heap etc] on each block and save it into the disk.
3. Use k-way external merge sort over blocks of data.
	1. Read two blocks of data from disk into the memory.
	2. Use k pointer approach to do the external sorting.
	3. As any block pointer reaches the end, load another block from the disk into the memory and continue until both pointer reaches the end of the data.

Going for higher k reduces multiple disk seek which is costly.

 




