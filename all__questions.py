# Add import files
import pickle



# -----------------------------------------------------------
def question1():
    answers = {}

    # type: bool (True/False)
    answers["(a)"] = True

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "Hierarchical clustering takes a step-by-step approach, like building a pyramid. It starts with individual data points and gradually merges similar ones into bigger groups, forming a hierarchy. This makes it less sensitive to outliers and gives a clearer picture of how data points are connected.K-means clustering, on the other hand, jumps straight to the answer. It assumes a specific number of pre-defined groups (like pre-built buckets) and assigns data points to the closest one. This can be swayed by outliers, which might pull entire groups in the wrong direction."
    
    # type: bool (True/False)
    answers["(b)"] = False

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "Hierarchical clustering builds connections step-by-step, offering a flexible view of data but with some variation in results. K-means sorts data quickly into predefined groups, but can be swayed by outliers and initial conditions."

    # type: bool (True/False)
    answers["(c)"] = False

    # type: explanatory string (at least four words)
    answers["(c) explain"] = "The addition of a new centroid can lead to an increased distance between the centroid and the data points. As a consequence, the Sum of Squared Residuals (SSE) may witness an increment."
    # type: bool (True/False)
    answers["(d)"] = True

    # type: explanatory string (at least four words)
    answers["(d) explain"] = "This occurs because the split is intended to generate two sub-clusters that could be more homogeneous, thereby bringing data points closer to their respective centroids. Consequently, the total sum of squared distances within each sub-cluster (SSE) might decrease, resulting in a reduced SSE for the entire clustering solution."   
    # type: bool (True/False)
    answers["(e)"] = True

    # type: explanatory string (at least four words)
    answers["(e) explain"] = "In K-means clustering, the goal is to minimize the Sum of Squared Errors (SSE), representing the total distance between data points. The reduction in SSE indicates that the data points are moving closer to their respective cluster centroids."

    # type: bool (True/False)
    answers["(f)"] = False

    # type: explanatory string (at least four words)
    answers["(f) explain"] = "In K-means clustering, a higher SSB (Between-Cluster Sum of Squares) directly translates to better separation between clusters."

    # type: bool (True/False)
    answers["(g)"] = True

    # type: explanatory string (at least four words)
    answers["(g) explain"] = "Tighter clusters (low SSE) don't guarantee good separation (high SSB), so we can be close within groups without being well-defined between them."
    # type: bool (True/False)
    answers["(h)"] = False

    # type: explanatory string (at least four words)
    answers["(h) explain"] = "Think of the total variation in your data (TSS) as a pie. You can slice it up in two ways: variation within clusters (SSE) and variation between clusters (SSB). These slices (SSE and SSB) can change size depending on how well your data is clustered, but the total pie (TSS) always stays the same."

    # type: bool (True/False)
    answers["(i)"] = False

    # type: explanatory string (at least four words)
    answers["(i) explain"] = "While minimizing SSE improves within-cluster similarity, it doesn't guarantee better separation between clusters (higher SSB)"
    return answers




# -----------------------------------------------------------
def question2():
    answers = {}

    # type: bool (True/False)
    answers["(a)"] = True

    # type: explanatory string (at least four words)
    answers["(a) explain"] = " After K-means clustering, each colored circle (cluster) will have a single centroid (center point) that best represents the data points within that cluster.."
    
    # type: bool (True/False)
    answers["(b)"] = False

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "Even after running k-means, some clusters might still contain points from both shaded areas.."

    # type: bool (True/False)
    answers["(c)"] = True

    # type: explanatory string (at least four words)
    answers["(c) explain"] = "K-means aims to create k distinct clusters, but sometimes it can leave one empty. This happens when no data points are close enough to be assigned to that particular cluster.."

    return answers




# -----------------------------------------------------------
def question3():
    answers = {}

    # type: a string that evaluates to a float
    answers["(a) SSE"] = '4*R^2'

    # type: a string that evaluates to a float
    answers["(b) SSE"] = '4*squart(a^2+b^2)'

    # type: a string that evaluates to a float
    answers["(c) SSE"] = '10*R^2'

    return answers




# -----------------------------------------------------------
def question4():
    answers = {}

    # type: int
    answers["(a) Circle (a)"] = 1

    # type: int
    answers["(a) Circle (b)"] = 1

    # type: int
    answers["(a) Circle (c)"] = 1

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "optimal clusturing will happen"

    # type: int
    answers["(b) Circle (a)"] = 1

    # type: int
    answers["(b) Circle (b)"] = 1

    # type: int
    answers["(b) Circle (c)"] = 1

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "Though circles A, B, and C are close, their centroids might wander during K-means. This is because centroids are placed based on which data points are closest, not just the initial circles"    
    # type: int
    answers["(c) Circle (a)"] = 1

    # type: int
    answers["(c) Circle (b)"] = 0

    # type: int
    answers["(c) Circle (c)"] = 2

    # type: explanatory string (at least four words)
    answers["(c) explain"] = "This data spread ensures each centroid belongs to its starting circle! Since nearby points influence centroid placement in K-means, similar distances within circles lock the centroids in their initial positions.."

    return answers




# -----------------------------------------------------------
def question5():
    answers = {}

    # type: set
    answers["(a)"] = {"Group A","Group B"}

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "if there are no obstacles or restrictions on movement, the shortest path between two points is simply the straight line connecting them.."

    # type: set
    answers["(b)"] = {'Group A','Group C'}

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "In a flat, unrestricted space, the straight line connecting the two points is their farthest possible separation."

    return answers




