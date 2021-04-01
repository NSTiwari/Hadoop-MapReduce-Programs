# K-means Clustering using MapReduce on Hadoop

## Steps:

1. Clone the repository on your local machine.

2. Vectorize text corpus:
   ```java -jar ProcessCorpus.jar```

3. Generate centroids:
  ```java -jar GetCentroids.jar```
  
4. Apply K-means:
  ```java -jar KMeans.jar```

5. Get the distribution of points:
  ```java -jar GetDistribution.jar```
  
6. MapReduce job on Hadoop:
  ```hadoop jar MapRedKMeans.jar KMeans /data /clusters 2```
