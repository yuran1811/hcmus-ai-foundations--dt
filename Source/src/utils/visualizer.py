import os

import graphviz
from sklearn.tree import DecisionTreeClassifier, export_graphviz

os.makedirs("key_trees", exist_ok=True)


def train_and_visualize(
    X_train, y_train, feature_names, class_names, split_ratio, max_depth
):
    clf = DecisionTreeClassifier(criterion="entropy", max_depth=max_depth)
    clf.fit(X_train, y_train)

    # Export tree only for 80/20 split and depths 2/5
    if split_ratio == 0.8 and max_depth in [2, 5]:
        dot_data = export_graphviz(
            clf,
            out_file=None,
            feature_names=feature_names,
            class_names=class_names,
            filled=True,
            rounded=True,
        )
        filename = f"key_trees/tree_{split_ratio}_depth_{max_depth}"
        graphviz.Source(dot_data).render(filename, format="png", cleanup=True)

    return clf
