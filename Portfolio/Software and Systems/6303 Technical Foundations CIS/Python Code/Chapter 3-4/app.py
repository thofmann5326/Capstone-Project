import graphviz
from sklearn import tree

tree_data = tree.export_graphviz(model,
                                 out_file=None,
                                 feature_names=X.columns,
                                 class_names=['no', 'yes'],
                                 label='all',
                                 rounded=True,
                                 filled=True,
                                 max_depth=5
                                 )

graph = graphviz.Source(tree_data, format="png")
graph
