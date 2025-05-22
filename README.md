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

### Augmented Tree Design
- **Subtree Size Tracking**: Each node maintains count of elements in its subtree
- **Efficient Range Operations**: Leverages subtree counts for O(h) range queries
- **Memory Optimized**: Minimal overhead per node while maximizing query capabilities

### Intelligent Range Counting
The range counting algorithm demonstrates advanced tree traversal optimization:
- **Pruning Strategy**: Eliminates unnecessary subtree visits
- **Count Aggregation**: Leverages precomputed subtree sizes
- **Boundary Optimization**: Handles edge cases with mathematical precision

### Order Statistics Implementation
The k-th smallest element algorithm showcases:
- **Rank-based Navigation**: Uses subtree counts to navigate directly to target
- **No Auxiliary Storage**: Achieves O(1) space complexity
- **Deterministic Performance**: Consistent O(h) time regardless of data distribution

### Time Complexity Analysis
| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Insert/Delete | O(h) | O(1) |
| Search | O(h) | O(1) |
| Range Count | O(h) | O(1) |
| k-th Smallest | O(h) | O(1) |
| Count Less/Greater | O(h) | O(1) |

*Where h is the height of the tree*

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

### Real-time Analytics
- **Sliding Window Statistics**: Maintain sorted order with insertions/deletions
- **Threshold Alerting**: Fast count-based monitoring
- **Data Stream Processing**: Efficient order statistics on streaming data