# -----------------------------------------------------------
def question6():
    answers = {}

    # type: set
    answers["(a) core"] = {'E','B','F','G','C','L','M','I'}

    # type: set
    answers["(a) boundary"] = {'D','G'}

    # type: set
    answers["(a) noise"] = {'A','H'}

    # type: set
    answers["(b) cluster 1"] = {'B','C','E','F','G','D'}

    # type: set
    answers["(b) cluster 2"] = {'I','J','L','M'}

    # type: set
    answers["(b) cluster 3"] = set()

    # type: set
    answers["(b) cluster 4"] = set()

    # type: set
    answers["(c)-a core"] = {'B','C','D','E','F','G','I','J','L','M'}

    # type: set
    answers["(c)-a boundary"] = {'A','H'}

    # type: set
    answers["(c)-a noise"] = set()

    # type: set
    answers["(c)-b cluster 1"] = {'A','B','C','D','E','F','G','H','I','J','L','M'}

    # type: set
    answers["(c)-b cluster 2"] = {'A'}

    # type: set
    answers["(c)-b cluster 3"] = set()

    # type: set
    answers["(c)-b cluster 4"] = set()

    return answers




# -----------------------------------------------------------
def question7():
    answers = {}

    # type: string
    answers["(a)"] = "cluster 4"

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "Cluster 4 shows the highest entropy, indicating a varied composition of land cover types within it."

    # type: string
    answers["(b)"] = "cluster 1"

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "Cluster 1 showcases the lowest entropy, signifying a more uniform assortment of land cover categories within it."

    return answers




# -----------------------------------------------------------
def question8():
    answers = {}

    # type: string
    answers["(a) Matrix 1"] = "Dataset-z"

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 1"] = "Blue likely represents well-defined clusters. Since short distances are often used to show tight clusters, blue suggests data points within each cluster are close together."

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 1"] = "Colorful clusters hint at a different way to group the data."

    # type: string
    answers["(a) Matrix 2"] = "Dataset-x"

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 2"] = "Blue clusters likely mean well-separated groups. The color association with distance suggests data points within each blue cluster are close together, signifying clear separation between clusters.."

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 2"] = "Blue shows tight clusters, while other colors reveal distinct boundaries between distant clusters (based on the distance-color link).."

    # type: string
    answers["(a) Matrix 3"] = "Dataset-y"

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 3"] = "In a distance matrix, the diagonal entries are always zero (or the minimum distance) because a point's distance to itself is zero"

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 3"] = "Green and yellow areas likely represent overlapping or unclear clusters. The color scheme suggests these regions contain data points that belong to both or neither cluster very clearly.."

    # type: string
    answers["(b) Row 1"] = "Cluster-a"

    # type: string
    answers["(b) Row 2"] = "Cluster-b"

    # type: string
    answers["(b) Row 3"] = "Cluster-c"

    # type: string
    answers["(b) Row 4"] = "Cluster-d"

    # type: explanatory string (at least four words)
    answers["(b) Row 1 explain"] = ""

    # type: explanatory string (at least four words)
    answers["(b) Row 2 explain"] = ""

    # type: explanatory string (at least four words)
    answers["(b) Row 3 explain"] = ""

    # type: explanatory string (at least four words)
    answers["(b) Row 4 explain"] = ""

    return answers




# -----------------------------------------------------------
def question9():
    answers = {}

    # type: list
    answers["(a)"] = ['hierarchical', 'overlapping', 'partial']

    # type: list
    answers["(b)"] = ['partitional', 'exclusive', 'complete']

    # type: list
    answers["(c)"] = ['partitional', 'fuzzy', 'complete']

    # type: list
    answers["(d)"] = ['hierarchical','overlapping', 'partial']

    # type: list
    answers["(e)"] = ['partitional', 'exclusive', 'complete']

    # type: explanatory string (at least four words)
    answers["(e) explain"] = ""

    return answers




# -----------------------------------------------------------
def question10():
    answers = {}

    # type: string
    answers["(a) Figure (a)"] = "No"

    # type: string
    answers["(a) Figure (b)"] = "Yes"

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "Figure B shows DBSCAN's strength for facial recognition. Unlike other methods, it excels at considering how close data points (facial encodings) are packed together, allowing it to effectively identify clusters of similar faces"
    # type: string
    answers["(b) Figure (a)"] = "No"

    # type: string
    answers["(b) Figure (b)"] = "Yes"

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "K-means clustering groups similar data points. For faces, this means it can find patterns based on things like eye size, nose shape, and lip position."
    # type: string
    answers["(c)"] = "DBSCAN"

    return answers

# --------------------------------------------------------
if __name__ == '__main__':
    answers_dict = {}
    answers_dict['question1'] = question1()
    answers_dict['question2'] = question2()
    answers_dict['question3'] = question3()
    answers_dict['question4'] = question4()
    answers_dict['question5'] = question5()
    answers_dict['question6'] = question6()
    answers_dict['question7'] = question7()
    answers_dict['question8'] = question8()
    answers_dict['question9'] = question9()
    answers_dict['question10'] = question10()
    print('end code')

    with open('answers.pkl', 'wb') as f:
        pickle.dump(answers_dict, f)
