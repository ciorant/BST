# Advanced Binary Search Tree with Augmented Range Queries

A sophisticated implementation of an augmented Binary Search Tree (BST) optimized for statistical analysis and range-based operations.

## Key Features

### Core Operations
- **Dynamic Insertion/Deletion**: O(h) time complexity with automatic tree balancing considerations
- **Fast Search**: O(h) logarithmic search with early termination optimization
- **Order Statistics**: Find k-th smallest element in O(h) time using augmented node information
- **Range Queries**: Count elements within any range [start, end] in O(h) time

### Advanced Query Operations
- **Count Less Than**: Efficiently count elements below a threshold
- **Count Greater Than**: Efficiently count elements above a threshold
- **Range Counting**: Count elements within specified bounds
- **Order Statistics**: k-th smallest element retrieval without full traversal

### Algorithmic Optimizations
- **Early Termination**: Search operations terminate as soon as target is found/confirmed absent
- **Subtree Pruning**: Range queries skip entire subtrees when mathematically provable they don't contribute
- **Count Propagation**: Maintains subtree sizes during modifications with single-pass updates
- **Successor Finding**: Optimized in-order successor location for deletion operations


## Use Cases & Applications

### Statistical Analysis
- **Percentile Calculations**: Quick quantile computations on dynamic datasets
- **Histogram Operations**: Efficient bin counting for data visualization
- **Outlier Detection**: Fast threshold-based filtering

### Database Operations  
- **Range Scans**: Efficient range query processing
- **Order-by Operations**: k-th element retrieval for pagination
- **Index Maintenance**: Dynamic index updates with query optimization
